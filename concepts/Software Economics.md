---
type: concept
created: 2026-05-17
updated: 2026-05-28
status: active
sources:
  - "raw/new_economics_of_software.md"
  - "raw/The AI paradox More automation, more humans, more work  Dan Shipper.md"
tags: [software-economics, scarcity, abundance, saas-moats, attention-economy, agent-native-saas]
---

# Software Economics: From Scarcity to Abundance

## Key Points

Software development has shifted from a scarcity-driven discipline — where engineers were expensive, timelines were long, and ruthless prioritization was essential — to an abundance regime where implementation is nearly free and bottlenecks move to attention, governance, and judgment.

## Scarcity as the Old Constraint

Historically, software development was both expensive and slow:

- Each engineer-hour was costly; complex features took months
- Roadmaps were measured in quarters
- Prioritization meant whittling dozens of ideas down to a few
- Scarcity thinking was embedded in every process and organizational chart

## When Scarcity Collapses

AI agents, reusable components, and automation have collapsed the unit economics of code:

- **Development speed**: Tasks that once took months can now be completed in hours or days
- **SaaS moats erode**: If a CRUD app can be replicated in a weekend, code is no longer the primary competitive advantage. Moats shift to brand, data, ML models, and integration depth
- **Low-cost experimentation**: The long tail of ideas can now be evaluated and discarded efficiently rather than pre-rejected by cost constraints

## Agent-Native SaaS as a Counterpoint

Dan Shipper's "AI paradox" source complicates the strongest version of the SaaS-moat-erosion thesis. He argues that agents may increase demand for SaaS rather than replace it, because agents become additional users of existing systems and because companies still want trusted shared workflows, data, permissions, and collaboration surfaces.

In this view, the question for SaaS vendors shifts from "can we bolt an AI assistant onto the product?" to "can humans and agents collaborate on the same artifact?" Agent-native SaaS needs visibility into agent actions, approval queues, logs, rollback, high-throughput infrastructure, and interfaces that let a user's personal agent talk to the vendor's system or agent. If users bring their own model tokens through Codex-like or Claude-like work surfaces, the vendor may preserve margins while still supporting AI-heavy workflows.

## Bottlenecks Shift to Attention and Governance

As software creation accelerates, the constraints move downstream:

- **Go-to-market**: Prototyping is no longer a constraint — any idea can be built quickly, as can anyone else's. The scarce resource is attention, not implementation
- **Code review**: AI agents produce code faster than humans can evaluate it. Traditional review processes become insufficient; focus shifts to testing, validation, and quality assurance
- **Coherence and deletion**: When nontechnical staff and agents can produce more changes, the scarce work includes deciding what fits the whole system and what should be removed

## Jagged Intelligence

AI agents exhibit "jagged intelligence" — they may know the answer but will not surface it unless prompted correctly. Deep technical knowledge remains essential, not for writing code but for:

- Recognizing the right tools for a problem
- Asking precise, high-value questions
- Making informed tradeoffs
- Iterating quickly and learning from outcomes

The agent executes; humans provide judgment.

## The New Meta

With creation becoming cheap, the value-creating activities shift downstream. See [[concepts/The New Meta - Measurement, Ideation, Iteration]] for the full treatment of measurement, ideation, and iteration as the new bottlenecks.

## Connections

- [[concepts/Harness Engineering Principles]] covers the "code is free" thesis from an engineering operations perspective
- [[concepts/Understanding as the Human Bottleneck]] covers why human judgment cannot be outsourced
- [[concepts/Agentic Engineering vs Vibe Coding]] distinguishes exploration from production quality
- [[concepts/AI Slop and Garbage Collection]] addresses the quality degradation risk when abundant code is generated without governance
- [[concepts/The New Meta - Measurement, Ideation, Iteration]] — How the value-creating activities shift when building becomes cheap
- [[concepts/Software 3.0]] covers the broader shift in how software is created and maintained
- [[sources/The AI paradox More automation, more humans, more work  Dan Shipper]] - Counterpoint on SaaS demand, agent-native workflows, and automation as management work
