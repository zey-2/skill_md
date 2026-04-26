---
type: raw-source-note
created: 2026-04-26
updated: 2026-04-26
status: active
tags: [openai, agents-sdk, agent-skills, orchestration]
---

# OpenAI Agents SDK Official Source

## Source URLs

- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agents/orchestration
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/mcp/

## Key Source Claims

- OpenAI describes the Agents SDK as a code-first way to build agents and grow into more advanced runtime patterns.
- Agents are applications that plan, call tools, collaborate across specialists, and keep enough state to complete multi-step work.
- The docs distinguish direct OpenAI client libraries from Agents SDK usage: client libraries are for direct model requests, while the Agents SDK is for applications that own orchestration, tool execution, approvals, and state.
- The SDK supports TypeScript and Python repositories for installation, examples, issues, and language-specific reference details.
- The SDK exposes tools including hosted tools, local/runtime tools, function tools, agents-as-tools, Codex tool surfaces, and MCP-backed tools.
- The SDK describes two common multi-agent patterns: manager agents that call specialists as tools, and handoffs where a specialist becomes the active agent.
- The SDK's MCP support includes hosted MCP tool calls, Streamable HTTP servers, stdio servers, tool filtering, approval policies, metadata, caching, failure formatting, prompts, and tracing.

## Relevance to Agent Skills

The OpenAI Agents SDK is a runtime layer, not a skill package format. It is important for the wiki because it shows where Agent Skills sit in a working agent application:

- skills package reusable operating knowledge;
- tools and MCP servers expose executable capabilities and external context;
- the SDK owns turns, tool calls, handoffs, approvals, state, and traces.

This makes the SDK a useful reference when deciding whether a repeated behavior should be a portable skill, a function tool, an MCP server, a specialist agent, or a handoff workflow.

## Follow-Ups

- Track whether OpenAI's Agents SDK develops a first-class portable `SKILL.md` loading path or remains primarily a runtime/tool orchestration surface.
- Compare OpenAI Agents SDK agent-as-tool patterns with Codex subagents and Claude Agent SDK subagents.
