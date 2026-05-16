---
type: concept
created: 2026-05-02
updated: 2026-05-16
status: active
sources:
  - "raw/Andrej Karpathy From Vibe Coding to Agentic Engineering.md"
  - "raw/Building a Second Brain Vivian Balakrishnan AI Engineer Singapore.md"
  - "raw/You can outsource your thinking but not your understanding - Yacine MTB.md"
tags: [understanding, human-bottleneck, accountability, knowledge-management, karpathy, personal-agents]
---

# Understanding as the Human Bottleneck

## Key Points

> "You can outsource your thinking, but you can't outsource your understanding."
>
> — Yacine MTB (@yacineMTB / kache), February 2026

This distinction explains how technical knowledge is being reorganised in the agentic era. Syntax can be forgotten. Concepts must remain sharp. Understanding is what allows the human to write the right specification, and without it the agent fills in the blanks with its own assumptions.

Dr. Vivian Balakrishnan independently expressed the same insight with an added accountability dimension:

> "We're now at an age when you can outsource a lot of stuff — calculations, computation, memory, replication, dissemination of knowledge. The one thing which you cannot outsource is your personal understanding. And if you are in a position of authority, you can delegate work. You can't delegate accountability."
>
> — Dr. Vivian Balakrishnan, AI Engineer Singapore 2026

## What Can and Cannot Be Outsourced

| Can Outsource | Cannot Outsource |
|---------------|------------------|
| Calculations, computation | Personal understanding |
| Memory (storage, retrieval) | Accountability for decisions |
| Replication (copying, scaling) | Judgment of what matters |
| Dissemination (distribution, summarization) | The personal element in understanding |

The table is the practical framework. The trap is confusing the left column for the right column. When you outsource computation and feel productive, you may also be outsourcing understanding without noticing.

## Understanding and Accountability

Understanding and accountability are linked. You are accountable for decisions you make, but you cannot be accountable for decisions you do not understand. This is why the personal element matters: if you are in a position of authority, you can delegate the work of producing options, analysis, and recommendations. You cannot delegate the responsibility for choosing correctly.

Agents compound this risk. They produce options, analysis, and recommendations at high velocity. The human who does not understand the underlying concepts cannot distinguish a good recommendation from a plausible-sounding one. The accountability remains with the human, but the ability to exercise it has been outsourced.

## Syntax vs Concepts

Small API details can be outsourced. It is less important to remember every syntax difference, such as `keepdim` versus `keepdims`, or the exact method name for a library function. An agent can retrieve that quickly.

However, the underlying model still matters. For example, in tensor work, syntax can be looked up. But concepts such as memory layout, tensor views, copying, reshaping, and performance implications still need to be understood. Without that foundation, the agent may generate working code that is inefficient, incorrect, or fragile.

## The Hidden Risk: Obedient Before Wise

If the problem is poorly understood, the agent may still produce exactly what was requested. The failure is not that the model disobeyed. The failure is that the human asked for the wrong thing.

The agent is often obedient before it is wise. It may not:

- Challenge weak assumptions
- Know which business rule matters
- Distinguish between a prototype shortcut and a production requirement

Unless the human states these constraints explicitly, the system inherits the agent's assumptions.

## Understanding Enables Good Specs

The Stripe/email failure from Karpathy's interview illustrates this clearly. The agent tried to match accounts by email address — a reasonable default assumption that fails in real usage. Only a human who understood the business context (people use different emails across services) could write the correct specification.

Understanding becomes more valuable precisely because it is the layer that cannot be handed off. It is what separates a correct spec from a coherent-sounding but incomplete one.

## LLM Knowledge Bases as Comprehension Tools

LLM knowledge bases are interesting for the same reason. Their value is not just automation. Their value is comprehension. A model can take articles, transcripts, notes, or documents and project them into a wiki, comparison table, timeline, glossary, or question map. This is not a substitute for learning. It is a way to reshape learning.

Different projections onto the same data create insight. The wiki itself is an example of this pattern — raw sources are transformed into concept pages, and the transformation reveals connections that were not visible in the source material alone.

## Context for This Wiki

This concept is the foundational justification for the entire wiki's approach. [[concepts/LLM Fundamentals]] exists because understanding how models work is the layer that cannot be outsourced. [[concepts/Agentic Engineering vs Vibe Coding]] depends on this — the human writes the spec because the human understands the problem. The [[courses/ai-fundamentals-to-agent-skills/lesson-plan|AI Fundamentals to Agent Skills]] lesson plan is structured around this insight: fundamentals first, then tools, then automation.

## Connections

- [[concepts/LLM Fundamentals]] — The foundational knowledge that cannot be outsourced.
- [[concepts/Agentic Engineering vs Vibe Coding]] — Understanding is what enables good specs, which is what separates agentic engineering from vibe coding.
- [[courses/ai-fundamentals-to-agent-skills/lesson-plan]] — The lesson plan is structured around building understanding before building automation.
- [[concepts/Validation and Evaluation]] — Understanding enables the human to define what "correct" means; evaluation tests whether the agent met that definition.
- [[concepts/Replacing Code with Skills]] — Prompt-based isolation lacks the guarantees of hard-coded guardrails; understanding the failure modes is what prevents trusting the wrong model for the job.
- [[concepts/Personal AI Agents and Memory Systems]] — Dr. Balakrishnan's thesis: "the one thing which you cannot outsource is your personal understanding" — personal agents amplify understanding but cannot replace it.
- [[concepts/AI-Native Work Archetypes]] — The "adults" archetype is accountability embodied: judgment, earned intuition, and authority to say no.
- [[concepts/Harness Engineering Principles]] — "Every human interaction is a harness failure" — the human must understand the system well enough to design constraints that prevent failure without manual intervention.

## Source

- [[raw/Andrej Karpathy From Vibe Coding to Agentic Engineering]]
- [[raw/Building a Second Brain Vivian Balakrishnan AI Engineer Singapore]]
- [[raw/You can outsource your thinking but not your understanding - Yacine MTB]] — Original tweet source.
