---
type: raw-source-note
created: 2026-04-26
updated: 2026-04-26
status: active
tags: [openai, agents-sdk, tools, mcp, orchestration]
---

# OpenAI Agents SDK Tools, MCP, and Orchestration Source

## Source URLs

- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/multi_agent/
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/mcp/

## Key Source Claims

- In the OpenAI Agents SDK, an agent is an LLM configured with instructions, tools, optional handoffs, guardrails, structured outputs, hooks, sessions, and MCP servers.
- The SDK distinguishes tool categories including hosted OpenAI tools, local/runtime tools, function tools, agents as tools, and MCP-backed tools.
- Function tools wrap local Python functions and expose names, descriptions, and JSON Schema parameter definitions to the model.
- Hosted tool search can defer large tool surfaces until runtime. Namespaces and hosted MCP servers can help reduce tool-schema tokens and provide a better high-level search surface.
- MCP integrations include hosted MCP tool calls through the Responses API, Streamable HTTP MCP servers, legacy HTTP with SSE, stdio servers, and an MCP server manager.
- MCP integrations require decisions around tool filtering, prompt exposure, caching `list_tools()`, tracing, approval policies, per-call metadata, and failure formatting.
- The SDK describes two common multi-agent patterns:
  - Manager or agents-as-tools: a central agent keeps conversation control and calls specialist agents as tools.
  - Handoffs: a triage or peer agent delegates the conversation to a specialist, which becomes active.
- The orchestration guide distinguishes LLM-directed orchestration from code-directed orchestration. The docs say these patterns can be mixed.
- The OpenAI docs recommend specialized agents rather than expecting one general-purpose agent to be good at everything, plus monitoring, iteration, and evals.

## Relevance to Agent Skills

OpenAI's SDK makes the boundary between skills, tools, and agents visible:

- A skill is reusable operating guidance or domain knowledge.
- A function tool, hosted tool, MCP server, or runtime tool is an action/context surface.
- A specialist agent can be exposed as a callable tool or receive control through a handoff.
- Tool search and skill progressive disclosure are parallel ideas: both avoid loading every detail up front and rely on good descriptions/routing metadata.

For skill design, this suggests that a skill package should clarify which parts are instructions, which parts should be executable tools or scripts, and when a subagent or handoff is the better abstraction.

## Follow-Ups

- Add examples that map a single recurring workflow into three implementations: pure skill, skill plus MCP tool, and orchestrated multi-agent workflow.
