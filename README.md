# POOKA

**An Architectural Style for Human–AI Information Architecture**

A Design Paper by Maarten Meijer · Status: Draft · Version 0.3 · July 2026

---

## What is POOKA?

Most AI workflows reconstruct context, terminology, roles and behavioral expectations at runtime, inside the prompt, every time. That makes collaboration dependent on prompt quality and conversational continuity, and makes context transient and hard to reuse across tools, domains and models.

POOKA takes a different position: context, semantics, governance and behavior should be **persistent architectural elements**, not transient prompt content. It defines a conceptual model — independent of any programming language, storage technology, AI model or implementation framework — in which information is organized explicitly so that humans and AI can collaborate from a shared architectural foundation.

POOKA does not define software, an AI framework or a knowledge model. It defines an architectural style: a way of thinking about how information should be structured so that prompts become *consumers* of architecture rather than its primary source. See [paper/04-scope.md](paper/04-scope.md) and [paper/12-limitations.md](paper/12-limitations.md) for what is explicitly out of scope.

The name originally stood for *Personal Object-Oriented Knowledge Architecture*; the architecture has since outgrown that original scope, and the acronym is retained only as a reference to its origin (see [paper/01-introduction.md](paper/01-introduction.md)).

> POOKA is a design paper, not a scientific theory, formal standard or industry specification. It presents design proposals derived from practical observation and architectural reasoning, offered for discussion, implementation and refinement — see [paper/03-status.md](paper/03-status.md).

## Core Concepts

POOKA defines twelve Core Concepts, each with exactly one meaning throughout the paper (full definitions in [paper/08-core-concepts.md](paper/08-core-concepts.md)):

| Concept | Defines |
|---|---|
| **Ecosystem** | The complete architectural environment in which Identities, Actors, Domains, Contexts and Artifacts coexist |
| **Identity** | A persistent person, organization or other identifiable subject |
| **Actor** | Any human, AI or technical system capable of acting within an Ecosystem |
| **Delegation** | How an Actor may represent an Identity, and under which scope and constraints |
| **Domain** | A durable, bounded knowledge environment |
| **Context** | The active scope in which information is interpreted; adaptive, unlike a Domain |
| **Artifact** | Any addressable unit of information (a document, decision, task, dataset, ...) |
| **Relation** | An explicit connection between architectural concepts |
| **Semantics** | The explicit meaning assigned to information |
| **Behavior** | How Actors, including AI, are expected or constrained to operate |
| **Boundary** | Architectural separation: visibility, ownership, accessibility, scope |
| **Event** | Something that occurs at a point or period in time, introducing change |

These concepts combine into three architectural layers — **Knowledge** (what exists), **Governance** (who may act, and how), and **Behavior** (how collaboration takes place) — described in [paper/09-architectural-model.md](paper/09-architectural-model.md).

## Reading the paper

Start at [paper/00-cover.md](paper/00-cover.md) and read the chapters in order:

| # | Chapter |
|---|---|
| 00 | [Cover](paper/00-cover.md) |
| 01 | [Introduction](paper/01-introduction.md) |
| 02 | [The Architectural Challenge](paper/02-architectural-challenge.md) |
| 03 | [Status](paper/03-status.md) |
| 04 | [Scope](paper/04-scope.md) |
| 05 | [Foundational Assumptions](paper/05-foundational-assumptions.md) |
| 06 | [Existing Perspectives](paper/06-existing-perspectives.md) |
| 07 | [Design Principles](paper/07-design-principles.md) |
| 08 | [Core Concepts](paper/08-core-concepts.md) |
| 09 | [Architectural Model](paper/09-architectural-model.md) |
| 10 | [Architectural Patterns](paper/10-architectural-patterns.md) |
| 11 | [Implementation Principles](paper/11-implementation-principles.md) |
| 12 | [Limitations](paper/12-limitations.md) |
| 13 | [Discussion](paper/13-discussion.md) |
| 14 | [Future Evolution](paper/14-future-evolution.md) |
| 15 | [Conclusion](paper/15-conclusion.md) |

The original monolithic draft is preserved unchanged at [archive/POOKA_v0.1.md](archive/POOKA_v0.1.md).

## Diagrams

Editable source diagrams live in [diagrams/](diagrams/) (draw.io format — open with [diagrams.net](https://www.diagrams.net/)):

- [`core-concepts.drawio`](diagrams/core-concepts.drawio) — the Core Concepts and their relationships (chapter 8, §9.2)
- [`architectural-layers.drawio`](diagrams/architectural-layers.drawio) — the Knowledge, Governance and Behavior layers (§9.1)
- [`prompt-vs-architecture.drawio`](diagrams/prompt-vs-architecture.drawio) — runtime prompt context contrasted with persistent architecture (chapter 2, §7.2, §8.5)

Rendered exports for use in the paper go in [figures/](figures/).

## Directory structure

```
POOKA/
├── README.md               Repository overview (this file).
├── AUTHORING_GUIDE.md      Editorial rules for humans and AI.
├── CONTRIBUTING.md         Editing workflow and review process.
├── POOKA_STYLE_GUIDE.md    Style and terminology conventions.
├── CLAUDE.md               Working instructions for AI assistants.
├── POOKA.md                Reserved AI context file (placeholder).
├── CHANGELOG.md            Version history.
├── LICENSE.md              Licensing terms.
│
├── paper/                  The paper, one chapter per file (source of truth).
├── decisions/              Architecture Decision Records (ADRs).
├── diagrams/               Editable source diagrams (draw.io).
├── figures/                Exported images used by the paper.
├── references/             Bibliography, related work and terminology.
├── reviews/                Review records per reviewer and a shared log.
└── archive/                Frozen historical versions (POOKA_v0.1.md).
```

## Editing workflow

- The chapter files under [paper/](paper/) are the source of truth.
- Work one chapter at a time. Never rewrite the complete paper.
- Follow [AUTHORING_GUIDE.md](AUTHORING_GUIDE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
- Preserve terminology: every concept has exactly one meaning and one definition (see [references/terminology.md](references/terminology.md)).
- Record architectural choices as ADRs in [decisions/](decisions/).

## Review process

- Reviews are performed chapter by chapter, in Pull Request style.
- Every recommendation is explained; editorial remarks are kept separate from architectural concerns.
- Findings and decisions are recorded in [reviews/](reviews/), with a running log in [reviews/review-log.md](reviews/review-log.md).

## Status and versioning

The paper is currently Draft v0.3. See [CHANGELOG.md](CHANGELOG.md) for version history and [decisions/](decisions/) for the architectural decisions behind it (e.g. [ADR-001](decisions/ADR-001-why-these-core-concepts.md) on the choice of Core Concepts, [ADR-002](decisions/ADR-002-identity-ownership-vs-membership.md) on Identity).

## License

See [LICENSE.md](LICENSE.md) — to be determined. Until a license is set, no rights to reuse are granted beyond reading the material on GitHub.
