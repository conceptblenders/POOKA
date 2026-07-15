---
title: Design Principles
description: >-
  The ten Design Principles that form the architectural foundation of POOKA, from
  Meaning Before Mechanics to Architectures Outlive Implementations.
---

# Design Principles

The following Design Principles form the architectural foundation of POOKA. They describe how
information should be organized to enable sustainable collaboration between humans and AI.
They are normative principles that guide the architecture itself rather than specific technical
implementations.

!!! info "Source of truth"

    Each principle below carries its canonical title and its opening statement verbatim from
    [Chapter 7](paper/07-design-principles.md), which remains authoritative. Follow the link
    under a principle for its full rationale.

--8<-- "design-principles.md"

## From principle to implementation

The Design Principles guide the architecture. [Chapter 11](paper/11-implementation-principles.md)
describes what a conforming implementation should preserve, and
[section 11.8](paper/11-implementation-principles.md#118-conformance) defines conformance:
an implementation conforms to POOKA when it preserves the Core Concepts, their Relations and
their Boundaries, maintains the conceptual distinction between the Knowledge, Governance and
Behavior layers, and remains consistent with these Design Principles.

Conformance is a matter of architectural fidelity rather than certification. The paper defines
no compliance tests, certification criteria or mandatory technologies.
