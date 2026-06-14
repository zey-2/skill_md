---
type: concept
created: 2026-05-17
updated: 2026-05-28
status: active
sources:
  - "raw/new_economics_of_software.md"
  - "raw/The AI paradox More automation, more humans, more work  Dan Shipper.md"
  - "raw/Why We’ll Still Be Employed When AI Can Do Everything.md"
  - "raw/Geoffrey Huntley - Software Development Now Costs Less Than Minimum Wage.md"
tags: [software-economics, scarcity, abundance, saas-moats, attention-economy, agent-native-saas, compute-costs]
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

## Concrete Unit Economics

Geoffrey Huntley calculated that running frontier models in a loop costs ~$10.42/hour for autonomous software development (Sonnet 4.5 pricing). With cheaper models, it's cents per hour. This transforms the economics of building: a 5-person "model-first company" can produce the output of 100 people, operating on margins that make traditional SaaS companies uncompetitive.

The implication extends beyond software. If knowledge work costs $10.42/hour to automate, every industry structured on knowledge scarcity — legal, medical, financial, consulting — faces the same pressure. The shift is from a knowledge-scarcity economy (charge more because knowledge is rare) to a knowledge-abundance economy (AI amplifies what anyone knows).

Source: `raw/Geoffrey Huntley - Software Development Now Costs Less Than Minimum Wage.md`.

## Model-First Companies

A new organizational form is emerging: the model-first company. These companies work "with the grain of the wood" — using languages and tools that frontier labs dogfood (Rust, Python) rather than fighting the grain with languages where models are weaker (Java, .NET). They have 5–20 people, focus on automating job functions rather than writing code, and produce parabolic revenue growth.

The competitive dynamic: model-first companies are "apex predators that can work on margins." When a 10-person company enters a market against an incumbent with 1,000 employees, the incumbent cannot respond fast enough. The timeline is compressed from years to months because model-first companies improve automatically as models improve — they're building with latent space.

The cascading effect: displaced engineers from incumbents go to new employers, implement AI there, and displace more people. "It could get recursively feral really fast."

## Agent-Native SaaS as a Counterpoint

Dan Shipper's "AI paradox" source complicates the strongest version of the SaaS-moat-erosion thesis. He argues that agents may increase demand for SaaS rather than replace it, because agents become additional users of existing systems and because companies still want trusted shared workflows, data, permissions, and collaboration surfaces.

In this view, the question for SaaS vendors shifts from "can we bolt an AI assistant onto the product?" to "can humans and agents collaborate on the same artifact?" Agent-native SaaS needs visibility into agent actions, approval queues, logs, rollback, high-throughput infrastructure, and interfaces that let a user's personal agent talk to the vendor's system or agent. If users bring their own model tokens through Codex-like or Claude-like work surfaces, the vendor may preserve margins while still supporting AI-heavy workflows.

The agent-native SaaS paradigm also creates qualitatively better support loops. When a user's agent encounters a bug, it sends a bug report with exact reproduction steps, suspected code locations, and context — far superior to a human support ticket. This enables a closed loop where the user's agent talks to the company's agent, which fixes the issue. This changes both the support economics and the user experience of software maintenance.

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

## The Compute Cost Ceiling

After scarcity collapses, a second constraint emerges: compute costs. AI models can outperform humans on many tasks, but intelligence costs energy. Humans run on heuristics evolved over millions of years; AI brute-forces equivalent judgment through expensive inference tokens. The question shifts from "Can AI do this?" to "Is it worth the compute?"

The empirical case: Waymo is objectively safer than human drivers (90% fewer claims per Swiss Re data) and already cheaper than Uber/Lyft for riders. Yet San Francisco's taxi workforce grew. AGI for driving has arrived, and humans are still employed — because scaling compute-intensive driving to every trip doesn't outweigh the marginal cost of human drivers for many use cases.

This creates a ceiling that is economic, not technical. A $20/month model handles routine tasks. A $200/month model handles complex work. But at $2,000/month, the tradeoff for slide decks and email becomes questionable. The "jagged free lunch" — the period when AI capability dramatically exceeds its cost — is temporary. As AI absorbs more tasks, the remaining ones require more compute, and the cost curve bends upward.

See [[concepts/The Compute Cost Tradeoff]] for the full treatment.

Source: MT's counterpoint in `raw/Why We’ll Still Be Employed When AI Can Do Everything.md`.

## The New Meta

With creation becoming cheap, the value-creating activities shift downstream. See [[concepts/The New Meta - Measurement, Ideation, Iteration]] for the full treatment of measurement, ideation, and iteration as the new bottlenecks.

## Connections

- [[concepts/Harness Engineering Principles]] covers the "code is free" thesis from an engineering operations perspective
- [[concepts/Understanding as the Human Bottleneck]] covers why human judgment cannot be outsourced
- [[concepts/Agentic Engineering vs Vibe Coding]] distinguishes exploration from production quality
- [[concepts/AI Slop and Garbage Collection]] addresses the quality degradation risk when abundant code is generated without governance
- [[concepts/The New Meta - Measurement, Ideation, Iteration]] — How the value-creating activities shift when building becomes cheap
- [[concepts/Software 3.0]] covers the broader shift in how software is created and maintained
- [[concepts/The Compute Cost Tradeoff]] — The economic ceiling on AI adoption when compute exceeds human labor costs
- [[concepts/AI-Native Engineering Organizations]] — Model-first companies as the organizational template; middle management collapse
- [[sources/The AI paradox More automation, more humans, more work  Dan Shipper]] - Counterpoint on SaaS demand, agent-native workflows, and automation as management work
- [[sources/Geoffrey Huntley - Software Development Now Costs Less Than Minimum Wage]] - $10.42/hour unit economics, model-first companies, K-shaped economy
