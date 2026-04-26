---
type: raw-source-note
created: 2026-04-26
updated: 2026-04-26
status: active
tags: [anthropic, claude, agent-sdk, agent-skills, mcp]
---

# Claude Agent SDK Source

## Source URLs

- https://code.claude.com/docs/en/agent-sdk/overview
- https://platform.claude.com/docs/en/agent-sdk/typescript
- https://platform.claude.com/docs/en/agent-sdk/python
- https://platform.claude.com/docs/en/agent-sdk/mcp

## Key Source Claims

- Anthropic now documents this surface as the Claude Agent SDK. Older Claude Code SDK URLs redirect into the Agent SDK docs.
- The Agent SDK is presented as a way to build custom agents with Claude Code's agent harness, tool execution, session handling, and configuration surfaces.
- The TypeScript SDK package is `@anthropic-ai/claude-agent-sdk`; its primary `query()` function streams SDK messages as an async generator.
- The TypeScript SDK can define type-safe MCP tools with `tool()` and create in-process SDK MCP servers with `createSdkMcpServer()`.
- The Python SDK package is `claude-agent-sdk`. The docs distinguish one-off `query()` use from `ClaudeSDKClient`, which maintains an explicit continuous conversation.
- The SDK supports Claude Code filesystem-based configuration by default, including skills in `.claude/skills/*/SKILL.md`, slash commands, memory files, and plugins. Settings sources can be restricted.
- The SDK's MCP guide says MCP connects agents to external tools and data sources, and servers can run as local processes, over HTTP, or directly inside an SDK application.
- SDK MCP configuration can be passed in code or loaded from `.mcp.json`, and tool access is controlled through `allowedTools` patterns such as `mcp__server__*`.

## Relevance to Agent Skills

Claude Agent SDK is one of the clearest examples of a runtime that can combine:

- filesystem skills;
- project or user-level configuration;
- custom MCP tools;
- sessions and streamed messages;
- programmatic permissions and allowed tool lists.

For this wiki, the key point is that a skill can be a durable instruction package while the Agent SDK supplies the execution harness around it. The SDK also strengthens the need to track where a behavior lives: `SKILL.md`, slash command, memory file, plugin, MCP server, custom tool, or SDK session logic.

## Follow-Ups

- Compare Claude Agent SDK's default loading of `.claude/skills/*/SKILL.md` with Codex's `.agents/skills` and plugin model.
- Add a focused page later if the wiki needs exact Python/TypeScript code patterns for using skills in the SDK.
