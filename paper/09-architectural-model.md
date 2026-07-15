# 9. Architectural Model

The architectural model describes how the Core Concepts interact to establish a sustainable environment for Human–AI collaboration.

Rather than focusing on software components or implementation details, POOKA models the architectural relationships between information, meaning, governance and behavior.

The architecture intentionally separates relatively stable concepts from concepts that are expected to change over time. This distinction allows knowledge to remain durable while enabling AI interactions to remain adaptive.

---

## 9.1 Architectural Layers

POOKA distinguishes three complementary architectural layers. These layers are illustrated in Figure 3 (diagrams/architectural-layers.drawio).

### Knowledge Layer

The Knowledge Layer describes what exists.

It contains the persistent representation of knowledge, independent of any specific interaction. Concepts such as Domains, Contexts, Artifacts, Relations and Semantics define the informational structure upon which collaboration is based.

Knowledge should remain stable regardless of which Actor accesses it or which AI model processes it.

---

### Governance Layer

The Governance Layer defines who may act and under which conditions.

Identity, Actor, Delegation and Boundaries determine authority, representation, ownership and responsibility throughout the architecture.

Governance is considered part of the information architecture rather than application logic.

---

### Behavior Layer

The Behavior Layer defines how collaboration takes place.

Behavior specifies how Actors, including AI systems, are expected or permitted to operate within a particular Context.

Unlike knowledge, behavior is intentionally adaptive. It may vary between Domains, Contexts or Delegations while remaining constrained by the architectural model.

---

## 9.2 Architectural Relationships

The Core Concepts form a connected architectural graph. This graph is illustrated in Figure 2 (diagrams/core-concepts.drawio).

An Ecosystem contains one or more Identities.

An Identity may delegate representation to one or more Actors.

Actors operate within one or more Contexts.

Contexts exist within Domains.

Domains contain Artifacts.

Artifacts are connected through explicit Relations.

Semantics define the meaning of architectural concepts and their relationships.

Behavior governs how Actors interact with information.

Boundaries constrain the movement of information, semantics and behavior between architectural elements.

Events introduce change into the architecture by creating, modifying or relating Artifacts and Contexts over time.

---

## 9.3 Persistence and Change

Not every architectural concept changes at the same rate.

POOKA distinguishes between relatively persistent architectural concepts and concepts that are expected to evolve continuously.

Examples of relatively persistent concepts include:

- Ecosystem
- Identity
- Domain
- Artifact
- Semantics

Examples of adaptive concepts include:

- Context
- Delegation
- Behavior
- Event

This distinction allows architectural stability without reducing operational flexibility.

---

## 9.4 Architectural Independence

The architectural model is independent of implementation technology.

The concepts defined by POOKA may be implemented using files, databases, graph technologies, object-oriented systems, document stores or future technologies not yet available.

Compliance with POOKA depends upon preserving the architectural concepts and their relationships rather than adopting a particular technical implementation.

---

## 9.5 An Illustrative Example

The following example illustrates how the Core Concepts operate together. It is deliberately conceptual and technology-independent: it describes an architecture, not an implementation, and none of its elements prescribe any particular tool, platform or product.

Consider an independent researcher who organizes a personal knowledge environment as an **Ecosystem**.

The researcher is represented as an **Identity**: the persistent subject within the Ecosystem, remaining stable regardless of which tools or assistants are used.

Two **Actors** operate within the Ecosystem: the researcher, acting as a human Actor, and an AI assistant.

The AI assistant does not implicitly represent the researcher. An explicit **Delegation** defines that the assistant may organize and summarize research material on behalf of the researcher, within a defined scope and without the authority to publish results or make decisions.

The Ecosystem contains a durable **Domain** for the research work, alongside other Domains such as personal administration.

Within the research Domain, the study currently being carried out forms a **Context**: the active scope in which information is interpreted. When the researcher begins a new study, the Context changes while the Domain remains stable. Each Context is represented persistently as part of the architecture, even though the active Context itself is adaptive.

The research Domain contains **Artifacts** such as interview notes, source materials and a draft article.

When a new interview takes place, this **Event** introduces change into the architecture: it creates a new interview-notes Artifact and influences the active Context.

An explicit **Relation** connects the draft article to the interview notes on which it is based, so that this connection does not depend on textual proximity or on the memory of a conversation.

**Semantics** define explicitly what these Artifacts represent: what an interview note is, what a source is and how they differ. The researcher and the AI assistant can therefore interpret the same information consistently.

**Behavior** defines how the AI assistant is expected to operate within this Context: for example, that summaries must remain neutral and must be distinguishable from the researcher's own conclusions.

A **Boundary** separates the research Domain from the personal administration Domain. The Delegation grants the AI assistant access to the former but not to the latter, and information does not cross this Boundary implicitly.

The same architecture could be realized using files, databases, graph structures or technologies that do not yet exist, and it corresponds to the Personal Knowledge Environment pattern described in Chapter 10.
