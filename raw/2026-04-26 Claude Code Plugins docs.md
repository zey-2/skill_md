---
type: source-summary
created: 2026-04-26
updated: 2026-04-26
status: active
source_type: web
source_url:
  - "https://code.claude.com/docs/en/plugins"
  - "https://code.claude.com/docs/en/discover-plugins"
  - "https://code.claude.com/docs/en/plugin-marketplaces"
  - "https://code.claude.com/docs/en/plugins-reference"
accessed: 2026-04-26
tags: [claude-code, plugins, agent-skills, mcp]
---

# Claude Code Plugins Docs

## Source Identity

Anthropic's Claude Code plugin documentation describes plugins as self-contained extension directories for Claude Code and marketplaces as catalogs for distributing those plugins.

## Relevant Extracted Facts

- Claude Code plugins can extend Claude Code with skills, agents, hooks, MCP servers, LSP servers, monitors, themes, and related configuration.
- Standalone `.claude/` configuration is recommended for personal workflows, project-specific customizations, and quick experiments.
- Plugins are recommended for sharing with teammates or the community, reusing the same components across projects, versioned releases, marketplace distribution, and avoiding name conflicts through plugin namespaces.
- Claude Code plugin directories use `.claude-plugin/plugin.json` for plugin identity, metadata, and component paths.
- Plugin skills live under `skills/` or `commands/`; skills in `skills/` are directories with `SKILL.md` and optional supporting files.
- Plugin skills and commands are automatically discovered when the plugin is installed, and Claude can invoke skills automatically based on task context.
- Plugins can bundle specialized subagents, hooks, MCP servers, LSP servers, monitors, and themes.
- Plugin MCP servers can live in `.mcp.json` or inline in `plugin.json`; they start when the plugin is enabled and appear as standard MCP tools.
- Plugin installation scopes include user, project, local, and managed. Project-scoped plugins can be shared through version control; managed plugins are read-only.
- Plugin marketplaces provide centralized discovery, version tracking, automatic updates, and support for multiple source types such as Git repositories and local paths.
- Claude Code marketplaces are added first; users then install individual plugins from the catalog.
- Claude Code copies marketplace-installed plugins into a local cache for security and verification. Installed plugins cannot reference files outside their directory through path traversal after installation.
- Plugins can use a persistent data directory for dependency caches and generated state that should survive plugin updates.

## Relevance to Agent Skills

Claude Code plugins show that skills can be only one component in a larger extension bundle. A plugin can distribute the instructions, agents, hooks, MCP servers, dependency state, and marketplace metadata needed to make a capability practical across projects and teams.

## Follow-Ups

- Add a cross-vendor plugin manifest comparison if plugin authoring becomes a recurring task.
- Track how Claude Code managed plugin settings and official marketplace submission evolve.
