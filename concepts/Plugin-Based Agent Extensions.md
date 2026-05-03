---
type: concept
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/2026-04-26 OpenAI Codex Plugins docs.md"
  - "raw/2026-04-26 Claude Code Plugins docs.md"
  - "raw/2026-04-26 OpenAI Codex Agent Skills docs.md"
  - "raw/2026-04-26 Claude Code Agent Skills docs.md"
  - "raw/anthropicsskills Public repository for Agent Skills.md"
  - "raw/2026-04-26 MCP architecture and Agent Skills integration source.md"
  - "raw/2026-04-26 Claude Agent SDK source.md"
tags: [plugins, agent-skills, mcp, distribution]
---

# Plugin-Based Agent Extensions

## Summary

Plugins are installable extension bundles for agent clients. Around Agent Skills, their significance is that they package more than instructions: they can distribute skills together with app integrations, MCP server configuration, subagents, hooks, assets, marketplace metadata, install policy, and update behavior.

In plain language: a skill teaches the agent how to do a task; a plugin ships a reusable capability to users and teams.

Sources: `raw/2026-04-26 OpenAI Codex Plugins docs.md`, `raw/2026-04-26 Claude Code Plugins docs.md`, `raw/2026-04-26 OpenAI Codex Agent Skills docs.md`, `raw/2026-04-26 Claude Code Agent Skills docs.md`, and `raw/anthropicsskills Public repository for Agent Skills.md`.

## Why Plugins Matter

Plugins fill the gap between "I wrote a useful skill" and "other people can reliably install, update, trust, and use this capability."

The current sources show four reasons plugins matter:

- Distribution: plugins can be listed in marketplaces or curated local catalogs instead of copied by hand into skill folders.
- Composition: plugins can bundle the skill instructions with the tools, connectors, MCP servers, subagents, hooks, and assets the workflow expects.
- Namespacing: plugin-owned components can avoid name collisions when multiple packages expose similar skills.
- Governance: plugin manifests and marketplaces create surfaces for versioning, publisher metadata, installation policy, authentication timing, and review.

This makes plugins especially important for capabilities that cross the boundary from local guidance into external systems. A "summarize Gmail threads" workflow is not just a skill prompt; it also needs an app connector, authentication, permissions, and a visible install surface. A database assistant may need a skill plus MCP server configuration and approval boundaries.

## Plugin Components

The Codex and Claude Code sources differ in exact file names and component lists, but they agree on the pattern: a plugin is a directory with metadata plus optional components.

| Layer | What It Carries | Example Evidence |
| --- | --- | --- |
| Manifest | Identity, version, description, publisher metadata, component paths, interface metadata. | Codex uses `.codex-plugin/plugin.json`; Claude Code uses `.claude-plugin/plugin.json`. |
| Skills | `SKILL.md`-based instructions and optional supporting files. | Codex plugin manifests can point to `./skills/`; Claude Code plugins discover skills under `skills/`. |
| Tool and app access | App integrations, MCP server configuration, or other external capability surfaces. | Codex plugins can include `.app.json` and `.mcp.json`; Claude Code plugins can bundle MCP servers in `.mcp.json` or `plugin.json`. |
| Runtime helpers | Subagents, hooks, LSP servers, monitors, scripts, or dependency caches. | Claude Code plugin docs list agents, hooks, LSP servers, monitors, themes, persistent data, and MCP servers. |
| Marketplace metadata | Catalog entries, install policy, categories, display names, and update sources. | Codex uses `.agents/plugins/marketplace.json`; Claude Code marketplaces use `marketplace.json`. |

## Local Skills, Plugins, and Marketplaces

| Surface | Best For | Tradeoff |
| --- | --- | --- |
| Local skill folder | One repo, one user, quick iteration, narrow workflow. | Easy to edit, but weaker for sharing, versioning, bundled integrations, and review. |
| Plugin | Reusable capability shared across projects, teams, or communities. | More structure to maintain, but can ship skills with required integrations and metadata. |
| Marketplace or curated plugin list | Discovery, installation, update tracking, team rollout, and policy. | Adds catalog governance and trust questions. |

Codex docs explicitly advise starting with a local skill when iterating on one repo or personal workflow, then building a plugin when sharing across teams, bundling app integrations or MCP configuration, or publishing a stable package. Claude Code docs make a similar distinction between standalone `.claude/` configuration and plugins.

## Relationship to MCP

MCP and plugins solve different problems. MCP exposes tools, resources, and prompts through a protocol. Plugins distribute a bundle of agent-facing components. A plugin can include MCP server configuration, but it is not itself the same thing as an MCP server.

A useful boundary:

- Put procedure and judgment in [[Agent Skills]].
- Put executable external actions and shared context behind MCP servers or tools.
- Use plugins when the skill and the tool surface need to be installed, versioned, and presented together.

This is why plugin significance grows as a workflow becomes more operational. A skill can explain how to use a CRM safely; an MCP server can expose CRM actions; a plugin can package the skill, MCP configuration, marketplace metadata, icon, default prompts, and authentication expectations.

## Security and Governance

Plugins widen the review surface. A standalone skill mostly changes instructions and maybe local scripts. A plugin can also introduce app connections, MCP servers, hooks, persistent dependency state, subagents, or language servers.

The sources therefore support treating plugins as supply-chain artifacts:

- Review the manifest, component paths, bundled skills, scripts, MCP configuration, and hooks.
- Keep path references inside the plugin root where the platform expects that boundary.
- Record publisher metadata, version, source URL, license, and update path.
- Make authentication timing and approval boundaries visible.
- Prefer marketplace entries or managed settings for team rollout when consistency matters.

This does not mean plugins are unsafe by default. It means their value and risk come from the same feature: they package a whole working capability, not just one instruction file.

## Connections

- [[Agent Skills]] explains the reusable instruction layer that plugins often package.
- [[Skill Distribution and Installation]] explains the broader installation landscape.
- [[concepts/Discovery Conventions]] explains how plugins fit into the discovery hierarchy alongside SKILL.md files and skill repositories.
- [[concepts/Skill Repository Architecture]] provides the organizational patterns that plugin marketplaces and catalogs build on top of.
- [[MCP and Tool-Integration Architecture]] explains the tool/context layer that plugins can bundle or configure.
- [[Tools Supporting Agent Skills]] compares current client support.
- [[Skill Governance and Metrics]] covers trust, review, and quality practices for shared agent artifacts.
- [[Agent SDKs and Codex Automation]] explains why packaged capabilities matter more when agents are embedded in repeatable workflows.
- [[concepts/Replacing Code with Skills]] — Cursor's worktree feature shows that some "plugin-like" functionality can be replaced entirely by skills/commands, reducing the boundary between plugins and prompt packages.
- [[concepts/Claude Code Architecture Deep Dive]] shows at source level how plugins fit into Claude Code's extensibility spectrum, accepting 10 component types in the plugin manifest and sitting between skills and MCP in context cost.

## Open Questions

- Will Codex and Claude Code plugin manifests converge, or remain vendor-specific distribution wrappers around similar components?
- Should portable Agent Skills define a standard way to declare plugin dependencies, MCP server requirements, and app permissions?
- How should teams evaluate a plugin as a whole, rather than evaluating only its bundled skills?
- Will public plugin directories develop signing, provenance, or audit norms comparable to package registries?
