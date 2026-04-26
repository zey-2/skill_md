---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://opencode.ai/docs/skills"
  - "https://open-code.ai/en/docs/skills"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, opencode]
---

# OpenCode Agent Skills docs

## Source Identity

OpenCode documentation describes Agent Skills as reusable `SKILL.md` definitions loaded by OpenCode.

## Relevant Extracted Facts

- OpenCode Agent Skills define reusable behavior via `SKILL.md` definitions.
- Skills let OpenCode discover reusable instructions from a repository or home directory.
- Skills are loaded on demand through OpenCode's native `skill` tool.
- OpenCode agents see available skills and can load full content when needed.
- Each skill is one folder per skill name with a `SKILL.md` inside it.
- OpenCode searches project config at `.opencode/skills/<name>/SKILL.md`.
- OpenCode searches global config at `~/.config/opencode/skills/<name>/SKILL.md`.
- OpenCode also searches Claude-compatible paths `.claude/skills/<name>/SKILL.md` and `~/.claude/skills/<name>/SKILL.md`.
- OpenCode also searches agent-compatible paths `.agents/skills/<name>/SKILL.md` and `~/.agents/skills/<name>/SKILL.md`.
- For project-local paths, OpenCode walks up from the current working directory to the git worktree root.
- Recognized frontmatter fields include required `name` and `description`, plus optional `license`, `compatibility`, and `metadata`.
- Unknown frontmatter fields are ignored.
- The skill `name` must match the directory name and follow a lowercase hyphenated naming pattern.

## Tool Support Evidence

This is primary evidence that OpenCode supports Agent Skills, including its own `.opencode/skills/` paths plus compatibility paths for `.claude/skills/` and `.agents/skills/`.

## Open Questions

- The docs emphasize reusable instructions rather than external tools; tool permissions are a separate configuration concern.
