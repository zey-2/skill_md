---
type: concept
created: 2026-05-03
updated: 2026-06-14
status: active
sources:
  - "raw/Harness engineering leveraging Codex in an agent-first world.md"
  - "raw/Harness Engineering How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"
  - "raw/after-automation.pdf"
tags: [ai-slop, garbage-collection, code-quality, technical-debt, openai]
---

# AI Slop and Garbage Collection

## Key Points

Full agent autonomy introduces a novel problem: agents replicate patterns that already exist in the repository — including uneven or suboptimal ones. Over time, this inevitably leads to drift and accumulation of "AI slop." The solution is to encode golden principles and build a recurring cleanup process that functions like garbage collection for technical debt.

## What Slop Actually Is

Dan Shipper provides the most precise definition: **"Slop is not any one particular mistake. It is not the use of em dashes, or a certain sentence rhythm, or purple accents on a landing page. Slop is visible sameness, repeated ad nauseam."** It is what gets produced by default when humans in many different circumstances use the same tool, trained on the same corpus, without thinking too hard.

This reframes slop as a systemic problem, not an individual quality failure. The same models, trained on the same data, produce the same defaults. An abundance of sameness rapidly becomes a commodity. The antidote is not better prompting — it is human judgment that breaks the pattern.

Source: `raw/after-automation.pdf`.

## The Slop Accumulation Problem

When agents generate code at high throughput:

- Agents pattern-match against existing code, propagating bad patterns
- Suboptimal implementations get copied across PRs
- Local coherence (within a package) is prioritized over using shared utilities
- Code style and architecture drift over time

Initially, teams addressed this manually — spending every Friday (20% of the week) cleaning up AI slop. This did not scale.

## Golden Principles

Golden principles are opinionated, mechanical rules that keep the codebase legible and consistent for future agent runs. Examples:

1. Prefer shared utility packages over hand-rolled helpers to keep invariants centralized
2. Don't probe data "YOLO-style" — validate boundaries or rely on typed SDKs so agents can't accidentally build on guessed shapes
3. Parse data shapes at the boundary (parse-don't-validate)
4. One way to do bounded concurrency helpers, one ORM, one programming language, one way of writing CI scripts

## Continuous Garbage Collection

Technical debt is like a high-interest loan: it's almost always better to pay it down continuously in small increments than to let it compound and tackle it in painful bursts.

The approach:

- Background Codex tasks run on a regular cadence scanning for deviations
- Quality grades are updated automatically
- Targeted refactoring pull requests are opened by agents
- Most refactoring PRs can be reviewed in under a minute and automerged
- Human taste is captured once, then enforced continuously on every line of code

## Encoding Taste

Human taste is fed back into the system continuously:

- Review comments become documentation updates or encoded into tooling
- Refactoring pull requests surface patterns that need standardization
- User-facing bugs reveal gaps in guardrails
- When documentation falls short, the rule is promoted into code (lints, tests)

The resulting code does not always match human stylistic preferences, and that's acceptable. As long as the output is correct, maintainable, and legible to future agent runs, it meets the bar.

## Persona-Based Review Buckets

To systematize slop detection, review feedback is bucketed by persona:

- Front-end architect
- Reliability engineer
- Scalability expert
- Security reviewer
- Product-minded reviewer

For each persona, a review agent is spun up that triggers on every push, asking: "Is this code good? Surface any P2s or above that would block this PR from merging based on documentation that says what good looks like."

## Connections

- [[concepts/Harness Engineering Principles]] — Garbage collection is one mechanism for encoding human taste into the repository.
- [[concepts/Collaborative AI Engineering]] — Craftsmanship separates exceptional software from "vibe-coded slop"; alignment ensures teams invest time in quality over volume.
- [[concepts/Replacing Code with Skills]] — Hard-coded guardrails prevent slop entirely (physical isolation); prompt-based skills accumulate slop when models forget constraints, requiring evals and garbage collection.
- [[concepts/Zeno's Paradox of AI]] — Slop is the output of the cheap competence cycle (step 3). Garbage collection is the expert response.
- [[sources/After Automation]] — Shipper's definition: "Slop is visible sameness, repeated ad nauseam."

## Source

- [[raw/Harness engineering leveraging Codex in an agent-first world]]
- [[raw/Harness Engineering How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]]
