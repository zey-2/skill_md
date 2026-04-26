---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://docs.github.com/en/copilot/concepts/agents/about-agent-skills"
  - "https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/add-skills"
  - "https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-skills"
  - "https://code.visualstudio.com/docs/copilot/customization/agent-skills"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, github-copilot, vscode]
---

# GitHub Copilot and VS Code Agent Skills docs

## Source Identity

GitHub Docs and VS Code documentation describe Agent Skills support in Copilot cloud agent, GitHub Copilot CLI, and GitHub Copilot in VS Code.

## Relevant Extracted Facts

- GitHub Docs says Agent Skills work with Copilot cloud agent, GitHub Copilot CLI, and agent mode in Visual Studio Code.
- GitHub Docs describes skills as folders of instructions, scripts, and resources that Copilot can load when relevant.
- GitHub Docs says the Agent Skills specification is an open standard used by different AI systems.
- Copilot project skills can live in `.github/skills`, `.claude/skills`, or `.agents/skills`.
- Copilot personal skills can live in `~/.copilot/skills`, `~/.claude/skills`, or `~/.agents/skills`.
- GitHub Docs says organization-level and enterprise-level skills are planned but not yet available.
- When Copilot uses a skill, `SKILL.md` is injected into the agent context.
- VS Code documentation says Agent Skills work across GitHub Copilot in VS Code, GitHub Copilot CLI, and GitHub Copilot coding agent.
- VS Code supports project skills from `.github/skills/`, `.claude/skills/`, and `.agents/skills/`.
- VS Code supports personal skills from `~/.copilot/skills/`, `~/.claude/skills/`, and `~/.agents/skills/`.
- VS Code can use `chat.agentSkillsLocations` to configure additional skill search paths.
- VS Code supports skills as slash commands.
- VS Code recognizes required `name` and `description` fields and optional fields such as `argument-hint`, `user-invocable`, and `disable-model-invocation`.
- VS Code extensions can contribute skills through the `chatSkills` contribution point.

## Tool Support Evidence

This is primary evidence that GitHub Copilot and VS Code support Agent Skills across local editor, CLI, and cloud coding-agent contexts.

## Open Questions

- Organization and enterprise skill distribution for Copilot is described as coming later, so current wiki claims should not treat it as available.
