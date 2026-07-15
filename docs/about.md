---
title: About
description: >-
  About the POOKA Design Paper: its status, scope, limitations, author, and how the
  paper is written, reviewed and versioned.
---

# About

POOKA defines an architectural style for Human–AI Information Architecture. This site
publishes the POOKA Design Paper, which is written and maintained in the open.

--8<-- "status.md"

## What this paper is

POOKA is an architectural philosophy emerging from practical experimentation with Human–AI
collaboration.

It is not a scientific theory, formal standard or industry specification. The concepts
presented are design proposals derived from practical observation, iterative refinement and
architectural reasoning. They have not been empirically validated through controlled scientific
research and should therefore not be interpreted as established facts.

POOKA intentionally builds upon existing knowledge from information architecture, software
architecture, knowledge management, object-oriented design, graph-based modeling, identity
management and AI-assisted knowledge work. Where existing concepts adequately describe a
problem, they are adopted rather than reinvented.

This paper should be read as a design paper: an invitation to discussion, implementation,
validation and further evolution.

[Read Chapter 3: Status](paper/03-status.md)

## What this paper is not

POOKA addresses a specific class of architectural problems and should not be regarded as a
universal solution for every Human–AI scenario. In particular, POOKA is:

- **not an AI framework.** It does not prescribe language models, prompting techniques,
  reasoning methods, machine learning algorithms or agent implementations.
- **not a software architecture.** It does not prescribe programming languages, APIs,
  databases, cloud platforms or deployment models.
- **not a knowledge model.** It defines how knowledge is organized rather than what knowledge
  should contain, and avoids prescribing domain vocabularies, ontologies or taxonomies.

POOKA supports collaboration between humans and AI but does not transfer responsibility from
humans to AI systems. Accountability for decisions remains with the responsible human or
organization.

[Read Chapter 4: Scope](paper/04-scope.md) · [Read Chapter 12: Limitations](paper/12-limitations.md)

## Author

The POOKA Design Paper is written by **Maarten Meijer**.

## How the paper is written

The chapter files under `paper/` in the [repository](https://github.com/conceptblenders/POOKA)
are the source of truth. This website is generated from them: every chapter, the glossary and
the bibliography are copied verbatim on each build, and the Core Concepts, Design Principles
and Related Work pages are derived from the canonical chapters rather than maintained by hand.
The website can therefore never say something the paper does not.

The editorial rules are deliberately strict:

- Work chapter by chapter. Never rewrite the complete paper.
- One concept has exactly one definition. A concept is defined once and referenced elsewhere.
- One paragraph has one purpose.
- Architecture before implementation.
- No marketing language, no hype, no unsupported claims.

These rules are recorded in `AUTHORING_GUIDE.md` and `POOKA_STYLE_GUIDE.md`.

## How the paper is reviewed

Reviews are performed chapter by chapter, in Pull Request style. Every recommendation is
explained, and editorial remarks are kept separate from architectural concerns. Findings and
decisions are recorded in `reviews/`, with a running log in `reviews/review-log.md`.

Architectural choices are recorded as Architecture Decision Records in `decisions/`, for
example the rationale for the choice of Core Concepts (ADR-001) and the treatment of Identity
as coexistence rather than ownership (ADR-002).

## Versions and evolution

The concepts described represent the current state of the architectural style. Future
experience, technological developments and community feedback may lead to refinement,
extension or replacement of individual concepts while preserving the overall architectural
philosophy.

POOKA should therefore be regarded as an evolving architectural style rather than a fixed
specification. Version history is recorded in `CHANGELOG.md`, and the original monolithic draft
is preserved unchanged at `archive/POOKA_v0.1.md`.

[Read Chapter 14: Future Evolution](paper/14-future-evolution.md)

## Contributing

The long-term development of POOKA depends on practical application, critical discussion and
contributions from a broader community of practitioners, architects and researchers.

If you would like to challenge a concept, propose a refinement or discuss an implementation,
please open an issue or a pull request on
[GitHub](https://github.com/conceptblenders/POOKA). The editing workflow is described in
`CONTRIBUTING.md`.

## Licensing

Licensing terms are still to be determined; see `LICENSE.md` in the repository. Until a licence
is set, no rights to reuse are granted beyond reading the material.
