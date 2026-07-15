---
title: POOKA
description: >-
  POOKA is an architectural style for Human-AI Information Architecture. It defines
  context, semantics, governance and behavior as persistent architectural elements
  rather than transient prompt content.
hide:
  - navigation
---

<div class="pooka-hero" markdown="1">
<h1 class="pooka-hero__title"><span class="pooka-mark pooka-hero__mark" role="img" aria-label="POOKA"></span></h1>

<p class="pooka-hero__subtitle">An Architectural Style for Human–AI Information Architecture</p>

<p class="pooka-hero__lead">POOKA defines a conceptual model in which information, semantics, governance
and behavior are organized explicitly, allowing humans and AI systems to collaborate from a
shared architectural foundation.</p>
</div>

--8<-- "status.md"

## The architectural challenge

Many current AI workflows reconstruct context during every interaction. Prompts are used to
establish roles, context, behavioral expectations, terminology and relevant knowledge at
runtime. While this provides considerable flexibility, it also makes collaboration dependent
on prompt quality, repetition and conversational continuity. Context remains transient,
semantics remain implicit, and knowledge is difficult to reuse consistently across domains,
tools and AI models.

POOKA interprets the growing importance of prompt engineering not as an architectural
solution, but as an architectural symptom: it suggests the absence of persistent structures
capable of representing meaning, context, governance and behavior independently of individual
conversations.

The architectural challenge addressed by POOKA is therefore not how to create better prompts,
but how to design information environments in which prompts become consumers of architecture
rather than its primary source.

POOKA does not define software, programming models, storage technologies or implementation
frameworks. It defines a design philosophy for organizing information independently of AI
models, applications and technical implementations.

<div class="pooka-actions" markdown="1">
[<span class="pooka-actions__title">Read the Design Paper</span><span class="pooka-actions__note">The complete paper, chapter by chapter, in its canonical order.</span>](paper/00-cover.md)
[<span class="pooka-actions__title">Explore the Architecture</span><span class="pooka-actions__note">The Knowledge, Governance and Behavior layers, and how they connect.</span>](architectural-model.md)
[<span class="pooka-actions__title">View Core Concepts</span><span class="pooka-actions__note">The twelve architectural concepts and their definitions.</span>](core-concepts.md)
[<span class="pooka-actions__title">Download</span><span class="pooka-actions__note">The Markdown source, the bibliography and citation information.</span>](downloads.md)
[<span class="pooka-actions__title">GitHub Repository</span><span class="pooka-actions__note">The canonical source of the paper, open for review and discussion.</span>](https://github.com/conceptblenders/POOKA)
</div>

## About the name

The name **POOKA** originally stood for *Personal Object-Oriented Knowledge Architecture*.

The concept originated from the practical challenge of organizing personal knowledge to
enable more effective collaboration with AI. As the underlying concepts evolved, the central
question gradually shifted from *"How should I organize my own knowledge?"* to *"How should
information be architected so that humans and AI can collaborate through a shared semantic
structure?"*

Although the original acronym reflects the historical origin of the work, it no longer defines
its scope. Today, POOKA refers to the architectural style itself.

[The origin of the name, in full](paper/01-introduction.md#11-about-the-name)

## Status

POOKA is an architectural philosophy emerging from practical experimentation with Human–AI
collaboration. It is not a scientific theory, formal standard or industry specification. The
concepts presented in the paper are design proposals derived from practical observation,
iterative refinement and architectural reasoning. They have not been empirically validated
through controlled scientific research and should not be interpreted as established facts.

Adopting POOKA does not guarantee better AI performance, improved knowledge quality or
organizational success. POOKA provides an architectural foundation rather than a guarantee of
outcomes.

## An invitation

This paper should be read as a design paper: an invitation to discussion, implementation,
validation and further evolution.

Whether POOKA ultimately proves valuable will not be determined by the paper alone, but by its
ability to support practical implementations, encourage architectural dialogue and evolve
through continued application and critical evaluation.

Reviews are performed chapter by chapter, in Pull Request style. If you would like to
challenge a concept, propose a refinement or record an architectural decision, the
[repository](https://github.com/conceptblenders/POOKA) is the place to do it. The
[About](about.md) page describes how the paper is written and reviewed.
