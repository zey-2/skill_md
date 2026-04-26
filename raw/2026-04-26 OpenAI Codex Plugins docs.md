---
type: source-summary
created: 2026-04-26
updated: 2026-04-26
status: active
source_type: web
source_url:
  - "https://developers.openai.com/codex/plugins"
  - "https://developers.openai.com/codex/plugins/build"
accessed: 2026-04-26
tags: [codex, plugins, agent-skills, mcp]
---

# OpenAI Codex Plugins Docs

## Source Identity

OpenAI's Codex plugin documentation describes plugins as reusable extension bundles for Codex. The docs distinguish everyday plugin use from plugin authoring and local marketplace setup.

## Relevant Extracted Facts

- Codex plugins bundle reusable workflows with skills, app integrations, and MCP servers.
- A plugin can contain Agent Skills, app connections such as GitHub, Slack, Gmail, Google Drive, or other connectors, MCP server configuration, and presentation assets.
- Codex can use an installed plugin implicitly from a task description, or the user can invoke a plugin or bundled skill explicitly with `@`.
- Installing a plugin makes its workflows available, but Codex approval settings still apply.
- Apps bundled through a plugin may require separate sign-in and remain subject to the connected app's own terms and privacy policy.
- MCP servers bundled through a plugin may require setup or authentication before use.
- Plugin authors are advised to start with a local skill for one repo or one personal workflow, then build a plugin when sharing across teams, bundling app integrations or MCP config, or publishing a stable package.
- Codex provides a `$plugin-creator` skill that scaffolds `.codex-plugin/plugin.json` and can generate a local marketplace entry for testing.
- A Codex marketplace is a JSON catalog of plugins. A repo-scoped marketplace can live at `$REPO_ROOT/.agents/plugins/marketplace.json`; a personal marketplace can live at `~/.agents/plugins/marketplace.json`.
- A minimal Codex plugin has `.codex-plugin/plugin.json` with fields such as `name`, `version`, `description`, and `skills`.
- A published plugin manifest can also include `author`, `homepage`, `repository`, `license`, `keywords`, `skills`, `mcpServers`, `apps`, and an `interface` object for install-surface metadata.
- Plugin paths should stay relative to the plugin root and start with `./`. `skills`, `apps`, and `mcpServers` point to bundled component locations.
- OpenAI says official public plugin directory publishing and self-serve plugin management are coming soon.

## Relevance to Agent Skills

Codex plugins are a higher-level packaging and distribution layer around skills. A local skill is enough for a narrow workflow. A plugin becomes important when the same workflow needs versioning, marketplace discovery, app connectors, MCP server configuration, presentation metadata, or broader team/community reuse.

## Follow-Ups

- Track the official Codex Plugin Directory when public publishing becomes available.
- Compare Codex plugin manifests with Claude Code plugin manifests if the wiki later needs cross-vendor plugin authoring guidance.
