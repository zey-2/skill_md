---
type: source-summary
created: 2026-06-07
updated: 2026-06-07
status: active
sources:
  - "raw/Why We’ll Still Be Employed When AI Can Do Everything.md"
tags: [software-economics, compute-costs, ai-adoption, enterprise-ai, agent-skills, every]
---

# Why We'll Still Be Employed When AI Can Do Everything

**Source**: Every newsletter, `https://every.to/context-window/why-we-ll-still-be-employed-when-ai-can-do-everything`
**Author**: Laura Entis (staff writer, Every), with contributions from Mike Taylor, MT, and Naveen Naidu
**Published**: 2026-06-05

## Summary

An Every Context Window newsletter covering four items: (1) Spiral 4.0 launch with agent-native MCP and token-based pricing, (2) Microsoft's rapid but possibly-too-late OpenClaw pivot as a case study in enterprise AI roadmap difficulty, (3) Naveen Naidu's workflow for building custom skills to improve agent efficiency, and (4) a debate between Dan Shipper and MT on whether AI creates more work forever or will eventually outpace humans but keep them employed anyway due to compute cost economics.

## Key Points

### Enterprise AI Roadmaps Are Hard

- Microsoft moved from Nadella calling OpenClaw a "virus" (Feb 2026) to internal testing of ClawPilot (May) to launching Scout at Build (June) — blindingly fast for a 100K-engineer company.
- But OpenClaw search traffic peaked in January and declined sharply, helped by Anthropic ending subsidized Max plan usage in April.
- The lesson: enterprise product teams can do everything right and still be behind the news cycle by launch day. The viral moment passes faster than organizational response times.

### Make Your Agent More Efficient with Custom Skills

- Naveen Naidu (Monologue GM) works in the Codex app with Fin (Intercom) open in the browser.
- His workflow: Codex investigates customer issues, creates bug reports in Linear, links tickets, drafts replies — all without leaving the app.
- Fin's MCP has 13 generic actions; Naveen needed something more specific. He asked Codex: "What tools can I give you so you can work more quickly?"
- Built a repository-local skill: a small CLI script that calls the Fin API, pulls the active conversation, and returns it as markdown.
- Added a project-level instruction: if customer context is missing, use the custom skill to pull the Fin thread.
- **Naveen's rule of thumb**: "Don't download any skills. Start interacting with the agent, see where it is inefficient, and then ask it to create skills."

### AI Creates More Work (Dan Shipper's Frame)

- Dan argues AI progress creates more work, not less. Each time models saturate a benchmark, the frame resets: the model saturates that frame too, and the cycle repeats forever.
- MT's progression: prompts → context supply → agent orchestration → defining evals and goals. Each time AI absorbs a piece, the frame expands to more abstract, higher-level work.

### The Counterpoint: AI Will Outpace Us, But It Won't Be Cheap

- MT predicts that in a year or two, AI will execute every knowledge-worker task better than humans — including setting the frames.
- But intelligence costs energy. Evolution already optimized human cognition for constrained resources. AI doesn't inherit DNA encoded with millions of years of evolution; it brute-forces through expensive "thinking" tokens.
- **The key question shifts from "Can AI do this?" to "Is it worth the compute?"**
- Waymo is objectively safer than human drivers, yet riders pay one-third or more the price of Uber/Lyft. The city's taxi workforce grew anyway.
- Prediction: models will outpace humans in raw capability, but humans will stay employed because some work isn't worth the compute, and some people will prefer human work.

### Model Linguistic Quirks

- GPT-5.5 cannot stop making goblin references (OpenAI's own blog post about this).
- Claude: "locked in," "load bearing," "get some rest!"
- Codex: "my instinct is," framing things as "X smart thing rather than Y dumb thing."
- Models consistently soften creative writing with notes to "be less mean."

## Evidence

- Google Trends data shows OpenClaw search interest spiked in January 2026 and declined soon after (screenshot by Mike Taylor).
- Anthropic ended subsidized Max plan usage for OpenClaw in April 2026, forcing users to scramble for cheaper models.
- Gemini Spark launched at Google I/O; Claude and Codex adopted agentic features inspired by OpenClaw.
- Waymo data: Swiss Re shows 90% fewer claims than human drivers; OBI data shows riders pay 1/3+ the price of equivalent rides; San Francisco taxi workforce grew despite AGI-level driving capability.
- OpenAI blog post on GPT-5.5's goblin references as an example of intractable model personality quirks.

## Connections

- [[concepts/Software Economics]] — The compute cost tradeoff as the next constraint after scarcity collapses.
- [[concepts/The Compute Cost Tradeoff]] — New concept: AI capability ≠ AI adoption when compute costs exceed human labor costs for subjective tasks.
- [[concepts/AI-Native Work Archetypes]] — The frame-reset cycle describes how work evolves, not disappears.
- [[concepts/Enterprise AI Adoption Flywheel]] — Microsoft/OpenClaw timeline shows the speed mismatch between viral moments and enterprise response.
- [[concepts/Prompting Skills Not Prompts]] — Naveen's workflow is a concrete example of building skills from agent inefficiency.
- [[concepts/Skill Authoring Workflow]] — "Ask your agent what tools it needs" as a skill discovery method.
- [[concepts/Understanding as the Human Bottleneck]] — MT's argument that framing isn't magic but still requires embodied experience.
- [[concepts/The AI-Native Engineer and the Rising Ceiling]] — The progression from prompts to orchestration to evals as the rising ceiling in practice.
- [[concepts/Ride the Models]] — The career strategy for navigating the frame-reset cycle.

## Contradictions or Tensions

- Dan Shipper says the frame resets forever; MT says AI will eventually outpace humans at framing too. These are directly contradictory positions published in the same newsletter.
- The "compute cost keeps humans employed" argument assumes energy costs stay high. If inference costs drop dramatically (as they have historically), the compute barrier weakens.
- Naveen's "don't download skills" advice contradicts the broader skill marketplace model. His point is about discovery — start with interaction, then build — but it could be read as anti-marketplace.
