---
type: source-summary
created: 2026-05-10
updated: 2026-05-10
status: active
sources:
  - "raw/Agent Skills Overview.md"
tags: [agent-skills, agentskills-io, open-standard]
---

# Agent Skills Overview (agentskills.io)

**Source**: [agentskills.io/home](https://agentskills.io/home)
**Created**: 2026-05-10

## Summary

The official Agent Skills open standard homepage. Defines the skill format as a folder containing a `SKILL.md` file, describes the three-stage progressive disclosure loading model, and emphasizes cross-product reuse as a core benefit.

## Key Points

- **Format**: A skill is a folder with a required `SKILL.md` (minimum: `name` and `description` metadata + instructions) and optional bundled scripts, references, templates, and resources.
- **Three-stage loading**: (1) Discovery — agents load only name/description at startup. (2) Activation — when a task matches, the agent reads full `SKILL.md`. (3) Execution — agent follows instructions, optionally executing bundled code or loading referenced files.
- **Cross-product reuse**: "Build a skill once and use it across any skills-compatible agent." This is the core value proposition of the open standard.
- **Domain expertise, repeatable workflows, cross-product reuse** are the three main problems skills solve.
- The standard was originally developed by Anthropic, released as an open standard, and adopted by a growing number of agent products. Open to ecosystem contributions.

## Connections

- [[concepts/Agent Skills]] — The open standard definition of what the wiki's concept page describes.
- [[concepts/Progressive Disclosure]] — This source provides the concise three-stage naming: Discovery, Activation, Execution.
- [[concepts/Skill Distribution and Installation]] — Cross-product reuse is the central promise of the open standard.
- [[concepts/Tools Supporting Agent Skills]] — The Client Showcase at agentskills.io/clients lists compatible tools.
