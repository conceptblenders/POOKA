# ADR-001: Why These Core Concepts?

## Status

Accepted

## Context

POOKA defines a fixed set of Core Concepts (Ecosystem, Identity, Actor, Delegation, Domain, Context, Artifact, Relation, Semantics, Behavior, Boundary, Event). A reviewer observed that these concepts are not all of the same kind: some (Ecosystem, Identity, Domain, Context, Artifact, Event) read as architectural entities, while others (Relation, Delegation, Boundary, Semantics, Behavior) read as relationships, constraints, or cross-cutting aspects. The reviewer questioned whether concepts of such different kinds should be presented as equivalent Core Concepts.

Before accepting or rejecting that observation, we assessed whether it is architecturally valid. That assessment rests on the following positions.

**Why POOKA defines a fixed set of Core Concepts.** An architectural style is defined by a vocabulary of primitive abstractions together with the rules by which they combine. A fixed, small vocabulary is what makes the style describable, teachable and stable: the principles, the layer model, the relationships and the conformance criteria all refer to these concepts. The set is deliberately bounded so that it captures the minimum abstractions required to describe Human-AI Information Architecture, without expanding into implementation detail.

**What qualifies as a Core Concept.** A Core Concept is a first-class, primitive abstraction of the style that carries a single stable meaning, is not reducible to a combination of the other concepts, and is required to describe or reason about the architecture. The test is whether the architecture must name, constrain and reason about the abstraction explicitly and independently, not whether the abstraction happens to be a thing.

**Why a Core Concept need not represent a physical entity.** The qualifying test above is independent of ontological category. An abstraction earns first-class status by being primitive, load-bearing and necessary, not by being an entity. Requiring every Core Concept to be an entity would exclude abstractions that the architecture genuinely depends on.

**Why relationships, constraints, semantic abstractions and behavioral abstractions may legitimately be first-class.** Reifying a relationship, a constraint or an aspect as a first-class concept is standard architectural practice whenever that element carries its own meaning and rules and must be reasoned about on its own terms. A relationship that has its own attributes and constraints (such as Delegation, which carries scope, permissions, constraints and responsibilities) is legitimately first-class. A separation that is architecturally decisive (Boundary) is legitimately first-class. Meaning (Semantics) and expected or permitted conduct (Behavior) are legitimately first-class in a style whose purpose is the explicit organization of meaning and governance. Their kind is orthogonal to their status as Core Concepts.

**Why the reviewer correctly identified heterogeneous concept types.** The observation is factually correct: the Core Concepts do belong to different kinds. Some are structural entities, some are reified relationships (Relation, Delegation), and some are cross-cutting aspects or constraints (Semantics, Behavior, Boundary). Presenting them as a single undifferentiated list can make distinct kinds appear equivalent and can create the appearance of overlap.

**Why this heterogeneity is intentional and architecturally valid.** The heterogeneity is a property of the vocabulary, not a defect in it. An architectural style is expected to name entities, the relationships between them, and the constraints and aspects that govern them within one coherent vocabulary. Removing or demoting the relational, constraint-based or aspectual concepts would discard abstractions that the model requires. The heterogeneity therefore reflects the scope of the architecture, and the concept set is sound.

**Why the architectural model itself remains unchanged.** Because every concept is primitive, load-bearing and irreducible, none should be removed, merged, renamed or redefined. Changing the concept set would destabilize the principles, the layer model, the relationship graph, the patterns and the conformance definition, all of which depend on the current vocabulary, and would solve a presentation problem by damaging a correct model.

**Why only the presentation and explanation should be improved.** The reviewer's concern is real but sits at the level of conceptual organization, not the concept set. The concepts of different kinds are equivalent in status (all first-class) but differ in role. Making those roles explicit, as a descriptive lens reconciled with the existing layer model, resolves the concern without altering the architecture.

## Decision

Keep the existing Core Concept model unchanged. Clarify its presentation and rationale.

The set of Core Concepts and their definitions remain as they are. No concept is added, removed, renamed or redefined. The improvement is limited to explaining that Core Concepts may be of different kinds (entities, relationships, constraints, semantic abstractions and behavioral abstractions) and that all of them are legitimately first-class. Any role-based classification introduced for clarity is descriptive only, permits a concept to hold more than one role, is reconciled with the existing layer model rather than competing with it, and carries no new architectural obligations. It must not establish a two-tier hierarchy: relational, constraint-based and aspectual concepts remain fully first-class.

## Consequences

Easier:
- The rationale for the Core Concepts becomes defensible against the objection that they mix kinds, because mixing kinds is shown to be intentional and standard.
- Readers can understand each concept's role without re-deriving the entity, relationship and aspect distinctions themselves, reducing the appearance of overlap.
- The concept set, the principles, the layers, the relationships, the patterns and the conformance criteria remain stable, since nothing in the model changes.

Harder or requiring care:
- A role classification must avoid false crispness (some concepts are multi-role) and must be reconciled with the Knowledge, Governance and Behavior layers to prevent two overlapping classifications.
- The distinction between first-class status (equal for all Core Concepts) and role (different per concept) must be stated carefully so that clarification is not misread as demotion or as a change to the model.

This decision records an architectural position only. It does not modify the POOKA Design Paper; any later improvement to the paper's presentation is a separate, paper-level action outside this ADR.
