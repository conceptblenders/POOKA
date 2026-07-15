# 7. Design Principles

The following Design Principles form the architectural foundation of POOKA. They describe how information should be organized to enable sustainable collaboration between humans and AI. They are normative principles that guide the architecture itself rather than specific technical implementations.

## 7.1 Meaning Before Mechanics

Architecture begins with meaning, not implementation.

Information should first describe what something is before defining how it is stored, processed or presented. Technologies, storage mechanisms and AI models evolve continuously; meaning should remain stable.

POOKA therefore models information independently from implementation technologies.

---

## 7.2 Context Before Prompt

Context is an architectural concept rather than a conversational construct.

Current AI workflows frequently establish context through prompts at runtime. While effective for individual interactions, this makes context transient and difficult to reuse consistently.

POOKA defines Context explicitly as part of the information architecture, allowing prompts to become consumers of context rather than its primary source. It is the representation of Context that persists; the Context itself remains adaptive.

---

## 7.3 Explicit Semantics

Semantics should never rely solely on interpretation.

Concepts, relationships and meaning should be represented explicitly wherever possible, reducing ambiguity for both humans and AI.

Explicit semantics are intended to improve consistency, discoverability and long-term maintainability of knowledge.

---

## 7.4 Explicit Relationships

Knowledge does not exist in isolation.

Relationships between concepts should be represented explicitly rather than inferred through textual proximity or conversational history.

Understanding often emerges from relationships rather than from individual information objects.

---

## 7.5 Boundaries Are Architecture

Boundaries define the architecture as much as the information itself.

Domains, Contexts and other architectural constructs require explicit boundaries that determine scope, visibility, ownership, semantics and behavior.

Boundaries enable multiple perspectives to coexist without unnecessary coupling.

---

## 7.6 Representation Must Be Explicit

An Actor never implicitly represents an Identity.

Whenever an Actor performs actions on behalf of an Identity, this relationship should be explicitly defined through Delegation.

Representation determines authority, responsibility and behavioral constraints and therefore forms part of the architecture itself.

---

## 7.7 Structure Before Automation

POOKA assumes that Artificial Intelligence operates most effectively on well-structured information.

Rather than compensating for missing structure through increasingly complex prompts, POOKA encourages explicit modeling of knowledge before introducing automation.

Automation should emerge from architecture rather than replace it.

---

## 7.8 Minimum Necessary Context

AI should only receive the information required to perform the intended task.

Providing unnecessary context is expected to increase complexity, computational cost and the likelihood of unintended reasoning.

POOKA therefore promotes the explicit selection of relevant Context rather than exposing complete knowledge environments by default.

---

## 7.9 Local First, Cloud When Necessary

Architectural decisions should preserve autonomy wherever practical.

Knowledge should remain under the control of its owning Identity whenever possible. External services and cloud-based AI can extend capabilities but should not become architectural dependencies without explicit reason.

This principle promotes portability, resilience and long-term sustainability.

---

## 7.10 Architectures Outlive Implementations

Architectural concepts should survive technological change.

POOKA intentionally separates conceptual architecture from implementation. Storage technologies, AI models, programming languages and software platforms may change over time without affecting the underlying architectural principles.

The architecture should remain valid even when today's technologies no longer exist.
