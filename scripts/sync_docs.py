"""Synchronise the canonical POOKA sources into the MkDocs documentation tree.

The repository is the source of truth. The canonical paper lives in ``paper/``,
the canonical glossary and bibliography in ``references/`` and the canonical
exported figures in ``figures/``. Nothing in this script may alter that content:
it copies canonical files verbatim and derives navigational fragments from the
canonical headings, so the website can never drift from the paper.

Outputs (all generated, all git-ignored, never edit by hand):

    docs/paper/*.md              verbatim copies of paper/*.md, with a banner
    docs/reference/*.md          verbatim copies of references/{terminology,bibliography}.md
    docs/assets/images/*         copies of figures/*
    build/partials/*.md          fragments derived from the canonical headings

This module doubles as an MkDocs hook (registered via ``hooks:`` in mkdocs.yml),
so synchronisation always runs before ``mkdocs serve`` and ``mkdocs build``.
It is also runnable standalone::

    python scripts/sync_docs.py            # synchronise
    python scripts/sync_docs.py --check    # verify without writing (exit 1 on drift)

Writes are idempotent: a file is only rewritten when its content actually
changes. That keeps ``mkdocs serve`` from rebuilding itself in a loop, and makes
the content-identity check meaningful.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

PAPER_DIR = REPO_ROOT / "paper"
REFERENCES_DIR = REPO_ROOT / "references"
FIGURES_DIR = REPO_ROOT / "figures"

DOCS_DIR = REPO_ROOT / "docs"
DOCS_PAPER_DIR = DOCS_DIR / "paper"
DOCS_REFERENCE_DIR = DOCS_DIR / "reference"
DOCS_IMAGES_DIR = DOCS_DIR / "assets" / "images"
DOCS_PDF_DIR = DOCS_DIR / "assets" / "pdf"

PARTIALS_DIR = REPO_ROOT / "build" / "partials"

BANNER = (
    "<!--\n"
    "  GENERATED FILE - DO NOT EDIT.\n"
    "  Canonical source: {source}\n"
    "  Regenerate with:  python scripts/sync_docs.py\n"
    "  Any edit made here is discarded on the next build.\n"
    "-->\n\n"
)

PARTIAL_BANNER = (
    "<!--\n"
    "  GENERATED FRAGMENT - DO NOT EDIT.\n"
    "  Derived from: {source}\n"
    "  Regenerate with: python scripts/sync_docs.py\n"
    "-->\n\n"
)

# The figures the paper refers to, in the paper's own numbering.
# Figure numbers and captions come from the chapters that cite them:
# chapter 2 (Figure 1), section 9.2 / chapter 8 (Figure 2), section 9.1 (Figure 3).
FIGURES = (
    {
        "slug": "prompt-vs-architecture",
        "number": 1,
        "caption": "Runtime prompt context contrasted with persistent architecture.",
        "alt": (
            "Diagram contrasting context supplied to an AI system inside a prompt at "
            "runtime with context represented persistently as part of the information "
            "architecture."
        ),
        "source": "diagrams/prompt-vs-architecture.drawio",
        "cited_in": "Chapter 2",
    },
    {
        "slug": "core-concepts",
        "number": 2,
        "caption": "The Core Concepts and their relationships.",
        "alt": (
            "Graph of the twelve POOKA Core Concepts and the relationships between "
            "them: an Ecosystem contains Identities, an Identity delegates to Actors, "
            "Actors operate within Contexts, Contexts exist within Domains, Domains "
            "contain Artifacts, and Artifacts are connected through Relations."
        ),
        "source": "diagrams/core-concepts.drawio",
        "cited_in": "Chapter 8 and section 9.2",
    },
    {
        "slug": "architectural-layers",
        "number": 3,
        "caption": "The Knowledge, Governance and Behavior layers.",
        "alt": (
            "Diagram of the three POOKA architectural layers: the Knowledge Layer "
            "describing what exists, the Governance Layer defining who may act and "
            "under which conditions, and the Behavior Layer defining how "
            "collaboration takes place."
        ),
        "source": "diagrams/architectural-layers.drawio",
        "cited_in": "Section 9.1",
    },
)

FIGURE_EXTENSIONS = (".svg", ".png")

# Generated docs page -> canonical repository path, used to point the
# "Edit this page" action at the real source instead of the generated copy.
CANONICAL_EDIT_TARGETS: dict[str, str] = {}


class SyncError(RuntimeError):
    """Raised when synchronisation cannot produce a faithful copy."""


# --------------------------------------------------------------------------- #
# small helpers
# --------------------------------------------------------------------------- #


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _slugify_heading(heading: str) -> str:
    """Reproduce Python-Markdown's default `toc` slugify for a heading string.

    Mirrors markdown.extensions.toc.slugify with separator '-': strip non-word
    characters, then replace whitespace runs with the separator. Used to build
    links into the canonical chapters and to fail loudly if they would break.
    """
    value = re.sub(r"[^\w\s-]", "", heading).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


class _Writer:
    """Idempotent writer that records what changed and can run read-only."""

    def __init__(self, *, check: bool, verbose: bool) -> None:
        self.check = check
        self.verbose = verbose
        self.written: list[Path] = []
        self.drift: list[Path] = []

    def write(self, path: Path, content: str) -> None:
        rel = path.relative_to(REPO_ROOT)
        current = _read(path) if path.exists() else None

        if current == content:
            return

        if self.check:
            reason = "missing" if current is None else "differs from canonical source"
            self.drift.append(rel)
            print(f"  DRIFT  {rel} ({reason})", file=sys.stderr)
            return

        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        self.written.append(rel)
        if self.verbose:
            print(f"  write  {rel}")

    def copy_binary(self, src: Path, dst: Path) -> None:
        rel = dst.relative_to(REPO_ROOT)
        src_bytes = src.read_bytes()
        dst_bytes = dst.read_bytes() if dst.exists() else None

        if src_bytes == dst_bytes:
            return

        if self.check:
            self.drift.append(rel)
            print(f"  DRIFT  {rel} (differs from {src.relative_to(REPO_ROOT)})", file=sys.stderr)
            return

        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        self.written.append(rel)
        if self.verbose:
            print(f"  copy   {rel}")


# --------------------------------------------------------------------------- #
# canonical parsing
# --------------------------------------------------------------------------- #


def _parse_numbered_sections(chapter: Path, chapter_number: int) -> list[dict[str, str]]:
    """Extract the ``## <chapter>.<n> <Title>`` sections from a canonical chapter.

    Returns the title verbatim and the first paragraph that follows it, verbatim.
    Nothing is reworded: the website only ever re-presents canonical sentences.
    """
    text = _read(chapter)
    pattern = re.compile(
        rf"^## ({chapter_number}\.\d+) (.+?)$\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )

    sections: list[dict[str, str]] = []
    for match in pattern.finditer(text):
        number, title, body = match.group(1), match.group(2).strip(), match.group(3)

        paragraphs = [
            block.strip()
            for block in body.split("\n\n")
            if block.strip() and block.strip() != "---"
        ]
        if not paragraphs:
            raise SyncError(f"{chapter.name}: section {number} {title!r} has no body text")

        heading = f"{number} {title}"
        sections.append(
            {
                "number": number,
                "title": title,
                "statement": paragraphs[0].replace("\n", " ").strip(),
                "anchor": _slugify_heading(heading),
            }
        )

    if not sections:
        raise SyncError(f"{chapter.name}: no '## {chapter_number}.x' sections found")

    return sections


def _parse_terminology() -> dict[str, str]:
    """Read the canonical glossary table into {term: definition}, verbatim."""
    text = _read(REFERENCES_DIR / "terminology.md")
    definitions: dict[str, str] = {}

    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 2:
            continue
        term, definition = cells
        if term in ("Term", "----") or set(term) <= {"-", " "}:
            continue
        definitions[term] = definition

    if not definitions:
        raise SyncError("references/terminology.md: no glossary rows parsed")

    return definitions


# --------------------------------------------------------------------------- #
# generators
# --------------------------------------------------------------------------- #


def _sync_paper(writer: _Writer) -> None:
    chapters = sorted(PAPER_DIR.glob("*.md"))
    if not chapters:
        raise SyncError("paper/ contains no chapters; refusing to build an empty paper")

    for chapter in chapters:
        source = f"paper/{chapter.name}"
        target = DOCS_PAPER_DIR / chapter.name
        writer.write(target, BANNER.format(source=source) + _read(chapter))
        CANONICAL_EDIT_TARGETS[f"paper/{chapter.name}"] = source


def _sync_references(writer: _Writer) -> None:
    for name in ("terminology.md", "bibliography.md"):
        canonical = REFERENCES_DIR / name
        if not canonical.exists():
            raise SyncError(f"references/{name} is missing")
        source = f"references/{name}"
        writer.write(DOCS_REFERENCE_DIR / name, BANNER.format(source=source) + _read(canonical))
        CANONICAL_EDIT_TARGETS[f"reference/{name}"] = source


def _sync_figures(writer: _Writer) -> list[str]:
    """Copy exported figures and generate one include-fragment per figure.

    A figure that has not been exported yet yields a clearly marked placeholder
    instead of a broken image, so the site keeps building while the export is
    still outstanding. Nothing is invented.
    """
    missing: list[str] = []

    for figure in FIGURES:
        slug = figure["slug"]
        exported = next(
            (FIGURES_DIR / f"{slug}{ext}" for ext in FIGURE_EXTENSIONS if (FIGURES_DIR / f"{slug}{ext}").exists()),
            None,
        )

        if exported is None:
            missing.append(f"figures/{slug}.svg")
            fragment = (
                f'!!! warning "Figure {figure["number"]} has not been exported yet"\n\n'
                f'    This figure is defined in the canonical source `{figure["source"]}`\n'
                f'    and cited in {figure["cited_in"]}, but no export exists yet.\n'
                f"    Expected file: `figures/{slug}.svg`.\n"
            )
        else:
            writer.copy_binary(exported, DOCS_IMAGES_DIR / exported.name)
            href = f"assets/images/{exported.name}"
            fragment = (
                '<figure markdown="span">\n'
                f'  [![{figure["alt"]}]({href}){{ width="840" loading="lazy" }}]'
                f'({href} "Open figure {figure["number"]} at full size")\n'
                f'  <figcaption>Figure {figure["number"]}. {figure["caption"]}</figcaption>\n'
                "</figure>\n"
            )

        writer.write(
            PARTIALS_DIR / "figures" / f"{slug}.md",
            PARTIAL_BANNER.format(source=figure["source"]) + fragment,
        )

    return missing


def _generate_core_concepts(writer: _Writer) -> None:
    """Derive the Core Concepts fragment from chapter 8 plus the canonical glossary.

    The definitions are the canonical glossary sentences, used verbatim. The order
    and section anchors come from chapter 8. A mismatch between the two canonical
    sources fails the build rather than silently publishing a stale concept list.
    """
    sections = _parse_numbered_sections(PAPER_DIR / "08-core-concepts.md", 8)
    definitions = _parse_terminology()

    chapter_terms = [section["title"] for section in sections]
    glossary_terms = list(definitions)
    if chapter_terms != glossary_terms:
        raise SyncError(
            "Core Concepts drift between canonical sources.\n"
            f"  paper/08-core-concepts.md: {chapter_terms}\n"
            f"  references/terminology.md: {glossary_terms}"
        )

    lines: list[str] = []
    for section in sections:
        term = section["title"]
        lines.append(f'<div class="pooka-concept" markdown="1">')
        lines.append(f'<h2 id="{term.lower()}">{term}</h2>')
        lines.append("")
        lines.append(definitions[term])
        lines.append("")
        lines.append(
            f'<p class="pooka-concept__source">'
            f'<a href="../paper/08-core-concepts/#{section["anchor"]}">'
            f'Section {section["number"]} in the Design Paper</a></p>'
        )
        lines.append("</div>")
        lines.append("")

    writer.write(
        PARTIALS_DIR / "core-concepts.md",
        PARTIAL_BANNER.format(source="paper/08-core-concepts.md + references/terminology.md")
        + "\n".join(lines),
    )


def _generate_design_principles(writer: _Writer) -> None:
    """Derive the Design Principles fragment from chapter 7, verbatim."""
    sections = _parse_numbered_sections(PAPER_DIR / "07-design-principles.md", 7)

    lines: list[str] = []
    for section in sections:
        lines.append('<div class="pooka-principle" markdown="1">')
        lines.append(f'<h2 id="{_slugify_heading(section["title"])}">{section["title"]}</h2>')
        lines.append("")
        lines.append(f'<p class="pooka-principle__statement">{section["statement"]}</p>')
        lines.append("")
        lines.append(
            f'<p class="pooka-principle__source">'
            f'<a href="../paper/07-design-principles/#{section["anchor"]}">'
            f'Section {section["number"]} in the Design Paper</a></p>'
        )
        lines.append("</div>")
        lines.append("")

    writer.write(
        PARTIALS_DIR / "design-principles.md",
        PARTIAL_BANNER.format(source="paper/07-design-principles.md") + "\n".join(lines),
    )


def _generate_related_work(writer: _Writer) -> None:
    """Derive the Existing Perspectives fragment from chapter 6, verbatim."""
    sections = _parse_numbered_sections(PAPER_DIR / "06-existing-perspectives.md", 6)

    lines: list[str] = []
    for section in sections:
        if section["title"] == "Positioning":
            continue
        lines.append('<div class="pooka-perspective" markdown="1">')
        lines.append(f'<h2 id="{_slugify_heading(section["title"])}">{section["title"]}</h2>')
        lines.append("")
        lines.append(section["statement"])
        lines.append("")
        lines.append(
            f'<p class="pooka-perspective__source">'
            f'<a href="../paper/06-existing-perspectives/#{section["anchor"]}">'
            f'Section {section["number"]} in the Design Paper</a></p>'
        )
        lines.append("</div>")
        lines.append("")

    writer.write(
        PARTIALS_DIR / "related-work.md",
        PARTIAL_BANNER.format(source="paper/06-existing-perspectives.md") + "\n".join(lines),
    )


def _generate_pdf_link(writer: _Writer, version: str) -> bool:
    """Point the Downloads page at the PDF edition, or say plainly that it is absent.

    The PDF is built by scripts/build_pdf.py, which is not part of the site build:
    it needs a browser. So the site must render correctly either way, and must
    never advertise a download that does not exist.
    """
    name = f"pooka-design-paper-v{version}.pdf"
    pdf = DOCS_PDF_DIR / name

    if pdf.exists():
        size_mb = pdf.stat().st_size / (1024 * 1024)
        fragment = (
            '<div class="pooka-actions" markdown="1">\n'
            f'[<span class="pooka-actions__title">Download the PDF</span>'
            f'<span class="pooka-actions__note">The complete paper, {size_mb:.1f} MB. '
            f"Draft v{version}, rendered from the canonical chapters.</span>]"
            f"(assets/pdf/{name})\n"
            "</div>\n"
        )
    else:
        fragment = (
            '!!! note "PDF"\n\n'
            "    No PDF edition has been built for this version yet. It is generated from\n"
            "    the canonical chapters with `python scripts/build_pdf.py`, and appears here\n"
            "    once built. Until then the Markdown source and this website are the only\n"
            "    editions, and neither should be cited as a PDF.\n"
        )

    writer.write(
        PARTIALS_DIR / "pdf-download.md",
        PARTIAL_BANNER.format(source="docs/assets/pdf/ (built by scripts/build_pdf.py)") + fragment,
    )
    return pdf.exists()


def _parse_cover_field(text: str, label: str) -> str:
    match = re.search(rf"^\*\*{label}\*\*\s*\n(.+?)$", text, re.MULTILINE)
    if not match:
        raise SyncError(f"paper/00-cover.md: field {label!r} not found")
    return match.group(1).strip()


def _generate_status(writer: _Writer) -> dict[str, str]:
    """Derive version, status, author and date from the canonical cover page."""
    cover = _read(PAPER_DIR / "00-cover.md")
    meta = {
        "author": _parse_cover_field(cover, "Author"),
        "status": _parse_cover_field(cover, "Status"),
        "version": _parse_cover_field(cover, "Version"),
        "date": _parse_cover_field(cover, "Date"),
    }

    fragment = (
        '<p class="pooka-status">'
        f'<span class="pooka-status__item"><span class="pooka-status__key">Version</span> {meta["version"]}</span>'
        f'<span class="pooka-status__item"><span class="pooka-status__key">Status</span> {meta["status"]}</span>'
        f'<span class="pooka-status__item"><span class="pooka-status__key">Date</span> {meta["date"]}</span>'
        f'<span class="pooka-status__item"><span class="pooka-status__key">Author</span> {meta["author"]}</span>'
        "</p>\n"
    )
    writer.write(
        PARTIALS_DIR / "status.md",
        PARTIAL_BANNER.format(source="paper/00-cover.md") + fragment,
    )
    return meta


# --------------------------------------------------------------------------- #
# entry points
# --------------------------------------------------------------------------- #


def synchronise(*, check: bool = False, verbose: bool = False) -> _Writer:
    for required in (PAPER_DIR, REFERENCES_DIR):
        if not required.is_dir():
            raise SyncError(f"canonical directory missing: {required.relative_to(REPO_ROOT)}")

    writer = _Writer(check=check, verbose=verbose)

    _sync_paper(writer)
    _sync_references(writer)
    missing_figures = _sync_figures(writer)
    _generate_core_concepts(writer)
    _generate_design_principles(writer)
    _generate_related_work(writer)
    meta = _generate_status(writer)
    has_pdf = _generate_pdf_link(writer, meta["version"])

    if verbose:
        print(
            f"  paper v{meta['version']} ({meta['status']}) | "
            f"{len(writer.written)} file(s) updated"
        )
        for name in missing_figures:
            print(f"  NOTE   figure not exported yet: {name}")
        if not has_pdf:
            print(f"  NOTE   no PDF for v{meta['version']} yet: python scripts/build_pdf.py")

    return writer


# --- MkDocs hook events ---------------------------------------------------- #


def on_pre_build(config, **kwargs):  # noqa: ARG001 - MkDocs calls this
    """Synchronise canonical content before MkDocs collects files.

    Raising here aborts the build, which is intentional: a site that cannot be
    proven to match the canonical paper must not be published.
    """
    synchronise(check=False, verbose=False)


def on_page_markdown(markdown, page, config, files, **kwargs):  # noqa: ARG001
    """Point 'Edit this page' at the canonical source, not the generated copy."""
    canonical = CANONICAL_EDIT_TARGETS.get(page.file.src_uri.replace("\\", "/"))
    if canonical and config.repo_url:
        page.edit_url = f"{config.repo_url.rstrip('/')}/edit/main/{canonical}"
    return markdown


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the generated tree matches the canonical sources; write nothing",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="list every file touched")
    args = parser.parse_args()

    try:
        writer = synchronise(check=args.check, verbose=args.verbose or not args.check)
    except SyncError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    if args.check:
        if writer.drift:
            print(
                f"error: {len(writer.drift)} generated file(s) do not match the canonical "
                "sources; run: python scripts/sync_docs.py",
                file=sys.stderr,
            )
            return 1
        print("ok: generated documentation is identical to the canonical sources")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
