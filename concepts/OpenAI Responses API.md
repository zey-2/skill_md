---
type: concept
created: 2026-05-01
updated: 2026-05-01
status: active
sources:
  - "raw/OpenAI API Responses vs. Chat Completions.md"
  - "raw/Why we built the Responses API.md"
tags: [openai, api-design, agent-architecture, reasoning-models]
---

# OpenAI Responses API

## Key Points

OpenAI's **Responses API** (`/v1/responses`) is the successor to Chat Completions as the recommended API for building agentic and reasoning-model applications. It introduces server-side state management, preserved reasoning state, polymorphic output items, and hosted tool primitives — making it the first API primitive designed from the ground up for the agentic loop.

## API Evolution

| Generation | Endpoint | Paradigm | Status |
|---|---|---|---|
| Completions | `/v1/completions` | Text completion | Legacy |
| Chat Completions | `/v1/chat/completions` | Turn-based chat with roles | Supported indefinitely |
| Assistants | `/v1/assistants` | Hosted threads and runs | Deprecated, sunset Aug 2026 |
| **Responses** | `/v1/responses` | Stateful agentic loop | **Recommended for new development** |

## Key Differences from Chat Completions

| Aspect | Chat Completions | Responses API |
|---|---|---|
| **State** | Client-managed message arrays | Server-managed via `store: true` + `previous_response_id` |
| **Reasoning state** | Dropped between calls | Preserved encrypted across turns (+5% on TAUBench) |
| **Output shape** | Single `message` per response | Polymorphic items: messages, function calls, reasoning summaries |
| **Built-in tools** | None (client must implement) | Web search, file search, code interpreter, image gen, MCP |
| **Reasoning models** | Reasoning lost between turns | Optimized for o-series, GPT-5 |
| **Cache utilization** | Standard | 40–80% better cache utilization |
| **Streaming** | Token-level events | Semantic streaming events with tagged polymorphism |

## Design Rationale

The Responses API treats the agent loop as a first-class primitive. Instead of the client manually managing the ReAct loop (send tools → receive tool calls → execute → send results → repeat), the API preserves the model's reasoning state server-side and emits structured output items that distinguish what the model *said* from what it *did*.

Reasoning state is encrypted and hidden from the client — this is intentional. Raw chain-of-thought is not exposed because of hallucination risks, harmful content that wouldn't appear in final responses, and competitive concerns. The API allows safe continuation via `previous_response_id` without exposing internal reasoning.

## Hosted Tools

The Responses API includes several server-side hosted tools that execute without bouncing back through the client backend:

- **`web_search_preview`** — same search as ChatGPT, priced $25–$50 per 1K queries
- **`file_search`** — vector store integration for RAG, $2.50 per 1K queries
- **`computer_use_preview`** — sandboxed computer control (similar to Claude Computer Use)
- **MCP** — hosted MCP tool execution server-side for better latency

## Implications for Agent Skills

The Responses API shift has two implications for this wiki's Agent Skills focus:

1. **Skills live in the client/harness layer**, not the API layer. The Responses API manages conversation state and tool execution, but skills (as `SKILL.md` packages) operate at the agent harness level — guiding *what* the agent does, not *how* the API manages state.

2. **Hosted tools reduce the need for custom MCP servers** in simple cases. When web search, file search, or code interpreter are available as built-in tools, skills can reference them directly rather than requiring custom tool definitions. However, MCP remains important for team-specific or enterprise tools that shouldn't be hardcoded to one API.

## Connections

- [[concepts/Agent SDKs and Codex Automation]] — the OpenAI Agents SDK uses the Responses API as its underlying transport for tool use and state management.
- [[concepts/MCP and Tool-Integration Architecture]] — MCP is available as a hosted tool within the Responses API, bridging the API and external tool layers.
- [[concepts/Agent Frameworks and Orchestration]] — the Responses API's built-in agentic loop overlaps with what orchestration frameworks provide; developers must decide when to use the API's native loop vs. a framework's graph workflow.
- [[concepts/LLM Provider Selection for AI Tools]] — the Responses API is OpenAI-specific; providers following the OpenAI-compatible standard typically only implement Chat Completions.

## Open Questions

- Will other providers adopt a Responses-like stateful API, or remain at the Chat Completions level?
- How should Agent Skills declare dependency on hosted tools (web search, file search) vs. custom MCP tools?
- Does server-side reasoning state change how skills should manage context, or is the skill layer independent of API-level state?
