---
type: concept
created: 2026-06-01
updated: 2026-06-01
status: active
sources:
  - "raw/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md"
  - "raw/Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic).md"
tags: [comprehension, ai-usage-patterns, planning, spec, human-in-the-loop]
---

# Comprehension-Driven Development

## Summary

Comprehension-Driven Development (CDD) is the pattern where the majority of AI-assisted work time is spent understanding existing code, context, and requirements rather than generating new code. Empirical data from Priscila Andre de Oliveira's analysis of 116 Claude sessions at Sentry shows **67% comprehension, 2% generation**. Thariq Shihipar's complementary finding is that **99% of AI tokens should go to planning, interfaces, and communication** rather than production code. Both practitioners independently arrived at the same conclusion: the human's job is to build and maintain understanding, not to write code.

Sources: `raw/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md` and `raw/Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic).md`.

## The Comprehension Imperative

Two independent practitioners at AI-forward companies measured where their AI time actually goes:

| Practitioner | Role | Measurement | Comprehension | Generation |
|---|---|---|---|---|
| Priscila (Sentry) | Senior engineer | 116 sessions analyzed | 67% | 2% |
| Shihipar (Anthropic) | Claude Code engineer | Token allocation observation | ~99% (planning + communication) | ~1% (production code) |

These numbers converge on the same insight from different angles. Priscila measured actual session classifications; Shihipar measured token allocation across his workflow.

## Why Comprehension Dominates

Several factors explain why understanding consumes most AI-assisted work:

- **Large codebases are complex.** Sentry has 15+ years of code, 100 PRs merged daily, constant deprecations and additions. Understanding what exists before changing it is the primary bottleneck.
- **Agents need steering.** If you don't understand the codebase, you cannot effectively direct an agent. The agent may go in the wrong direction and you won't notice.
- **Repeated comprehension questions.** Priscila noticed her prompts kept repeating — the same "how does this work?" questions across different sessions. This led her to create the "Catch Me Up" skill.
- **Review requires context.** Approving a PR or reviewing generated code requires enough understanding to judge whether the change is correct, not just whether it compiles.
- **Planning needs alignment.** Shihipar's workflow requires understanding what to build before delegating. The spec-review loop exists to preserve human understanding while delegating implementation.

## The "Catch Me Up" Pattern

Priscila's "Catch Me Up" skill is a concrete implementation of CDD. It structures comprehension into six exploration modes:

1. **Architecture** — organogram and structure diagrams
2. **Convention** — how things are done in this codebase
3. **Feature Trace** — follow a feature through the codebase
4. **Syntax** — understand specific code patterns or APIs
5. **Testing** — how tests work and what they cover
6. **History** — what changed, why, and who changed it

The skill produces visual summaries — tables, diagrams, flowcharts — because visual formats are more scannable and retain attention better than raw text. This aligns with Shihipar's finding that HTML specs get read while Markdown plans do not.

## Practical Tactics

- **Track your own AI usage.** Have Claude analyze your session cache and classify sessions by type. The distribution is likely surprising.
- **Create comprehension skills.** When the same questions repeat, package them as a reusable skill with structured exploration modes.
- **Understand before you prompt.** Build a mental model of what exists and what needs to change before delegating implementation.
- **Use visual formats for comprehension.** Tables, diagrams, and flowcharts are more scannable than prose for understanding code structure and flows.
- **Don't ship slop code.** Comprehension ensures you understand what you're shipping. The codebase that pays your salary deserves understanding, not vibes.
- **Research → Understand → Plan → Implement.** The missing step between research and planning is understanding the research the agent did.

## Relationship to Other Concepts

CDD extends [[concepts/Understanding as the Human Bottleneck]] by providing empirical evidence: comprehension is not just important, it is the dominant activity in real AI-assisted work.

It complements [[concepts/Harness Engineering Principles]] because comprehension skills like "Catch Me Up" are personal harness components that preserve scarce human attention for understanding.

It connects to [[concepts/Ride the Models]] through Priscila's role evolution: from coder to "agent manager" who continuously adapts how she uses AI. The comprehension-first stance is one way to ride the models effectively.

It reinforces [[concepts/Tokenmaxxing]] — spending tokens on comprehension (research, analysis, context gathering) is where the investment pays off, not on rapid code generation.

## Contradictions or Tensions

- The 67/2 split may not generalize. Developers in greenfield projects, solo projects, or different domains may see very different ratios. The finding is specific to a senior engineer in a large, mature codebase.
- "Haven't coded since December 2025" is aspirational. Priscila still reviews, approves, and steers — activities that involve code reading and sometimes editing.
- Thariq's "99% on planning" and Priscila's "67% comprehension" measure different things (tokens vs. sessions) but point to the same pattern. The exact numbers should not be over-interpreted.
- The emphasis on comprehension could be misread as "don't generate code." The point is that generation without comprehension produces slop.

## Connections

- [[concepts/Understanding as the Human Bottleneck]] — The human bottleneck is understanding, not typing.
- [[concepts/Harness Engineering Principles]] — Comprehension skills are harness components that protect human attention.
- [[concepts/Ride the Models]] — Priscila's role shift exemplifies riding the models.
- [[concepts/Tokenmaxxing]] — Spending tokens on comprehension is the high-ROI pattern.
- [[concepts/HTML as AI Spec Format]] — Shihipar's HTML workflow is a comprehension tool for both humans and agents.
- [[concepts/Skill Authoring Workflow]] — Repeated comprehension questions naturally crystallize into skills.
- [[concepts/Progressive Disclosure]] — Comprehension skills should present information progressively, not dump everything at once.
- [[sources/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry]] — Primary source for 67/2 finding and "Catch Me Up" skill.
- [[sources/Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic)]] — Complementary source for 99% planning token allocation and HTML spec format.

## Open Questions

- What is the comprehension/generation split for developers in different roles and project types?
- Can comprehension skills be shared across teams and codebases, or are they inherently project-specific?
- How should organizations invest in comprehension tooling versus generation tooling?
- What metrics should track comprehension quality, not just comprehension time?
