---
type: concept
created: 2026-05-02
updated: 2026-05-02
status: active
sources:
  - "raw/Andrej Karpathy From Vibe Coding to Agentic Engineering.md"
tags: [agentic-engineering, vibe-coding, quality-bar, karpathy]
---

# Agentic Engineering vs Vibe Coding

## Key Points

Vibe coding and agentic engineering serve different purposes. Vibe coding raises the floor — anyone can build. Agentic engineering preserves the ceiling — production quality without sacrificing speed. The distinction is about quality, responsibility, and control.

## Vibe Coding: Exploration

Vibe coding lowers the barrier to building. A user can describe an idea, let the AI generate code, keep nudging it, and eventually produce something functional. This is valuable because:

- More people can prototype
- More ideas can be tested
- More small tools can be built without waiting for a full engineering team

However, vibe coding is not sufficient for production systems.

## Agentic Engineering: Production

Agentic engineering is the discipline of coordinating powerful but fallible agents to go faster without sacrificing the quality bar. It addresses:

- **Security**: Agents must not introduce vulnerabilities
- **Responsibility**: You are still accountable for your software
- **Control**: Agents are fast but stochastic; oversight is required

## The Intern Analogy

Agents are like interns with strong recall but no judgment. They can:

- Read documentation
- Fill in API details
- Migrate code
- Generate tests
- Handle repetitive implementation tasks

But they do not automatically have judgment. The human still owns the important layers: specification, architecture, security assumptions, product taste, quality bar, and final responsibility.

## Spec > Plan Mode

A plan can sound coherent while remaining vague. A specification is executable. The difference between vibe coding and agentic engineering is visible in the quality of the spec.

A weak instruction: "Build a login system."

A strong specification: "Users authenticate using Google OAuth. Stripe customer records must map to internal user IDs, not email addresses, because users may use different emails for Google and payment. Access control must be enforced server-side. Include tests for mismatched Google and Stripe emails."

The difference is not wording. The difference is understanding.

## The Stripe/Email Failure

Karpathy's agent tried to match a Stripe account to a Google account using an email address. That seems reasonable at first glance, but it fails in real usage because people may use different emails across services. The agent selected the obvious implementation. The human needed to identify the correct assumption.

This is the gap: the agent can fill in details, but the human must define the system correctly.

## Context for This Wiki

The distinction between vibe coding and agentic engineering directly informs [[concepts/Validation and Evaluation]] — vibe coding output may be functionally correct but structurally weak (bloaty code, awkward abstractions, brittle patterns). Agentic engineering requires stricter validation. It also connects to [[concepts/Skill Governance and Metrics]] because skills designed for agentic engineering must include quality guardrails that vibe coding workflows may skip.

## Connections

- [[concepts/Software 3.0]] — Agentic engineering operates on the Software 3.0 paradigm; the spec is the program, and the agent is the interpreter.
- [[concepts/Validation and Evaluation]] — Production-quality output requires stricter evaluation than exploration-quality output.
- [[concepts/Skill Governance and Metrics]] — Skills for agentic engineering must encode quality and security guardrails.
- [[concepts/Agent Skills]] — Skills package the reusable operating knowledge that separates agentic engineering from ad-hoc prompting.

## Source

- [[raw/Andrej Karpathy From Vibe Coding to Agentic Engineering]]
