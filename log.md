---
type: log
created: 2026-04-26
updated: 2026-04-26
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/openaiskills Skills Catalog for Codex.md"
  - "raw/anthropicsskills Public repository for Agent Skills.md"
  - "raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md"
  - "raw/obrasuperpowers An agentic skills framework & software development methodology that works.md"
  - "raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md"
  - "raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md"
tags: [log, agent-skills]
---

# Log

## [2026-04-26] ingest | skill.md for AI Agents

Built a concept-organized wiki from `raw/skill.md for AI Agents.md`, with articles organized by idea rather than by source, vendor, or person.

Files created or updated:

- `index.md`
- `log.md`
- `concepts/Agent Skills.md`
- `concepts/SKILL.md Package Anatomy.md`
- `concepts/Portable Skill Core.md`
- `concepts/Vendor Adapters.md`
- `concepts/Progressive Disclosure.md`
- `concepts/Skill Authoring Workflow.md`
- `concepts/Skill Repository Architecture.md`
- `concepts/Validation and Evaluation.md`
- `concepts/Provenance and Versioning.md`
- `concepts/Discovery Conventions.md`
- `concepts/Skill Repository Tooling.md`
- `concepts/Skill Governance and Metrics.md`

Important decisions:

- Kept raw sources unchanged.
- Cited the local raw source directly in each concept article for provenance.
- Did not create source-summary or person/vendor pages, because the requested organization is concept-first.
- Recorded disagreement as differences in platform scope, metadata requirements, discovery paths, and evaluation maturity.

Follow-ups:

- Add source-summary pages only if future wiki maintenance needs a source-oriented audit trail.
- Add external URLs or page-level source notes if the raw source is expanded with full citation metadata.

## [2026-04-26] ingest | Skill ecosystem repositories and installation patterns

Processed only raw files not already represented in the prior ingest entry. The following raw files were treated as newly added for this run:

- `raw/anthropicsskills Public repository for Agent Skills.md` - last seen modified `2026-04-26T02:36:33Z`
- `raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md` - last seen modified `2026-04-26T02:46:51Z`
- `raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md` - last seen modified `2026-04-26T02:40:43Z`
- `raw/obrasuperpowers An agentic skills framework & software development methodology that works.md` - last seen modified `2026-04-26T02:43:09Z`
- `raw/openaiskills Skills Catalog for Codex.md` - last seen modified `2026-04-26T02:39:10Z`
- `raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md` - last seen modified `2026-04-26T02:38:01Z`

What changed:

- Expanded existing concept pages with evidence about workflow-oriented skills, behavior-shaping guidance, precise routing descriptions, concrete progressive-disclosure heuristics, and public-skill trust concerns.
- Added a new concept page, `concepts/Skill Distribution and Installation.md`, because installation patterns did not fit cleanly into the existing concept set.
- Updated the index so the new concept and all processed raw sources are visible from the wiki map.

Files created or updated:

- `index.md`
- `log.md`
- `concepts/Agent Skills.md`
- `concepts/Portable Skill Core.md`
- `concepts/Progressive Disclosure.md`
- `concepts/Skill Authoring Workflow.md`
- `concepts/Discovery Conventions.md`
- `concepts/Skill Repository Tooling.md`
- `concepts/Skill Governance and Metrics.md`
- `concepts/Skill Distribution and Installation.md`

Important decisions:

- Treated `raw/skill.md for AI Agents.md` as already processed because it already has a dedicated ingest entry and this run was scoped to newly added or changed raw files.
- Folded new material into existing concept pages rather than creating vendor, author, or repository profile pages.
- Treated the single-file `CLAUDE.md` source as adjacent evidence about behavior-shaping guidance, but marked it as different from a portable `SKILL.md` package.
- Marked security and quality advice from the curated catalog as ecosystem guidance rather than a universal audited standard.

Follow-ups:

- If future runs need stricter change detection, add hashes or recorded file sizes alongside timestamps in the log.
- If more sources focus on registries, signing, or supply-chain trust, consider a separate concept page for skill trust and security.

## [2026-04-26] ingest | Tools Supporting Agent Skills

Searched the web for current tools and frameworks that support `SKILL.md` or Agent Skills-style packages, then added dated raw source notes and synthesized the support landscape.

Raw source notes created:

- `raw/2026-04-26 agentskills.io Agent Skills overview and quickstart.md`
- `raw/2026-04-26 OpenAI Codex Agent Skills docs.md`
- `raw/2026-04-26 Claude Code Agent Skills docs.md`
- `raw/2026-04-26 Gemini CLI Agent Skills docs.md`
- `raw/2026-04-26 GitHub Copilot and VS Code Agent Skills docs.md`
- `raw/2026-04-26 Cursor Agent Skills support sources.md`
- `raw/2026-04-26 OpenCode Agent Skills docs.md`
- `raw/2026-04-26 OpenClaw Skills docs.md`
- `raw/2026-04-26 Windsurf Cascade Skills docs.md`
- `raw/2026-04-26 Microsoft Agent Framework Agent Skills docs.md`

Generated pages created or updated:

- `concepts/Tools Supporting Agent Skills.md`
- `concepts/Discovery Conventions.md`
- `concepts/Skill Distribution and Installation.md`
- `index.md`
- `log.md`

Important decisions:

- Treated OpenAI Codex, Claude Code, Gemini CLI, GitHub Copilot/VS Code, OpenCode, OpenClaw, Windsurf, and Microsoft Agent Framework docs as primary support evidence.
- Treated Cursor support as primary-confirmed from the official Cursor 2.4 changelog, but kept path details moderate-confidence because the current Cursor docs page did not expose readable text during extraction.
- Categorized Microsoft Agent Framework separately from coding-agent clients because it consumes skills through a provider/tool pattern inside an agent framework.
- Stored source notes as concise raw web captures rather than full page dumps, to preserve provenance without making the raw folder noisy.

Follow-ups:

- Recheck Cursor's current docs page with a browser or alternate fetch path to confirm discovery paths and precedence.
- Consider adding a dedicated page for cross-agent compatibility paths if `.agents/skills/` continues to appear in more primary sources.

## [2026-04-26] ingest | LLM providers for AI tools

Searched current official/provider documentation for reputable and popular LLM providers that could power AI tools, starting with Google Cloud, AWS, and Azure, then expanding to direct frontier providers and inference hubs.

Raw source notes created:

- `raw/2026-04-26 Google Cloud Vertex AI and Model Garden LLM provider source.md`
- `raw/2026-04-26 AWS Amazon Bedrock LLM provider source.md`
- `raw/2026-04-26 Azure AI Foundry Models LLM provider source.md`
- `raw/2026-04-26 OpenAI API LLM provider source.md`
- `raw/2026-04-26 Anthropic Claude API LLM provider source.md`
- `raw/2026-04-26 Cohere LLM provider source.md`
- `raw/2026-04-26 Mistral AI LLM provider source.md`
- `raw/2026-04-26 xAI Grok API LLM provider source.md`
- `raw/2026-04-26 DeepSeek API LLM provider source.md`
- `raw/2026-04-26 Open model inference providers source.md`
- `raw/2026-04-26 Perplexity Sonar API LLM provider source.md`

Generated pages created or updated:

- `concepts/LLM Provider Selection for AI Tools.md`
- `index.md`
- `log.md`

Important decisions:

- Treated Google Cloud Vertex AI / Model Garden, AWS Amazon Bedrock, and Azure AI Foundry Models as the first-pass reputable enterprise model hubs.
- Treated OpenAI, Anthropic, Cohere, Mistral AI, xAI, and DeepSeek as direct or model-origin providers worth separate evaluation.
- Grouped Together AI, Groq, Fireworks AI, and Hugging Face Inference Providers into one open-model inference-hub source because the current decision point is category-level provider exploration.
- Treated Perplexity Sonar as a specialized search-grounded provider rather than a default general-purpose LLM provider.

Follow-ups:

- Add model-level benchmark pages once target AI tools and evaluation tasks are known.
- Confirm pricing, availability, data retention, and regional support immediately before implementation because these provider catalogs change frequently.

## [2026-04-26] ingest | OpenRouter LLM provider router

Added OpenRouter as a provider-routing layer for AI tool provider selection.

Raw source note created:

- `raw/2026-04-26 OpenRouter LLM provider router source.md`

Generated pages updated:

- `concepts/LLM Provider Selection for AI Tools.md`
- `index.md`
- `log.md`

Important decisions:

- Categorized OpenRouter as a routing/API aggregation layer rather than a model-origin provider.
- Added it to the third-priority exploration tier alongside open-model inference hubs because its main value is provider comparison, fallback routing, and price/latency/throughput routing.
- Highlighted route-level privacy and data-retention checks as the main caution for sensitive workloads.

Follow-ups:

- If provider benchmarking becomes a recurring workflow, create a dedicated OpenRouter benchmark page with candidate model slugs, provider preferences, and routing policies.

## [2026-04-26] ingest | Validation and Evaluation of agent skills

Reinforced the wiki's Validation and Evaluation material with current sources on Agent Skills validation, trigger evaluation, output evaluation, trace grading, trajectory evaluation, and agent reliability metrics.

Raw source notes created:

- `raw/2026-04-26 Agent Skills specification evaluation and description optimization.md`
- `raw/2026-04-26 OpenAI agent evaluation and trace grading docs.md`
- `raw/2026-04-26 Anthropic evals for AI agents.md`
- `raw/2026-04-26 LangSmith AgentEvals trajectory evaluation docs.md`
- `raw/2026-04-26 tau-bench tool-agent reliability benchmark.md`

Generated pages updated:

- `concepts/Validation and Evaluation.md`
- `index.md`
- `log.md`

Important decisions:

- Treated AgentSkills.io as primary skill-specific evidence for `SKILL.md` validation, description trigger testing, and output-quality eval loops.
- Treated OpenAI, Anthropic, and LangSmith documentation as agent-evaluation evidence to adapt to skill evaluation, especially traces, trajectories, graders, and human calibration.
- Treated tau-bench as benchmark evidence for multi-turn tool-agent reliability and final-state grading rather than as a direct `SKILL.md` conformance test.
- Added trigger evaluation as its own layer because a valid skill that never loads, or over-triggers on near misses, is behaviorally broken.

Follow-ups:

- Build an actual `evals/evals.json` template for local skill packages.
- Add a portable eval-harness page if the wiki later tracks concrete runners for Codex, Claude Code, Gemini CLI, and Copilot.

## [2026-04-26] ingest | MCP tools and agent orchestration around Agent Skills

Brushed up the wiki's missing material on MCP/tool-integration architecture and agent frameworks/orchestration, while keeping the focus on how these layers relate to Agent Skills.

Raw source notes created:

- `raw/2026-04-26 MCP architecture and Agent Skills integration source.md`
- `raw/2026-04-26 MCP security and authorization source.md`
- `raw/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md`
- `raw/2026-04-26 Agent orchestration frameworks source.md`

Generated pages created:

- `concepts/MCP and Tool-Integration Architecture.md`
- `concepts/Agent Frameworks and Orchestration.md`

Generated pages updated:

- `concepts/Agent Skills.md`
- `concepts/Skill Authoring Workflow.md`
- `concepts/Tools Supporting Agent Skills.md`
- `index.md`
- `log.md`

Important decisions:

- Treated MCP as the action/context protocol layer around skills: tools for executable actions, resources for context, prompts for user-controlled templates, and Agent Skills for reusable agent operating procedures.
- Used the official MCP "Build with Agent Skills" page as the strongest bridge evidence because it explicitly describes skills for MCP server design, deployment choices, tool patterns, auth, widgets, and packaging.
- Treated OpenAI Agents SDK, LangGraph, Microsoft Agent Framework, and CrewAI as orchestration/framework evidence, but kept detailed framework comparison conservative.
- Framed the key design question as runtime-layer ownership: knowledge and procedure belong in skills, deterministic execution belongs in code/tools, external systems belong in MCP/tools, and explicit control flow belongs in frameworks.

Follow-ups:

- Create an `Agent Security and Tool Permissions` concept page connecting MCP security, skill governance, sandboxing, supply-chain trust, and approval boundaries.
- Add framework-specific pages only if the wiki needs concrete implementation guidance for LangGraph, OpenAI Agents SDK, Microsoft Agent Framework, or CrewAI.
- Build a decision table for choosing between portable skills, project instruction files, function tools, scripts, MCP servers, subagents, handoffs, and graph workflows.

## [2026-04-26] ingest | Agent SDKs and Codex automation around Agent Skills

Added current SDK and app-server surfaces requested by the user, centered on their relationship to Agent Skills rather than as standalone API tutorials.

Raw source notes created:

- `raw/2026-04-26 OpenAI Agents SDK official source.md`
- `raw/2026-04-26 OpenAI Codex SDK and App Server source.md`
- `raw/2026-04-26 Claude Agent SDK source.md`

Generated pages created:

- `concepts/Agent SDKs and Codex Automation.md`

Generated pages updated:

- `concepts/Agent Skills.md`
- `concepts/MCP and Tool-Integration Architecture.md`
- `concepts/Agent Frameworks and Orchestration.md`
- `concepts/Tools Supporting Agent Skills.md`
- `index.md`
- `log.md`

Important decisions:

- Treated OpenAI Agents SDK as a general code-first agent runtime for applications that own orchestration, tools, approvals, state, and traces.
- Treated Codex SDK as the programmatic automation surface for local Codex agents, and Codex App Server as the deeper Codex client protocol for auth, conversation history, approvals, and streamed events.
- Treated Anthropic's current "Claude Agent SDK" naming as primary, while noting that older Claude Code SDK URLs redirect to the Agent SDK docs.
- Kept the main synthesis around runtime-layer ownership: skills package reusable operating knowledge; SDKs and app servers execute, embed, stream, approve, and resume agent work.
- Did not install an OpenAI docs MCP server locally; used official web docs as source material for the knowledge base update.

Follow-ups:

- Compare OpenAI Agents SDK agents-as-tools, Codex subagents, and Claude Agent SDK subagents in a dedicated page if multi-agent implementation becomes a priority.
- Add code-pattern pages only when the wiki needs implementation-ready examples for a specific SDK.
- Track maturity and stability of Codex SDK Python support and Codex App Server WebSocket transport.

## [2026-04-26] ingest | Plugin-based agent extensions

Expanded the wiki's thin plugin coverage into a dedicated concept page and cross-linked it from the adjacent Agent Skills, MCP/tooling, distribution, and tool-support pages.

Raw source notes created:

- `raw/2026-04-26 OpenAI Codex Plugins docs.md`
- `raw/2026-04-26 Claude Code Plugins docs.md`

Generated pages created:

- `concepts/Plugin-Based Agent Extensions.md`

Generated pages updated:

- `concepts/Agent Skills.md`
- `concepts/Skill Distribution and Installation.md`
- `concepts/MCP and Tool-Integration Architecture.md`
- `concepts/Tools Supporting Agent Skills.md`
- `index.md`
- `log.md`

Important decisions:

- Treated plugins as the packaging and distribution layer above local skills, especially when a workflow needs app integrations, MCP server configuration, assets, marketplace metadata, authentication expectations, or team rollout.
- Kept the boundary explicit: skills package procedure, MCP exposes external tool/context surfaces, and plugins bundle installable capabilities that may contain both.
- Added governance framing because plugins can include more review surface than a standalone skill: manifests, app connectors, MCP servers, hooks, scripts, assets, persistent state, publisher metadata, and update paths.

Follow-ups:

- Compare Codex and Claude Code plugin manifests if cross-vendor plugin authoring becomes important.
- Track Codex public plugin directory publishing and self-serve plugin management when they become available.
- Add plugin-level evaluation guidance if the wiki later needs to test full extension bundles, not only `SKILL.md` behavior.
