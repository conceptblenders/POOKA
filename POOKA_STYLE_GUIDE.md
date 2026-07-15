# POOKA Style Guide

Editorial and terminology conventions for the POOKA Design Paper. These conventions describe how the paper is written and edited. They do not change its content.

## Language and voice

- The paper is written in English.
- The register is calm, precise and architectural. It describes an architectural style; it does not sell it.
- Prefer plain declarative sentences. Avoid marketing language.

## Structure

- Chapters are numbered files under `paper/`, one chapter per file.
- Architecture is introduced before implementation.
- One paragraph has one purpose.

## Terminology

- One concept has exactly one definition. A concept is defined once and referenced elsewhere, never redefined.
- The Core Concepts are capitalized when used as defined terms, for example Ecosystem, Identity, Actor, Delegation, Domain, Context, Artifact, Relation, Semantics, Behavior, Boundary and Event.
- Keep terminology aligned with `references/terminology.md`.

## Formatting

- Use `#`, `##` and `###` heading levels consistently with the existing chapters.
- Use `–` (en dash) in the compound "Human–AI", consistent with the source text.
- Preserve Markdown formatting when editing; do not reflow or restructure text that is not part of the change.

## Reviews

- Use Pull Request style reviews. Record findings and decisions in `reviews/`.
