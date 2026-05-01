---
type: index
created: 2026-04-26
updated: 2026-05-01
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/openaiskills Skills Catalog for Codex.md"
  - "raw/anthropicsskills Public repository for Agent Skills.md"
  - "raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md"
  - "raw/obrasuperpowers An agentic skills framework & software development methodology that works.md"
  - "raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md"
  - "raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md"
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
  - "raw/2026-04-30 Microsoft Copilot SKILL.md support roadmap.md"
  - "raw/2026-04-26 Google Cloud Vertex AI and Model Garden LLM provider source.md"
  - "raw/2026-04-26 AWS Amazon Bedrock LLM provider source.md"
  - "raw/2026-04-26 Azure AI Foundry Models LLM provider source.md"
  - "raw/2026-04-26 OpenAI API LLM provider source.md"
  - "raw/2026-04-26 Anthropic Claude API LLM provider source.md"
  - "raw/2026-04-26 Cohere LLM provider source.md"
  - "raw/2026-04-26 Mistral AI LLM provider source.md"
  - "raw/2026-04-26 xAI Grok API LLM provider source.md"
  - "raw/2026-04-26 DeepSeek API LLM provider source.md"
  - "raw/2026-04-26 OpenRouter LLM provider router source.md"
  - "raw/2026-04-26 Open model inference providers source.md"
  - "raw/2026-04-26 Perplexity Sonar API LLM provider source.md"
  - "raw/2026-04-26 Agent Skills specification evaluation and description optimization.md"
  - "raw/2026-04-26 OpenAI agent evaluation and trace grading docs.md"
  - "raw/2026-04-26 Anthropic evals for AI agents.md"
  - "raw/2026-04-26 LangSmith AgentEvals trajectory evaluation docs.md"
  - "raw/2026-04-26 tau-bench tool-agent reliability benchmark.md"
  - "raw/2026-04-26 MCP architecture and Agent Skills integration source.md"
  - "raw/2026-04-26 MCP security and authorization source.md"
  - "raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md"
  - "raw/2026-04-26 Agent orchestration frameworks source.md"
  - "raw/2026-04-26 OpenAI Agents SDK official source.md"
  - "raw/2026-04-26 OpenAI Codex SDK and App Server source.md"
  - "raw/2026-04-26 Claude Agent SDK source.md"
  - "raw/2026-04-26 OpenAI Codex Plugins docs.md"
  - "raw/2026-04-26 Claude Code Plugins docs.md"
  - "raw/OpenAI's 5 Levels Of 'Super AI' (AGI To Outperform Human Capability).md"
  - "raw/LangChain vs LangGraph vs LangSmith vs LangFlow Key Differences Explained.md"
  - "raw/n8n A Guide to Workflow Automation.md"
  - "raw/Agent SDK overview.md"
  - "raw/Agent Development Kit (ADK).md"
  - "raw/Deploy n8n on Cloud Run  Google Cloud Blog.md"
  - "raw/Deep Dive into LLMs like ChatGPT.md"
  - "raw/OpenAI API Responses vs. Chat Completions.md"
  - "raw/Why we built the Responses API.md"
  - "raw/VILA-LabDive-into-Claude-Code A Systematic Analysis and Discussion of Claude Code for Designing Today's and Future AI Agent Systems.md"
tags: [index, agent-skills, llm-providers]
---

# Index

## Concept Articles

- [[concepts/AI Coding Plans|AI Coding Plans]] - Compares model-provider coding plans (Alibaba 百炼, BytePlus ModelArk, Kimi Code, Zhipu GLM, MiniMax, Infini) and coding-tool subscriptions (Copilot, Cursor, Claude Code, Kilo Code).
- [[concepts/Agent Skills|Agent Skills]] - Defines skills as reusable agent operating procedures, including task helpers, workflow guides, and guardrails.
- [[concepts/SKILL.md Package Anatomy|SKILL.md Package Anatomy]] - Explains the core `SKILL.md` file and supporting folders such as `scripts/`, `references/`, and `assets/`.
- [[concepts/Portable Skill Core|Portable Skill Core]] - Describes the small cross-platform metadata core centered on `name` and `description`, and why precise wording matters.
- [[concepts/Vendor Adapters|Vendor Adapters]] - Explains how platform-specific metadata can live outside the canonical skill package.
- [[concepts/Progressive Disclosure|Progressive Disclosure]] - Shows why skills should load metadata, instructions, and resources in layers, with practical size heuristics.
- [[concepts/Skill Authoring Workflow|Skill Authoring Workflow]] - Outlines how recurring tasks such as planning, TDD, review, and guardrails become reusable skills.
- [[concepts/Skill Repository Architecture|Skill Repository Architecture]] - Describes how to organize a repository of skill packages, indexes, adapters, and metadata.
- [[concepts/Validation and Evaluation|Validation and Evaluation]] - Separates structural validation, trigger evals, output evals, traces, outcomes, and reliability checks for agent skills.
- [[concepts/Provenance and Versioning|Provenance and Versioning]] - Explains how source tracking, release records, and sync metadata keep skills maintainable.
- [[concepts/Discovery Conventions|Discovery Conventions]] - Distinguishes package-level `SKILL.md`, site-level `skill.md`, and tool-specific local skill paths.
- [[concepts/Skill Distribution and Installation|Skill Distribution and Installation]] - Summarizes catalogs, plugin marketplaces, installers, local folders, and project-level instruction files.
- [[concepts/Skill Repository Tooling|Skill Repository Tooling]] - Summarizes practical tools for storing, validating, searching, publishing, and installing skills.
- [[concepts/Skill Governance and Metrics|Skill Governance and Metrics]] - Covers ownership, licensing, trust, quality metrics, and common repository pitfalls.
- [[concepts/Tools Supporting Agent Skills|Tools Supporting Agent Skills]] - Compares current Agent Skills support across Codex, Claude Code, Gemini CLI, GitHub Copilot/VS Code, Cursor, OpenCode, OpenClaw, Windsurf, Microsoft Agent Framework, Copilot Cowork (M365), and Copilot Studio.
- [[concepts/LLM Provider Selection for AI Tools|LLM Provider Selection for AI Tools]] - Prioritizes cloud model hubs, direct frontier providers, routing layers, and specialized/open-model inference providers for powering AI tools.
- [[concepts/MCP and Tool-Integration Architecture|MCP and Tool-Integration Architecture]] - Explains how Agent Skills relate to MCP hosts, clients, servers, tools, resources, prompts, approval policies, and tool security.
- [[concepts/Claude Code Third-Party Provider Configuration|Claude Code Third-Party Provider Configuration]] - Explains how to configure Claude Code in VS Code with OpenRouter, LiteLLM, Bedrock, Vertex AI, and Foundry via environment variables and settings files.
- [[concepts/Plugin-Based Agent Extensions|Plugin-Based Agent Extensions]] - Explains plugins as installable bundles that can package skills, app integrations, MCP servers, metadata, and marketplace distribution.
- [[concepts/Agent Frameworks and Orchestration|Agent Frameworks and Orchestration]] - Compares when skills should be combined with tools, subagents, handoffs, graph workflows, state, human review, and orchestration frameworks.
- [[concepts/Agent SDKs and Codex Automation|Agent SDKs and Codex Automation]] - Compares OpenAI Agents SDK, OpenAI Codex SDK, Codex App Server, and Claude Agent SDK as runtime surfaces around Agent Skills.
- [[concepts/OpenAI AGI Progression Framework|OpenAI AGI Progression Framework]] - Describes OpenAI's five-level AGI progression (conversational → reasoners → agents → innovators → organizations) and its implications for skill design.
- [[concepts/LangChain Ecosystem Components|LangChain Ecosystem Components]] - Compares LangChain (foundation), LangGraph (orchestrator), LangSmith (observer), and LangFlow (visual builder) for building production-ready LLM applications.
- [[concepts/n8n Workflow Automation|n8n Workflow Automation]] - Explains n8n as an open-source workflow automation platform with node-based visual workflows, AI/LLM orchestration, and deployment options including Cloud Run and self-hosting.
- [[concepts/Google Agent Development Kit (ADK)|Google Agent Development Kit (ADK)]] - Covers Google's multi-language (Python, TypeScript, Go, Java) framework for building production-grade multi-agent systems with progressive complexity, open model support, context management, and evaluation.
- [[concepts/Claude Code Architecture Deep Dive|Claude Code Architecture Deep Dive]] - Source-level analysis of Claude Code v2.1.88 (~512K lines): 98.4% infrastructure, 1.6% AI; 7 safety layers, 5 compaction stages, 4 extensibility mechanisms, 7 permission modes.
- [[concepts/OpenAI Responses API|OpenAI Responses API]] - OpenAI's stateful agentic API with preserved reasoning state, hosted tools (web search, file search, MCP), and server-side conversation management.
- [[concepts/LLM Fundamentals|LLM Fundamentals]] - How LLMs work: tokenization, transformer pretraining, RLHF fine-tuning, and autoregressive inference. Foundational mental models for understanding why skills are structured the way they are.

## Lesson Plans

- [[lesson-plan/AI Fundamentals to Agent Skills|AI Fundamentals to Agent Skills]] - 16-module curriculum (~40-60 hours) progressing from ML basics through authoring, testing, and publishing reusable Agent Skills. Includes three learning pathways (Skill Author, Agent Developer, Quick Start).

## Raw Sources

- `raw/skill.md for AI Agents.md` - Broad synthesis of `skill.md` conventions, portability, repository design, validation, and governance.
- `raw/openaiskills Skills Catalog for Codex.md` - OpenAI catalog note on built-in, curated, and experimental Codex skills plus installer flow.
- `raw/anthropicsskills Public repository for Agent Skills.md` - Anthropic repository overview with examples, template structure, and plugin-marketplace installation.
- `raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md` - Personal skill catalog showing workflow-oriented skills such as PRD writing, TDD, and git guardrails.
- `raw/obrasuperpowers An agentic skills framework & software development methodology that works.md` - Multi-skill framework emphasizing planning, TDD, review, and subagent-driven development across tools.
- `raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md` - Large curated catalog with cross-tool paths, quality criteria, and security cautions.
- `raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md` - Project-level behavior guide that is adjacent to, but not identical with, a portable skill package.
- `raw/2026-04-26 agentskills.io Agent Skills overview and quickstart.md` - Standard overview and VS Code/GitHub Copilot quickstart evidence for Agent Skills.
- `raw/2026-04-26 OpenAI Codex Agent Skills docs.md` - Codex support across CLI, IDE extension, and app, including `.agents/skills`, plugins, and `$skill-installer`.
- `raw/2026-04-26 Claude Code Agent Skills docs.md` - Claude Code support for personal, project, plugin, enterprise, and slash-invoked skills.
- `raw/2026-04-26 Gemini CLI Agent Skills docs.md` - Gemini CLI discovery tiers, `.agents/skills` alias, activation tool, and `gemini skills` commands.
- `raw/2026-04-26 GitHub Copilot and VS Code Agent Skills docs.md` - Copilot cloud agent, Copilot CLI, and VS Code Agent Skills paths and invocation model.
- `raw/2026-04-26 Cursor Agent Skills support sources.md` - Cursor support evidence from official changelog plus noted uncertainty around full path details.
- `raw/2026-04-26 OpenCode Agent Skills docs.md` - OpenCode native `skill` tool, `.opencode/skills`, and compatibility discovery paths.
- `raw/2026-04-26 OpenClaw Skills docs.md` - OpenClaw AgentSkills-compatible folders, precedence, watchers, and environment filtering.
- `raw/2026-04-26 Windsurf Cascade Skills docs.md` - Windsurf Cascade workspace, global, enterprise, and compatibility skill paths.
- `raw/2026-04-26 Microsoft Agent Framework Agent Skills docs.md` - Microsoft Agent Framework provider model for loading and exposing skills.
- `raw/2026-04-30 Microsoft Copilot SKILL.md support roadmap.md` - Microsoft Copilot family SKILL.md support: GitHub Copilot in VS Code/Visual Studio 2026, Copilot Cowork (M365 OneDrive/SharePoint), Copilot Studio, and timeline through April 2026.
- `raw/2026-04-26 Google Cloud Vertex AI and Model Garden LLM provider source.md` - Google Cloud model hub evidence for Gemini, open models, partner models, deployment, and MLOps.
- `raw/2026-04-26 AWS Amazon Bedrock LLM provider source.md` - AWS Bedrock model hub evidence for Amazon and third-party foundation models, agents, knowledge bases, and provisioned throughput.
- `raw/2026-04-26 Azure AI Foundry Models LLM provider source.md` - Azure Foundry Models evidence for Microsoft's broad curated model catalog and serverless model deployment.
- `raw/2026-04-26 OpenAI API LLM provider source.md` - OpenAI direct API evidence for current frontier models, multimodal support, and tool capabilities.
- `raw/2026-04-26 Anthropic Claude API LLM provider source.md` - Anthropic Claude evidence for current Claude models, long context, platform availability, and agentic coding positioning.
- `raw/2026-04-26 Cohere LLM provider source.md` - Cohere evidence for Command, Embed, Rerank, Transcribe, Aya, and enterprise RAG use cases.
- `raw/2026-04-26 Mistral AI LLM provider source.md` - Mistral evidence for Studio, API/SDKs, agents, RAG, fine-tuning, and coding tooling.
- `raw/2026-04-26 xAI Grok API LLM provider source.md` - xAI evidence for Grok API models, coding/chat use cases, multimodal APIs, and server-side tools.
- `raw/2026-04-26 DeepSeek API LLM provider source.md` - DeepSeek evidence and hosting-path notes for cost-sensitive reasoning and coding provider evaluation.
- `raw/2026-04-26 OpenRouter LLM provider router source.md` - OpenRouter evidence for one-API model routing, provider fallback, routing controls, and model metadata.
- `raw/2026-04-26 Open model inference providers source.md` - Together AI, Groq, Fireworks AI, and Hugging Face evidence for open-model inference hubs.
- `raw/2026-04-26 Perplexity Sonar API LLM provider source.md` - Perplexity Sonar evidence for search-grounded, real-time web answer APIs.
- `raw/2026-04-26 Agent Skills specification evaluation and description optimization.md` - AgentSkills.io evidence for `SKILL.md` validation, trigger evals, output evals, assertions, baselines, and iteration.
- `raw/2026-04-26 OpenAI agent evaluation and trace grading docs.md` - OpenAI evidence for traces, graders, datasets, eval runs, tool-call accuracy, handoff accuracy, and grader types.
- `raw/2026-04-26 Anthropic evals for AI agents.md` - Anthropic evidence for agent eval vocabulary, grader types, capability vs regression suites, pass@k, pass^k, and eval maintenance.
- `raw/2026-04-26 LangSmith AgentEvals trajectory evaluation docs.md` - LangSmith evidence for trajectory matching, subset/superset tool-call checks, and LLM-as-judge trajectory grading.
- `raw/2026-04-26 tau-bench tool-agent reliability benchmark.md` - Benchmark evidence for multi-turn tool-agent evaluation, final-state grading, and reliability via pass^k.
- `raw/2026-04-26 MCP architecture and Agent Skills integration source.md` - MCP official evidence for host/client/server architecture, tools/resources/prompts, transports, and Agent Skills for MCP server development.
- `raw/2026-04-26 MCP security and authorization source.md` - MCP official evidence for OAuth-based authorization, consent, least privilege, sandboxing, approval, and programmatic tool-call security.
- `raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md` - OpenAI Agents SDK evidence for tools, hosted MCP, local MCP, agents-as-tools, handoffs, and orchestration patterns.
- `raw/2026-04-26 Agent orchestration frameworks source.md` - LangGraph, Microsoft Agent Framework, and CrewAI evidence for graph workflows, durable execution, state, human-in-the-loop, observability, and multi-agent orchestration.
- `raw/2026-04-26 OpenAI Agents SDK official source.md` - OpenAI official evidence for the Agents SDK as a code-first runtime for orchestration, tools, approvals, state, and agent workflow growth paths.
- `raw/2026-04-26 OpenAI Codex SDK and App Server source.md` - OpenAI official evidence for Codex SDK, Codex App Server, Codex Skills, and Codex subagents.
- `raw/2026-04-26 Claude Agent SDK source.md` - Anthropic/Claude official evidence for the Claude Agent SDK, TypeScript and Python packages, MCP integration, sessions, permissions, and filesystem skills.
- `raw/2026-04-26 OpenAI Codex Plugins docs.md` - OpenAI Codex plugin evidence for bundling skills, app integrations, MCP servers, manifests, marketplaces, and install-surface metadata.
- `raw/2026-04-30 AI Coding Plans Comparison 2026.md` - Comprehensive comparison of six Chinese coding plans and four international coding-tool subscriptions with pricing, quotas, model access, and selection guidance.
- `raw/2026-04-30 Claude Code Third-Party LLM Provider Configuration.md` - Raw synthesis of Claude Code third-party provider setup including OpenRouter, LiteLLM, Bedrock, Vertex AI, Foundry, environment variables, and VS Code integration.
- `raw/2026-04-26 Claude Code Plugins docs.md` - Claude Code plugin evidence for plugin components, marketplaces, scopes, MCP servers, caching, and distribution behavior.
- `raw/OpenAI's 5 Levels Of 'Super AI' (AGI To Outperform Human Capability).md` - Forbes article on OpenAI's five-level AGI framework: conversational, reasoners, agents, innovators, and organizations, with timeline estimates.
- `raw/LangChain vs LangGraph vs LangSmith vs LangFlow Key Differences Explained.md` - DataCamp comparison of the LangChain ecosystem: LCEL chains, tool calling, structured outputs, memory, LangGraph state graphs, LangSmith tracing, and LangFlow visual builder.
- `raw/n8n A Guide to Workflow Automation.md` - DigitalOcean guide to n8n: trigger/action/logic/code nodes, pre-built templates, self-hosting vs cloud, best practices, and comparison to Zapier.
- `raw/Deploy n8n on Cloud Run  Google Cloud Blog.md` - Google Cloud blog on deploying n8n to Cloud Run with Cloud SQL persistence, Gemini AI integration, and Google Workspace OAuth connectivity.
- `raw/Agent SDK overview.md` - Official Claude Agent SDK overview: built-in tools (Read, Write, Edit, Bash, Monitor, Glob, Grep, WebSearch, WebFetch, AskUserQuestion), filesystem configuration (skills, slash commands, memory, plugins), Client SDK vs Agent SDK comparison, and branding guidelines.
- `raw/Agent Development Kit (ADK).md` - Google ADK official site: multi-language framework (Python, TypeScript, Go, Java) for production multi-agent systems, progressive complexity from prompts to graph workflows, open model support, structured context management, and one-command Google Cloud deployment.
- `raw/Deep Dive into LLMs like ChatGPT.md` - Andrej Karpathy's 2025 video transcript: full pipeline from internet data collection through tokenization, transformer training, RLHF fine-tuning, and autoregressive inference. Best introductory resource for LLM mental models.
- `raw/OpenAI API Responses vs. Chat Completions.md` - Simon Willison's analysis of the new Responses API: server-side state management, hosted tools, reasoning preservation, and the Chat Completions vs. Responses tradeoff.
- `raw/Why we built the Responses API.md` - OpenAI developer blog: design rationale for the Responses API as a stateful, multimodal agentic loop optimized for reasoning models like GPT-5, with 40–80% better cache utilization.
- `raw/VILA-LabDive-into-Claude-Code A Systematic Analysis and Discussion of Claude Code for Designing Today's and Future AI Agent Systems.md` - arXiv paper 2604.14228: source-level architectural analysis of Claude Code v2.1.88 (~512K lines), finding 98.4% deterministic infrastructure, 7 safety layers, 5 compaction stages, 27 hook events, and 13 design principles.
