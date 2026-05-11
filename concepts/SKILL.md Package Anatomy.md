---
type: concept
created: 2026-04-26
updated: 2026-05-11
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/mattpocockskills Skills for Real Engineers. Straight from my .claude directory.md"
  - "raw/2026-05-10 Skill Authoring Patterns Cross-Project Research.md"
tags: [agent-skills, skill-md, package-anatomy]
---

# SKILL.md Package Anatomy

## Summary

`SKILL.md` is the main file inside an agent skill package. It usually contains YAML front matter at the top and Markdown instructions below. The package may also include folders for scripts, references, and assets.

The simplest mental model is:

- `SKILL.md` tells the agent what the skill is and how to use it.
- `references/` holds longer background material.
- `scripts/` holds deterministic helper code.
- `assets/` holds images, templates, or other supporting files.

Source: `raw/skill.md for AI Agents.md`, sections "What skill.md is for AI agents" and "Recommended repository model and schema".

## Key Ideas and Evidence

The raw source says the package pattern appears across OpenAI Codex, Anthropic skills, GitHub Copilot skills, Mintlify, and the Agent Skills project. It identifies `SKILL.md` as the operational unit an agent installs and loads, while site-level lowercase `skill.md` is more of a discovery surface.

The required fields are usually small. The source says `name` and `description` are the most consistently required fields and often determine routing. Extra fields such as owners, versions, examples, constraints, and source provenance are useful for repository management, but they are not equally supported across all vendors.

## Where Sources Agree

The sources summarized in the raw note agree that a skill package should have a main Markdown instruction file. They also agree that the package can include supporting resources, especially when the skill needs detailed examples, API references, scripts, or assets.

They agree on a practical separation of concerns: the main file should orient the agent, while deeper material should be loaded only when needed.

## Where Sources Disagree

The sources differ on naming, optional metadata, and platform-specific files. For example, the raw note describes OpenAI as recommending `agents/openai.yaml` for UI metadata, while Anthropic's public guidance is framed around progressive disclosure and keeping `SKILL.md` lean. Mintlify's format is described as adding minimal optional front matter such as `metadata.internal`.

These disagreements are not necessarily contradictions. They reflect different goals: runtime execution, UI display, documentation discovery, and repository governance.

## Connections

- [[Portable Skill Core]] explains which fields travel best across platforms.
- [[Vendor Adapters]] explains how to keep platform-specific metadata separate.
- [[Progressive Disclosure]] explains why package resources should be loaded in layers.
- [[Skill Authoring Workflow]] explains how to draft a package from concrete use cases.
- [[Meta-Skills and Skillification]] — the skillify meta-skill and SKILL.md quality bar (under 500 lines).
- [[Self-Improving Skills]] — how SKILL.md becomes an editable target for autonomous improvement loops.

## Matt Pocock's Skill Patterns

Matt Pocock's skill collection (`github.com/mattpocock/skills`) demonstrates a practical engineering-oriented approach. His skills are designed to fix common failure modes with coding agents:

### Failure Modes Addressed

1. **The agent didn't do what I want** — solved with "grilling sessions" (`/grill-me`, `/grill-with-docs`) that force the agent to ask detailed questions before starting work.
2. **The agent is way too verbose** — solved with `CONTEXT.md` (a shared language document) that establishes ubiquitous terminology, reducing token waste and improving code naming.
3. **The code doesn't work** — solved with `/tdd` (red-green-refactor loop) and `/diagnose` (disciplined debugging loop).
4. **We built a ball of mud** — solved with `/to-prd` (which quizzes about modules), `/zoom-out` (system-level perspective), and `/improve-codebase-architecture` (periodic architecture rescue).

### SKILL.md Categories

Pocock organizes skills into three tiers:

| Category | Examples | Purpose |
|---|---|---|
| Engineering | diagnose, tdd, to-prd, to-issues, triage, zoom-out, improve-codebase-architecture | Code work, daily development |
| Productivity | caveman, grill-me, write-a-skill | General workflow tools |
| Misc | git-guardrails, migrate-to-shoehorn, scaffold-exercises, setup-pre-commit | Rarely used but available |

### CONTEXT.md as a Companion File

A notable pattern is using `CONTEXT.md` alongside skills — a project-level document that establishes:
- Shared terminology (ubiquitous language from DDD).
- Hard-to-explain decisions (ADRs).
- Domain model glossary.

This makes skills more concise because they can reference shared terms instead of re-explaining them each session.

## Open Questions

- Which optional folders will become expected by most platforms?
- Should repository-only metadata live in `SKILL.md` front matter or in a separate index file?
