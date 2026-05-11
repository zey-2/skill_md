---
type: concept
created: 2026-05-11
updated: 2026-05-11
status: active
sources:
  - "raw/Meta-Meta-Prompting The Secret to Making AI Agents Work.md"
  - "raw/2026-05-10 Skill Authoring Patterns Cross-Project Research.md"
tags: [meta-skills, skillification, personal-ai, skill-composition]
---

# Meta-Skills and Skillification

## Summary

Meta-skills are skills that create, manage, or orchestrate other skills. Skillification is the process of extracting a repeatable workflow from a one-off task and encoding it as a tested skill file. Garry Tan's GBrain/GStack system demonstrates this at scale: over 100 skills, many created by the `skillify` meta-skill itself, composing together into complex workflows like book-mirror (which calls brain-ops, enrich, cross-modal-eval, and pdf-generation).

Sources: Garry Tan's "Meta-Meta-Prompting" article and the Skill Authoring Patterns cross-project research.

## Key Ideas and Evidence

### Skillification: From Manual to Automated

The skill development cycle from GBrain:

> "If you have to ask your agent for something twice, it should already be a skill running on a cron. First time is discovery. Second time is system failure."

**5-step cycle:**
1. **Concept** — Do something manually the first time.
2. **Run manually** — Execute the workflow 3-10 times.
3. **Evaluate output** — Review results, identify patterns and failures.
4. **Codify into SKILL.md** — Extract the repeatable pattern into a tested skill file.
5. **Add to cron** — Schedule the skill for automatic execution.

The `skillify` meta-skill automates step 4: after a manual workflow, you say "skillify this" and it examines what just happened, extracts the repeatable pattern, writes a tested skill file with triggers and edge cases, and registers it in the resolver.

### Fat Skills, Thin Harness

Tan's architecture separates concerns:

- **Thin harness** — OpenClaw is the runtime. It receives messages, figures out which skill applies, and dispatches. A few thousand lines of routing logic. It doesn't know anything about books, meetings, or founders. It just routes.
- **Fat skills** — Over 100 SKILL.md files, each a self-contained markdown with detailed instructions for one specific task. Skills encode operational knowledge that would take a new human assistant months to learn.
- **Fat data** — 100,000 pages of structured knowledge (the "brain"). Every person, company, meeting, book, article, and idea gets a page. The schema is simple: compiled truth above the line, append-only timeline below, raw data sidecars.
- **Interchangeable models** — Opus 4.7 for precision, GPT-5.5 for recall, DeepSeek V4-Pro for creative work. The skill decides which model to call. The harness doesn't care.

### Skill Composition

Skills compose into complex workflows:

- **book-mirror** calls brain-ops (storage), enrich (context), cross-modal-eval (quality), and pdf-generation (output).
- **meeting-ingestion** creates structured summaries and propagates entity updates to person and company pages.
- **enrich** pulls from five sources and merges into a single brain page.
- **perplexity-research** checks what the brain already knows before synthesizing new findings.

Each skill does one thing. When one skill improves, every workflow that uses it gets better automatically.

### Cross-Modal Evaluation

Every skill output runs through multiple models that score each other:
- Opus 4.7 catches precision errors.
- GPT-5.5 catches missing context.
- DeepSeek V4-Pro catches when something reads as generic.

This caught factual errors in book-mirror (e.g., wrong family history). The fix got baked into the skill, and every subsequent mirror was clean.

### GStack Skills (Virtual Development Team)

GStack presents skills as specialist roles:
- CEO, Engineering Manager, Staff Engineer, Debugger, Designer, etc.
- Each skill has a bash preamble handling updates, session management, config, telemetry, and routing.
- "Boil the Lake" principle: AI makes completeness cheap — do the complete thing.
- Fix-First Review: auto-fix issues first, then ask about the rest.
- Specialist dispatch ("Review Army"): parallel specialist subagents merged with confidence gates.

### GBrain Skill Development Quality Bar

Skills must pass a checklist before deployment:
- Tested on 3-10 real items with user approval.
- SKILL.md under 500 lines.
- Citation enforcement.
- No stubs.
- MECE discipline: each entity type has exactly one owner skill.

### Example Skills from GBrain

| Skill | Purpose |
|---|---|
| book-mirror | Extract chapters, summarize ideas, map to user's life |
| meeting-ingestion | Transcript → structured summary → entity propagation to person/company pages |
| enrich | Merge five sources into a single brain page |
| media-ingest | Handle video, audio, PDF, screenshots, GitHub repos |
| perplexity-research | Web research augmented with existing brain context |
| email-triage | Detect portfolio updates in email, extract metrics |
| calendar-check | Conflict detection and travel impossibility |

### Compounding Infrastructure

The thesis: the future belongs to individuals who build compounding AI systems, not individuals who use corporate-owned centralized AI tools.

Every meeting adds to the brain. Every book enriches the context for the next book. Every skill makes the next workflow faster. Every person page update sharpens the next meeting prep.

The difference is "between keeping a journal and having a nervous system. The filing cabinet stores things. The nervous system connects them, flags what's changed, and surfaces what's relevant to right now."

## Connections

- [[sources/Meta-Meta-Prompting The Secret to Making AI Agents Work|Meta-Meta-Prompting The Secret to Making AI Agents Work]] — source summary for Garry Tan's fat skills/fat data/thin harness article.
- [[Skill Authoring Workflow]] — skillification is one method of authoring skills.
- [[Self-Improving Skills]] — both approaches use eval-driven iteration, but skillification is human-directed while self-improvement is autonomous.
- [[SKILL.md Package Anatomy]] — the 500-line constraint and reference file patterns.
- [[Harness Engineering Principles]] — thin harness over fat skills is a core architecture pattern.
- [[Context Development Lifecycle]] — the brain is a continuously maintained context repository.
- [[Understanding as the Human Bottleneck]] — skillification addresses the bottleneck by encoding human judgment into reusable patterns.

## Open Questions

- How do you prevent skill explosion? At what point does maintaining 100+ skills become a full-time job?
- What happens when two skills produce conflicting outputs for the same entity page?
- How do you version and migrate a large skill graph when the underlying models change?
- Is the "thin harness" approach portable across different agent runtimes, or is it tightly coupled to OpenClaw/Hermes?
