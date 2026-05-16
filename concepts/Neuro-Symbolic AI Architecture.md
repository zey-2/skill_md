---
type: concept
created: 2026-05-16
updated: 2026-05-16
status: active
sources:
  - "raw/Building a Second Brain Vivian Balakrishnan AI Engineer Singapore.md"
tags: [neuro-symbolic, ai-architecture, llm-limitations, reasoning, world-models]
---

# Neuro-Symbolic AI Architecture

## Summary

The argument that pure LLMs — pattern recognition systems with attention and memory — are not the end state of AI. The more likely path forward combines neural networks (pattern recognition, semantic understanding) with symbolic systems (deterministic rules, explicit logic, verifiable reasoning). This tension matters for Agent Skills: if symbolic guarantees are needed, skills may encode rules the LLM cannot override.

## Key Points

- **LLMs are pattern recognition with emergent behavior** — they excel at language, abstraction, drafting, and semantic search, but their reasoning is statistical, not logical.
- **Nature uses more efficient structures** — as an eye surgeon, Dr. Balakrishnan notes that cortical computation for vision, language, and cognition uses "far more efficient structures than the energy-gobbling systems" of current LLMs. The human brain has fewer layers of computation than many modern LLMs.
- **Hammer-and-nail problem** — "for a man with a hammer, everything looks like a nail." LLMs are currently being thrown at every step in a pipeline, but there are good economic and design advantages to using them selectively alongside deterministic and rule-based systems.
- **Neuro-symbolic combines the best of both** — neural systems for pattern recognition, ambiguity, and natural language; symbolic systems for verifiable logic, constraints, and explicit rules. The hybrid avoids both the brittleness of pure symbolic systems and the unpredictability of pure neural systems.
- **Yann LeCun agrees** — LLMs are great but not how nature solved cognition. LeCun advocates for world models and objective-driven learning (JEPA) over autoregressive next-token prediction.
- **Token economics matter** — LLM tokens are not cheap. Compute power is limited. Electricity prices have risen. Throwing every problem at an LLM is economically unsustainable.
- **Skills can encode symbolic constraints** — Agent Skills that enforce structural rules (binary assertions, format constraints, forbidden patterns) are already a form of neuro-symbolic design: the LLM generates content while the skill's evals enforce symbolic guarantees.

## Evidence

- Dr. Balakrishnan's keynote explicitly argues for a neuro-symbolic future, citing LeCun's critique of pure LLM approaches and the biological inefficiency of current models.
- He identifies multiple systemic constraints: token pricing (possibly subsidized currently), compute limits, rising electricity costs, and geopolitical supply chain pressures.
- The self-improving skills pattern (binary assertions enforcing structural rules) demonstrates an already-working neuro-symbolic hybrid: the LLM produces creative content while deterministic evals enforce format constraints.

## Connections

- [[concepts/LLM Fundamentals]] — Understanding how LLMs work (autoregressive token prediction) is essential to understanding their architectural limitations.
- [[concepts/Self-Improving Skills]] — Binary assertion loops are already a neuro-symbolic pattern: LLM creativity + deterministic structural guarantees.
- [[concepts/Personal AI Agents and Memory Systems]] — Balakrishnan's neuro-symbolic argument is part of his broader critique of over-relying on LLMs for every step.
- [[concepts/Validation and Evaluation]] — Symbolic rules are deterministically verifiable; neural outputs require probabilistic evaluation. The evaluation strategy differs by architecture layer.
- [[concepts/Harness Engineering Principles]] — Deterministic guardrails and rules-based systems are the harness around the LLM's creative but unpredictable output.
- [[concepts/Skill Authoring Workflow]] — Skills can encode "must" and "must not" constraints as explicit rules, not just LLM guidance.

## Contradictions or Tensions

- **Pure LLM momentum vs. neuro-symbolic theory** — The entire AI industry is currently investing billions in scaling pure LLMs. The neuro-symbolic argument is theoretically stronger but lacks the funding, tooling, and ecosystem momentum. Following the theory may mean betting against the market.
- **What counts as "symbolic"** — Skills with binary assertions, format constraints, and eval pipelines are a lightweight form of neuro-symbolic design. But is a YAML assertion file truly "symbolic" in the same sense as a logic programming language or knowledge graph? The boundary is fuzzy.
- **LeCun's JEPA vs. other neuro-symbolic approaches** — There is no single neuro-symbolic paradigm. JEPA (world models), logic programming, constraint satisfaction, and hybrid architectures are all different approaches. The wiki does not yet track which approaches are gaining traction.

## Open Questions

- Which neuro-symbolic architectures are gaining practical adoption (beyond research papers)?
- Can Agent Skills be designed to explicitly encode symbolic constraints that the LLM cannot override, rather than just persuasive instructions?
- Does the economic argument (token costs, compute limits) drive neuro-symbolic adoption even if the technical argument does not?
- How do neuro-symbolic systems change the skill authoring workflow? Skills may need to target two different system layers simultaneously.
