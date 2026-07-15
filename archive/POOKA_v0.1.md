# POOKA

## An Architectural Style for Human–AI Information Architecture

### A Design Paper

---

**Author**  
Maarten Meijer

**Status**  
Draft

**Version**  
0.1

**Date**  
July 2026

---

# 1. Introduction

## 1.1 About the Name

The name **POOKA** originally stood for **Personal Object-Oriented Knowledge Architecture**.

The concept originated from the practical challenge of organizing personal knowledge to enable more effective collaboration with AI. Initially, the focus was on structuring information, context and behavior within a personal knowledge environment.

As the underlying concepts evolved, it became clear that the architectural principles extended beyond personal knowledge management. The central question gradually shifted from *"How should I organize my own knowledge?"* to *"How should information be architected so that humans and AI can collaborate through a shared semantic structure?"*

Although the original acronym reflects the historical origin of the work, it no longer defines its scope. Today, **POOKA** refers to the architectural style itself. The original name has intentionally been preserved as a reference to the project's origin while allowing the architecture to evolve beyond its initial interpretation.

---

## 1.2 Purpose

The rapid adoption of generative AI has introduced a new way of working with information. Large Language Models have become increasingly capable of interpreting, generating, transforming and reasoning over knowledge. Yet the quality of collaboration between humans and AI remains highly dependent on the way information is organized, contextualized and governed.

Most current AI workflows reconstruct context during every interaction. Prompts are used to establish roles, context, behavioral expectations, terminology and relevant knowledge at runtime. While this provides considerable flexibility, it also makes collaboration dependent on prompt quality, repetition and conversational continuity. As a consequence, context remains transient, semantics remain implicit, and knowledge is difficult to reuse consistently across domains, tools and AI models.

POOKA addresses this challenge by defining context, semantics, governance and behavior as persistent architectural elements rather than transient prompt content. Instead of reconstructing these concepts during every interaction, POOKA defines them as part of the information architecture itself, shifting a significant part of the responsibility for context from runtime prompt engineering to architectural design.

POOKA defines an architectural style for **Human–AI Information Architecture**. It defines a conceptual model in which information, semantics, governance and behavior are organized explicitly, allowing humans and AI systems to collaborate from a shared architectural foundation.

POOKA does not define software, programming models, storage technologies or implementation frameworks. It defines a design philosophy for organizing information independently of AI models, applications and technical implementations.

The purpose of this paper is to define that architectural philosophy, establish a common conceptual language, and provide a foundation for discussion, implementation, evaluation and further refinement.

# 2. Status

POOKA is an architectural philosophy emerging from practical experimentation with Human–AI collaboration.

It is not a scientific theory, formal standard or industry specification. The concepts presented in this paper are design proposals derived from practical observation, iterative refinement and architectural reasoning. They have not been empirically validated through controlled scientific research and should therefore not be interpreted as established facts.

POOKA intentionally builds upon existing knowledge from information architecture, software architecture, knowledge management, object-oriented design, graph-based modeling, identity management and AI-assisted knowledge work. Where existing concepts adequately describe a problem, they are adopted rather than reinvented. Where existing concepts do not sufficiently address the architectural challenges of Human–AI collaboration, POOKA introduces new abstractions and relationships.

This paper therefore should be read as a design paper: an invitation to discussion, implementation, validation and further evolution.

# 3. Scope

POOKA defines an architectural style for organizing information intended for collaboration between humans and AI.

The architecture focuses on the explicit organization of meaning, context, governance and behavior. It defines a conceptual model that can be implemented using different technologies, storage mechanisms and AI systems.

POOKA intentionally does not prescribe:

- programming languages;
- software architectures;
- database technologies;
- file formats;
- AI models;
- implementation frameworks;
- user interfaces.

Likewise, POOKA does not attempt to replace existing architectural disciplines such as Enterprise Architecture, Information Architecture, Knowledge Management or Identity & Access Management. Instead, it provides an architectural perspective specifically focused on sustainable Human–AI collaboration.

Any implementation that preserves the conceptual model while using different technical solutions may still conform to POOKA.

# 4. Foundational Assumptions

POOKA is based on several architectural assumptions. These assumptions are not presented as universally proven truths but as the foundation upon which the architecture has been developed.

## Information outlives interaction

Conversations are temporary. Information is persistent. Sustainable Human–AI collaboration requires knowledge to exist independently of individual conversations.

## Meaning should be explicit

Information becomes more reusable when its semantics are represented explicitly rather than being inferred from conversational context.

## Context is architecture

Context should not primarily be reconstructed through prompts. It should be represented as a persistent architectural concept.

## Governance is part of information

Questions such as who may act, on whose behalf, under which conditions and within which boundaries belong to the architecture itself rather than to implementation logic.

## Structure precedes automation

AI should operate on well-defined structures instead of compensating for missing structure through increasingly complex prompts.

## Human judgement remains external

AI may analyse, suggest, summarize, transform and reason. Responsibility for judgement and decision-making remains outside the AI itself.

## Architectures should survive implementations

Architectural concepts should remain applicable regardless of future AI models, software platforms or storage technologies.

# 5. Design Principles

The following Design Principles form the architectural foundation of POOKA. They describe how information should be organized to enable sustainable collaboration between humans and AI. They are normative principles that guide the architecture itself rather than specific technical implementations.

## 5.1 Meaning Before Mechanics

Architecture begins with meaning, not implementation.

Information should first describe what something is before defining how it is stored, processed or presented. Technologies, storage mechanisms and AI models evolve continuously; meaning should remain stable.

POOKA therefore models information independently from implementation technologies.

---

## 5.2 Context Before Prompt

Context is an architectural concept rather than a conversational construct.

Current AI workflows frequently establish context through prompts at runtime. While effective for individual interactions, this makes context transient and difficult to reuse consistently.

POOKA defines Context explicitly as part of the information architecture, allowing prompts to become consumers of context rather than its primary source.

---

## 5.3 Explicit Semantics

Semantics should never rely solely on interpretation.

Concepts, relationships and meaning should be represented explicitly wherever possible, reducing ambiguity for both humans and AI.

Explicit semantics improve consistency, discoverability and long-term maintainability of knowledge.

---

## 5.4 Explicit Relationships

Knowledge does not exist in isolation.

Relationships between concepts should be represented explicitly rather than inferred through textual proximity or conversational history.

Understanding often emerges from relationships rather than from individual information objects.

---

## 5.5 Boundaries Are Architecture

Boundaries define the architecture as much as the information itself.

Domains, Contexts and other architectural constructs require explicit boundaries that determine scope, visibility, ownership, semantics and behavior.

Boundaries enable multiple perspectives to coexist without unnecessary coupling.

---

## 5.6 Representation Must Be Explicit

An Actor never implicitly represents an Identity.

Whenever an Actor performs actions on behalf of an Identity, this relationship should be explicitly defined through Delegation.

Representation determines authority, responsibility and behavioral constraints and therefore forms part of the architecture itself.

---

## 5.7 Structure Before Automation

Artificial Intelligence performs best when operating on well-structured information.

Rather than compensating for missing structure through increasingly complex prompts, POOKA encourages explicit modeling of knowledge before introducing automation.

Automation should emerge from architecture rather than replace it.

---

## 5.8 Minimum Necessary Context

AI should only receive the information required to perform the intended task.

Providing unnecessary context increases complexity, computational cost and the likelihood of unintended reasoning.

POOKA therefore promotes the explicit selection of relevant Context rather than exposing complete knowledge environments by default.

---

## 5.9 Local First, Cloud When Necessary

Architectural decisions should preserve autonomy wherever practical.

Knowledge should remain under the control of its owning Identity whenever possible. External services and cloud-based AI can extend capabilities but should not become architectural dependencies without explicit reason.

This principle promotes portability, resilience and long-term sustainability.

---

## 5.10 Architectures Outlive Implementations

Architectural concepts should survive technological change.

POOKA intentionally separates conceptual architecture from implementation. Storage technologies, AI models, programming languages and software platforms may change over time without affecting the underlying architectural principles.

The architecture should remain valid even when today's technologies no longer exist.

# 6. Core Concepts

POOKA defines a small set of fundamental architectural concepts. Together these concepts establish a common language for organizing information, semantics, governance and behavior within Human–AI Information Architecture.

Each concept has a single, well-defined meaning throughout this paper. Implementations may extend these concepts, but should not redefine them.

---

## 6.1 Ecosystem

An **Ecosystem** defines the complete architectural environment within which one or more Identities, Actors, Domains, Contexts and Artifacts coexist.

An Ecosystem establishes the highest architectural boundary of a POOKA implementation. It provides the environment in which information, governance and behavior are organized.

An Ecosystem may represent an individual, a family, an organization, a community or any other coherent knowledge environment.

---

## 6.2 Identity

An **Identity** defines the person, organization or other identifiable entity for whom an Ecosystem exists.

Identity represents the enduring subject of the architecture rather than the individual Actors operating within it.

Multiple Actors may represent a single Identity through explicit Delegation.

---

## 6.3 Actor

An **Actor** defines any human, AI or technical system capable of performing actions within an Ecosystem.

Actors consume, create, modify and relate information according to the architectural constraints defined by POOKA.

An Actor never implicitly represents an Identity.

---

## 6.4 Delegation

**Delegation** defines how an Actor may represent an Identity.

Delegation specifies the scope, permissions, constraints and responsibilities under which an Actor operates.

Representation within POOKA is always explicit.

Delegation therefore forms the architectural bridge between Identity and Actor.

---

## 6.5 Domain

A **Domain** defines a durable and bounded knowledge environment.

Domains organize information around a coherent subject, objective or responsibility. They establish stable boundaries for knowledge, semantics, governance and behavior.

Domains are intended to remain relatively stable over time.

---

## 6.6 Context

A **Context** defines the active scope in which information is interpreted.

Contexts exist within Domains and provide the situational perspective required for collaboration between humans and AI.

Unlike Domains, Contexts are expected to change as work, conversations and objectives evolve.

---

## 6.7 Artifact

An **Artifact** defines any addressable unit of information.

Artifacts may represent documents, people, decisions, meetings, projects, ideas, tasks, datasets or other meaningful information objects.

Artifacts exist independently of the technology used to store them.

---

## 6.8 Relation

A **Relation** defines an explicit connection between architectural concepts.

Relations express meaning by describing how concepts are connected rather than relying upon textual proximity or implicit interpretation.

Relations may exist between Artifacts, Domains, Contexts, Actors or other architectural concepts.

---

## 6.9 Semantics

**Semantics** define the explicit meaning assigned to information.

Semantics describe what information represents rather than how it is stored or presented.

Explicit semantics reduce ambiguity and improve consistency for both humans and AI.

---

## 6.10 Behavior

**Behavior** defines how Actors or AI are expected, permitted or constrained to operate within the architecture.

Behavior may include operational rules, interaction patterns, stylistic guidance, reasoning constraints or other behavioral expectations.

Behavior is defined explicitly rather than embedded implicitly within prompts.

---

## 6.11 Boundary

A **Boundary** defines architectural separation.

Boundaries determine visibility, ownership, accessibility, semantic scope, behavioral scope and the conditions under which information may cross between architectural elements.

Boundaries are explicit architectural constructs rather than implementation details.

---

## 6.12 Event

An **Event** defines something that occurs at a specific point or period in time.

Events may create, modify or relate Artifacts, influence Context or trigger Behavior.

Unlike Artifacts, Events are inherently temporal and describe change rather than persistent knowledge.

# 7. Architectural Model

The architectural model describes how the Core Concepts interact to establish a sustainable environment for Human–AI collaboration.

Rather than focusing on software components or implementation details, POOKA models the architectural relationships between information, meaning, governance and behavior.

The architecture intentionally separates relatively stable concepts from concepts that are expected to change over time. This distinction allows knowledge to remain durable while enabling AI interactions to remain adaptive.

---

## 7.1 Architectural Layers

POOKA distinguishes three complementary architectural layers.

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

## 7.2 Architectural Relationships

The Core Concepts form a connected architectural graph.

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

## 7.3 Persistence and Change

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

## 7.4 Architectural Independence

The architectural model is independent of implementation technology.

The concepts defined by POOKA may be implemented using files, databases, graph technologies, object-oriented systems, document stores or future technologies not yet available.

Compliance with POOKA depends upon preserving the architectural concepts and their relationships rather than adopting a particular technical implementation.

# 8. Implementation Principles

POOKA intentionally separates architecture from implementation.

The architectural concepts defined by POOKA are independent of programming languages, storage technologies, AI models and software platforms. Multiple implementations may therefore conform to POOKA while making fundamentally different technical choices.

The purpose of this chapter is not to prescribe implementation, but to describe the characteristics that a conforming implementation should preserve.

---

## 8.1 Preserve Meaning

The primary responsibility of an implementation is to preserve meaning.

Architectural concepts such as Identity, Domain, Context and Artifact should remain explicit regardless of the underlying technology.

Implementations should avoid reducing architectural concepts to technical constructs that obscure their semantic meaning.

---

## 8.2 Preserve Relationships

Relationships between architectural concepts should remain explicit.

Implementations may represent relationships using references, graphs, object references, hyperlinks or other mechanisms, provided the relationship itself remains identifiable and meaningful.

Relationships should never rely solely on textual proximity or implicit interpretation.

---

## 8.3 Preserve Boundaries

Architectural Boundaries should remain visible throughout the implementation.

Whether implemented using folders, databases, access control, namespaces or graph partitions, Boundaries should continue to express ownership, visibility, responsibility and semantic scope.

Boundaries should not become implementation details.

---

## 8.4 Separate Architecture from AI

Artificial Intelligence consumes the architecture but does not define it.

AI models should operate upon the architectural concepts rather than replacing them.

Changes in AI technology should not require changes to the conceptual architecture.

---

## 8.5 Design Before Prompt

Prompt engineering remains a valuable implementation technique.

POOKA does not replace prompts; it reduces their architectural responsibility.

Information that is stable across interactions should preferably be represented as architecture rather than repeatedly reconstructed through prompts.

Prompt engineering therefore shifts from defining architecture at runtime towards consuming architecture during execution.

---

## 8.6 Technology Independence

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

## 8.7 Evolution

Architectures evolve.

Implementations should therefore allow Domains, Contexts, Behavior, Relations and Semantics to evolve without requiring structural redesign.

POOKA encourages iterative refinement while preserving conceptual consistency over time.

# 9. Discussion

POOKA does not attempt to replace existing disciplines such as Information Architecture, Enterprise Architecture, Knowledge Management, Identity & Access Management or software architecture. Instead, it introduces an architectural perspective specifically focused on sustainable collaboration between humans and AI.

Many of the concepts described in POOKA build upon existing architectural principles. Concepts such as explicit semantics, bounded contexts, data minimization, local-first thinking, object-oriented design and graph-based relationships have well-established foundations in existing literature and practice. POOKA does not seek to redefine these concepts, but to integrate them into a coherent architectural style for Human–AI Information Architecture.

The primary contribution of POOKA is therefore not the invention of entirely new concepts, but the architectural synthesis of existing principles into a model that explicitly separates information, governance and behavior while treating context as a persistent architectural construct rather than transient conversational state.

POOKA should not be interpreted as a universal solution for every AI application. Different domains, organizations and technical environments may require alternative architectural decisions or additional concepts. The architecture intentionally remains technology-independent and leaves implementation choices to individual implementations.

As AI technology continues to evolve, new architectural challenges will inevitably emerge. POOKA should therefore be regarded as an evolving architectural philosophy rather than a fixed standard. Its long-term value depends on practical application, critical evaluation and continuous refinement by the broader community.

The concepts presented in this paper are intended to provide a common language for discussing Human–AI Information Architecture. Whether individual concepts remain unchanged, evolve or are eventually replaced is less important than establishing an explicit architectural dialogue around the organization of information for sustainable Human–AI collaboration.

# 10. Future Evolution

POOKA is intentionally designed as an evolving architectural philosophy.

The concepts presented in this paper should not be regarded as complete or final. As Human–AI collaboration continues to evolve, new architectural challenges, implementation patterns and conceptual refinements are expected to emerge.

Future evolution of POOKA may include, but is not limited to:

- refinement of the Core Concepts and their relationships;
- additional architectural patterns for specific domains;
- formal semantic models;
- reference implementations across different technologies;
- interoperability with existing architectural standards;
- methods for validating architectural consistency;
- governance models for collaborative knowledge environments.

The long-term development of POOKA depends on practical application, critical discussion and contributions from a broader community of practitioners, architects and researchers.

Architectural evolution should preserve conceptual consistency while allowing the model to adapt to new technologies, new forms of collaboration and future generations of AI.

# 11. Conclusion

Artificial Intelligence continues to advance rapidly. Models become more capable, interactions become more natural and new applications emerge almost daily. Yet sustainable Human–AI collaboration depends on more than increasingly capable AI systems. It depends on the architecture through which information, meaning, context, governance and behavior are organized.

POOKA defines an architectural style that approaches this challenge from the perspective of information architecture rather than prompt engineering or software implementation. By treating context, semantics, governance and behavior as explicit architectural concepts, POOKA aims to establish a durable foundation upon which both humans and AI can collaborate.

The architecture intentionally remains independent of specific technologies, AI models and implementation choices. Its purpose is not to prescribe a single way of building Human–AI systems, but to provide a coherent conceptual framework that can be discussed, implemented, challenged and refined.

Whether POOKA ultimately proves valuable will not be determined by this paper alone, but by its ability to support practical implementations, encourage architectural dialogue and evolve through continued application and critical evaluation.

Like every architectural style, POOKA will ultimately be judged not by the elegance of its concepts, but by the quality, longevity and adaptability of the systems built upon it.

