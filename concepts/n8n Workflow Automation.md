---
type: concept
created: 2026-05-01
updated: 2026-05-01
status: active
sources:
  - "raw/n8n A Guide to Workflow Automation.md"
  - "raw/Deploy n8n on Cloud Run  Google Cloud Blog.md"
tags: [n8n, workflow-automation, ai-agents, self-hosting, cloud-run]
---

# n8n Workflow Automation

## Key Points

**n8n** (pronounced "n-eight-n") is an open-source, node-based workflow automation platform that connects apps, services, and APIs through visual workflows. It supports complex logic, branching, error handling, custom code, and AI/ML orchestration.

## Core Components

- **Trigger Nodes**: Start workflows (on app event, schedule, chat message, webhook)
- **Action Nodes**: Execute tasks (send email, create records, call APIs, transform data)
- **Logic Nodes**: Control flow (IF conditions, Switch, Merge, Filter, Looping)
- **Code Nodes**: Custom JavaScript/Python for data transformations and advanced logic when built-in nodes are insufficient

## Key Characteristics

- **Open-source and self-hostable**: Full control over data and infrastructure; free for self-hosted use
- **Developer-friendly**: Supports complex logic, custom code, and API integrations beyond no-code limits
- **AI/LLM workflow support**: Can orchestrate LLM calls, build RAG pipelines, coordinate AI agents, and automate batch inference
- **400+ built-in integrations**: Connects to Gmail, Google Calendar, Google Sheets, Telegram, databases, and many more
- **Pre-built workflow templates**: Available at n8n.io/workflows/ for common use cases (e.g., email-to-calendar scheduling, nutrition tracking with AI)

## Deployment Options

| Option | Description |
|--------|-------------|
| **n8n Cloud** | Fully managed hosting; quick setup, no infrastructure maintenance |
| **Self-hosting (Docker/Kubernetes)** | Full control over security, data, and scaling; best for customization |
| **Google Cloud Run** | Serverless deployment with auto-scaling from zero; persistent data via Cloud SQL; pay only for compute used |
| **DigitalOcean 1-Click** | Instant deployment on a Droplet with Caddy for HTTPS |

## Google Cloud Run Deployment

Deploy n8n to Cloud Run for a managed, serverless environment:
- One-command deploy: `gcloud run deploy --image=n8nio/n8n --allow-unauthenticated --port=5678 --no-cpu-throttling --memory=2Gi`
- Durable mode: Connect to Cloud SQL for persistent storage and Secrets Manager for credentials
- Google Workspace integration: Configure OAuth to access Gmail, Calendar, and Drive directly from workflows
- AI agents in n8n can call **Gemini** as the LLM for text classification, scheduling, and content generation

## Best Practices

- Keep workflows modular and reusable (single responsibility per workflow)
- Use descriptive node names for readability
- Log critical steps for debugging
- Enable error workflows for production alerting
- Avoid hardcoding credentials; use n8n's credential system
- Version control workflows via export to Git

## Comparison to Similar Tools

- **vs Zapier**: n8n offers more flexibility, self-hosting, advanced logic, and lower long-term cost; Zapier is simpler but limits customization and becomes expensive at scale
- **vs LangChain/LangGraph**: n8n is a visual workflow platform for connecting apps and services; LangChain/LangGraph are code-first LLM application frameworks. n8n can use LLM nodes (Gemini, OpenAI) within its workflows but doesn't provide the same agent orchestration primitives (state graphs, checkpointers, handoffs)

## Relationship to This Wiki

n8n represents a **visual workflow automation layer** that can complement code-based agent frameworks. While Agent Skills (SKILL.md) package reusable agent procedures, n8n provides the execution surface for multi-step automations connecting external services. n8n's AI nodes and agent capabilities overlap with [[concepts/Agent Frameworks and Orchestration]] as a no-code/low-code orchestration alternative. n8n's 400+ integrations and custom code nodes serve as tool-call surfaces that could be exposed through [[concepts/MCP and Tool-Integration Architecture]], allowing skills to guide agents toward n8n workflows as external tools.

## Sources

- DigitalOcean conceptual guide by Shaoni Mukherjee, 2025-12-18
- Google Cloud blog by Ryan Pei, 2025-11-08
- [[raw/n8n A Guide to Workflow Automation]]
- [[raw/Deploy n8n on Cloud Run  Google Cloud Blog]]
