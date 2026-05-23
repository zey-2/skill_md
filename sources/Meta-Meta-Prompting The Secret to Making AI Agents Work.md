---
type: source-summary
created: 2026-05-10
updated: 2026-05-23
status: active
sources:
  - "raw/Meta-Meta-Prompting The Secret to Making AI Agents Work.md"
tags: [agent-skills, skillification, personal-ai, gbrain, openclaw]
---

# Meta-Meta-Prompting: The Secret to Making AI Agents Work

**Source**: [X / @garrytan](https://x.com/garrytan/status/2053127519872614419)
**Author**: Garry Tan
**Published**: 2026-05-09
**Created**: 2026-05-10

## Summary

Garry Tan describes his personal AI system built around the "fat skills, fat code, thin harness" architecture. He demonstrates how skills compose into complex workflows, how a meta-skill ("Skillify") creates new skills from repeated work, and how a structured knowledge base ("brain") compounds value over time. Part of his series on personal AI as an operating system rather than a chat window.

## Key Points

### Architecture: Fat Skills, Fat Code, Thin Harness

- **Thin harness**: OpenClaw or Hermes Agent as runtime — a few thousand lines of routing logic that receives messages, figures out which skill applies, and dispatches. Knows nothing about domains (books, meetings, founders).
- **Fat skills**: 100+ self-contained Markdown files with detailed instructions for specific tasks. Examples include book-mirror, meeting-ingestion, enrich, media-ingest, perplexity-research, email-triage, and more.
- **Fat data**: ~100,000 pages of structured knowledge — every person, company, meeting, book, article, and idea, all linked and continuously updated.
- **Interchangeable models**: Opus 4.7 1M for precision, GPT-5.5 for recall/extraction, DeepSeek V4-Pro for creative work, Groq/Llama for speed. **The skill decides which model to call for which task.** "The model is just the engine. Everything else is the car."

### Skillify: Skills That Build Skills

- Skillify is a **meta-skill** that creates new skills. When encountering a repeated workflow, saying "skillify this" examines what happened, extracts the repeatable pattern, writes a tested skill file with triggers and edge cases, and registers it in the resolver.
- Every fix compounds across all future runs of that skill. "When I improve one skill, every workflow that uses it gets better automatically."

### Book-Mirror: A Skillified Workflow

- The book-mirror skill extracts all chapters of a book, runs a sub-agent per chapter that summarizes ideas and maps them to the user's actual life using accumulated context.
- Iterated through multiple versions: V1 had factual errors → added mandatory fact-check step → V3 added deep retrieval with per-section brain searches and citations.
- Each subsequent mirror knows about all previous mirrors — the context compounds.

### The Brain: 100,000 Pages of Structured Knowledge

- Schema: compiled truth at top, append-only timeline below, raw data sidecars for source material.
- After every meeting: entity propagation walks through every person/company mentioned and updates their brain pages.
- "The difference between having a filing cabinet and having a nervous system. The filing cabinet stores things. The nervous system connects them."

### How to Start

1. **Pick a harness** — OpenClaw, Hermes Agent, or build your own. Keep it thin.
2. **Start a brain with GBrain** — Git repo where every entity gets a page. 97.6% recall on LongMemEval. Ships 39 installable skills.
3. **Do something interesting** — Don't plan architecture first. Do a task, iterate until good, then Skillify the pattern. Run `check_resolvable` to verify wiring.
4. **Keep using it** — The skill will be mediocre at first. Use cross-modal eval to catch errors. Fix gets baked into the skill. In 6 months you have something no chatbot can replicate.

## Evidence

The source-summary claims above are grounded in the local raw source file listed in frontmatter.

## Connections

- [[concepts/Agent Skills]] — Real-world example of fat, composable skills in production.
- [[concepts/Progressive Disclosure]] — Skills as self-contained expertise packages loaded on demand.
- [[concepts/Skill Authoring Workflow]] — The Skillify loop: do work manually → extract pattern → write skill → iterate → compound.
- [[concepts/Harness Engineering Principles]] — Thin harness routing to fat skills; "code is free, scarce resources are human time and context."
- [[concepts/Replacing Code with Skills]] — Parallel theme: encoding workflows as skills rather than hard-coded application logic.
- [[concepts/Context Development Lifecycle]] — The brain as a continuously growing context repository with entity propagation as the distribution loop.

## Sources

- [X: Meta-Meta-Prompting](https://x.com/garrytan/status/2053127519872614419) — Garry Tan's article (part of the Fat Skills series)
- [GStack](https://github.com/garrytan/gstack) — Coding skill framework (87,000+ stars)
- [GBrain](https://github.com/garrytan/gbrain) — Knowledge infrastructure with 39 installable skills
- [OpenClaw](https://openclaw.ai/) — Agent harness runtime
- [Hermes Agent](https://hermes-agent.nousresearch.com/) — Alternative agent harness
