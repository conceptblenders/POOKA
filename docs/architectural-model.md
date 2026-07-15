---
title: Architectural Model
description: >-
  How the POOKA Core Concepts interact: the Knowledge, Governance and Behavior layers,
  the Core Concepts graph, and prompt context contrasted with persistent architecture.
---

# Architectural Model

The architectural model describes how the Core Concepts interact to establish a sustainable
environment for Human–AI collaboration.

Rather than focusing on software components or implementation details, POOKA models the
architectural relationships between information, meaning, governance and behavior.

The architecture intentionally separates relatively stable concepts from concepts that are
expected to change over time. This distinction allows knowledge to remain durable while
enabling AI interactions to remain adaptive.

## Prompt context and architectural context

In architectural terms, a prompt is the means by which context and behavior are supplied to an
AI system at the moment of interaction. Understood this way, a prompt is a runtime carrier of
context rather than a persistent part of the information architecture.

POOKA treats information architecture as the primary carrier of context. Persistence here
refers to the architectural representation of concepts rather than to their content: a Context
is represented persistently as part of the information architecture, while the Context itself
remains adaptive.

--8<-- "figures/prompt-vs-architecture.md"

[Read Chapter 2: The Architectural Challenge](paper/02-architectural-challenge.md)

## The three architectural viewpoints

POOKA distinguishes three complementary architectural layers. They represent distinct
architectural viewpoints on the same model rather than isolated partitions.

--8<-- "figures/architectural-layers.md"

### Knowledge viewpoint

The Knowledge Layer describes **what exists**. It contains the persistent representation of
knowledge, independent of any specific interaction. Concepts such as Domains, Contexts,
Artifacts, Relations and Semantics define the informational structure upon which collaboration
is based.

Knowledge should remain stable regardless of which Actor accesses it or which AI model
processes it.

### Governance viewpoint

The Governance Layer defines **who may act and under which conditions**. Identity, Actor,
Delegation and Boundaries determine authority, representation, ownership and responsibility
throughout the architecture.

Governance is considered part of the information architecture rather than application logic.

### Behavior viewpoint

The Behavior Layer defines **how collaboration takes place**. Behavior specifies how Actors,
including AI systems, are expected or permitted to operate within a particular Context.

Unlike knowledge, behavior is intentionally adaptive. It may vary between Domains, Contexts or
Delegations while remaining constrained by the architectural model.

[Read section 9.1: Architectural Layers](paper/09-architectural-model.md#91-architectural-layers)

## The Core Concepts graph

The Core Concepts form a connected architectural graph. An Ecosystem contains one or more
Identities. An Identity may delegate representation to one or more Actors. Actors operate
within one or more Contexts. Contexts exist within Domains. Domains contain Artifacts.
Artifacts are connected through explicit Relations. Semantics define the meaning of
architectural concepts and their relationships. Behavior governs how Actors interact with
information. Boundaries constrain the movement of information, semantics and behavior between
architectural elements. Events introduce change into the architecture over time.

--8<-- "figures/core-concepts.md"

[Read section 9.2: Architectural Relationships](paper/09-architectural-model.md#92-architectural-relationships)
· [View the twelve Core Concepts](core-concepts.md)

## An illustrative example

The paper closes the architectural model with a deliberately conceptual, technology-independent
example: an independent researcher who organizes a personal knowledge environment as an
Ecosystem, an AI assistant that never implicitly represents the researcher but operates under
an explicit Delegation, a durable research Domain, a Context that changes as studies change,
and a Boundary that separates research from personal administration.

The same architecture could be realized using files, databases, graph structures or
technologies that do not yet exist.

[Read section 9.5: An Illustrative Example](paper/09-architectural-model.md#95-an-illustrative-example)

## Architectural independence

The architectural model is independent of implementation technology. The concepts defined by
POOKA may be implemented using files, databases, graph technologies, object-oriented systems,
document stores or future technologies not yet available.

Compliance with POOKA depends upon preserving the architectural concepts and their
relationships rather than adopting a particular technical implementation.

[Read Chapter 9: Architectural Model](paper/09-architectural-model.md)
· [Read Chapter 10: Architectural Patterns](paper/10-architectural-patterns.md)
