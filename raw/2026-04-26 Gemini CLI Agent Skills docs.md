---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://geminicli.com/docs/cli/skills/"
  - "https://geminicli.com/docs/cli/creating-skills/"
  - "https://geminicli.com/docs/cli/cli-reference/"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, gemini-cli, google]
---

# Gemini CLI Agent Skills docs

## Source Identity

Gemini CLI documentation describes Agent Skills support, creation, discovery, and command-line management.

## Relevant Extracted Facts

- Gemini CLI Agent Skills extend the CLI with specialized expertise, workflows, and task-specific resources.
- The docs explicitly say Gemini CLI skills are based on the Agent Skills open standard.
- Gemini decides when to use a skill based on the user request and the skill's description.
- Gemini CLI activates a skill with an `activate_skill` tool.
- Discovery tiers include workspace skills, user skills, and extension skills.
- Workspace skills live in `.gemini/skills/` or the `.agents/skills/` alias.
- User skills live in `~/.gemini/skills/` or the `~/.agents/skills/` alias.
- Extension skills are bundled within installed extensions.
- Precedence is workspace over user over extension.
- Within a user or workspace tier, `.agents/skills/` takes precedence over `.gemini/skills/`.
- The interactive `/skills` command can list, link, enable, disable, and reload skills.
- The terminal `gemini skills` command can list, install, link, uninstall, enable, and disable skills.
- Skill installation can use a Git repository, local directory, or zipped `.skill` file.
- The creation guide recommends a built-in `skill-creator` skill and the standard folders `scripts/`, `references/`, and `assets/`.
- `SKILL.md` requires `name` and `description`; the body contains the active instructions.

## Tool Support Evidence

This is primary evidence that Gemini CLI supports Agent Skills, including `.gemini/skills/`, `.agents/skills/`, an activation tool, and CLI management commands.

## Open Questions

- Gemini CLI's `.agents/skills/` alias suggests deliberate cross-agent compatibility, but exact behavior may differ from other clients.
