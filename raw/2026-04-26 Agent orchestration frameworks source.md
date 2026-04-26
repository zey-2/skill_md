---
type: raw-source-note
created: 2026-04-26
updated: 2026-04-26
status: active
tags: [agent-frameworks, orchestration, langgraph, microsoft-agent-framework, crewai]
---

# Agent Orchestration Frameworks Source

## Source URLs

- https://docs.langchain.com/oss/python/langgraph/overview
- https://learn.microsoft.com/en-us/agent-framework/overview/
- https://learn.microsoft.com/en-us/agent-framework/workflows/
- https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/sequential
- https://docs.crewai.com/en

## Key Source Claims

- LangGraph is positioned as a low-level orchestration framework and runtime for long-running, stateful agents. Its highlighted capabilities include durable execution, streaming, human-in-the-loop control, memory, debugging, and production deployment.
- Microsoft Agent Framework distinguishes agents from workflows. Use agents for open-ended or conversational tasks with autonomous planning/tool use; use workflows when steps are defined, execution order must be controlled, or multiple agents/functions need coordination.
- Microsoft Agent Framework combines AutoGen-style agent abstractions with Semantic Kernel-style enterprise features such as session state, type safety, middleware, telemetry, model/embedding support, graph workflows, and human-in-the-loop scenarios.
- Microsoft workflows use graph concepts such as executors, edges, events, and workflow builder/execution. Built-in orchestration patterns include sequential, concurrent, hand-off, and magentic coordination.
- Microsoft sequential orchestration treats agents as a pipeline where each agent processes the task in order. It can wrap sensitive tools in approval-required functions and pause workflows for human responses.
- CrewAI positions itself around agents, crews, flows, tasks/processes, memory, knowledge, guardrails, callbacks, human-in-the-loop triggers, observability, deployment, triggers, and enterprise automations.

## Relevance to Agent Skills

Agent frameworks and Agent Skills solve different but adjacent problems:

- Frameworks manage runtime execution: state, control flow, events, tool calls, memory, observability, and deployment.
- Skills package reusable know-how for an agent: procedures, domain references, scripts, and when-to-use metadata.
- Skills can live inside a framework as context providers or resources, as Microsoft Agent Framework demonstrates with its skills provider.
- Frameworks can also be the subject of skills: a skill can teach an agent how to build a LangGraph workflow, design a Microsoft Agent Framework workflow, or create a CrewAI crew/flow.

The important design question is not "skill or framework?" but "which layer owns the behavior?" Stable control flow belongs in code/workflows; reusable procedure and domain guidance belongs in skills; external actions and data access belong in tools or MCP servers.

## Follow-Ups

- Build a decision table for choosing between a portable skill, MCP server, function tool, subagent, handoff, graph workflow, or project-level instruction file.
- Add a framework-specific adapter page if the wiki later tracks how each framework loads Agent Skills directly.
