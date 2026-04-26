---
type: synthesis
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/2026-04-26 agentskills.io Agent Skills overview and quickstart.md"
  - "raw/2026-04-26 OpenAI Codex Agent Skills docs.md"
  - "raw/2026-04-26 Claude Code Agent Skills docs.md"
  - "raw/2026-04-26 Gemini CLI Agent Skills docs.md"
  - "raw/2026-04-26 GitHub Copilot and VS Code Agent Skills docs.md"
  - "raw/2026-04-26 Cursor Agent Skills support sources.md"
  - "raw/2026-04-26 OpenCode Agent Skills docs.md"
  - "raw/2026-04-26 OpenClaw Skills docs.md"
  - "raw/2026-04-26 Windsurf Cascade Skills docs.md"
  - "raw/2026-04-26 Microsoft Agent Framework Agent Skills docs.md"
  - "raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md"
  - "raw/2026-04-26 MCP architecture and Agent Skills integration source.md"
  - "raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md"
  - "raw/2026-04-26 Agent orchestration frameworks source.md"
  - "raw/2026-04-26 OpenAI Codex SDK and App Server source.md"
  - "raw/2026-04-26 Claude Agent SDK source.md"
  - "raw/2026-04-26 OpenAI Codex Plugins docs.md"
  - "raw/2026-04-26 Claude Code Plugins docs.md"
tags: [agent-skills, tool-support, comparison]
---

# Tools Supporting Agent Skills

## Summary

Several current agent clients support `SKILL.md` or Agent Skills-style packages, but they do not all use the same discovery paths, invocation model, or distribution mechanism. The stable common core is a skill folder containing `SKILL.md` with at least `name` and `description`; the unstable layer is where each tool looks for skills and how it exposes them to users.

The strongest primary-source support in this ingest covers OpenAI Codex, Claude Code, Gemini CLI, GitHub Copilot/VS Code, OpenCode, OpenClaw, Windsurf Cascade, and Microsoft Agent Framework. Cursor has primary support evidence from its official changelog, but the current text extraction did not expose its full docs page, so detailed Cursor path claims should stay moderate-confidence until rechecked.

## Support Matrix

| Tool or client | Support evidence | Main discovery paths or scopes | Invocation and behavior | Notes |
| --- | --- | --- | --- | --- |
| OpenAI Codex | Codex docs say skills are available in CLI, IDE extension, and app. | `.agents/skills` in repository paths, `$HOME/.agents/skills`, `/etc/codex/skills`, and bundled system skills. | Explicit `/skills` or `$skill` mention; implicit selection by `description`. | Plugins are the recommended distribution unit for reusable skills beyond local folders. |
| Claude Code | Claude Code docs describe personal, project, plugin, and enterprise skills. | `~/.claude/skills/`, `.claude/skills/`, plugin skills, and enterprise scope. | Model-invoked skills plus slash-command invocation in newer docs. | Claude-specific `allowed-tools` can restrict tool access for a skill. |
| GitHub Copilot and VS Code | GitHub Docs and VS Code docs say skills work with Copilot cloud agent, Copilot CLI, and VS Code agent mode. | Project: `.github/skills/`, `.claude/skills/`, `.agents/skills/`. Personal: `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/`. | Copilot injects `SKILL.md` when relevant; VS Code also exposes slash commands. | VS Code extensions can contribute skills with `chatSkills`. Organization and enterprise skills are described as future work. |
| Gemini CLI | Gemini CLI docs describe Agent Skills, `activate_skill`, and `gemini skills` commands. | Workspace: `.gemini/skills/` or `.agents/skills/`. User: `~/.gemini/skills/` or `~/.agents/skills/`. Extension skills also exist. | Agent calls `activate_skill`; users can manage skills with `/skills` and `gemini skills`. | `.agents/skills/` has precedence over `.gemini/skills/` within a tier. |
| Cursor | Cursor 2.4 changelog says the editor and CLI support Agent Skills. | Existing local ecosystem source lists `.cursor/skills/` and `~/.cursor/skills/`; forum discussion also mentions `.agents/skills/` as a cross-agent path. | Changelog says skills can be discovered by agents and invoked from the slash command menu. | Full path and precedence details need direct confirmation from a readable Cursor docs extract. |
| OpenCode | OpenCode docs describe reusable `SKILL.md` behavior loaded by a native `skill` tool. | `.opencode/skills/`, `~/.config/opencode/skills/`, `.claude/skills/`, `~/.claude/skills/`, `.agents/skills/`, `~/.agents/skills/`. | Agents see available skills and load full content on demand through the native skill tool. | Unknown frontmatter fields are ignored; `name` must match the directory. |
| OpenClaw | OpenClaw docs describe AgentSkills-compatible folders. | `<workspace>/skills`, `<workspace>/.agents/skills`, `~/.agents/skills`, `~/.openclaw/skills`, bundled skills, and configured extra dirs. | Loads and filters skills at startup based on environment/config/binary presence; watches folders for changes. | Precedence favors workspace skills over managed, bundled, and extra-dir skills. |
| Windsurf Cascade | Windsurf docs describe Cascade Skills and point to agentskills.io. | `.windsurf/skills/`, `~/.codeium/windsurf/skills/`, enterprise system paths, `.agents/skills/`, `~/.agents/skills/`; optionally `.claude/skills/`. | Automatic invocation by matching `description`; manual invocation with `@skill-name`. | Claude-compatible paths are conditional on Claude Code config reading. |
| Microsoft Agent Framework | Microsoft Learn documents an Agent Skills provider. | Configured skill directories; the provider searches for `SKILL.md` up to two levels deep. | Exposes tools such as `load_skill`, `read_skill_resource`, and optionally `run_skill_script`. | This is a framework integration rather than a standalone coding-agent client. |

## Patterns

- The common file format is stable enough to reuse: `SKILL.md` with `name`, `description`, and Markdown instructions appears across sources.
- `.agents/skills/` is emerging as a cross-agent compatibility path, especially in Codex, Gemini CLI, GitHub Copilot/VS Code, OpenCode, OpenClaw, and Windsurf.
- Vendor-native paths still matter: `.claude/skills/`, `.gemini/skills/`, `.opencode/skills/`, `.windsurf/skills/`, `.github/skills/`, and `.copilot/skills/` all appear in current docs.
- Some tools support direct local folders, while others emphasize plugins, extensions, or framework providers.
- Plugins are becoming the richer distribution layer when a capability needs more than a `SKILL.md` folder. Codex plugins can bundle skills, app integrations, and MCP servers; Claude Code plugins can bundle skills, agents, hooks, MCP servers, LSP servers, monitors, themes, and related configuration.
- Activation is usually description-driven, with optional manual invocation through slash commands, `$skill`, or `@skill-name` depending on the client.
- Tool support and framework support are adjacent but different. Coding clients discover skills for an assistant session; frameworks such as OpenAI Agents SDK, LangGraph, Microsoft Agent Framework, and CrewAI use skills, tools, agents, handoffs, memory, state, and workflows as runtime building blocks.
- SDK support is another adjacent layer. Codex SDK, Codex App Server, and Claude Agent SDK do not merely discover skills for an interactive UI; they let applications automate or embed skill-guided agents.

## Contradictions or Tensions

The ecosystem uses the same broad package idea but not a single install convention. A skill can be portable as content while still needing per-client placement, symlinks, plugin wrapping, or an installer.

Cursor is the main uncertainty in this ingest. The official changelog confirms support, but a direct readable docs capture is still needed to confirm current path precedence.

## Connections

- [[Discovery Conventions]] tracks where clients look for skills.
- [[Skill Distribution and Installation]] explains how skills move from repositories or catalogs into local clients.
- [[Plugin-Based Agent Extensions]] explains how plugins package skills with tool surfaces, marketplace metadata, and governance boundaries.
- [[Vendor Adapters]] explains why platform-specific metadata should stay outside the portable core.
- [[Portable Skill Core]] explains why `name` and `description` are the most reusable fields.
- [[MCP and Tool-Integration Architecture]] explains how tool surfaces relate to skill packages.
- [[Agent Frameworks and Orchestration]] explains how frameworks coordinate skills with subagents, handoffs, workflows, and state.
- [[Agent SDKs and Codex Automation]] explains SDK and app-server surfaces around skill-guided agents.

## Open Questions

- Will `.agents/skills/` become the dominant shared path, or remain one compatibility path among many?
- Will Cursor's official docs expose a complete discovery table comparable to the other clients?
- Will framework-level consumers such as Microsoft Agent Framework converge on the same metadata and validation rules as coding-agent clients?
- Will Agent Skills gain a common way to declare required MCP servers, tool permissions, and orchestration dependencies?
