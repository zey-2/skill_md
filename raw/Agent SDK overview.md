---
title: "Agent SDK overview"
source: "https://code.claude.com/docs/en/agent-sdk/overview"
author:
published:
created: 2026-05-01
description: "Build production AI agents with Claude Code as a library"
tags:
  - "clippings"
---
The Claude Code SDK has been renamed to the Claude Agent SDK. If you’re migrating from the old SDK, see the [Migration Guide](https://code.claude.com/docs/en/agent-sdk/migration-guide).

Build AI agents that autonomously read files, run commands, search the web, edit code, and more. The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript.

Opus 4.7 (`claude-opus-4-7`) requires Agent SDK v0.2.111 or later. If you see a `thinking.type.enabled` API error, see [Troubleshooting](https://code.claude.com/docs/en/agent-sdk/quickstart#troubleshooting).

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Find and fix the bug in auth.py",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Bash"]),
    ):
        print(message)  # Claude reads the file, finds the bug, edits it

asyncio.run(main())
```

The Agent SDK includes built-in tools for reading files, running commands, and editing code, so your agent can start working immediately without you implementing tool execution. Dive into the quickstart or explore real agents built with the SDK:

## [Quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart)

Build a bug-fixing agent in minutes

## [Example agents](https://github.com/anthropics/claude-agent-sdk-demos)

Email assistant, research agent, and more

## Get started

**Ready to build?** Follow the [Quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart) to create an agent that finds and fixes bugs in minutes.

## Capabilities

Everything that makes Claude Code powerful is available in the SDK:

- Built-in tools
- Hooks
- Subagents
- MCP
- Permissions
- Sessions

Your agent can read files, run commands, and search codebases out of the box. Key tools include:

| Tool | What it does |
| --- | --- |
| **Read** | Read any file in the working directory |
| **Write** | Create new files |
| **Edit** | Make precise edits to existing files |
| **Bash** | Run terminal commands, scripts, git operations |
| **Monitor** | Watch a background script and react to each output line as an event |
| **Glob** | Find files by pattern (`**/*.ts`, `src/**/*.py`) |
| **Grep** | Search file contents with regex |
| **WebSearch** | Search the web for current information |
| **WebFetch** | Fetch and parse web page content |
| **[AskUserQuestion](https://code.claude.com/docs/en/agent-sdk/user-input#handle-clarifying-questions)** | Ask the user clarifying questions with multiple choice options |

This example creates an agent that searches your codebase for TODO comments:

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Find all TODO comments and create a summary",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Glob", "Grep"]),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

### Claude Code features

The SDK also supports Claude Code’s filesystem-based configuration. With default options the SDK loads these from `.claude/` in your working directory and `~/.claude/`. To restrict which sources load, set `setting_sources` (Python) or `settingSources` (TypeScript) in your options.

| Feature | Description | Location |
| --- | --- | --- |
| [Skills](https://code.claude.com/docs/en/agent-sdk/skills) | Specialized capabilities defined in Markdown | `.claude/skills/*/SKILL.md` |
| [Slash commands](https://code.claude.com/docs/en/agent-sdk/slash-commands) | Custom commands for common tasks | `.claude/commands/*.md` |
| [Memory](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts) | Project context and instructions | `CLAUDE.md` or `.claude/CLAUDE.md` |
| [Plugins](https://code.claude.com/docs/en/agent-sdk/plugins) | Extend with custom commands, agents, and MCP servers | Programmatic via `plugins` option |

## Compare the Agent SDK to other Claude tools

The Claude Platform offers multiple ways to build with Claude. Here’s how the Agent SDK fits in:

- Agent SDK vs Client SDK
- Agent SDK vs Claude Code CLI
- Agent SDK vs Managed Agents

The [Anthropic Client SDK](https://platform.claude.com/docs/en/api/client-sdks) gives you direct API access: you send prompts and implement tool execution yourself. The **Agent SDK** gives you Claude with built-in tool execution.

With the Client SDK, you implement a tool loop. With the Agent SDK, Claude handles it:

```python
# Client SDK: You implement the tool loop
response = client.messages.create(...)
while response.stop_reason == "tool_use":
    result = your_tool_executor(response.tool_use)
    response = client.messages.create(tool_result=result, **params)

# Agent SDK: Claude handles tools autonomously
async for message in query(prompt="Fix the bug in auth.py"):
    print(message)
```

## Changelog

View the full changelog for SDK updates, bug fixes, and new features:

- **TypeScript SDK**: [view CHANGELOG.md](https://github.com/anthropics/claude-agent-sdk-typescript/blob/main/CHANGELOG.md)
- **Python SDK**: [view CHANGELOG.md](https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md)

## Reporting bugs

If you encounter bugs or issues with the Agent SDK:

- **TypeScript SDK**: [report issues on GitHub](https://github.com/anthropics/claude-agent-sdk-typescript/issues)
- **Python SDK**: [report issues on GitHub](https://github.com/anthropics/claude-agent-sdk-python/issues)

## Branding guidelines

For partners integrating the Claude Agent SDK, use of Claude branding is optional. When referencing Claude in your product:

**Allowed:**

- “Claude Agent” (preferred for dropdown menus)
- “Claude” (when within a menu already labeled “Agents”)
- ” Powered by Claude” (if you have an existing agent name)

**Not permitted:**

- “Claude Code” or “Claude Code Agent”
- Claude Code-branded ASCII art or visual elements that mimic Claude Code

Your product should maintain its own branding and not appear to be Claude Code or any Anthropic product. For questions about branding compliance, contact the Anthropic [sales team](https://www.anthropic.com/contact-sales).

## License and terms

Use of the Claude Agent SDK is governed by [Anthropic’s Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), including when you use it to power products and services that you make available to your own customers and end users, except to the extent a specific component or dependency is covered by a different license as indicated in that component’s LICENSE file.

## Next steps

## [Example agents](https://github.com/anthropics/claude-agent-sdk-demos)

Email assistant, research agent, and more