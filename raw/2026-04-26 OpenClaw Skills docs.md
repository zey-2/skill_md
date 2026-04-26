---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://docs.openclaw.ai/tools/skills"
  - "https://github.com/openclaw/openclaw/blob/main/docs/tools/skills.md"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, openclaw]
---

# OpenClaw Skills docs

## Source Identity

OpenClaw documentation describes its skills system and AgentSkills-compatible folders.

## Relevant Extracted Facts

- OpenClaw uses AgentSkills-compatible skill folders to teach the agent how to use tools.
- Each skill is a directory containing `SKILL.md` with YAML frontmatter and instructions.
- OpenClaw loads bundled skills plus optional local overrides.
- OpenClaw can filter skills at load time based on environment, config, and binary presence.
- Current documentation lists sources including extra skill folders, bundled skills, managed/local skills, personal agent skills, project agent skills, and workspace skills.
- Extra skill folders are configured with `skills.load.extraDirs`.
- Managed/local skills use `~/.openclaw/skills`.
- Personal agent skills use `~/.agents/skills`.
- Project agent skills use `<workspace>/.agents/skills`.
- Workspace skills use `<workspace>/skills`.
- Precedence is `<workspace>/skills` over `<workspace>/.agents/skills`, then `~/.agents/skills`, then `~/.openclaw/skills`, then bundled skills, then extra dirs.
- OpenClaw watches skill folders by default and refreshes when `SKILL.md` files change.
- The docs discuss token impact for injecting a compact list of available skills.

## Tool Support Evidence

This is primary evidence that OpenClaw supports AgentSkills-compatible `SKILL.md` folders and multiple local discovery locations.

## Open Questions

- Marketplace claims and third-party security commentary should be cited separately from official OpenClaw docs.
