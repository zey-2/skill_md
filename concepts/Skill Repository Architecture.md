---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/skill.md for AI Agents.md"
tags: [agent-skills, repositories, architecture]
---

# Skill Repository Architecture

## Summary

A skill repository is a maintained collection of agent skill packages. It should not be just a pile of Markdown files. The raw source recommends treating each skill as a package with instructions, resources, adapters, provenance, validation results, and release metadata.

Source: `raw/skill.md for AI Agents.md`, section "Recommended repository model and schema".

## Key Ideas and Evidence

The source recommends a three-layer repository:

- canonical package layer: one directory per skill, with `SKILL.md` and resources
- repository index layer: YAML or JSON entries for search, ownership, release, and validation metadata
- vendor adapter layer: generated files such as `agents/openai.yaml` or internal manifests

This structure supports both humans and machines. Humans can browse the repository, review changes, and understand ownership. Machines can validate fields, build indexes, generate adapters, and search for relevant skills.

## Where Sources Agree

The sources agree that a skill is more than a single prose page. OpenAI, Anthropic, and GitHub Copilot are summarized as supporting optional supplementary files. Repository practice is summarized as adding indexes, generation metadata, and source SHAs.

They also agree that the main skill file should remain connected to its resources. A repository architecture should make those connections visible and checkable.

## Where Sources Disagree

The sources do not fully agree on where every piece of metadata belongs. Some metadata can live in front matter, some in a separate repository index, and some in vendor adapter files.

The raw source recommends using front matter for human-editable package metadata and JSON or JSON Schema for stronger machine validation. That is an inference from current formats, not a universal requirement.

## Connections

- [[SKILL.md Package Anatomy]] covers individual package structure.
- [[Portable Skill Core]] covers the minimum shared metadata.
- [[Vendor Adapters]] covers platform-specific exports.
- [[Provenance and Versioning]] covers release metadata and source tracking.
- [[Validation and Evaluation]] covers repository checks.

## Open Questions

- At what repository size does a separate machine-readable index become necessary?
- Should indexes be handwritten, generated, or both?
