# 8. Core Concepts

POOKA defines a small set of fundamental architectural concepts. Together these concepts establish a common language for organizing information, semantics, governance and behavior within Human–AI Information Architecture.

POOKA intentionally limits itself to a small set of Core Concepts. These concepts are not intended to describe every aspect of knowledge or collaboration, but to capture the architectural abstractions considered necessary to describe Human–AI Information Architecture. Further detail is expected to emerge within implementations and domains rather than within the architecture itself.

The Core Concepts are intentionally heterogeneous: they include persistent structures, relationships, semantic abstractions, behavioral abstractions and architectural constraints. All are presented as Core Concepts because each represents an irreducible architectural abstraction required to describe a POOKA-conformant Human–AI Information Architecture. Equal status as a Core Concept therefore does not imply an identical architectural role.

Each concept has a single, well-defined meaning throughout this paper. Implementations may extend these concepts, but should not redefine them. The Core Concepts and their relationships are illustrated in Figure 2 (diagrams/core-concepts.drawio).

---

## 8.1 Ecosystem

An **Ecosystem** defines the complete architectural environment within which one or more Identities, Actors, Domains, Contexts and Artifacts coexist.

An Ecosystem establishes the highest architectural boundary of a POOKA implementation. It provides the environment in which information, governance and behavior are organized.

An Ecosystem may represent an individual, a family, an organization, a community or any other coherent knowledge environment.

---

## 8.2 Identity

An **Identity** represents a persistent person, organization or other identifiable subject within an Ecosystem.

Identity represents the enduring subject of the architecture rather than the individual Actors operating within it.

Multiple Actors may represent a single Identity through explicit Delegation.

---

## 8.3 Actor

An **Actor** defines any human, AI or technical system capable of performing actions within an Ecosystem.

Actors consume, create, modify and relate information according to the architectural constraints defined by POOKA.

An Actor never implicitly represents an Identity.

---

## 8.4 Delegation

**Delegation** defines how an Actor may represent an Identity.

Delegation specifies the scope, permissions, constraints and responsibilities under which an Actor operates.

Representation within POOKA is always explicit.

Delegation therefore forms the architectural bridge between Identity and Actor.

---

## 8.5 Domain

A **Domain** defines a durable and bounded knowledge environment.

Domains organize information around a coherent subject, objective or responsibility. They establish stable boundaries for knowledge, semantics, governance and behavior.

Domains are intended to remain relatively stable over time.

---

## 8.6 Context

A **Context** defines the active scope in which information is interpreted.

Contexts exist within Domains and provide the situational perspective required for collaboration between humans and AI.

Unlike Domains, Contexts are expected to change as work, conversations and objectives evolve.

---

## 8.7 Artifact

An **Artifact** defines any addressable unit of information.

Artifacts may represent documents, people, decisions, meetings, projects, ideas, tasks, datasets or other meaningful information objects.

Artifacts exist independently of the technology used to store them.

---

## 8.8 Relation

A **Relation** defines an explicit connection between architectural concepts.

Relations express meaning by describing how concepts are connected rather than relying upon textual proximity or implicit interpretation.

Relations may exist between Artifacts, Domains, Contexts, Actors or other architectural concepts.

---

## 8.9 Semantics

**Semantics** define the explicit meaning assigned to information.

Semantics describe what information represents rather than how it is stored or presented.

Explicit semantics are intended to reduce ambiguity and improve consistency for both humans and AI.

---

## 8.10 Behavior

**Behavior** defines how Actors or AI are expected, permitted or constrained to operate within the architecture.

Behavior may include operational rules, interaction patterns, stylistic guidance, reasoning constraints or other behavioral expectations.

Behavior is defined explicitly rather than embedded implicitly within prompts.

---

## 8.11 Boundary

A **Boundary** defines architectural separation.

Boundaries determine visibility, ownership, accessibility, semantic scope, behavioral scope and the conditions under which information may cross between architectural elements.

Boundaries are explicit architectural constructs rather than implementation details.

---

## 8.12 Event

An **Event** defines something that occurs at a specific point or period in time.

Events may create, modify or relate Artifacts, influence Context or trigger Behavior.

Unlike Artifacts, Events are inherently temporal and describe change rather than persistent knowledge.
