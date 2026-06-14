---
type: concept
created: 2026-06-07
updated: 2026-06-14
status: active
sources:
  - "raw/How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code.md"
  - "raw/Reflecting on a year of Claude Code.md"
tags: [parallel-agents, agent-management, verification, context-rot, workflow, gardening, routines]
---

# Parallel Agent Management

## Summary

Parallel agent management is the practice of running multiple AI coding agents simultaneously, splitting attention between actively managed foreground agents and minimally supervised background agents. The social media narrative of 50–100 productive parallel agents is misleading; in practice, senior engineers run 2–4 foreground agents and a variable number of background "fire-and-forget" agents. The bottleneck is not generating code — it's verifying it. Effective parallel workflows depend on task sizing, planning-execution separation, and cross-agent verification loops.

Source: `raw/How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code.md`.

## Foreground vs. Background Agents

The distinction between foreground and background agents is the core mental model:

| Type | Count | Attention | Use Case |
|---|---|---|---|
| Foreground | 2–4 | Active: watch, review, steer, interrupt | Complex tasks, high-stakes changes, architecture work |
| Background | 0–20+ | Passive: review result after completion | Small maintenance tasks, change markers, boilerplate, fire-and-forget PRs |

**Foreground agents** demand continuous human attention. Igor (senior engineer, architecture tasks): "even with SOTA models, output quality on complex tasks drops quickly unless you stay close to the work. The higher the stakes, the less you can afford to treat the agent as a black box."

**Background agents** produce PRs that pass or fail in tests. You look at the final result later. Mark describes them as "fire-and-forget" — each agent ships a PR, tests run, and Mark decides whether to merge or reject. "These small, background parallel tasks are easy to evaluate."

The practical implication: when someone claims to be "running 100 agents," ask what "running" means. Active management of 100 agents is not possible for a human. Passive monitoring of 100 small PRs is possible but only if each PR is small enough to review quickly.

## The Context Window Goldilocks Zone

Task sizing is the most important practical skill for parallel agents. Too small and prompting is slower than writing the code. Too large and the agent runs out of context and starts making confident wrong calls.

**Quality drops at 60% context fill**, well before the 95% threshold where compaction kicks in for many coding agents. By compaction time, hallucinations have already started. This is [[concepts/Context Rot]] in practice — the advertised context window is not the usable window.

Igor's workaround: split coding tasks into smaller sub-agents, so each one finishes before its context fills up. He optimizes the scope of each task so the work completes before auto-compression kicks in.

Practical heuristics for task sizing:

- **Size by reviewability.** A good agent task should produce an output a human can review in one sitting. If the diff is too large to inspect carefully, the task was too large.
- **Use OpenAI's GCCD framework** (Goal, Context, Constraints, Definition of done) when structuring prompts.
- **Avoid mixing task types.** "Refactor this service, improve performance, add analytics, and clean up tests" is four agent tasks, not one.

## Plan Harder, Implement Faster

The most effective pattern among Kilo engineers separates planning from execution using different models:

| Phase | Model | Purpose |
|---|---|---|
| Planning | Slow, thinking model (GPT-5.5 Thinking, Claude in plan mode) | Investigate the problem, produce a detailed plan |
| Execution | Fast model (GPT-5.5 Fast, Sonnet) | Implement the plan quickly |

Florian's approach: research agents prepare plans for tasks he wants to do. By the time planning finishes, he has a queue of pre-investigated problems ready for execution agents.

Imanol found that GPT-5.5 Fast mode is incredibly quick but error-prone. Using a thinking model for planning and GPT-5.5 Fast for implementation was "so much better."

Boris Cherny (Claude Code creator) uses the same pattern: plan mode → iterate on plan → one-shot implementation. "Once there is a good plan, it will one-shot the implementation almost every time."

This confirms the [[concepts/Comprehension-Driven Development|comprehension-driven development]] finding that most effective AI work is planning, not generation.

## Verification Loops

The bottleneck has shifted from writing code to verifying it. The most important pattern for managing parallel agents is building verification loops where agents review each other.

**Florian's PR-review-feedback agent**: when a reviewer leaves comments on a PR, an agent reads the feedback, makes code changes, and sends a message back with new changes. Repeat across hundreds of PRs and the saved time compounds.

**Why separate reviewers work better**: "The person who wrote the code is the worst person to review it." A fresh session has no attachment to what it's looking at. Boris Cherny: giving an agent the ability to verify its work results in 2–3x quality improvement.

Kilo ships separate agents for code review, security, and hosted workflows — making cross-agent verification a first-class product feature.

## Software as Gardening

Mark's metaphor: "I like to think of software engineering as gardening instead of building." Instead of doing the grunt work (boilerplate, scaffolds), you apply judgment. "You can just say: take care of that, remove that weed. That's much closer to how it feels to interact with an agent."

Background agents fit this model: you give them a small piece of work, let them progress on their own, and come back later to prune. The agents do the building. You do the gardening.

This complements Geoffrey Huntley's "software as clay on a pottery wheel" metaphor — both suggest less front-loading and more iterative shaping, but gardening implies ongoing maintenance while clay implies shaping and discarding.

## Routines: The First Programmatic Application

Boris Cherny identifies routines as the first obvious application of programmatic Claude Code. An engineer set up a routine that listens for every GitHub issue and bug report about voice mode, proactively puts up a fix, and pings the PR. When Boris shipped a feature with an edge case, another engineer's routine had already fixed the bug within five hours — before Boris knew about it. "There's always like another person's Claude that's working on it."

Routines handle code review, babysitting PRs, fixing CI, and rebasing. "I haven't done that in a long time." This is the background agent pattern from Kilo Code, but automated: instead of manually dispatching fire-and-forget tasks, routines trigger on events (new issues, bug reports, PR comments) and act autonomously.

Source: `raw/Reflecting on a year of Claude Code.md`.

## Hundreds of Agents: Agent View, Voice Mode, and Remote Control

Boris describes running hundreds of agents simultaneously, using three product features:

| Feature | Purpose |
|---|---|
| Agent view | Single-tab view of all running agents instead of six terminal tabs |
| Desktop app | Handles worktree cloning automatically |
| Remote Control | Start, monitor, and steer agents from a phone |

"Half my engineering now I do on my phone. I start agents from my phone, use voice mode to talk to them, walk around getting coffee while they work." Cat: "You would leave work, have your computer on your desk open, plugged in, screen locked... and then it happened again the next day."

This pushes beyond the Kilo Code finding of 2–4 foreground agents. The difference is tooling: Boris uses agent view (a dashboard), Remote Control (phone-based monitoring), and routines (event-driven automation). The Kilo Code engineers used terminal tabs and manual dispatch. Better tooling may raise the practical foreground limit.

Source: `raw/Reflecting on a year of Claude Code.md`.

## Auto Mode: The Permission Model Evolved

Boris no longer uses plan mode. "The newer models don't actually need a planning step anymore. Starting with 4.6 and definitely with 4.7, it just doesn't need that planning step." Instead, auto mode routes permission prompts to a classifier model that checks for security. "When you accept 99% of requests, your eyes just glaze over. Auto mode is more safe than reading every single permission prompt."

The security model behind auto mode:
1. Thousands of transcripts of full agent trajectories with permission prompts.
2. Auto mode classifies whether each was safe — "extremely good at this."
3. Red teamers tried to prompt inject and hack the codebase.
4. Evals ensured all attacks were denied.
5. Internal teams tried to prompt inject — auto mode improved to catch them.

This tensions with the plan-then-execute pattern from Kilo Code. The resolution is model-dependent: older models needed explicit planning steps; 4.6/4.7 plan implicitly and benefit from auto mode's continuous permission model rather than a front-loaded planning phase.

Source: `raw/Reflecting on a year of Claude Code.md`.

## Connections

- [[concepts/Context Rot]] — The 60% quality drop threshold is concrete evidence for context rot in practice.
- [[concepts/Harness Engineering Principles]] — Foreground agents are the harness; background agents are the production line.
- [[concepts/Collaborative AI Engineering]] — Verification loops as cross-agent alignment.
- [[concepts/Tokenmaxxing]] — Parallel agents as structured tokenmaxxing: not just more tokens, but better-allocated tokens across planning and execution.
- [[concepts/Comprehension-Driven Development]] — Planning-first workflow confirmed by Kilo engineers.
- [[concepts/Prompting Skills Not Prompts]] — Task sizing and prompt structuring as skill design inputs.
- [[concepts/Self-Improving Skills]] — Verification loops are a form of quality improvement, though not autonomous self-improvement.
- [[concepts/AI Slop and Garbage Collection]] — Verification loops as garbage collection for agent output.
- [[sources/How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code]] — Source summary.
- [[sources/Reflecting on a year of Claude Code]] — Boris Cherny on hundreds of agents, routines, auto mode, and Remote Control as tooling that raises the practical parallel agent limit.

## Contradictions or Tensions

- The "2–4 foreground agents" finding directly contradicts social media narratives of 50–100 productive parallel agents. The Kilo engineers call this hype explicitly.
- The plan-then-execute pattern assumes the planning model is reliable. If the plan is wrong, the fast executor confidently implements the wrong thing. There is no verification of the plan itself.
- "Software as gardening" and "software as clay" both suggest less front-loading, but they imply different maintenance postures. Gardening is ongoing; clay is shape-and-ship.
- Boris Cherny's "hundreds of agents" and "half my engineering on my phone" contradicts the Kilo Code finding of 2–4 foreground agents. The difference is tooling: agent view, Remote Control, and routines raise the practical limit. Both may be correct for their respective tooling levels.
- Auto mode replacing plan mode tensions with the plan-then-execute pattern. The resolution is model-dependent: 4.6/4.7 plan implicitly; older models needed explicit planning.

## Open Questions

- What is the optimal ratio of foreground to background agents for different task types?
- How should verification loops be structured when the reviewer agent has a different model or capability than the implementation agent?
- At what point does managing background agent PRs become its own bottleneck?
- How do you detect when a background agent has produced a subtly wrong PR that passes tests but violates intent?
