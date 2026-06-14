---
type: concept
created: 2026-06-14
updated: 2026-06-14
status: active
sources:
  - "raw/The Ideation Process from Problems to Practical Solutions.md"
  - "raw/Superpowers How Jesse Built the 1 AI Claude Code  Codex Plugin — and Stopped Writing Code.md"
  - "raw/new_economics_of_software.md"
tags: [ideation, brainstorming, taste, discernment, socratic, diverge-converge, ai-native-work]
---

# AI-Enhanced Ideation

## Summary

AI enhances ideation not by replacing human creativity, but by expanding the option space, accelerating research, and forcing clarity through Socratic dialogue. When AI collapses implementation cost to near-zero, ideation shifts from a bottleneck to the primary value-creating activity — and the human skill of discernment (taste) becomes the scarce resource. The winning pattern is human judgment directing AI execution across a structured diverge-then-converge pipeline.

## AI as Socratic Brainstorming Partner

The most proven pattern treats AI not as an idea generator, but as a questioner that forces clarity. Jesse Vincent's Superpowers workflow demonstrates this concretely:

- **Socratic dialogue** — Claude asks probing questions that push past surface-level requests into actual intent. As Vincent describes: *"It tricks me into explaining what I wants. It asks me relevant questions because it has pretty good world knowledge. It can make proposals. But the goal is to get me to figure out what I want and explain it to the point where it can go and write a spec."*
- **Independent research during ideation** — AI performs background research (technology feasibility, competitive analysis) while you brainstorm, reducing uncertainty before committing to a direction. Vincent reports spending *"four and a half hours in brainstorm with Claude like it was a half day planning process"* including technology choice validation.
- **Visual proposals** — Generate mockups or prototypes mid-conversation to test whether an idea "feels right" before investing further.

The critical design choice: Vincent removed a convenient question-clicking UX because it let him approve answers without forming the underlying intent. Good AI-assisted ideation increases human understanding rather than replace it.

## Why AI Makes Ideation More Important

The collapse of implementation cost removes the traditional filter ("we can only afford to build three of these"). This creates a new problem:

| Old world | New world |
|---|---|
| Can we build it? → Yes/No | Should we build it? → Which of 30 ideas? |
| Scarcity is engineering time | Scarcity is **taste and discernment** |
| Ideation is the fun part | Ideation is the *hard* part |

When all thirty ideas can be built in hours, choosing which ones matter becomes the critical skill. AI doesn't replace ideation — it makes ideation the bottleneck.

## The Diverge-then-Converge Pipeline (AI-Accelerated)

The structured ideation methodology maps directly onto AI-assisted workflows:

| Stage | How AI helps |
|---|---|
| **Understand** | Researches the problem space, surfaces related work, challenges assumptions |
| **Explore** | Generates broad candidate directions you might not see (divergent thinking) |
| **Generate** | Produces volume — many candidates quickly, expanding the option space |
| **Combine** | Identifies patterns across ideas, suggests mashups and hybrids |
| **Evaluate** | Runs feasibility checks, competitive analysis, cost estimates |
| **Prototype** | Builds quick-and-dirty implementations to test ideas in hours, not weeks |
| **Learn** | Instruments prototypes, analyzes user data, feeds back into the next cycle |

The key principle is to **diverge widely before converging carefully**. AI excels at the divergent phases (volume, research, breadth) while humans own the convergent phases (judgment, taste, selection).

## What AI Cannot Do

Ideation and taste depend on human understanding that cannot be outsourced:

- **Taste** — knowing which ideas will resonate with users — requires lived experience, domain knowledge, and empathy that AI does not have
- **Judgment** — understanding users, markets, and tradeoffs — compounds over time and cannot be automated because it requires context the agent does not have
- **The filter problem** — without human discernment, teams risk building everything and achieving nothing. Taste becomes the new prioritization mechanism

## Practical Pattern: Human Judgment + AI Execution

The winning workflow:

1. **You** define the problem and set criteria for what "good" looks like
2. **AI** expands the option space (research, generate, prototype)
3. **You** exercise taste to pick what matters
4. **AI** builds, measures, and iterates
5. **You** interpret the results and refine direction

Ideation is not automated — it is **augmented**. AI handles the divergent, high-volume, research-heavy phases while humans own the convergent, judgment-heavy ones.

## Connections

- [[concepts/The New Meta - Measurement, Ideation, Iteration]] — The broader framework where ideation is one of three value-creating activities when building becomes cheap
- [[concepts/Understanding as the Human Bottleneck]] — Taste and discernment require human understanding that cannot be outsourced to agents
- [[concepts/Comprehension-Driven Development]] — AI-assisted ideation is comprehension-heavy: understanding the problem space dominates over generating solutions
- [[concepts/Software Economics]] — The economic shift from scarcity to abundance that elevates ideation's importance
- [[concepts/Spec-Driven Development]] — Ideation feeds into specs; the Socratic brainstorming phase produces the clarity needed for spec writing
- [[concepts/Tokenmaxxing]] — Spending tokens on ideation research and exploration is high-ROI investment
- [[concepts/Ride the Models]] — Effective ideation requires adapting how you use AI as models evolve
- [[sources/The Ideation Process from Problems to Practical Solutions]] — The structured ideation pipeline methodology
- [[sources/Superpowers How Jesse Built the 1 AI Claude Code Codex Plugin]] — Primary source for the Socratic brainstorming pattern

## Open Questions

- How does AI-assisted ideation differ across domains (software, product design, research, creative work)?
- What prompts or skill structures best elicit Socratic questioning from AI rather than direct answers?
- How do teams calibrate the diverge/converge balance — when is more AI-generated breadth counterproductive?
- Can taste be taught, or is it purely experiential? If teachable, can AI assist in developing taste?
