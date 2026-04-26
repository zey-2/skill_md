---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://agentskills.io/home"
  - "https://agentskills.io/skill-creation/quickstart"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, standard, vscode, github-copilot]
---

# agentskills.io Agent Skills overview and quickstart

## Source Identity

The Agent Skills site presents Agent Skills as an open format for giving agents reusable capabilities and expertise. The quickstart uses VS Code with GitHub Copilot as the tutorial environment.

## Relevant Extracted Facts

- A skill is a folder containing a required `SKILL.md` file.
- The minimum metadata is `name` and `description`; these are used for discovery and activation.
- Supporting folders can include `scripts/`, `references/`, and `assets/`.
- The site describes progressive disclosure in three stages: discovery of name/description, activation by loading the full `SKILL.md`, and execution with optional resources or scripts.
- The overview states that skills can be reused across skills-compatible agents.
- The quickstart says VS Code looks for skills in `.agents/skills/` by default.
- The quickstart says the same skill works in compatible agents including Claude Code and OpenAI Codex.
- The quickstart tests the skill in VS Code by opening Copilot Chat in Agent mode and using `/skills` to confirm that the skill is discovered.

## Tool Support Evidence

The quickstart is direct evidence that VS Code with GitHub Copilot supports Agent Skills. The overview is general evidence that the standard is intended for multiple agent clients.

## Open Questions

- The client showcase page states that supporting products exist, but the text extraction did not expose a concrete client list.
