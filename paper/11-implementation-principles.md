# 11. Implementation Principles

POOKA intentionally separates architecture from implementation.

The architectural concepts defined by POOKA are independent of programming languages, storage technologies, AI models and software platforms. Multiple implementations may therefore conform to POOKA while making fundamentally different technical choices.

The purpose of this chapter is not to prescribe implementation, but to describe the characteristics that a conforming implementation should preserve.

---

## 11.1 Preserve Meaning

The primary responsibility of an implementation is to preserve meaning.

Architectural concepts such as Identity, Domain, Context and Artifact should remain explicit regardless of the underlying technology.

Implementations should avoid reducing architectural concepts to technical constructs that obscure their semantic meaning.

---

## 11.2 Preserve Relationships

Relationships between architectural concepts should remain explicit.

Implementations may represent relationships using references, graphs, object references, hyperlinks or other mechanisms, provided the relationship itself remains identifiable and meaningful.

Relationships should never rely solely on textual proximity or implicit interpretation.

---

## 11.3 Preserve Boundaries

Architectural Boundaries should remain visible throughout the implementation.

Whether implemented using folders, databases, access control, namespaces or graph partitions, Boundaries should continue to express ownership, visibility, responsibility and semantic scope.

Boundaries should not become implementation details.

---

## 11.4 Separate Architecture from AI

Artificial Intelligence consumes the architecture but does not define it.

AI models should operate upon the architectural concepts rather than replacing them.

Changes in AI technology should not require changes to the conceptual architecture.

---

## 11.5 Design Before Prompt

Prompt engineering remains a valuable implementation technique.

POOKA does not replace prompts; it reduces their architectural responsibility.

Information that is stable across interactions should preferably be represented as architecture rather than repeatedly reconstructed through prompts.

Prompt engineering therefore shifts from defining architecture at runtime towards consuming architecture during execution.

---

## 11.6 Technology Independence

A POOKA implementation should remain portable.

The architecture should not become dependent on any particular:

- AI model;
- software platform;
- storage technology;
- programming language;
- file format;
- cloud provider;
- vendor ecosystem.

Technology choices may change over time while preserving the architectural model.

---

## 11.7 Evolution

Architectures evolve.

Implementations should therefore allow Domains, Contexts, Behavior, Relations and Semantics to evolve without requiring structural redesign.

POOKA encourages iterative refinement while preserving conceptual consistency over time.

---

## 11.8 Conformance

Conformance to POOKA is conceptual rather than technical.

An implementation conforms to POOKA when it preserves the Core Concepts, their Relations and their Boundaries, maintains the conceptual distinction between the Knowledge, Governance and Behavior layers, and remains consistent with the Design Principles. These layers represent distinct architectural viewpoints on the same model rather than isolated partitions; conformance requires preserving their conceptual distinctions, not separating the concepts themselves. The architectural meaning of each concept should remain explicit and recognizable regardless of the technologies used to represent it.

Conformance therefore depends on preserving architecture rather than adopting particular tools. Two implementations may make entirely different technical choices and both conform, provided each retains the concepts, relationships and governance the architecture defines.

Conformance is a matter of architectural fidelity rather than certification. This paper defines no compliance tests, certification criteria or mandatory technologies. An implementation may preserve the architecture more or less completely, and partial adoption remains meaningful as long as the concepts it uses retain their defined meaning.
