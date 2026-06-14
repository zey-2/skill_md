---
type: source-summary
created: 2026-06-07
updated: 2026-06-07
status: active
sources:
  - "raw/How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code.md"
tags: [parallel-agents, agent-management, verification, context-rot, workflow]
---

# How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code

**Source**: Kilo Code blog, `https://blog.kilo.ai/p/how-7-kilo-code-engineers-run-up`
**Author**: Darko Gjorgjievski
**Published**: 2026-05-26

## Summary

Seven senior Kilo Code engineers (who build coding agents, not just use them) share their parallel agent workflows. The key finding: the social media hype of 50–100 parallel agents is misleading. In practice, engineers run 2–4 foreground agents they actively manage, plus a variable number of background "fire-and-forget" agents. The bottleneck is shifting from writing code to verifying it. Practical patterns include task sizing by reviewability, planning with thinking models and executing with fast models, and cross-agent verification loops.

## Key Points

### Foreground vs. Background Agents

- **Foreground agents** (2–4): the ones you actively manage — watching, reviewing, steering, interrupting when they drift. This is the human attention bottleneck.
- **Background agents** (up to 20+): fire-and-forget jobs that produce PRs. You review the result later, not the process. Mark runs 20+ but most are background.
- "Running 100 agents" is meaningless without specifying what "running" means. Simon Willison: "I can focus on reviewing and landing one significant change at a time." Mitchell Hashimoto: "the mayor," managing at most 2 agents.

### The Context Window Goldilocks Zone

- **Quality drops at 60% context fill**, well before the 95% compaction threshold. By compaction time, hallucinations have already started.
- **The advertised context window is not the usable window.** Igor's workaround: split tasks into smaller sub-agents so each finishes before context fills.
- This is [[concepts/Context Rot]] in practice.
- **Size tasks by reviewability.** If the diff is too large to inspect carefully, the task was too large.
- **Avoid mixing task types.** "Refactor this service, improve performance, add analytics, and clean up tests" is four tasks, not one.
- Use OpenAI's GCCD framework for structuring prompts.

### Plan Harder, Implement Faster

- **Florian**: research agents prepare plans; execution agents work from the queue. Plans are pre-investigated before implementation starts.
- **Imanol**: GPT-5.5 Fast mode for implementation is quick but error-prone. Better: slow thinking model for planning, GPT-5.5 Fast for execution. "So much better."
- **Kirill**: GPT-5.5 with Thinking for planning, Sonnet for fast execution.
- Boris Cherny (Claude Code creator): same pattern — plan mode, iterate on plan, one-shot implementation. "Once there is a good plan, it will one-shot the implementation almost every time."

### Verification Loops

- **Florian's PR-review-feedback agent**: when a reviewer leaves comments, an agent reads feedback, makes changes, sends message back. Across hundreds of PRs, saved time compounds.
- Boris Cherny: giving an agent the ability to verify its work results in 2–3x quality improvement.
- "The person who wrote the code is the worst person to review it." A fresh session has no attachment.
- Separate agents for code review, security, and hosted workflows.

### Software as Gardening

- Mark: "I like to think of software engineering as gardening instead of building." You apply judgment; agents do the grunt work. "You can just say: take care of that, remove that weed."
- Background agents are gardening. You give them a small piece of work, let them progress, come back to prune.

## Evidence

- Simon Willison, Mitchell Hashimoto, Addy Osmani (Google) all run 2–5 foreground agents max.
- Addy Osmani: "runs four to five background agents handling low-to-medium complexity work."
- Boris Cherny on plan-then-execute: "once there is a good plan, it will one-shot the implementation almost every time."
- An Anthropic employee wrote about "bad compacting" risks when context grows too large.
- Kilo ships separate agents for code review, security, and hosted workflows.

## Connections

- [[concepts/Parallel Agent Management]] — New concept capturing foreground/background split, Goldilocks zone, and verification loops.
- [[concepts/Context Rot]] — The 60% quality drop is concrete evidence for context rot in practice.
- [[concepts/Harness Engineering Principles]] — Foreground agents are the harness; background agents are the production line.
- [[concepts/Collaborative AI Engineering]] — Verification loops as cross-agent alignment.
- [[concepts/Tokenmaxxing]] — Parallel agents as tokenmaxxing with structure (not just more tokens, but better-allocated tokens).
- [[concepts/Comprehension-Driven Development]] — Planning-first workflow (67% comprehension) confirmed by Kilo engineers.
- [[concepts/Skill Authoring Workflow]] — Task sizing and prompt structuring as skill design inputs.

## Contradictions or Tensions

- The "2–4 foreground agents" finding contradicts the social media narrative of 50–100 productive parallel agents. The Kilo engineers explicitly call this out as hype.
- "Software as gardening" tensions with the "software as clay" metaphor from Geoffrey Huntley. Both suggest less front-loading, but gardening implies ongoing maintenance while clay implies shaping and discarding.
- The plan-then-execute pattern assumes the planning model is reliable. If the plan is wrong, the fast executor confidently implements the wrong thing.
