---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/openaiskills Skills Catalog for Codex.md"
  - "raw/anthropicsskills Public repository for Agent Skills.md"
  - "raw/obrasuperpowers An agentic skills framework & software development methodology that works.md"
  - "raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md"
  - "raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md"
  - "raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md"
  - "raw/2026-04-26 OpenAI Codex Agent Skills docs.md"
  - "raw/2026-04-26 Claude Code Agent Skills docs.md"
  - "raw/2026-04-26 Gemini CLI Agent Skills docs.md"
  - "raw/2026-04-26 GitHub Copilot and VS Code Agent Skills docs.md"
  - "raw/2026-04-26 OpenCode Agent Skills docs.md"
  - "raw/2026-04-26 OpenClaw Skills docs.md"
  - "raw/2026-04-26 Windsurf Cascade Skills docs.md"
  - "raw/2026-04-26 Microsoft Agent Framework Agent Skills docs.md"
  - "raw/2026-04-26 OpenAI Codex Plugins docs.md"
  - "raw/2026-04-26 Claude Code Plugins docs.md"
tags: [agent-skills, distribution, installation]
---

# Skill Distribution and Installation

## Summary

Skill distribution and installation describe how a skill reaches an agent runtime and where it lives after that. The current ecosystem shows several patterns: built-in system skills, curated catalogs, plugin marketplaces, command-line installers, project-local folders, global folders, project-level instruction files, and full plugin bundles.

In plain language: writing a good skill is only half the story. The other half is making it discoverable and installable in the tool people actually use.

Sources: `raw/openaiskills Skills Catalog for Codex.md`, `raw/anthropicsskills Public repository for Agent Skills.md`, `raw/obrasuperpowers An agentic skills framework & software development methodology that works.md`, `raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md`, `raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md`, and `raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md`.

## Key Ideas and Evidence

The raw sources show several distinct installation models:

- OpenAI's catalog says some skills are automatically installed as `.system` skills, while `.curated` and `.experimental` skills are installed through `$skill-installer`, after which Codex should be restarted.
- OpenAI's current Codex docs distinguish local authoring folders from reusable distribution via plugins, and still describe `$skill-installer` for curated local setup.
- OpenAI's Codex plugin docs describe plugins as bundles of skills, app integrations, and MCP servers; repo and personal marketplaces can expose curated plugin lists.
- Anthropic's public skills repository can be added as a plugin marketplace and then installed as plugin packages.
- Claude Code supports personal, project, plugin, and enterprise skill scopes.
- Claude Code's plugin docs distinguish standalone `.claude/` configuration from plugins: standalone configuration suits personal or project-specific experimentation, while plugins suit sharing, versioning, marketplace distribution, and reuse across projects.
- GitHub Copilot and VS Code support repository/project skills, personal skills, and extension-contributed skills; GitHub organization and enterprise skills are described as future work.
- Gemini CLI includes interactive `/skills` management and terminal commands such as `gemini skills install`, `link`, `uninstall`, `enable`, and `disable`.
- OpenCode emphasizes local project/global discovery plus compatibility paths rather than a marketplace in the captured docs.
- OpenClaw includes bundled skills, managed/local skills, workspace skills, compatibility paths, and configured extra directories.
- Windsurf supports workspace, global, enterprise, and cross-agent compatibility discovery paths.
- Microsoft Agent Framework consumes skills through a provider configured with one or more skill directories, rather than through an end-user client install flow.
- Superpowers advertises installation across Claude Code, Codex, Cursor, OpenCode, GitHub Copilot CLI, and Gemini CLI, which suggests that one conceptual skill system can still require many platform-specific install flows.
- Matt Pocock's repository uses a package-manager style command, `npx skills@latest add ...`, to install individual skills.
- VoltAgent's curated list documents per-tool local paths such as `.agents/skills/`, `.claude/skills/`, and `.cursor/skills/`.
- The Forrest Chang source shows an adjacent pattern: behavior guidance can also be distributed as a project-level `CLAUDE.md`, either created fresh or appended to an existing file.

Together, these sources show that "portable skill" does not yet mean "portable installation."

## Where Sources Agree

The sources agree that installation is a separate concern from authoring. A well-structured `SKILL.md` package still needs a delivery path.

They also agree that scope matters. Some installs are global. Some are project-local. Some are bundled by the platform. Some are merged into project instructions instead of being installed as standalone skills.

## Where Sources Disagree

The sources disagree on the delivery surface. Some ecosystems emphasize plugin marketplaces. Others emphasize direct folder placement. Others emphasize helper installers or package-manager style commands. The `CLAUDE.md` example again sits nearby but does not fully match the package-based model.

Plugin distribution also changes the unit of review. A standalone skill can usually be reviewed as instructions plus optional support files. A plugin may need review as a package: manifest, publisher metadata, bundled skills, app connectors, MCP server configuration, hooks, scripts, assets, authentication timing, and update source.

There is also no sign yet of a single universal registry or signing system across the raw sources. That is an inference from what is missing as much as from what is present.

## Connections

- [[Discovery Conventions]] explains the file names and local directories tools use to find installed skills.
- [[Skill Repository Tooling]] explains the broader tooling stack around catalogs and installers.
- [[Plugin-Based Agent Extensions]] explains why plugin packages matter when skills need connectors, MCP servers, metadata, and marketplace distribution.
- [[Skill Governance and Metrics]] explains why public distribution raises trust and review concerns.
- [[Agent Skills]] explains why installation differences do not erase the shared underlying concept.
- [[concepts/Claude Code Architecture Deep Dive]] explains the 4-level CLAUDE.md hierarchy and how skills sit in the graduated extensibility spectrum (Hooks → Skills → Plugins → MCP).

## Open Questions

- Will a common cross-platform registry emerge for skills, or will each agent ecosystem keep its own marketplace and installer flow?
- How should users decide between project-local skills, global skills, and project-level instruction files?
