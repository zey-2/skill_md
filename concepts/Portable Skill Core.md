---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md"
tags: [agent-skills, metadata, portability]
---

# Portable Skill Core

## Summary

The portable skill core is the small part of a skill package that most agent platforms can understand. According to the raw sources, that core is mainly `name` and `description`, plus concise instructions in `SKILL.md`.

In plain language: if you want a skill to travel across platforms, do not assume every runtime understands your custom fields. Put the essential routing information up front, and treat everything else as optional or platform-specific.

Sources: `raw/skill.md for AI Agents.md` and `raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md`.

## Key Ideas and Evidence

The original synthesis says the cross-vendor portable core is small. It says the only universally recurring required fields are `name` and `description`, and routing often depends mostly on those two fields.

The same synthesis recommends adding more structure for practical operation, such as:

- `when_to_use`
- `when_not_to_use`
- `inputs`
- `outputs`
- `steps`
- `decision_rules`
- `constraints`
- `failure_modes`
- `examples`
- `test_prompts`

However, those fields are presented as a recommended repository schema, not as a fully standardized public requirement.

One curated ecosystem source adds a practical quality rule: the description should say what the skill does and when to use it, in concrete language with specific keywords that an agent can match on. That strengthens the earlier point that vague metadata hurts routing quality.

## Where Sources Agree

The sources agree that metadata matters because it helps the agent decide whether a skill applies. They also agree that vague descriptions hurt routing quality.

They further agree that the main file should be short enough to be useful in context. A portable core should therefore be precise, compact, and written around real tasks.

## Where Sources Disagree

The disagreement is about how much metadata belongs in the canonical skill file. Some ecosystems encourage extra metadata for UI display, internal status, or repository management. Others focus on the minimal executable package.

There is also some uncertainty about whether operational hints such as tool dependencies should be treated as part of the portable core or as platform-specific extensions. The curated quality guidance argues for explicit, scoped tool declarations, but it does not by itself prove that every platform supports the same mechanism.

The safest synthesis is still the earlier one: keep the portable core clean, and place richer lifecycle or vendor-specific metadata in indexes or adapters.

## Connections

- [[Vendor Adapters]] covers platform-specific metadata.
- [[SKILL.md Package Anatomy]] covers where metadata lives.
- [[Validation and Evaluation]] covers how to test metadata quality.
- [[Skill Repository Architecture]] covers repository-level indexes.

## Open Questions

- Will fields like `when_to_use` and `when_not_to_use` become standard, or remain best-practice additions?
- How much metadata can be added before a portable skill becomes vendor-specific?
