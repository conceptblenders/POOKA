# ADR-002: Identity Ownership vs Membership

## Status

Accepted

This ADR was originally raised as Proposed with a recommendation of Alternative A (a single owning Identity per Ecosystem). Following an architectural clarification from the author, that recommendation is withdrawn. The ADR is accepted in its revised form: the architectural model is coherent and unchanged, and no ownership decision is required. The original alternatives are retained below as the record of the ownership-framed analysis that the clarification supersedes.

## Context

The architectural review observed an ambiguity in the relationship between Ecosystem and Identity. An Ecosystem is described as the environment within which one or more Identities coexist (8.1), while Identity is described as the entity for whom an Ecosystem exists (8.2). The first phrasing suggests participation by several Identities; the second suggests a single owning Identity. This ADR does not address the phrasing. It determines the intended architecture: how ownership and participation relate.

Three facts about the current model constrain the alternatives, and none of them may be changed here:

- Ownership is already expressed through Boundary. A Boundary determines visibility, ownership, accessibility and the conditions under which information may cross (8.11). The outermost Boundary of an Ecosystem is therefore the natural carrier of ownership.
- Representation is already expressed through Delegation. Delegation is the bridge between an Identity and an Actor (8.4); it is not a relationship between two Identities.
- Multi-party arrangements are already supported by existing patterns. A Shared Knowledge Environment lets several Identities collaborate within a common Ecosystem while each retains its own governance, sharing selected Domains, Contexts or Artifacts through explicit Boundaries and Delegations (10.2). A Federated Knowledge Environment lets independent Ecosystems collaborate across Ecosystem Boundaries while each preserves its own autonomy, governance and Identity (10.5).

Against this background the three alternatives were evaluated. They were framed on the assumption that ownership is an architectural axis of the Ecosystem-Identity relationship. The Re-evaluation section revisits that assumption; the alternatives are retained as the record of that analysis.

### Alternative A — An Ecosystem has exactly one owning Identity; additional Identities participate through explicit Delegation or other architectural relationships

- **Architectural consistency.** Consistent. It reads 8.2 literally (a single subject for whom the Ecosystem exists) and reads 8.1 as one owner plus participating Identities that coexist in the environment. It aligns with 10.2 (participants retain their own governance) and with 10.5 (co-equal parties federate their own Ecosystems).
- **Governance implications.** Strongest. Every Ecosystem has one determinate root of authority and accountability on its outermost Boundary, matching the principle that responsibility remains with a specific human or organization (12.4). Delegation chains root in the owning Identity.
- **Identity model.** Unchanged. Owner and participant differ by relationship, not by kind, consistent with the position that concepts differ by role rather than by category (ADR-001).
- **Delegation model.** Unchanged and not overloaded. Delegation stays Identity to Actor. A participating Identity acts through its own Actors and is admitted through Boundaries granted by the owner; Delegation is never stretched to mean Identity-to-Identity ownership.
- **Boundary implications.** Clean. The outermost Boundary has exactly one owner (ownership determinate per 8.11); inner Boundaries grant scoped participation.
- **Advantages.** Determinate accountability; single root of trust; simplest governance; genuine co-equal multi-party handled by Federation; requires no new concept.
- **Disadvantages.** Cannot represent a single Ecosystem that is jointly owned by co-equal Identities; such cases must be modeled through Federation or by nominating one owner, which some may find restrictive. It also imports ownership into the architecture as a required relationship, which the Re-evaluation shows was never the intent.

### Alternative B — An Ecosystem may have multiple owning Identities; ownership is shared

- **Architectural consistency.** Weak. It reads 8.1 literally but contradicts 8.2, and it strains 10.2, which grants each collaborating Identity its own governance rather than a shared governance of one environment.
- **Governance implications.** Problematic. Multiple owners of the outermost Boundary produce joint control with no defined arbitration. The model has no conflict-resolution mechanism, and adding one would introduce a new concept, which is out of scope. Accountability becomes diffuse, weakening 12.4.
- **Identity model.** Weakened. The "entity for whom the Ecosystem exists" becomes plural, blurring the enduring-subject role.
- **Delegation model.** Unchanged but unhelpful here. Shared ownership is not expressible through Delegation (Identity to Actor); it would have to be carried by a multi-owner Boundary, which reintroduces the arbitration gap.
- **Boundary implications.** Ambiguous. The outermost Boundary would hold multiple owners and multi-valued crossing conditions with no defined way to reconcile them.
- **Advantages.** Directly models genuine joint ownership within a single Ecosystem; matches 8.1 literally.
- **Disadvantages.** Diffuse accountability; no resolution mechanism and none addable without a new concept; friction with 8.2 and 10.2; relocates the very ambiguity this ADR seeks to remove rather than resolving it.

### Alternative C — Ownership and Membership are independent relationships; an Ecosystem may have one or more owning Identities and also contain participating Identities

- **Architectural consistency.** Mixed. Separating ownership from participation is sound and expressive. However, allowing more than one owning Identity inherits Alternative B's arbitration problem, while constraining it to a single owner collapses C into A.
- **Governance implications.** Conditional. With a single owner, governance is as clean as A. With multiple owners, it degrades to B. The separation of ownership (accountability) from membership (participation) is nevertheless a genuine improvement in clarity.
- **Identity model.** Faithful. It most accurately reflects that owners and participants are different roles of the same kind of Identity, consistent with ADR-001.
- **Delegation model.** Unchanged. Representation remains Delegation (Identity to Actor); membership is realized through Boundary-granted access and the participant's own Delegations. This is acceptable only if ownership and membership are expressed through existing concepts (Boundary, Delegation, and Relation, which may connect Identities per 8.8) and are not reified as new Core Concepts.
- **Boundary implications.** Elegant when single-owner: ownership sits on the outermost Boundary; participation is granted through inner Boundaries. This mirrors 10.2 and 10.5.
- **Advantages.** Most expressive; cleanly separates accountability from participation; aligns with the shared and federated patterns and with ADR-001.
- **Disadvantages.** In the multi-owner case it inherits B's ambiguity; risks drifting toward a new "membership" concept, which must be avoided; heavier than necessary if most Ecosystems have a single owner.

## Re-evaluation (Architectural Clarification)

The author has clarified the architectural intent, which was never that an Ecosystem requires exactly one owning Identity. The intended model is:

- Ecosystem is the architectural container.
- Multiple Identities may legitimately coexist within one Ecosystem.
- Identity and Ecosystem are related, but the relationship is coexistence and participation, not necessarily ownership.
- Delegation concerns representation.
- Governance concerns authority.
- Ownership, where relevant, is implementation-specific and not necessarily an architectural concern.

**Classification of finding F1.** Against this clarification, F1 is **not (A) a genuine architectural contradiction**. It is best classified as **(C) a misunderstanding caused by wording, arising from (B) an ambiguous definition**. The reasoning:

- The architectural statement (8.1: one or more Identities coexist within an Ecosystem) is internally consistent and expresses the intended model directly. Nothing in the model requires a single owning Identity.
- The apparent conflict came entirely from reading 8.2 ("the entity for whom an Ecosystem exists") as an ownership claim. That phrase is an ambiguous definition (B): it can be read as ownership, though ownership was never the intended relationship. The reviewer's contradiction (F1) is the misunderstanding (C) that this ambiguity produced.
- Ownership does appear once in the model, but only as one of several attributes a Boundary may determine (8.11), never as a mandatory Ecosystem-Identity relationship. So there is no rule that an Ecosystem has an owning Identity, and therefore no contradiction with 8.1.
- Delegation (representation) and governance (authority) remain the architectural carriers of who may act and under which conditions. Ownership is orthogonal to both and, where it matters at all, is an implementation concern.

Because the model is coherent, the ownership-framed question this ADR originally posed does not arise. Alternatives A, B and C all presuppose ownership as an architectural axis; the clarification removes that premise. Alternative A in particular is withdrawn, because a single-owner constraint would add an architectural restriction the model never intended.

## Decision

The architectural model is coherent and requires no change.

- The Ecosystem-Identity relationship is coexistence and participation, not ownership. Multiple Identities may legitimately exist within one Ecosystem, as stated in 8.1.
- Ownership is not a required architectural relationship. Where relevant it is implementation-specific and outside the architectural core. Authority is carried by governance; representation is carried by Delegation.
- Finding F1 is reclassified as (C) a wording-induced misunderstanding, rooted in (B) an ambiguous definition, and is **not** (A) an architectural contradiction.
- The earlier recommendation of Alternative A is withdrawn. Alternatives A, B and C are retained above only as the record of the superseded ownership-framed analysis.

The only residual action is a definitional wording clarification in the paper, to remove the ownership connotation from the phrase "the entity for whom an Ecosystem exists" in the Identity definition. That is a separate, paper-level action and is deliberately **not** performed here.

## Consequences

Easier:
- No architectural change is required. The concept set, the governance model, the Delegation model and the Boundary model all stand as they are.
- Multiple Identities within one Ecosystem are confirmed as legitimate, aligning directly with the Shared Knowledge Environment pattern (10.2).
- Ownership is kept outside the architectural core, so the model avoids the arbitration and shared-authority problems that Alternatives B and C would otherwise raise.

Harder or requiring care:
- Until the Identity definition is clarified at the paper level (a separate action), the wording remains a latent source of the same misreading.
- Care must be taken not to reintroduce ownership as an architectural relationship. Governance (authority) and Delegation (representation) remain the architectural carriers; ownership stays implementation-specific.

Disposition: **Accepted** — the architectural model is coherent; F1 is a wording-level ambiguity (B) that caused a misunderstanding (C), not an architectural contradiction (A). No architectural change is required, and a separate paper-level wording clarification is recommended but out of scope for this ADR.
