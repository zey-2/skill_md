---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://docs.claude.com/en/docs/claude-code/skills"
  - "https://code.claude.com/docs/en/skills"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, claude-code, anthropic]
---

# Claude Code Agent Skills docs

## Source Identity

Anthropic's Claude Code skills documentation describes how to create, use, and manage Agent Skills in Claude Code.

## Relevant Extracted Facts

- Claude Code skills are directories with a `SKILL.md` file plus optional supporting files such as scripts, templates, examples, and references.
- Personal skills live under `~/.claude/skills/`.
- Project skills live under `.claude/skills/`.
- Plugin skills can be bundled with Claude Code plugins.
- `SKILL.md` uses YAML frontmatter and Markdown content.
- `description` is critical because Claude decides when to use a skill based on the request and the skill description.
- Claude Code supports both model-invoked skill use and slash-command invocation in newer docs.
- Newer Claude Code docs describe skill scopes including enterprise, personal, project, and plugin skills.
- Skill locations have priority rules, with enterprise and personal/project levels handled separately from plugin namespaces.
- Claude Code can detect live changes in watched skill directories during a session, except when a top-level skills directory did not exist at session start.
- Claude Code can discover nested `.claude/skills/` directories when working in subdirectories, which helps monorepos.
- `allowed-tools` is a Claude Code-specific frontmatter field for restricting tools when a skill is active.
- Legacy `.claude/commands/` files continue working, but skills are recommended because they support supporting files.

## Tool Support Evidence

This is primary evidence that Claude Code supports Agent Skills using `.claude/skills/`, plugin skills, slash-style invocation, and model-chosen activation.

## Open Questions

- Claude.ai account-level Skills are related but not identical to local Claude Code Agent Skills; this source is primarily about Claude Code.
