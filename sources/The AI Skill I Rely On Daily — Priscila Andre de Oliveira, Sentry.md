---
type: source-summary
created: 2026-06-01
updated: 2026-06-01
status: active
sources:
  - "raw/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md"
tags: [comprehension, skill-authoring, ai-usage-patterns, sentry, ai-native-work]
---

# The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry

**Source**: AI Engineer World's Fair talk / YouTube, `https://www.youtube.com/watch?v=li0SaBt9RDM`  
**Speaker**: Priscila Andre de Oliveira (Sentry, Verdaccio maintainer, Vienna JS co-organizer)  
**Published**: 2026-05-28  
**Created**: 2026-06-01

## Summary

Priscila Andre de Oliveira analyzed 116 of her own Claude sessions from daily work at Sentry and found that **67% of AI usage was comprehension and only 2% was code generation**. This empirical data supports the thesis that the biggest unlock from AI in large codebases is not generation but understanding. She built a personal skill called "Catch Me Up" that structures comprehension queries into six exploration modes: Architecture, Convention, Feature Trace, Syntax, Testing, and History.

## Key Points

- Priscila describes herself as an "agent manager" — she hasn't coded directly since December 2025, only prompting.
- At Sentry, ~100 PRs merge daily across a 15+ year codebase. Comprehension is the daily bottleneck.
- She had Claude analyze 116 of her sessions and classify them into six categories: Comprehension, Modification, Process, Review, Generation, and Other.
- **67% comprehension, 2% generation** — the distribution surprised even her.
- Her prompts kept repeating, so she created a local skill called "Catch Me Up" to structure comprehension queries.
- The skill offers six exploration modes: Architecture (organogram/structure), Convention (how things are done), Feature Trace (follow a feature), Syntax (understand specific code), Testing (how tests work), and History (what changed and why).
- She is a visual person and designed the skill to produce tables, diagrams, and visual summaries — not just text.
- She uses the skill for onboarding to new repositories and for PR review when she has partial context.
- She emphasizes the "understand before you prompt" principle: you need a mental model alignment before the code flows naturally.
- She warns against shipping "slop code" into the codebase that pays your salary — "ship keynote code."
- References Jack Nation's "vibe coding our way to disaster" post and Armin Ronacher's concern about developers not knowing what code is in their own codebase.
- She agrees that research → planning → implementation is the right sequence, but argues that **understanding the research the agent did** is a missing step that must come before planning.

## Evidence

- The 116-session analysis was done by having Claude examine her actual session cache and classify each session.
- The "Catch Me Up" skill is a `.md` file with human-readable instructions — it demonstrates skills as personal, local tools, not necessarily shared packages.
- She demoed the skill on a new repository she was unfamiliar with, asking Claude to explain how it works (simulating Sentry envelopes during tests). The output included a flow diagram, summary, and answers to specific questions.
- Sentry's internal AI projects include Abacus (AI usage tracking), Warden (code review agent for PRs), and Junior (Slack bot that analyzes bug reports and creates PRs).
- Sentry spent a "quality quarter" removing `any` types, TODOs, unused feature flags — demonstrating that code quality maintenance remains essential even with AI.

## Connections

- [[concepts/Ride the Models]] — Priscila exemplifies riding the models: adapting her role from coder to "agent manager" by continuously experimenting with AI in real work.
- [[concepts/Comprehension-Driven Development]] — Primary source for the 67% comprehension finding and the "Catch Me Up" skill pattern.
- [[concepts/Understanding as the Human Bottleneck]] — Empirical evidence that understanding dominates generation in real AI-assisted work.
- [[concepts/Agent Skills]] — Demonstrates skill creation from personal usage pattern analysis (self-quantification → repeated pattern → skill).
- [[concepts/Skill Authoring Workflow]] — Shows how recurring prompts naturally crystallize into reusable skills.
- [[concepts/The AI-Native Engineer and the Rising Ceiling]] — Priscila's role shift illustrates the rising ceiling: deep users become force multipliers.
- [[concepts/Harness Engineering Principles]] — The "Catch Me Up" skill is a personal harness that preserves her scarce attention for comprehension.

## Contradictions or Tensions

- The 67/2 split may be specific to Priscila's role (senior frontend engineer at a large, mature codebase). Developers in greenfield projects or different roles may see different ratios.
- Her "haven't coded since December 2025" claim is aspirational — she still reviews, approves, and steers work, which involves code reading and sometimes editing.
- The "ship keynote code" vs "slop code" framing raises the question of how to define quality thresholds when AI generates most of the code.

## Open Questions

- What is the comprehension/generation split for developers in different roles (backend, infra, greenfield, solo)?
- Can comprehension skills like "Catch Me Up" be generalized across codebases, or are they inherently project-specific?
- How should teams track and share comprehension patterns as reusable team skills rather than personal ones?
