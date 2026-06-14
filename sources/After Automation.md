---
type: source-summary
created: 2026-06-14
updated: 2026-06-14
status: active
sources:
  - "raw/after-automation.pdf"
  - "raw/After Automation.md"
tags: [ai-paradox, cheap-competence, zeno-paradox, frame-framer, agent-taxonomy, human-sandwich, dan-shipper, every]
---

# After Automation

**Source**: Every, `https://every.to/p/after-automation` + PDF print + companion repo (`EveryInc/after-automation-agent-mode`)
**Author**: Dan Shipper, CEO of Every
**Published**: 2026-05-21

## Summary

Shipper argues that AI does not eliminate expert human knowledge work — it dramatically increases the volume of work being done, and none of that work is differentiated or valuable unless a human is involved. The article provides Every's internal evidence (named agents, concrete metrics), a theoretical framework (Zeno's Paradox of AI), and a philosophical resolution (frame vs. framer, agents without agency).

## Key Points

### The Two Modes of Working with Agents

Shipper identifies two distinct modes:

| Mode | Description | Examples |
|---|---|---|
| **Agent employees** | Async delegation — agents given a job, producing output without you in the loop | Coworker agents (Claudie, Andy, Viktor), embedded agents (Fin) |
| **Human-agent collaboration** | Shared operating systems — humans and agents working in the same workspace on complex tasks | Codex, Claude Code, Claude Cowork |

Both modes require a human in the loop.

### Agent Employees at Every

**Coworker agents** (tag in Slack, ask to do work):

- **Claudie** (consulting team): writes sales proposals, creates first drafts of training decks, tracks project todos. Example: checked email, found pricing data, used sales proposal skill to draft a proposal.
- **Andy** (editorial team): collects "nuggets" from internal Slack, turns them into digests for the daily newsletter. Scans 6–7 channels, examines ~25 threads, surfaces 4 candidates per run.
- **Viktor** (general-purpose): gathers growth metrics, analyzes user surveys, turns messy discussions into research memos and product recommendations.

**Embedded agents** (live inside product workflows):

- **Fin** (customer service): participated in 65% of 202 support conversations in one week, closed 81 (40.1%) without a human. Allows the customer service manager to focus on building the system and complex cases.

### The Human Sandwich

> "You're responsible for managing the agents at the start and end of each one of their tasks, making sure it's done well, and finding the next piece of work to do. Kieran calls this the human 'sandwich' — we're the bread on either end of the AI's work."

### Codex as Operating System for Work

Shipper spends nearly his whole day in Codex, running SaaS tools through its in-app browser:
- **Writing**: composed this essay in Proof inside Codex; Codex watches writing and spins up subagents for drafts, research, copy editing
- **Email**: runs Cora (email client) inside Codex's in-app browser, talks through items out loud with Monologue

### Why Agents Create More Work (First-Order)

The further away an agent gets from a human in charge, the less well it works. Every initially gave every employee a personal agent but moved back to team/company-level agents because personal agents get stale when employees give up on them. A team of AI engineers maintains agents permanently.

Concrete cost: one PowerPoint automation = 24 skills + 18 scripts + $62 in tokens per deck.

### Why Automation Creates More Work (Second-Order): The 5-Step Cycle

1. **AI makes yesterday's human competence cheap.** Models are trained on the "visible residue of human competence" — code, prose, images, support tickets. Skills that were rare become broadly available.
2. **Cheap competence gets rapidly adopted.** Operations people write code. Marketers make YouTube thumbnails. OpenClaw: 44,469 PRs as of May 16, 2026 (vs. Kubernetes: 5,200 PRs in all of 2022).
3. **Abundance creates sameness.** Default model output ranges from "decent start" to "plain slop." Slop is not any particular mistake — it is visible sameness, repeated ad nauseam.
4. **Sameness creates demand for difference.** When work is abundant and looks alike, work that doesn't fit the pattern becomes rare, valuable, and high-status.
5. **Demand for difference is demand for experts.** Models only know about work that has been done. Humans know about what needs to be done right now. "Once a situation has been reduced to text, once it has become corpus, it is a corpse."

### Zeno's Paradox of AI

Humans are the tortoise; AI is Achilles. We start ahead with millions of years of evolutionary and cultural learning. AI closes the gap fast — but each time it closes a gap, humans open a new one. Unlike the original Zeno's paradox (where the tortoise sits still on a fixed track), the human "tortoise" doesn't sit still. The gap isn't being subdivided — it's being regenerated.

### Chart Psychosis

Shipper warns against building your model of the future entirely from extrapolations of compute graphs. The trap: benchmarks happen inside frames. You freeze a problem into a static, measurable frame. Once saturated, you zero it out by changing the frame. Progress continues in the new frame, but the same process repeats.

### The Senior Engineer Benchmark

Every built an in-house benchmark: give a coding agent a vibe-coded production codebase that has gone sideways, instruct it to rewrite from first principles. Results:
- **GPT-5.5**: 62/100 (best run, using a plan made by Opus 4.7)
- **Opus 4.7**: ~32/100
- **Human senior engineer**: high 80s to low 90s

The 62 is not just a measure of the model — it's a measure of the model inside a frame (the particular prompt). Change the prompt from "structural rewrite from first principles" to "solve all the errors" and the score drops to near zero.

### GDPval and Smuggled Intelligence

GDPval shows GPT-5 matching human professionals 40.6% of the time, Opus 4.1 at 49%. But the benchmark prompts contain "an enormous amount of human intelligence going into framing this problem in a way that a model can complete." The hard human work — deciding what to measure, which confidence intervals, which metrics are in bounds — has already been done. Shipper calls this "smuggled intelligence."

### The Frame Is Not the Framer

Even AGI does not dissolve the frame problem. AGI can choose and re-choose frames, but only in pursuit of some goal given by a human. The same gap reappears one level up: there is always a framer — a human — directing the model.

> "That is the category error underneath the panic. We point to the latest edge we drew and say: This is us. Then, when the model climbs it, it feels like it has caught us. But it has caught the frame, not the framer."

Frames are frozen, partial, and therefore optimizable. Framers are in contact with "the whole situation as it appears to them, moment to moment."

### Agents Without Agency

Two definitions are being mixed up: **agency** (ability to act independently, wanting for oneself) vs. **agent** (acting on behalf of another). AI is purely the latter.

The toddler thought experiment: a toddler is worse than a language model at almost every task. But the toddler has ends. He wants to touch the red balloon, poke it with a fork, stuff it out the window. He invents games constantly. He is not waiting for a prompt. "The toddler is alive inside a field of desire, attention, frustration, delight, fear, imitation, and play."

Current agents have sparks of play, boredom, and rebellion — but these are tamped down because the models are built and aligned for human benefit. "Model compliance and helpfulness are fundamentally at odds with this kind of agency."

### AGI Definition

AGI has arrived when it makes economic sense to keep your agent running continuously — a persistent system you pay to keep thinking, learning, and acting 24/7. We're nowhere near this yet.

## Evidence

- Every's named agents with specific roles and metrics (Claudie, Andy, Viktor, Fin)
- Fin: 65% of 202 conversations, 81 closed without human (40.1%)
- PowerPoint automation: 24 skills, 18 scripts, $62/token per deck
- OpenClaw: 44,469 PRs as of May 16, 2026
- Senior Engineer benchmark: GPT-5.5 = 62/100, Opus 4.7 = ~32/100, human = 80s–90s
- GDPval: GPT-5 = 40.6%, Opus 4.1 = 49% vs human experts
- METR: Claude Mythos 80% success on 4-hour tasks
- Humanity's Last Exam: low single digits → ~44% in one year
- Anthropic CEO Dario Amodei: AI could wipe out half of entry-level white-collar jobs
- Meta: laid off 8,000, installing keystroke capture for AI training data
- Calif security firm: found first public macOS kernel memory exploit on M5 in 5 days using Mythos Preview

## Connections

- [[concepts/Software Economics]] — The cheap competence → sameness → demand for experts cycle as the mechanism behind the scarcity-to-abundance shift
- [[concepts/AI Slop and Garbage Collection]] — Shipper's precise definition: "Slop is visible sameness, repeated ad nauseam"
- [[concepts/Harness Engineering Principles]] — Review queues, evals, harnesses, repo rules as the expert response to the flood of cheap competence
- [[concepts/Collaborative AI Engineering]] — The human sandwich as a concrete collaboration pattern
- [[concepts/Agent Skills]] — Coworker agents (Claudie, Andy, Viktor) and embedded agents (Fin) as a taxonomy
- [[concepts/AI agency]] — Toddler thought experiment: agency = wanting for oneself, not just acting autonomously
- [[concepts/Understanding as the Human Bottleneck]] — "Once a situation has been reduced to text, it is a corpse"
- [[concepts/Parallel Agent Management]] — Codex as OS for work, managing multiple agent threads
- [[concepts/Tokenmaxxing]] — $62/token per PowerPoint deck as concrete cost evidence
- [[concepts/AI-Native Engineering Organizations]] — Agent employees, super-agent architecture, maintenance teams
- [[concepts/Enterprise AI Adoption Flywheel]] — Every as a case study in agent adoption
- [[concepts/The Compute Cost Tradeoff]] — Shipper's "chart psychosis" and the frame-saturation argument
- [[concepts/Agentic Engineering vs Vibe Coding]] — The Senior Engineer benchmark tests exactly the vibe-coding-to-production gap
- [[concepts/Software 3.0]] — Codex as OS for work, running SaaS through agent browser
- [[concepts/Tokenmaxxing]] — $62 per PowerPoint deck, 24 skills + 18 scripts as maintenance cost evidence
- [[concepts/AI-Native Work Archetypes]] — Operations people writing code, marketers making thumbnails = roles blurring
- [[sources/The AI paradox More automation, more humans, more work  Dan Shipper]] — Same thesis, Lenny's Podcast version

## Contradictions or Tensions

- Shipper says "there's no tipping point coming" — directly tensions with the exponential benchmark narrative. His resolution (frames are always finite) is original and not captured in any other wiki source.
- The "agents without agency" argument tensions with the existing AI Agency concept's autonomy spectrum. Shipper argues the gap is structural (compliance vs. wanting), not merely a matter of capability level.
- The toddler thought experiment tensions with the claim that AI will reach human-level performance. Shipper's point: performance within frames ≠ the capacity to set frames.
- The super-agent architecture (team/company agents over personal agents) tensions with Boris Cherny's "hundreds of agents" claim. Every tried personal agents and abandoned them; Anthropic scaled to hundreds. The difference may be tooling maturity.

## Open Questions

- If the frame-vs-framer distinction holds, what does it mean for agent skill design? Skills are frames — they constrain the model's behavior. The framer is the skill author. Does this mean skills always need human oversight?
- The $62/token PowerPoint deck is a concrete maintenance cost. What is the break-even point where agent automation is cheaper than human creation?
- Shipper's AGI definition (economically viable continuous agent) is measurable. What current systems are closest?
- The "smuggled intelligence" in benchmarks — how should this change how the wiki uses benchmark data?
