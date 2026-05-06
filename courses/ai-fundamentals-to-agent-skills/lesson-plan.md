---
type: lesson-plan
created: 2026-05-01
updated: 2026-05-01
status: draft
tags: [lesson-plan, curriculum, agent-skills]
---

# AI Fundamentals to Agent Skills: A Lesson Plan

## Guiding Principles

**Why this order:** Each module builds on prerequisites from earlier modules. Learners should never encounter a concept without the foundation to understand it. The plan moves from *what* (concepts) → *how* (usage) → *build* (creation) → *scale* (production).

**Target outcome:** By the end, learners can author, test, and publish a reusable Agent Skill that integrates with MCP servers, uses tools correctly, and passes evaluation checks.

**Time estimate:** ~40-60 hours of focused study and practice, depending on prior programming experience.

---

## Phase 1: AI Foundations (Modules 1-4)

> **Goal:** Understand what AI/ML is, how modern language models work, and why they behave the way they do. No coding yet — build correct mental models first.

### Module 1: What Is Machine Learning?

**Why start here:** Most beginners conflate AI, ML, deep learning, and LLMs. Clarifying the hierarchy prevents confusion later.

**Topics:**
- Traditional programming vs. machine learning: the paradigm shift from "write rules" to "learn patterns from data"
- Supervised, unsupervised, and reinforcement learning — with one concrete example each
- Why neural networks: from perceptron → multi-layer → deep learning
- The role of compute, data, and algorithms in the modern AI boom
- Key terms: model, training, inference, parameters, weights, loss function

**Hands-on:** Nothing yet. Read and reflect. Draw the hierarchy: AI ⊃ ML ⊃ Deep Learning ⊃ Transformers ⊃ LLMs.

**Checkpoint question:** Explain the difference between training and inference to someone who has never coded.

### Module 2: How Large Language Models Work

**Why here:** You can't use LLMs effectively if you think they "know" things or "reason" like humans.

**Topics:**
- Tokens and tokenization: how text becomes numbers (Byte Pair Encoding intuition)
- The transformer architecture at a high level: attention mechanism, why it matters, context window
- Pre-training: next-token prediction on massive text corpora — what the model actually learns
- Fine-tuning vs. pre-training: why fine-tuning costs less and changes behavior
- RLHF (Reinforcement Learning from Human Feedback): why models are "helpful" and not just autocomplete
- Key limitations: hallucination, knowledge cutoff, no persistent memory by default, no true reasoning (pattern matching at scale)

**Hands-on:** Use a free LLM (any provider). Ask it the same question 5 times and compare outputs. Observe stochasticity.

**Checkpoint question:** Why does an LLM sometimes give different answers to the same prompt? What does "temperature" control?

### Module 3: Prompt Engineering Fundamentals

**Why here:** Before touching APIs or code, learners should know how to communicate effectively with LLMs through natural language.

**Topics:**
- Zero-shot, few-shot, and chain-of-thought prompting — when to use each
- System prompts vs. user prompts vs. assistant messages: the conversation structure
- Temperature, top_p, max_tokens: the generation parameters that matter
- Prompt injection: what it is, why it's a security concern, basic mitigation
- Structured outputs: asking for JSON, XML, or specific formats
- Common anti-patterns: overly vague instructions, contradictory constraints, embedding false premises

**Hands-on:** Write prompts that accomplish: (a) summarization, (b) code generation, (c) structured data extraction. Compare quality with and without few-shot examples.

**Checkpoint question:** Given a prompt that produces bad output, identify at least 3 specific problems and fix them.

### Module 4: The LLM Landscape — Models and Providers

**Why here:** Learners need to know which models exist, who makes them, and how to access them before building anything.

**Topics:**
- Frontier models: Claude (Anthropic), GPT (OpenAI), Gemini (Google), Llama (Meta), others
- Open vs. closed models: tradeoffs in cost, control, capability, and compliance
- Model capabilities comparison: reasoning, coding, multimodal, context length, speed, cost
- LLM providers and aggregators: direct APIs vs. routing layers (OpenRouter, LiteLLM)
- How to read a model card: what the provider tells you (and what they don't)
- *Reference existing wiki content:* [[concepts/LLM Provider Selection for AI Tools]]

**Hands-on:** Sign up for at least one LLM provider API. Get an API key. Make a simple curl or Python request.

**Checkpoint question:** You need to build a coding assistant. Which model would you pick and why? What tradeoffs are you accepting?

---

## Phase 2: Building with LLMs (Modules 5-8)

> **Goal:** Move from chatting with LLMs in a browser to integrating them into code and applications.

### Module 5: LLM APIs and SDKs

**Why here:** This is the bridge from "I can prompt" to "I can build." Everything after this depends on API literacy.

**Topics:**
- REST API fundamentals: endpoints, headers, authentication, request/response bodies
- The Chat Completions API pattern: messages array, roles, system prompt, streaming
- OpenAI-compatible API standard: why most providers follow it
- Python SDK usage (`openai`, `anthropic`): installation, client setup, making calls
- Streaming responses vs. blocking: when and why to use each
- Error handling: rate limits, context length exceeded, bad requests
- Prompt caching: how it works, why it matters for cost
- *Reference:* [[concepts/Claude Code Third-Party Provider Configuration]]

**Hands-on:** Build a Python script that: (1) takes user input from stdin, (2) sends it to an LLM API, (3) streams the response back. Add error handling for rate limits.

**Checkpoint question:** Your API call returns a 429 error. What happened and how should your code respond?

### Module 6: Tool Use and Function Calling

**Why here:** Tools are the mechanism that turns LLMs from text generators into agents. This is the single most important concept for Agent Skills.

**Topics:**
- What are tools: the LLM can request to call external functions instead of generating text
- Tool definition schema: name, description, parameters (JSON Schema)
- The tool-use loop: send tools → LLM chooses one → execute → send result back → repeat
- Multi-tool selection: when models call multiple tools in one turn
- Parallel tool calls: why and when tools can run concurrently
- Tool result injection: how the LLM sees tool outputs in context
- Common tool categories: file operations, web search, code execution, database queries, API calls
- Safety: tool approval policies, sandboxing, least privilege
- *Reference:* [[concepts/MCP and Tool-Integration Architecture]]

**Hands-on:** Using an SDK that supports tool calling, define a tool (e.g., "get_weather") and build a loop that: sends the tool definition, lets the LLM call it, executes the function, returns the result, and continues until the LLM gives a final text response.

**Checkpoint question:** Why can't you just put tool results directly in the system prompt? What's wrong with that approach?

### Module 7: MCP (Model Context Protocol)

**Why here:** MCP is the emerging standard for tool integration. Understanding it is essential before building skills that interact with external systems.

**Topics:**
- MCP architecture: hosts, clients, servers — who does what
- Tools, resources, and prompts: the three MCP primitives
- Transport mechanisms: stdio vs. HTTP/SSE
- MCP server as a tool provider: how agents discover and use MCP tools
- Authorization and consent: OAuth flow, user approval, least privilege
- Building a simple MCP server: the minimal implementation
- *Reference:* [[concepts/MCP and Tool-Integration Architecture]]

**Hands-on:** Build a minimal MCP server in Python or TypeScript that exposes one tool (e.g., read a file, query a database, fetch a URL). Test it with an MCP-compatible client.

**Checkpoint question:** An MCP server exposes a tool that can delete files. What safeguards should be in place?

### Module 8: Conversations, Memory, and Context Management

**Why here:** Real applications need to maintain state across turns. This module covers the mechanisms that make multi-turn interactions work.

**Topics:**
- Conversation history: passing message arrays, context window limits
- Context window management: truncation strategies, summarization, sliding windows
- Types of memory: conversation-level, session-level, persistent (file/database)
- Context compaction: how to compress long conversations without losing key information
- State machines for conversations: tracking where the user is in a workflow
- *Reference:* [[concepts/Google Agent Development Kit (ADK)]] — context management patterns

**Hands-on:** Extend the Module 5 script to maintain conversation history across multiple turns. Implement a simple truncation strategy when context gets too long.

**Checkpoint question:** Your conversation has exceeded the context window. What are three strategies to handle this, and when would you use each?

---

## Phase 3: Agents and Skills (Modules 9-12)

> **Goal:** Understand agent architectures, then learn the Agent Skills system — the core outcome of this curriculum.

### Module 9: What Is an AI Agent?

**Why here:** "Agent" is an overloaded term. This module pins down the precise meaning and distinguishes agents from simple LLM calls.

**Topics:**
- Agent = LLM + tools + loop + goals: the core formula
- ReAct pattern: Reason + Act — the foundational agent loop
- Agent architectures: single-agent, multi-agent with handoffs, hierarchical, swarm
- Planning and reflection: how agents break down tasks and self-correct
- Human-in-the-loop: approval gates, review points, escalation paths
- Agent limitations and failure modes: infinite loops, tool hallucination, goal drift
- *Reference:* [[concepts/OpenAI AGI Progression Framework]] — agents as level 3

**Hands-on:** Design (on paper) an agent that can: receive a bug report, find the relevant code, propose a fix, and run tests. Identify each tool it needs and the decision points.

**Checkpoint question:** What distinguishes an "agent" from a regular LLM API call? List the minimum components.

### Module 10: Agent Skills — Concepts and Architecture

**Why here:** This is the core subject. All prior modules prepare learners to understand what skills are and why they're structured the way they are.

**Topics:**
- What is a Skill: a reusable operating procedure for agents — task helpers, workflow guides, guardrails
- SKILL.md file anatomy: the core metadata file, supporting folders (scripts/, references/, assets/)
- Portable Skill Core: name, description, and why precise wording matters for discovery
- Progressive disclosure: loading metadata → instructions → resources in layers, size heuristics
- Discovery conventions: package-level SKILL.md, site-level skill.md, tool-specific paths
- Vendor adapters: platform-specific metadata outside the canonical package
- *Reference existing wiki content:* [[concepts/Agent Skills]], [[concepts/SKILL.md Package Anatomy]], [[concepts/Portable Skill Core]], [[concepts/Progressive Disclosure]], [[concepts/Discovery Conventions]], [[concepts/Vendor Adapters]]

**Hands-on:** Read 3 existing SKILL.md files from the wiki's raw sources or public repositories. Identify: name, description, trigger conditions, and what resources it loads.

**Checkpoint question:** Why does a skill use progressive disclosure instead of putting everything in one file? What happens if you do?

### Module 11: Authoring Your First Skill

**Why here:** Theory is insufficient. Learners need to create a skill from scratch to internalize the structure.

**Topics:**
- Identifying a recurring task worth skill-ifying
- Writing effective skill descriptions: precision, actionability, scope boundaries
- Structuring the SKILL.md: required fields, optional fields, platform-specific adapters
- Creating supporting resources: reference docs, scripts, example outputs
- Testing a skill locally: does it trigger correctly? Does it produce the expected behavior?
- Common authoring mistakes: vague triggers, oversized instructions, missing examples
- *Reference existing wiki content:* [[concepts/Skill Authoring Workflow]]

**Hands-on:** Author a complete skill package for a task you perform regularly (e.g., "write a PR description from a git diff", "review code for security issues", "generate test cases from a function signature"). Include SKILL.md, at least one reference file, and test it with an agent.

**Checkpoint question:** Your skill triggers when it shouldn't. What in the SKILL.md controls triggering, and how would you fix it?

### Module 12: Skill Distribution, Installation, and Governance

**Why here:** Skills are only valuable when others can find and use them. This covers the lifecycle beyond authoring.

**Topics:**
- Distribution channels: catalogs, plugin marketplaces, git repositories, local folders
- Installation flows: how users discover, install, and update skills
- Plugin bundles: packaging skills with app integrations, MCP servers, and metadata
- Versioning and provenance: tracking source, release records, sync metadata
- Governance: ownership, licensing, quality metrics, trust signals
- Repository architecture: organizing skills, indexes, adapters, and metadata at scale
- *Reference existing wiki content:* [[concepts/Skill Distribution and Installation]], [[concepts/Provenance and Versioning]], [[concepts/Skill Repository Architecture]], [[concepts/Plugin-Based Agent Extensions]], [[concepts/Skill Governance and Metrics]], [[concepts/Skill Repository Tooling]]

**Hands-on:** Publish your Module 11 skill to a git repository. Write a README that explains what it does, how to install it, and when to use it.

**Checkpoint question:** A user reports your skill broke after an update. What provenance information helps you diagnose the issue?

---

## Phase 4: Advanced Topics (Modules 13-16)

> **Goal:** Production-grade agent development: evaluation, orchestration, frameworks, and real-world deployment.

### Module 13: Validation and Evaluation

**Why here:** Without evaluation, you can't know if your skill or agent actually works. This is the quality gate.

**Topics:**
- Structural validation: is the SKILL.md well-formed? Does it parse?
- Trigger evaluation: does the skill activate on the right inputs and stay silent on wrong ones?
- Output evaluation: does the skill produce correct, safe, complete outputs?
- Traces and grading: recording agent behavior and scoring it
- Grader types: LLM-as-judge, rule-based, trajectory matching
- Metrics: pass@k, pass^k, tool-call accuracy, handoff accuracy
- Benchmark suites: tau-bench, agent evals, regression testing
- *Reference existing wiki content:* [[concepts/Validation and Evaluation]]

**Hands-on:** Write 5 test cases for your Module 11 skill: 3 that should trigger it, 2 that should not. For each triggering case, define what a "pass" looks like.

**Checkpoint question:** Your skill passes all manual tests but fails 30% of automated evals. What could explain this gap?

### Module 14: Agent Orchestration and Multi-Agent Systems

**Why here:** Complex tasks require multiple agents working together. This module covers how to compose agents, tools, and skills into workflows.

**Topics:**
- When to use orchestration: single agent vs. multi-agent decision criteria
- Handoff patterns: agent A delegates to agent B with context transfer
- Graph-based workflows: state machines, conditional routing, parallel branches
- State management across agents: shared context, isolation, conflict resolution
- Human review gates: when and where to insert human approval
- Framework comparison: LangGraph, OpenAI Agents SDK, Google ADK, CrewAI
- *Reference existing wiki content:* [[concepts/Agent Frameworks and Orchestration]], [[concepts/Agent SDKs and Codex Automation]], [[concepts/LangChain Ecosystem Components]], [[concepts/Google Agent Development Kit (ADK)]]

**Hands-on:** Design a multi-agent workflow for code review: one agent finds changes, another reviews for security, a third checks style. Define handoffs and shared state.

**Checkpoint question:** When should you use a multi-agent approach instead of a single agent with more tools? What's the cost?

### Module 15: Agent SDKs and Runtime Surfaces

**Why here:** SDKs are how you deploy agents beyond interactive CLI sessions. Understanding runtime surfaces enables production deployment.

**Topics:**
- OpenAI Agents SDK: tools, hosted MCP, handoffs, approvals, state management
- Claude Agent SDK: TypeScript/Python packages, MCP integration, sessions, permissions
- Codex SDK and App Server: skills, subagents, deployment model
- Client SDK vs. Agent SDK: when to use each
- Building a deployable agent: packaging, configuration, environment setup
- *Reference existing wiki content:* [[concepts/Agent SDKs and Codex Automation]]

**Hands-on:** Using either the OpenAI Agents SDK or Claude Agent SDK, build a simple agent that uses one custom tool and one skill. Run it programmatically (not interactively).

**Checkpoint question:** What's the difference between running an agent interactively in a CLI vs. programmatically via an SDK? What changes?

### Module 16: Production Deployment and Operations

**Why here:** The final module covers what it takes to run agents reliably in production — the gap between "works on my machine" and "works for users."

**Topics:**
- Deployment options: cloud functions, containers, serverless, self-hosted
- Persistence: state storage, session management, conversation history
- Monitoring and observability: logging, tracing, alerting on agent behavior
- Cost management: token usage optimization, caching, model selection per task
- Security in production: secrets management, tool approval, sandboxing, audit trails
- Workflow automation platforms: n8n as an alternative for non-code agent orchestration
- *Reference existing wiki content:* [[concepts/n8n Workflow Automation]]

**Hands-on:** Deploy your Module 15 agent to a cloud platform (Cloud Run, AWS Lambda, or similar). Set up basic logging and cost tracking.

**Checkpoint question:** Your agent's cost per request doubled overnight. What are the most likely causes and how do you investigate?

---

## Appendix: Prerequisites and Setup

### Required Background
- Basic programming ability (Python preferred for most hands-on exercises)
- Comfort with command-line basics (cd, ls, git)
- No prior AI/ML experience required

### Recommended Tool Setup
- Python 3.10+ with pip
- Node.js 18+ (for TypeScript SDK exercises)
- A git account (GitHub/GitLab)
- API keys from at least one LLM provider
- VS Code or equivalent editor

### Mapping to Existing Wiki Content

| Module | Wiki Concept Articles |
|--------|----------------------|
| 4 | LLM Provider Selection for AI Tools |
| 5 | Claude Code Third-Party Provider Configuration |
| 6-7 | MCP and Tool-Integration Architecture |
| 8 | Google Agent Development Kit (ADK) |
| 9 | OpenAI AGI Progression Framework |
| 10 | Agent Skills, SKILL.md Package Anatomy, Portable Skill Core, Progressive Disclosure, Discovery Conventions, Vendor Adapters |
| 11 | Skill Authoring Workflow |
| 12 | Skill Distribution and Installation, Provenance and Versioning, Skill Repository Architecture, Plugin-Based Agent Extensions, Skill Governance and Metrics, Skill Repository Tooling |
| 13 | Validation and Evaluation |
| 14 | Agent Frameworks and Orchestration, Agent SDKs and Codex Automation, LangChain Ecosystem Components, Google Agent Development Kit (ADK) |
| 15 | Agent SDKs and Codex Automation |
| 16 | n8n Workflow Automation |

---

## Suggested Learning Pathways

### Pathway A: Skill Author (focus on building skills)
Modules 1-3 → 5-6 → 10-13 → Done (~25-35 hours)

### Pathway B: Agent Developer (full stack)
All 16 modules (~40-60 hours)

### Pathway C: Quick Start (already has programming + AI basics)
Modules 6-7 → 10-15 (~20-30 hours)
