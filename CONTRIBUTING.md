# Contributing

This document describes the editing workflow for the POOKA Design Paper.

## Editing workflow

- **Work chapter by chapter.** Make changes within a single chapter file under `paper/` at a time.
- **Never rewrite the complete paper.** Improve the document incrementally; do not regenerate it as a whole.
- **Preserve terminology consistency.** Use the established terms exactly as defined; align with `POOKA_STYLE_GUIDE.md` and `references/terminology.md`.
- **One concept has exactly one definition.** A concept is defined in a single place and referenced elsewhere, never redefined.
- **One paragraph has one purpose.** Each paragraph makes a single point.
- **Architecture before implementation.** Establish architectural concepts before discussing implementation details.
- **Use Pull Request style reviews.** Propose changes as reviewable units, record findings and decisions in `reviews/`, and merge deliberately.

## Practical notes

- The chapter files under `paper/` are the source of truth.
- Record review activity in `reviews/review-log.md` and per-reviewer files.
- Keep `CHANGELOG.md` updated when a version is released.
