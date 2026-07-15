# 1. Introduction

## 1.1 About the Name

The name **POOKA** originally stood for **Personal Object-Oriented Knowledge Architecture**.

The concept originated from the practical challenge of organizing personal knowledge to enable more effective collaboration with AI. Initially, the focus was on structuring information, context and behavior within a personal knowledge environment.

As the underlying concepts evolved, it became clear that the architectural principles extended beyond personal knowledge management. The central question gradually shifted from *"How should I organize my own knowledge?"* to *"How should information be architected so that humans and AI can collaborate through a shared semantic structure?"*

Although the original acronym reflects the historical origin of the work, it no longer defines its scope. Today, **POOKA** refers to the architectural style itself. The original name has intentionally been preserved as a reference to the project's origin while allowing the architecture to evolve beyond its initial interpretation.

---

## 1.2 Purpose

The rapid adoption of generative AI has introduced a new way of working with information. Large Language Models have become increasingly capable of interpreting, generating, transforming and reasoning over knowledge. Yet the quality of collaboration between humans and AI remains highly dependent on the way information is organized, contextualized and governed.

Many current AI workflows reconstruct context during every interaction. Prompts are used to establish roles, context, behavioral expectations, terminology and relevant knowledge at runtime. While this provides considerable flexibility, it also makes collaboration dependent on prompt quality, repetition and conversational continuity. As a consequence, context remains transient, semantics remain implicit, and knowledge is difficult to reuse consistently across domains, tools and AI models.

POOKA addresses this challenge by defining context, semantics, governance and behavior as persistent architectural elements rather than transient prompt content. Instead of reconstructing these concepts during every interaction, POOKA defines them as part of the information architecture itself, shifting a significant part of the responsibility for context from runtime prompt engineering to architectural design.

POOKA defines an architectural style for **Human–AI Information Architecture**. It defines a conceptual model in which information, semantics, governance and behavior are organized explicitly, allowing humans and AI systems to collaborate from a shared architectural foundation.

POOKA does not define software, programming models, storage technologies or implementation frameworks. It defines a design philosophy for organizing information independently of AI models, applications and technical implementations.

The purpose of this paper is to define that architectural philosophy, establish a common conceptual language, and provide a foundation for discussion, implementation, evaluation and further refinement.
