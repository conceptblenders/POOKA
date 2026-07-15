# Licensing

This repository contains two kinds of work, licensed separately.

---

## The Design Paper and its figures

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

Copyright © 2026 Maarten Meijer.

This covers the POOKA Design Paper and the material that belongs to it:

- `paper/` — the Design Paper, one chapter per file
- `references/` — terminology and bibliography
- `diagrams/` and `figures/` — the diagram sources and their exports
- `decisions/` — the Architecture Decision Records
- `archive/` — frozen historical versions

You are free to:

- **Share** — copy and redistribute the material in any medium or format;
- **Adapt** — remix, transform and build upon the material for any purpose, including
  commercially.

Under the following term:

- **Attribution** — you must give appropriate credit, provide a link to the licence, and
  indicate if changes were made. You may do so in any reasonable manner, but not in any way
  that suggests the licensor endorses you or your use.

No additional restrictions: you may not apply legal terms or technological measures that
legally restrict others from doing anything the licence permits.

Full licence text: <https://creativecommons.org/licenses/by/4.0/legalcode>
Summary: <https://creativecommons.org/licenses/by/4.0/>

### Suggested attribution

> Meijer, M. (2026). *POOKA: An Architectural Style for Human–AI Information Architecture*
> (Design Paper, Draft v0.3). <https://pooka.info>. Licensed under CC BY 4.0.

### Please preserve the status

POOKA is a design paper, not a scientific theory, formal standard or industry specification,
and Chapter 3 says so explicitly. The licence permits adaptation, but misrepresenting POOKA as
a validated standard, or presenting a modified version as the original, is not something
attribution makes accurate. If you adapt the paper, indicate what you changed.

---

## The website and tooling

**MIT Licence**

Copyright © 2026 Maarten Meijer.

This covers the code that builds and publishes the site:

- `scripts/`, `mkdocs.yml`, `requirements*.txt`
- `docs/` (the website pages and stylesheets), `overrides/`, `.github/`

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## What these licences do not cover

**The POOKA name and logo.** Neither licence grants rights to the POOKA name or the POOKA
wordmark. CC BY covers copyright, not trademarks, and expressly does not grant trademark
rights. You may describe an implementation as *conforming to POOKA* or *based on POOKA*; using
the name or mark in a way that suggests endorsement, certification or authorship requires
permission.

**The brand font.** The POOKA logo is set in a licensed font that is deliberately not included
in this repository. The logo ships as outlines in `docs/assets/brand/`, which does not convey
any right to the underlying font.

**Third-party material.** Works cited in `references/bibliography.md` remain under their own
copyright; the bibliography lists them, it does not redistribute them. The website is built
with Material for MkDocs (MIT) and sets the paper in Newsreader and IBM Plex (SIL Open Font
License 1.1), each under its own licence.
