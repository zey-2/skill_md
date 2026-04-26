---
type: raw-source
created: 2026-04-26
source_type: web
source_url: "https://docs.windsurf.com/windsurf/cascade/skills"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, windsurf, cascade]
---

# Windsurf Cascade Skills docs

## Source Identity

Windsurf documentation describes Cascade Skills for bundling instructions and supporting files.

## Relevant Extracted Facts

- Cascade Skills help Cascade handle complex, multi-step tasks.
- Skills bundle scripts, templates, checklists, and other supporting files into folders Cascade can invoke.
- Windsurf docs say Cascade uses progressive disclosure: name and description are shown by default, while full `SKILL.md` content and supporting files load when invoked.
- The docs point to agentskills.io for the Skills specification.
- Workspace skills are manually created under `.windsurf/skills/<skill-name>/`.
- Global skills are manually created under `~/.codeium/windsurf/skills/<skill-name>/`.
- Each skill requires a `SKILL.md` file with YAML frontmatter.
- Required frontmatter fields are `name` and `description`.
- Skills can be automatically invoked when a request matches the description.
- Skills can also be manually invoked by typing `@skill-name`.
- Workspace scope uses `.windsurf/skills/`; global scope uses `~/.codeium/windsurf/skills/`.
- Enterprise system-level skills can be deployed under OS-specific paths such as `/Library/Application Support/Windsurf/skills/`, `/etc/windsurf/skills/`, and `C:\ProgramData\Windsurf\skills\`.
- For cross-agent compatibility, Windsurf also discovers `.agents/skills/` and `~/.agents/skills/`.
- If Claude Code config reading is enabled, Windsurf scans `.claude/skills/` and `~/.claude/skills/`.

## Tool Support Evidence

This is primary evidence that Windsurf Cascade supports `SKILL.md`-based skills with workspace, global, enterprise, and compatibility discovery paths.

## Open Questions

- The docs mention Claude compatibility only when Claude Code config reading is enabled, so that path should be treated as conditional.
