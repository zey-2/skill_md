---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/skill.md for AI Agents.md"
tags: [agent-skills, adapters, portability]
---

# Vendor Adapters

## Summary

Vendor adapters are platform-specific files or metadata generated from a canonical skill package. They let one skill support different agent platforms without mixing every platform's special fields into the main `SKILL.md`.

The raw source recommends a "portable skill core plus vendor adapters" model. In plain language: write the skill once, keep the shared part clean, then generate or maintain extra files for OpenAI, Anthropic, GitHub, Mintlify, or future clients as needed.

Source: `raw/skill.md for AI Agents.md`, sections "Executive summary" and "Recommended repository model and schema".

## Key Ideas and Evidence

The source presents OpenAI's optional `agents/openai.yaml` as an example of adapter metadata. It also notes that Mintlify uses a lighter metadata model and that the wider ecosystem has not fully converged beyond the portable core.

The recommended repository model has three layers:

- canonical package layer
- repository index layer
- vendor adapter layer

This keeps authoring ergonomic while allowing platform-specific export.

## Where Sources Agree

The sources agree that skills need a shared operational center: a main file with clear metadata and instructions. They also agree that different platforms expose different user experiences around skills.

That shared agreement supports the adapter pattern. If the core package is stable, adapters can change without rewriting the skill itself.

## Where Sources Disagree

The disagreement is over which fields belong in the core. OpenAI-specific display fields, Mintlify internal metadata, and repository ownership metadata may all be useful, but they serve different audiences.

The source's explanation is that these differences come from platform goals. Some metadata supports agent routing, some supports human browsing, some supports UI display, and some supports governance. Mixing them all together can make the canonical package less portable.

## Connections

- [[Portable Skill Core]] defines what should stay shared.
- [[SKILL.md Package Anatomy]] explains the package structure adapters extend.
- [[Skill Repository Architecture]] explains how adapters fit into a repository.
- [[Provenance and Versioning]] explains how generated adapters can stay traceable.

## Open Questions

- Should adapters be checked into the repository or generated during release?
- How should tools warn maintainers when an adapter drifts from the canonical package?
