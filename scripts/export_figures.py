"""Export the draw.io diagrams to the SVG figures the paper and website use.

`diagrams/*.drawio` are the editable sources; `figures/*.svg` are the exports the
website and any PDF edition consume. This script regenerates the exports so the
flags that matter are not lost between sessions.

Run it after editing a diagram:

    python scripts/export_figures.py

It needs draw.io Desktop, which is not part of the site toolchain and is not
installed in CI: the exports are committed, so a normal build never needs it.

    winget install JGraph.Draw          # Windows
    brew install --cask drawio          # macOS

Why `--svg-theme light` is not optional: draw.io defaults to `auto`, which emits
`color-scheme: light dark` into the SVG. The figures are then rendered by the
browser's dark theme, which flips the diagram's own colours to white-on-dark.
The website deliberately keeps figures on a paper background in dark mode, so an
auto-themed export renders white text on white paper and the labels disappear.
Forcing the light theme pins the diagram to the colours it was drawn in.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIAGRAMS_DIR = REPO_ROOT / "diagrams"
FIGURES_DIR = REPO_ROOT / "figures"

BORDER_PX = 12

CANDIDATES = (
    Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "draw.io" / "draw.io.exe",
    Path("C:/Program Files/draw.io/draw.io.exe"),
    Path("/Applications/draw.io.app/Contents/MacOS/draw.io"),
    Path("/usr/bin/drawio"),
)


def _find_drawio() -> Path:
    override = os.environ.get("DRAWIO")
    if override:
        path = Path(override)
        if not path.exists():
            raise SystemExit(f"error: DRAWIO is set but does not exist: {path}")
        return path

    on_path = shutil.which("drawio") or shutil.which("draw.io")
    if on_path:
        return Path(on_path)

    for candidate in CANDIDATES:
        if candidate.exists():
            return candidate

    raise SystemExit(
        "error: draw.io Desktop not found. Install it, or point DRAWIO at the binary.\n"
        "  Windows: winget install JGraph.Draw\n"
        "  macOS:   brew install --cask drawio"
    )


def main() -> int:
    drawio = _find_drawio()
    sources = sorted(DIAGRAMS_DIR.glob("*.drawio"))
    if not sources:
        raise SystemExit("error: diagrams/ contains no .drawio sources")

    FIGURES_DIR.mkdir(exist_ok=True)
    failures = 0

    for source in sources:
        target = FIGURES_DIR / f"{source.stem}.svg"
        result = subprocess.run(
            [
                str(drawio),
                "--export",
                "--format", "svg",
                # Pin the diagram to the colours it was drawn in; see module docstring.
                "--svg-theme", "light",
                "--border", str(BORDER_PX),
                "--output", str(target),
                # draw.io is an Electron app; these keep it headless-friendly.
                "--disable-gpu",
                "--no-sandbox",
                str(source),
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0 or not target.exists():
            failures += 1
            print(f"  FAILED  {source.name}", file=sys.stderr)
            if result.stderr.strip():
                print(f"          {result.stderr.strip().splitlines()[-1]}", file=sys.stderr)
            continue

        # An auto-themed export would defeat the point of the flag above.
        if "color-scheme: light dark" in target.read_text(encoding="utf-8", errors="ignore"):
            failures += 1
            print(f"  FAILED  {target.name}: still auto-themed", file=sys.stderr)
            continue

        print(f"  {source.name} -> figures/{target.name} ({target.stat().st_size // 1024} KB)")

    if failures:
        print(f"\n{failures} diagram(s) failed to export", file=sys.stderr)
        return 1

    print(f"\n{len(sources)} figure(s) exported. Rebuild the site to pick them up.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
