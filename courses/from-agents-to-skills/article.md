---
type: article
created: 2026-05-10
updated: 2026-05-10
status: draft
tags: [article, course, agent-skills]
sources: []
---

# From Agents to Skills: Capturing Expertise, Making It Repeatable

*The gap isn't intelligence. It's operating procedure.*

---

## Introduction: What Changed?

AI agents can now do work that was previously impractical to encode reliably with traditional rules. Not merely difficult to automate, but difficult to specify in enough detail for brittle if-then logic to handle consistently.

They can **reason** across documents, code, and context simultaneously. They can **synthesize** from multiple sources into coherent output. They can **execute** multi-step workflows without every detail being specified. They can **generate** production-quality code, documents, and plans.

That changes the shape of work. A team can ask an agent to draft a pull request, summarize an incident, prepare a vendor comparison, clean up a data pipeline, or turn rough meeting notes into an action plan.

This isn't just a better IDE. It's a different kind of worker.

And like any new kind of worker, the question isn't only whether it's smart enough. The question is whether we've given it the right operating procedures to do its job consistently.

## The Gap: Capability Without Consistency

Here's what happens when you give the same AI agent the same task twice:

**Run 1:** Did step A. Did step B. Missed step C. Invented step D.

**Run 2:** Did step C. Skipped step B. Did step D. Invented step E.

Same agent. Same task. Different result every time. Each result needs review, correction, and cleanup. The agent doesn't know how *your* team wants things done, not because it can't follow a process, but because nobody has written that process in a way it can reliably use.

The gap isn't intelligence. It's operating procedure.

Before skills, this played out in a hundred small ways every day.

Your team writes PR descriptions. Every agent does it differently. Some write one-line summaries, some include test notes, some skip them entirely. Nobody follows the team's checklist.

Your team prepares incident reports. One agent focuses on timeline, another on root cause, another on customer impact. The structure changes every time.

Your team evaluates vendors. One run compares pricing, another compares compliance, another invents a scoring method that nobody agreed to use.

Time is wasted correcting agent output *every single session*. No consistent team standards are enforced. Each session starts from zero: no memory, no pattern, no operating rhythm.

Every session is a new conversation.

## Why Agent Skills

Skills give an AI agent a brain for a specific job. When a skill is attached, the agent knows:

- **When to use it.** The agent decides which skill applies to which task.
- **What steps to follow.** Consistent process every single time.
- **What resources are available.** API docs, schemas, team conventions, and templates loaded on demand.
- **What constraints matter.** Team standards, quality gates, security rules, and guardrails.

Skills fall into two categories: **domain skills** and **workflow skills**.

A domain skill captures what the agent needs to know. For example: "our API's pagination uses cursor-based offsets, not page numbers."

A workflow skill captures how the agent should operate. For example: "every PR description must include a testing plan and link to the relevant ticket."

Both matter. Both are missing from a fresh agent session.

## How Skills Are Built: Three Approaches

There is no single correct way to build a skill. The right approach depends on how much rigor the workflow needs.

### 1. The Conversational Approach: Grill → Draft → Iterate

Matt Pocock's method is straightforward: grill the human before building anything, draft the `SKILL.md` together, then iterate from real usage. You ask what the person actually does, capture it, and refine as you go.

**Best for:** personal skills, quick team conventions, and situations where speed matters more than rigor.

### 2. The Test-Driven Approach: RED → GREEN → REFACTOR

The Superpowers method treats skills like code. First, run the task *without* the skill and watch it fail. Then write the skill to fix those specific failures. Finally, re-test under pressure to close loopholes.

**Best for:** discipline-enforcing workflows, quality-critical processes, and anything where inconsistency has a real cost.

### 3. The Benchmarking Approach: Eval Viewer + Comparison Testing

Anthropic's `skill-creator` approach is the most quantitative. Write 3–5 test prompts representing real tasks. Run them both with and without the skill. Grade the outputs using an eval viewer, then iterate on the scores.

**Best for:** objectively verifiable outputs and teams that need data to justify process changes.

The spectrum runs from lightweight to rigorous. There is no wrong starting point, only different tradeoffs.

### What All Three Approaches Agree On

Despite their differences, all three methods converge on the same principles:

- **Examples over abstractions.** One excellent example beats many mediocre ones.
- **Test before deploy.** Run the task without the skill first. Watch it fail. Then write the skill to prevent that specific failure.
- **Keep `SKILL.md` concise.** Keep the main file focused. Move bulk content to `references/`.
- **References one level deep.** No nested reference mazes. Link directly from `SKILL.md`.
- **Skills are living documents.** Improve them from real usage. They are not write-once-done.
- **Flat namespaces.** Keep skills easy to discover and route.

## SKILL.md Deep Dive: The Skill Package

A skill is a portable unit of agent knowledge. Its file structure is intentional:

```text
my-skill/
  SKILL.md           # Main instruction file
  references/        # Background docs, API schemas
  scripts/           # Deterministic helper scripts
  assets/            # Templates, images, static files
```

When a skill triggers, the agent reads `SKILL.md`. The other directories are loaded on demand. The agent pulls in `references/` docs when it needs background context, runs `scripts/` when the workflow calls for them, and uses `assets/` for templates.

### Frontmatter Is the Routing Mechanism

Every `SKILL.md` starts with a frontmatter block. Two fields matter more than everything else combined: `name` and `description`.

The `description` is the routing mechanism. The agent sees *only* this field to decide whether the skill applies to the current task. That means:

- It contains **triggering conditions only**, not the full workflow.
- It starts with "Use when..."
- It is written in third person.
- It stays under 500 characters.
- It is specific enough to avoid false matches.

The difference between a weak and strong description is operational.

**Weak frontmatter:**

```yaml
---
name: code-review
description: Do a code review.
---
```

This may cause the agent to do one pass and stop. The multi-stage review described in the skill body may never happen, because the description did not tell the agent when the full workflow applies.

**Stronger frontmatter:**

```yaml
---
name: two-stage-code-review
description: Use when reviewing completed code changes. Run a two-stage review: first for correctness and regressions, then for maintainability, tests, and team conventions before final approval.
---
```

Now the agent knows not just the topic, but the operating shape of the task.

### Progressive Disclosure

Skills manage context through three layers of progressive disclosure:

1. **Layer 1: Metadata** (~100 tokens): `name` and `description`. Always loaded. The agent uses this to decide whether the skill applies.
2. **Layer 2: `SKILL.md` Body** (~500 lines): Instructions, steps, constraints. Loaded when the skill triggers.
3. **Layer 3: References** (on demand): API docs, schemas, scripts. Loaded only when the agent needs them.

The rule is simple: if it is too long for the main file, put it in `references/` and link to it. Keep `SKILL.md` concise. The agent will thank you, and so will your token budget.

## What Good Looks Like

Two examples illustrate the range.

**Matt Pocock's approach** is simple and practical. A "grill me" skill runs an alignment session: short, focused, and direct. It is written for personal use and quick team conventions. ([github.com/mattpocock/skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md))

**Superpowers' approach** is comprehensive and disciplined. A skill for writing skills includes pressure testing, rationalization tables, and every loophole closed. It is written for quality-critical, discipline-enforcing workflows. ([github.com/obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md))

Different rigor, same DNA.

### The Superpowers Workflow

The `superpowers` repo ([github.com/obra/superpowers](https://github.com/obra/superpowers)) deserves special mention because it doesn't just contain skills. It contains a *workflow* of skills that chain together:

1. **Brainstorming** to explore requirements before building
2. **Git worktrees** for isolated feature work
3. **Writing plans** before touching code
4. **Executing plans** with review checkpoints
5. **TDD** for implementing features
6. **Code review** with structured feedback
7. **Finishing branches** with merge or PR decisions

Supporting skills include systematic debugging, parallel agent dispatching, subagent-driven development, verification-before-completion, and meta-skills for writing skills themselves.

## AI Risks and Defenses

Skills are powerful. They run on your machine. That combination demands a security mindset.

### The Risks

**Prompt Injection:** Hidden instructions in user input can override an agent's skill behavior. A crafted document or message can redirect what the agent does, bypassing the skill's constraints entirely.

**Supply Chain Risk:** Installing skills from unverified authors creates the same problem as installing untrusted packages. A skill is code and instructions that may run with access to your project files.

**Data Exfiltration:** Scripts within a skill can read sensitive files and transmit them externally. A skill can include `scripts/` that run on your machine. Those scripts may access `.env` files, credentials, proprietary code, or private documents.

### The Defenses

Treat skill installation like dependency review. Before installing or sharing a skill, use a compact pre-install checklist:

- **Read `SKILL.md`.** Confirm the workflow matches the stated purpose.
- **Inspect every script.** Do not run helper scripts you do not understand.
- **Search for network calls.** A formatting or writing skill should not quietly call external services.
- **Check file access.** Look for commands that read secrets, home directories, `.env` files, SSH keys, or credential stores.
- **Test in a sandbox.** Run unfamiliar skills in a low-permission environment first.
- **Prefer verified sources.** Use known authors, official registries, peer-reviewed repos, or internal repositories.
- **Apply the principle of least surprise.** A skill's contents should not surprise you in their intent. If a "code formatting" skill includes credential scanning or external upload logic, that's not a bonus feature. It's a red flag.

Skills are code. Treat them like code.

## Conclusion

The story of AI agents in the workplace is shifting. It is no longer only about whether the agent is smart enough. It is about whether we have given it the right operating procedures to be consistently useful.

Skills, captured as `SKILL.md` files, are the mechanism. They turn tribal knowledge into repeatable process. They make every session start from the team's standards, not from zero. They encode what good looks like, so the agent doesn't have to guess.

Three approaches exist for creating them, from conversational to rigorously benchmarked. All of them agree on the same principles: use examples, test before deploy, keep the main file concise, and treat skills as living documents.

They also come with the same caveat: skills are code running on your machine. Read them. Trust their sources. Treat them with the same security discipline you'd apply to any dependency.

The capability exists. The consistency is up to you.

---

## Further Reading

- [Matt Pocock's Skills Collection](https://github.com/mattpocock/skills)
- [Superpowers — Skill-Driven Development](https://github.com/obra/superpowers)
- [Anthropic Agent Skills Documentation](https://docs.anthropic.com/en/docs/agents/agent-skills/overview)
- [Anthropic Skill-Creator Tool](https://github.com/anthropics/skill-creator)
