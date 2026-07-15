---
title: Core Concepts
description: >-
  The twelve Core Concepts of POOKA: Ecosystem, Identity, Actor, Delegation, Domain,
  Context, Artifact, Relation, Semantics, Behavior, Boundary and Event.
---

# Core Concepts

POOKA defines a small set of fundamental architectural concepts. Together these concepts
establish a common language for organizing information, semantics, governance and behavior
within Human–AI Information Architecture.

POOKA intentionally limits itself to a small set of Core Concepts. These concepts are not
intended to describe every aspect of knowledge or collaboration, but to capture the
architectural abstractions considered necessary to describe Human–AI Information Architecture.

The Core Concepts are intentionally heterogeneous: they include persistent structures,
relationships, semantic abstractions, behavioral abstractions and architectural constraints.
Equal status as a Core Concept does not imply an identical architectural role.

Each concept has a single, well-defined meaning throughout the paper. Implementations may
extend these concepts, but should not redefine them.

!!! info "Source of truth"

    The definitions below are the canonical glossary entries from
    [`references/terminology.md`](reference/terminology.md), presented in the order of
    [Chapter 8](paper/08-core-concepts.md), which remains authoritative. Each concept links to
    its section in the paper, where the full definition and its architectural consequences are
    given.

--8<-- "core-concepts.md"

## How the concepts fit together

The Core Concepts form a connected architectural graph, described in
[section 9.2](paper/09-architectural-model.md#92-architectural-relationships) and illustrated
on the [Architectural Model](architectural-model.md) page.

Not every concept changes at the same rate.
[Section 9.3](paper/09-architectural-model.md#93-persistence-and-change) distinguishes the
relatively persistent concepts (Ecosystem, Identity, Domain, Artifact, Semantics) from the
adaptive ones (Context, Delegation, Behavior, Event). That distinction allows architectural
stability without reducing operational flexibility.
