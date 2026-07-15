"""Render the PDF edition of the POOKA Design Paper from the canonical chapters.

The chapters in `paper/` are the source of truth. This script reads them, renders
them to a single HTML document and prints that to PDF with Chromium. No chapter
file is read for anything other than its own text, and none is ever written to:
the PDF is a rendering of the paper, not a second copy of it.

    pip install -r requirements-pdf.txt
    python -m playwright install chromium
    python scripts/build_pdf.py

Output: docs/assets/pdf/pooka-design-paper-v<version>.pdf, where <version> comes
from `paper/00-cover.md`. The file is git-ignored; the site build picks it up and
the Downloads page links to it, or shows a placeholder when it has not been built.

Figures. The paper cites its figures but does not embed them, so a reader of the
PDF would be sent to a `.drawio` file they cannot open. This script therefore
places each figure directly after the paragraph that first cites it, using the
paper's own citation as the anchor. Placement is derived, never guessed, and it
happens in the rendered HTML only: the canonical Markdown keeps its current form.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

import markdown

REPO_ROOT = Path(__file__).resolve().parent.parent

PAPER_DIR = REPO_ROOT / "paper"
REFERENCES_DIR = REPO_ROOT / "references"
FIGURES_DIR = REPO_ROOT / "figures"
BRAND_DIR = REPO_ROOT / "docs" / "assets" / "brand"
FONTS_CSS = REPO_ROOT / "docs" / "assets" / "stylesheets" / "fonts.css"
PDF_CSS = REPO_ROOT / "docs" / "assets" / "stylesheets" / "pdf.css"

OUT_DIR = REPO_ROOT / "docs" / "assets" / "pdf"

# Figure number and caption per diagram, matching the paper's own numbering.
# `cite` is the string the paper uses to refer to the figure; it anchors placement.
FIGURES = (
    {
        "slug": "prompt-vs-architecture",
        "number": 1,
        "cite": "diagrams/prompt-vs-architecture.drawio",
        "caption": "Runtime prompt context contrasted with persistent architecture.",
        "alt": "Diagram contrasting context supplied inside a prompt at runtime with context represented persistently as part of the information architecture.",
    },
    {
        "slug": "core-concepts",
        "number": 2,
        "cite": "diagrams/core-concepts.drawio",
        "caption": "The Core Concepts and their relationships.",
        "alt": "Graph of the twelve POOKA Core Concepts and the relationships between them.",
    },
    {
        "slug": "architectural-layers",
        "number": 3,
        "cite": "diagrams/architectural-layers.drawio",
        "caption": "The Knowledge, Governance and Behavior layers.",
        "alt": "Diagram of the Knowledge, Governance and Behavior layers.",
    },
)

MD_EXTENSIONS = ["tables", "attr_list", "sane_lists"]


class BuildError(RuntimeError):
    """Raised when the PDF cannot be rendered faithfully."""


def _cover_field(text: str, label: str) -> str:
    match = re.search(rf"^\*\*{label}\*\*\s*\n(.+?)$", text, re.MULTILINE)
    if not match:
        raise BuildError(f"paper/00-cover.md: field {label!r} not found")
    return match.group(1).strip()


def _figure_html(figure: dict) -> str:
    svg = FIGURES_DIR / f"{figure['slug']}.svg"
    if not svg.exists():
        raise BuildError(
            f"figures/{figure['slug']}.svg is missing. Run: python scripts/export_figures.py"
        )
    return (
        '<figure class="figure">'
        f'<img src="{svg.as_uri()}" alt="{html.escape(figure["alt"])}">'
        f'<figcaption>Figure {figure["number"]}. {html.escape(figure["caption"])}</figcaption>'
        "</figure>"
    )


def _place_figures(chapter_html: str, pending: list[dict]) -> tuple[str, list[dict]]:
    """Insert each figure after the paragraph that first cites it.

    The paper cites a figure more than once (Figure 2 appears in chapter 8 and
    again in section 9.2). Only the first citation carries the figure, so the
    reader meets it where it is introduced and it is not repeated later.
    """
    remaining = []
    for figure in pending:
        pattern = re.compile(
            r"<p>(?:(?!</p>).)*?" + re.escape(figure["cite"]) + r"(?:(?!</p>).)*?</p>",
            re.DOTALL,
        )
        match = pattern.search(chapter_html)
        if not match:
            remaining.append(figure)
            continue
        chapter_html = (
            chapter_html[: match.end()] + _figure_html(figure) + chapter_html[match.end() :]
        )
    return chapter_html, remaining


def _render_chapters(md: markdown.Markdown) -> tuple[list[dict], list[dict]]:
    chapters = []
    pending = list(FIGURES)

    for path in sorted(PAPER_DIR.glob("*.md")):
        if path.name == "00-cover.md":
            continue

        md.reset()
        body = md.convert(path.read_text(encoding="utf-8"))
        body, pending = _place_figures(body, pending)

        title_match = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.DOTALL)
        if not title_match:
            raise BuildError(f"{path.name}: no <h1> heading found")
        title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip()

        chapters.append({"id": path.stem, "title": title, "body": body})

    return chapters, pending


def _render_reference(md: markdown.Markdown, name: str, anchor: str) -> dict:
    path = REFERENCES_DIR / name
    if not path.exists():
        raise BuildError(f"references/{name} is missing")
    md.reset()
    body = md.convert(path.read_text(encoding="utf-8"))
    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.DOTALL)
    title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip() if title_match else anchor
    return {"id": anchor, "title": title, "body": body}


def build_html() -> tuple[str, dict[str, str]]:
    cover = (PAPER_DIR / "00-cover.md").read_text(encoding="utf-8")
    meta = {
        "author": _cover_field(cover, "Author"),
        "status": _cover_field(cover, "Status"),
        "version": _cover_field(cover, "Version"),
        "date": _cover_field(cover, "Date"),
    }

    md = markdown.Markdown(extensions=MD_EXTENSIONS)
    chapters, unplaced = _render_chapters(md)
    if unplaced:
        raise BuildError(
            "these figures are cited nowhere in the paper, so they cannot be placed: "
            + ", ".join(f["slug"] for f in unplaced)
        )

    sections = chapters + [
        _render_reference(md, "terminology.md", "glossary"),
        _render_reference(md, "bibliography.md", "bibliography"),
    ]

    wordmark = (BRAND_DIR / "pooka-wordmark.svg").read_text(encoding="utf-8")

    toc = "\n".join(
        f'<li><a href="#{s["id"]}">{html.escape(s["title"])}</a></li>' for s in sections
    )
    body = "\n".join(
        f'<section class="chapter" id="{s["id"]}">{s["body"]}</section>' for s in sections
    )

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>POOKA — An Architectural Style for Human–AI Information Architecture</title>
<link rel="stylesheet" href="{FONTS_CSS.as_uri()}">
<link rel="stylesheet" href="{PDF_CSS.as_uri()}">
</head>
<body>

<section class="cover">
  <div class="cover__mark">{wordmark}</div>
  <h1 class="cover__title">An Architectural Style for<br>Human–AI Information Architecture</h1>
  <p class="cover__kind">A Design Paper</p>
  <dl class="cover__meta">
    <dt>Author</dt><dd>{html.escape(meta["author"])}</dd>
    <dt>Status</dt><dd>{html.escape(meta["status"])}</dd>
    <dt>Version</dt><dd>{html.escape(meta["version"])}</dd>
    <dt>Date</dt><dd>{html.escape(meta["date"])}</dd>
  </dl>
  <p class="cover__foot">
    pooka.info · github.com/conceptblenders/POOKA<br>
    <span>Licensed under CC BY 4.0. POOKA is a design paper, not a standard or specification.</span>
  </p>
</section>

<section class="toc">
  <h1>Contents</h1>
  <ol>{toc}</ol>
</section>

{body}

</body>
</html>
"""
    return doc, meta


def build_pdf(*, keep_html: bool = False) -> Path:
    from playwright.sync_api import sync_playwright

    doc, meta = build_html()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    scratch = OUT_DIR / ".paper.html"
    scratch.write_text(doc, encoding="utf-8")

    target = OUT_DIR / f"pooka-design-paper-v{meta['version']}.pdf"

    footer = (
        '<div style="width:100%;font-family:sans-serif;font-size:7pt;color:#6B7269;'
        'padding:0 20mm;display:flex;justify-content:space-between;">'
        "<span>POOKA — An Architectural Style for Human–AI Information Architecture</span>"
        f'<span>v{html.escape(meta["version"])} · <span class="pageNumber"></span></span>'
        "</div>"
    )

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(scratch.as_uri(), wait_until="load")
        # Let the webfonts settle before laying out pages.
        page.wait_for_timeout(2500)
        page.pdf(
            path=str(target),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=footer,
            margin={"top": "18mm", "bottom": "16mm", "left": "20mm", "right": "20mm"},
            # A 15-chapter paper needs a navigable outline; tagging keeps it accessible.
            outline=True,
            tagged=True,
        )
        browser.close()

    if not keep_html:
        scratch.unlink(missing_ok=True)

    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--keep-html", action="store_true", help="keep the intermediate HTML for debugging"
    )
    args = parser.parse_args()

    try:
        target = build_pdf(keep_html=args.keep_html)
    except BuildError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    size_kb = target.stat().st_size // 1024
    print(f"wrote {target.relative_to(REPO_ROOT)} ({size_kb} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
