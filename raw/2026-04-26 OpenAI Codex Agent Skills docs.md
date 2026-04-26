---
type: raw-source
created: 2026-04-26
source_type: web
source_url: "https://developers.openai.com/codex/skills"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, codex, openai]
---

# OpenAI Codex Agent Skills docs

## Source Identity

OpenAI's Codex documentation page, "Agent Skills", describes skills for Codex.

## Relevant Extracted Facts

- Codex skills extend Codex with task-specific capabilities.
- The docs say skills build on the open Agent Skills standard.
- Skills are available in the Codex CLI, IDE extension, and Codex app.
- Codex uses progressive disclosure: it starts with each skill's name, description, and file path, then loads the full `SKILL.md` only when it decides to use a skill.
- A skill is a directory with required `SKILL.md` plus optional `scripts/`, `references/`, `assets/`, and `agents/openai.yaml`.
- `SKILL.md` must include `name` and `description`.
- Codex supports explicit invocation through `/skills` or `$skill` mention and implicit invocation based on the description.
- Codex reads repository skills from `.agents/skills` along the path from current working directory up to the repository root.
- Codex also reads user skills from `$HOME/.agents/skills`, admin skills from `/etc/codex/skills`, and OpenAI-bundled system skills.
- Plugins are the recommended reusable distribution unit when skills should be shared beyond local folders or bundled with integrations.
- `$skill-installer` installs curated skills for local Codex setup.
- Optional `agents/openai.yaml` can configure Codex app UI metadata, invocation policy, and tool dependencies.

## Tool Support Evidence

This is primary evidence that OpenAI Codex supports Agent Skills across CLI, IDE extension, and app surfaces.

## Open Questions

- The docs describe Codex's own paths and plugin approach; other tools may not use the same discovery locations or adapter file.
