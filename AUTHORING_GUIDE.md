# Authoring Guide

This document defines the editorial rules for both humans and AI working on the POOKA Design Paper.

# Purpose

This repository contains the canonical POOKA Design Paper. All editorial work is performed against the chapter files under `paper/`, which are the single source of truth.

---

# Writing Style

- Neutral
- Technical
- Evidence-aware
- No marketing language
- No hype
- No unsupported claims
- Architecture before implementation

---

# Terminology

Every architectural concept has exactly one meaning.

Never introduce synonyms for:

- Ecosystem
- Identity
- Actor
- Delegation
- Domain
- Context
- Artifact
- Relation
- Semantics
- Behavior
- Boundary
- Event

---

# Review Rules

- Review one chapter at a time.
- Never rewrite the complete paper.
- Explain every recommendation.
- Separate editorial remarks from architectural concerns.
- Distinguish factual issues from stylistic suggestions.

---

# Definition of Done

A chapter is complete when:

- terminology is consistent;
- every paragraph has a single purpose;
- every concept has exactly one definition;
- every claim is defensible;
- no unnecessary implementation details exist;
- no marketing language remains.

---

# AI Instructions

When AI reviews this repository:

- preserve the architecture;
- preserve terminology;
- never invent concepts;
- avoid speculative improvements;
- provide rationale for every suggested change.
