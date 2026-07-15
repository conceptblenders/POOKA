---
title: Downloads
description: >-
  Download the POOKA Design Paper: Markdown source, the repository, the bibliography
  and citation information.
---

# Downloads

The POOKA Design Paper is maintained as Markdown in a public repository, one file per chapter.
That repository is the canonical source: this website and any export are generated from it.

--8<-- "status.md"

## The paper

<div class="pooka-actions" markdown="1">
[<span class="pooka-actions__title">Read online</span><span class="pooka-actions__note">The complete paper, chapter by chapter, in its canonical order.</span>](paper/00-cover.md)
[<span class="pooka-actions__title">Markdown source</span><span class="pooka-actions__note">The canonical chapter files under paper/ in the repository.</span>](https://github.com/conceptblenders/POOKA/tree/main/paper)
[<span class="pooka-actions__title">Download the repository</span><span class="pooka-actions__note">A ZIP archive of the current main branch, including diagrams and decisions.</span>](https://github.com/conceptblenders/POOKA/archive/refs/heads/main.zip)
[<span class="pooka-actions__title">GitHub repository</span><span class="pooka-actions__note">Browse the source, open an issue or propose a change.</span>](https://github.com/conceptblenders/POOKA)
</div>

!!! note "PDF"

    No PDF edition has been generated yet. When one is produced from the canonical chapters it
    will be published here. Until then the Markdown source and this website are the only
    editions, and neither should be cited as a PDF.

## Reference material

- [Glossary](reference/terminology.md) — the Core Concepts, one definition each.
  ([source](https://github.com/conceptblenders/POOKA/blob/main/references/terminology.md))
- [Bibliography](reference/bibliography.md) — the literature underlying the disciplines
  discussed in Chapter 6.
  ([source](https://github.com/conceptblenders/POOKA/blob/main/references/bibliography.md))
- [Diagrams](https://github.com/conceptblenders/POOKA/tree/main/diagrams) — editable draw.io
  sources for the figures.
- [Decisions](https://github.com/conceptblenders/POOKA/tree/main/decisions) — the Architecture
  Decision Records behind the model.

## Citation

The paper is a versioned draft. Cite the version you read, and prefer the repository over this
website when a permanent reference is needed.

=== "Plain"

    ```text
    Meijer, M. (2026). POOKA: An Architectural Style for Human–AI Information
    Architecture (Design Paper, Draft v0.3). https://pooka.info
    ```

=== "BibTeX"

    ```bibtex
    @techreport{meijer2026pooka,
      author      = {Meijer, Maarten},
      title       = {POOKA: An Architectural Style for Human--AI Information Architecture},
      type        = {Design Paper},
      number      = {Draft v0.3},
      year        = {2026},
      month       = {7},
      url         = {https://pooka.info},
      note        = {Canonical source: https://github.com/conceptblenders/POOKA}
    }
    ```

=== "APA"

    ```text
    Meijer, M. (2026, July). POOKA: An architectural style for Human–AI information
    architecture (Design paper, Draft v0.3). Retrieved from https://pooka.info
    ```

!!! warning "Cite the status, not just the title"

    POOKA is a design paper, not a standard, specification or empirically validated result.
    Chapter 3 states this explicitly, and any citation should preserve that framing.
