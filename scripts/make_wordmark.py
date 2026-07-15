"""Outline the POOKA logo from the brand font into static SVG artwork.

The POOKA logo is the word POOKA set in the brand face `POOKA.ttf` (Typocrafter),
a purpose-built logo font containing only the glyphs A, K, O and P. The font
itself is deliberately NOT committed to this repository, so this tool converts
the logo to vector outlines once. The resulting SVG is the artwork that ships:
it renders identically everywhere, needs no webfont download and no licence to
redistribute a font binary.

This is a one-off maintenance tool, not part of the site build. It is only rerun
when the logo itself changes, and it needs the licensed font on disk:

    pip install fonttools
    python scripts/make_wordmark.py --font path/to/POOKA.ttf

Letterform, tracking (0.04em) and colour behaviour follow the brand's
`--font-pooka` specification in the Polybrain + POOKA design system. The paths
use `fill="currentColor"` so the mark inherits the surrounding text colour and
works on both the light and the dark palette.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.misc.transform import Offset

REPO_ROOT = Path(__file__).resolve().parent.parent
BRAND_DIR = REPO_ROOT / "docs" / "assets" / "brand"

WORD = "POOKA"
TRACKING_EM = 0.04  # --ls-pooka: the design system tracks the mark at 0.04em

# Petrol 600 / paper, taken from the design system's colour tokens.
PETROL_700 = "#0B3E3A"
PAPER = "#FBFBF9"


def _compose(font: TTFont, word: str) -> tuple[str, tuple[float, float, float, float]]:
    """Return the SVG path data for `word` plus its bounding box in font units."""
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    upem = font["head"].unitsPerEm
    tracking = TRACKING_EM * upem

    path_pen = SVGPathPen(glyph_set)
    bounds = BoundsPen(glyph_set)

    x = 0.0
    for char in word:
        glyph_name = cmap.get(ord(char))
        if glyph_name is None:
            raise SystemExit(f"error: {char!r} is not in the font's cmap")
        glyph = glyph_set[glyph_name]
        offset = Offset(x, 0)
        glyph.draw(TransformPen(path_pen, offset))
        glyph.draw(TransformPen(bounds, offset))
        x += glyph.width + tracking

    if bounds.bounds is None:
        raise SystemExit("error: the composed logo has no outline")

    return path_pen.getCommands(), bounds.bounds


def _wordmark_svg(path_data: str, box: tuple[float, float, float, float]) -> str:
    min_x, min_y, max_x, max_y = box
    width, height = max_x - min_x, max_y - min_y
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}"\n'
        f'     role="img" aria-label="{WORD}">\n'
        f"  <title>{WORD}</title>\n"
        f'  <path fill="currentColor" transform="translate({-min_x:.0f} {max_y:.0f}) scale(1 -1)"\n'
        f'        d="{path_data}"/>\n'
        "</svg>\n"
    )


def _favicon_svg(font: TTFont) -> str:
    """A square tile carrying the logo's own P, for use at favicon sizes.

    The full wordmark is illegible at 16px, so the tile uses the first letterform
    of the approved logo rather than a separately drawn mark.
    """
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()

    path_pen = SVGPathPen(glyph_set)
    bounds = BoundsPen(glyph_set)
    glyph = glyph_set[cmap[ord("P")]]
    glyph.draw(path_pen)
    glyph.draw(bounds)

    min_x, min_y, max_x, max_y = bounds.bounds
    width, height = max_x - min_x, max_y - min_y

    tile = 64.0
    scale = (tile * 0.56) / max(width, height)
    tx = (tile - width * scale) / 2 - min_x * scale
    ty = (tile + height * scale) / 2 + min_y * scale

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="{WORD}">\n'
        f"  <title>{WORD}</title>\n"
        f'  <rect width="64" height="64" rx="12" fill="{PETROL_700}"/>\n'
        f'  <path fill="{PAPER}" transform="translate({tx:.2f} {ty:.2f}) scale({scale:.5f} {-scale:.5f})"\n'
        f'        d="{path_pen.getCommands()}"/>\n'
        "</svg>\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--font", required=True, type=Path, help="path to the licensed POOKA.ttf")
    args = parser.parse_args()

    if not args.font.exists():
        raise SystemExit(f"error: font not found: {args.font}")

    font = TTFont(args.font)
    BRAND_DIR.mkdir(parents=True, exist_ok=True)

    path_data, box = _compose(font, WORD)
    wordmark = BRAND_DIR / "pooka-wordmark.svg"
    wordmark.write_text(_wordmark_svg(path_data, box), encoding="utf-8", newline="\n")
    print(f"wrote {wordmark.relative_to(REPO_ROOT)}")

    favicon = BRAND_DIR / "favicon.svg"
    favicon.write_text(_favicon_svg(font), encoding="utf-8", newline="\n")
    print(f"wrote {favicon.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
