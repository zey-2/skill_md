---
type: concept
created: 2026-05-30
updated: 2026-05-30
status: active
sources:
  - "raw/How the engineer behind Claude Cowork actually uses Claude  Felix Rieseberg (Anthropic).md"
tags: [workflow-patterns, abstraction, automation, personal-productivity, anti-patterns]
---

# Anti-To-Do List and Abstraction Layering

## Summary

The anti-to-do list is a workflow pattern: whenever you find yourself doing something tedious or annoying, stop and go one abstraction layer up. First ask "Why am I doing this manually — can Claude do this?" Then go another layer up: "How do I never have to do this again?" The goal is not to complete the task but to eliminate the category of task.

Source: `raw/How the engineer behind Claude Cowork actually uses Claude  Felix Rieseberg (Anthropic).md`.

## The Pattern

Felix Rieseberg, engineering lead for Claude Cowork and Claude Code Desktop at Anthropic, describes a recursive abstraction technique:

1. **Layer 1 — Delegate**: Instead of manually entering furniture dimensions into a planner, tell Claude: "Figure out what furniture I have."
2. **Layer 2 — Discover**: Instead of telling Claude what furniture you own, give it access to your email and say: "Find all the furniture I bought."
3. **Layer 3 — Systematize**: Instead of one-off queries, build a persistent system (database, files, scheduled reminders) so the inventory updates automatically and new data mixes in over time.

Each layer removes more manual work and frees the human to focus on creative steering — in Rieseberg's case, designing the house planner's 3D walkthrough and custom features rather than cataloguing measurements.

## The Anti-To-Do List

The term comes from a product coach who uses it with executives: "Anytime you're doing something that's tedious, I just smack their hands. Why are you doing this? You don't do that. Your hands are not allowed to touch this. You need to go ask — go that abstraction layer up: how could Claude do this?"

The next question after "how could Claude do this" is "how will I never have to do this again?" This is the difference between a one-off automation and a durable system.

## Real Examples

| Task | Layer 1 (Delegate) | Layer 2 (Discover) | Layer 3 (Systematize) |
|---|---|---|---|
| Furniture inventory | Enter dimensions manually | "Find my furniture purchases in email" | Persistent inventory that auto-updates with new purchases |
| Promise tracking | Write promises in a notebook | "Read my messages and find commitments" | SQLite database + periodic reminders, no re-reading needed |
| Meeting prep | Read calendar manually | "Summarize today's meetings" | Pull Slack history, recent conversations, and context about each person beforehand |
| House floor plan | Draw units by hand | "Read floor plan PDF, add units" | Interactive 3D planner built from permit data |

## Why This Matters

The anti-to-do list is a behavioral discipline, not a technical capability. Most people stop at layer 1 — they delegate the manual task but still supervise closely. Going to layer 2 requires trust: you stop telling Claude what data you have and let it discover the data source. Going to layer 3 requires systems thinking: you ask for durability, not just a one-time result.

The creative payoff is significant. Rieseberg spent his time on "steering Claude on what the house planner should be like" and "adding stupid little features like I want to walk through the house myself in 3D" — creative direction — instead of measuring furniture.

## Connections

- [[concepts/Ride the Models]] - Abstraction layering is a skill that improves with model iteration and experimentation.
- [[concepts/Understanding as the Human Bottleneck]] - Going up abstraction layers requires understanding the task well enough to delegate the right thing.
- [[concepts/Harness Engineering Principles]] - Layer 3 systematization is organizational harness: building persistent systems rather than one-off prompts.
- [[concepts/Personal AI Agents and Memory Systems]] - The promise tracker and furniture inventory are personal agent memory patterns.
- [[concepts/AI-Native Work Archetypes]] - Product-minded builders naturally apply abstraction layering to their own work.
