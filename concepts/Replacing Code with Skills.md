---
type: concept
created: 2026-05-03
updated: 2026-05-03
status: active
sources:
  - "raw/Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"
tags: [skills, subagents, worktrees, prompt-as-code, cursor, evals, rl-training]
---

# Replacing Code with Skills

## Key Points

Cursor replaced ~12,000–15,000 lines of application code implementing its git worktrees feature with a ~200-line skill (markdown prompt). The feature lets users run agents in isolated checkouts, spin up parallel agent grids, and compare different models on the same task. The skill-based approach eliminated most of the codebase complexity while adding new capabilities the hard-coded version never had.

## The Original Implementation

The initial worktrees feature required writing and maintaining code for:

- Creating and managing git worktrees
- Feeding worktree context into agents
- Scoping and isolating agents so they couldn't escape their worktree
- Running user-configured setup scripts per worktree
- Built-in judging/grading of which model implementation looks best
- System reminders to keep agents on track
- Disk cleanup logic for abandoned worktrees

This was ~15,000 lines of code in the Cursor application itself, all hardcoded.

## The Skill-Based Replacement

Two existing primitives — **skills** and **subagents** — replaced the entire feature:

### `/worktree` Command (~200 lines of markdown)

Instructions telling the model how to create a worktree, run setup scripts, and stay on that checkout. The prompt must be aggressive about isolation ("do not ever work outside this directory"). Cross-platform instructions for Windows, Linux, and macOS are included in the skill.

### `/best-of` Command (~40 lines of markdown)

Instructs the parent agent to create subagents, one per model, each spinning up its own worktree. The parent waits for all subs to finish, then provides a comparison table with commentary and grading. Users can even ask the parent to stitch together pieces from different implementations.

These are implemented as commands (server-controlled prompts) rather than skills so the team can iterate on prompts without requiring a client update — but functionally they work the same way.

## What Was Gained

- **15,000 lines deleted.** Almost all application code for worktrees removed.
- **Users can switch to a worktree mid-conversation.** Previously required a dropdown choice at session start.
- **Multi-repo support works.** The old implementation was disabled for multi-repo setups. The skill-based version creates a worktree per repo and opens PRs for each.
- **Superior judging experience.** The parent agent has full context over what each sub did, and users can ask it to compose pieces from different implementations. Previously you had to pick one model's output wholesale.
- **Only power users pay the maintenance cost.** Worktrees are an advanced feature used by a small fraction of users. The skill approach means the core team spends almost no time maintaining it.

## What Was Lost

- **Hard guarantees on isolation.** The old implementation physically prevented agents from touching files outside their worktree. The new approach trusts the model via prompting. Over long sessions, models can forget which directory they should be operating in. Smaller/less capable models (e.g., Haiku) deviate more often than stronger ones (Composer, Grok).
- **Discoverability.** The old UI had a prominent dropdown. Now users must know to type `/worktree`. The team accepts this tradeoff for an advanced feature.
- **Perceived slowness.** The feature isn't actually slower, but watching the agent create the worktree in chat feels like wasted time compared to pre-provisioned isolation.

## Improving the Skill: Evals and RL Training

Cursor is addressing the isolation reliability gap through two channels:

- **Evals.** Using headless Cursor CLI with two scorers: one checking that work was done in the worktree, one checking that no work leaked into the primary checkout. Already revealed model-quality differences — smaller models deviate, stronger models comply.
- **RL training.** Adding worktree-scenario tasks into their RL pipeline for Composer model training. The model will be specifically trained for this environment rather than relying on prompts alone.

Better system reminders are a near-term mitigation while evals and training mature.

## What's Next

Cursor 3.0 introduces a new agentic UI where worktrees will get a more native (non-skill) implementation — the kind of user who parallelizes locally is the same user who prefers the agentic interface. The team is also exploring parallelization primitives beyond git worktrees (which are slow to create, disk-heavy, and git-only).

## Connections

- [[concepts/Software 3.0]] — The skill IS the program; markdown prompts replace application code. LLM is the interpreter.
- [[concepts/Spec-Driven Development]] — The skill spec replaces hardcoded logic; code becomes a compiled artifact of the prompt.
- [[concepts/Agent Skills]] — Skills as a mechanism for replacing application code with prompts.
- [[concepts/Harness Engineering Principles]] — The tradeoff between hard-coded guardrails and prompt-based instructions; evals as a harness improvement tool.
- [[concepts/Agentic Engineering vs Vibe Coding]] — Moving from "vibes-based" prompt trust to evals and RL training is the agentic engineering maturity curve.
- [[concepts/Symphony Orchestration]] — Subagents coordinating parallel worktrees is a microcosm of Symphony's multi-agent orchestration pattern.
- [[concepts/Validation and Evaluation]] — Evals with headless CLI and dual scorers (work done in worktree vs. work leaked to primary) as the reliability measurement.
- [[concepts/Progressive Disclosure]] — Commands load prompts only when invoked, surfacing instructions just-in-time rather than frontloading them.
- [[concepts/Agent Frameworks and Orchestration]] — The best-of command uses subagents, worktree isolation, and parent coordination as an orchestration pattern.
- [[concepts/The AI-Native Engineer and the Rising Ceiling]] — Deep engineers invest setup time in skills; the worktree skill is exactly this kind of compound leverage.
- [[concepts/Understanding as the Human Bottleneck]] — The human must understand why hard-coded guarantees and prompt-based trust have different failure modes; understanding can't be outsourced to the model.
- [[concepts/Agent Legibility]] — Skills make the codebase legible to agents by encoding rules in markdown; worktree skills make agent state legible to the UI.
- [[concepts/Discovery Conventions]] — The worktree prompts are commands (server-controlled), not SKILL.md packages — a different discovery path with different governance implications.
- [[concepts/Skill Distribution and Installation]] — Server-controlled prompts iterate without client updates; an alternative distribution model to portable skill packages.
- [[concepts/Tools Supporting Agent Skills]] — Cursor's command-vs-skill distinction shows platform-specific implementation choices within the broader skills ecosystem.
- [[concepts/Collaborative AI Engineering]] — The best-of command enables a form of collaborative planning: humans compare multiple model outputs and stitch pieces together.
- [[concepts/AI Slop and Garbage Collection]] — Prompt-based skills cause slop accumulation when models forget constraints; hard-coded guardrails prevent it entirely.

## Source

- [[raw/Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]]
