---
type: concept
created: 2026-05-01
updated: 2026-05-01
status: active
sources:
  - "raw/Agent Development Kit (ADK).md"
tags: [google-adk, agent-frameworks, multi-agent, gemini, evaluation]
---

# Google Agent Development Kit (ADK)

## Key Points

Google's **Agent Development Kit (ADK)** is an open, multi-language framework for building production-grade multi-agent systems. It supports Python, TypeScript, Go, and Java, and works with Gemini and other AI models (including locally-hosted ones).

## Core Features

- **Multi-language support**: `pip install google-adk` (Python), `npm install @google/adk` (TypeScript), `go get google.golang.org/adk` (Go), Maven artifact (Java)
- **Progressive complexity**: Start with simple prompt-and-tool-call agents, then grow to multi-agent orchestration, graph-based workflows, evaluation, and enterprise deployment
- **Open model support**: Works with Gemini, other leading model providers, adapters for many providers, and locally-running models; enterprise deployments can use hosted services on Google Cloud
- **Context management**: Treats context like source code — sessions, memory, tool outputs, and artifacts are assembled into a structured view. ADK auto-filters irrelevant events, summarizes older turns, lazy-loads artifacts, and tracks token usage
- **Evaluation framework**: Built-in visual debugging, open evaluation framework for testing entire agent execution trajectories, custom performance metrics, and optimization against results
- **AI-assisted development**: ADK agents can be written by both humans and AI; coding assistants can connect to ADK developer Skills to generate agents

## Deployment

- **Deploy anywhere**: Containerize and run on own infrastructure, or use native one-command deployment to Google Cloud
- **Google Cloud options**: Agent Runtime (Agent Platform), Cloud Run, or GKE
- **Inherit managed infrastructure**: Authentication, Cloud Trace observability, and enterprise security without code changes

## Relationship to This Wiki

ADK competes with and complements [[concepts/Agent Frameworks and Orchestration]] (LangGraph, Microsoft Agent Framework, CrewAI) as a multi-agent framework. Its open evaluation framework overlaps with [[concepts/Validation and Evaluation]]. ADK's support for Agent Skills through developer resources connects to [[concepts/Tools Supporting Agent Skills]]. ADK's open model support and provider adapters relate to [[concepts/LLM Provider Selection for AI Tools]] — the same cloud hubs (Vertex AI, Google Cloud) that serve as LLM providers also power ADK's hosted deployments.

## Source

- adk.dev official site
- [[raw/Agent Development Kit (ADK)]]
