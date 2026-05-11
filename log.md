---
type: log
created: 2026-04-26
updated: 2026-05-11
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/openaiskills Skills Catalog for Codex.md"
  - "raw/anthropicsskills Public repository for Agent Skills.md"
  - "raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md"
  - "raw/obrasuperpowers An agentic skills framework & software development methodology that works.md"
  - "raw/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md"
  - "raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md"
  - "raw/Equipping agents for the real world with Agent Skills.md"
  - "raw/Agent Skills Overview.md"
  - "raw/Agent Skills.md"
  - "raw/Introduction to Claude Skills.md"
  - "raw/Indirect Prompt Injection Attacks Hidden AI Risks.md"
  - "raw/Snyk Finds Prompt Injection in 36%, 1467 Malicious Payloads in a ToxicSkills Study of Agent Skills Supply Chain Compromise.md"
  - "raw/Meta-Meta-Prompting The Secret to Making AI Agents Work.md"
tags: [log, agent-skills, agentic-engineering]
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

## [2026-04-30] ingest | Claude Code Third-Party Provider Configuration

Answered user question about using non-Anthropic LLM APIs with Claude Code in VS Code, then searched the web and created a raw source note and concept page.

Raw source note created:

- `raw/2026-04-30 Claude Code Third-Party LLM Provider Configuration.md` - Synthesis of OpenRouter integration, LiteLLM gateway setup, cloud provider deployments, environment variables, model configuration, and VS Code integration.

Generated pages created:

- `concepts/Claude Code Third-Party Provider Configuration.md`

Generated pages updated:

- `index.md`

Important decisions:

- Categorized third-party provider configuration as a separate concept from the broader LLM provider landscape because it covers Claude Code-specific environment variables, gateway requirements, and VS Code extension behavior.
- Removed a broken frontmatter citation (`raw/2026-04-26 LLM gateway configuration - Claude Code Docs.md`) that referenced a non-existent raw file.

Follow-ups:

- Consider adding a raw source note from the official Claude Code LLM Gateway docs page for more complete provenance.

## [2026-04-30] ingest | AI Coding Plans

Searched the web for AI coding plan offerings across Chinese model-provider plans (Alibaba 百炼, BytePlus ModelArk, Kimi Code, Zhipu GLM, MiniMax, Infini) and international coding-tool subscriptions (Copilot, Cursor, Claude Code, Kilo Code, Qoder, Augment Code, Devin, Replit, Roo Code, Cline). Created raw comparison and concept synthesis pages.

Raw source note created:

- `raw/2026-04-30 AI Coding Plans Comparison 2026.md` - Comprehensive comparison of 6 Chinese coding plans and 10+ international coding-tool subscriptions with pricing, quotas, model access, selection guidance, and market trends.

Generated pages created:

- `concepts/AI Coding Plans.md`

Generated pages updated:

- `index.md`

Important decisions:

- Separated Chinese model-provider plans (fixed-quota API access) from international coding-tool subscriptions (bundled IDE/agent experience) as two complementary layers.
- Documented Roo Code's May 15, 2026 sunsetting announcement as historical note rather than active recommendation.
- Added five distinct pricing model categories (flat subscription, fixed-quota, credit-based, usage-based, free+BYOK) with strength/weakness analysis.

Follow-ups:

- Track usage-based billing migration for GitHub Copilot and Qoder (June 1, 2026) for accuracy.
- Monitor if new coding plans emerge from other providers.

## [2026-04-30] lint | Full wiki health check

Ran a comprehensive lint pass across all 20 concept pages, raw sources, index.md, and log.md.

Issues found and fixed:

1. **Critical**: Removed broken frontmatter citation (`raw/2026-04-26 LLM gateway configuration - Claude Code Docs.md`) from `concepts/Claude Code Third-Party Provider Configuration.md` — the referenced raw file did not exist.
2. **Medium**: Added two log entries for the 4 unlogged files created on 2026-04-30 (third-party provider config and coding plans).
3. **Medium**: Added `## Key Points` sections to `concepts/Claude Code Third-Party Provider Configuration.md` and `concepts/AI Coding Plans.md`.
4. **Low**: Deduplicated the `.agents/skills/` open question that appeared in both `Discovery Conventions.md` and `Tools Supporting Agent Skills.md` — kept it in the tool comparison page only.

No broken wikilinks detected. All index entries verified against disk. All concept pages have frontmatter with type/created/updated fields. No duplicate pages requiring consolidation.

## [2026-04-30] research | Microsoft Copilot SKILL.md support

Answered user question about Microsoft Copilot SKILL.md support, searched web for Copilot Cowork, Copilot Studio, and VS Code 2026 skill details.

Raw source note created:

- `raw/2026-04-30 Microsoft Copilot SKILL.md support roadmap.md` - Microsoft Copilot family SKILL.md coverage: GitHub Copilot in VS Code/Visual Studio 2026, Copilot Cowork (M365 OneDrive/SharePoint), Copilot Studio, and timeline through April 2026.

Generated pages updated:

- `concepts/Tools Supporting Agent Skills.md` — Added Copilot Cowork (M365) and Copilot Studio rows to support matrix; updated patterns to note SKILL.md expansion beyond coding tools into productivity agents; added open questions on Cowork governance and cross-product skill portability.
- `index.md` — Added new raw source to frontmatter and source list; updated Tools Supporting Agent Skills description to include Copilot Cowork and Copilot Studio.

Important decisions:

- Separated Copilot Cowork (productivity agent, M365) from GitHub Copilot (coding agent, dev tools) in the support matrix because they serve different user contexts and store skills in different locations.
- Treated Copilot Studio as a distinct business-process agent platform rather than a coding tool.
- Kept Microsoft Agent Framework in its existing row since it is a framework consumer, not a Copilot product.

Follow-ups:

- If Copilot Cowork gains developer-oriented features, revisit whether dev SKILL.md packages can port between GitHub Copilot and Cowork.
- Monitor whether Copilot Cowork skill governance (versioning, conflict resolution) becomes documented.

## [2026-05-01] ingest | Claude Agent SDK overview and Google ADK

Processed two newly added raw articles covering the Claude Agent SDK official overview and Google's Agent Development Kit.

Raw source notes processed:

- `raw/Agent SDK overview.md` - Official Claude Agent SDK documentation covering built-in tools, filesystem configuration, Client SDK vs Agent SDK comparison, and branding guidelines.
- `raw/Agent Development Kit (ADK).md` - Google ADK official site covering multi-language framework capabilities, progressive complexity, context management, evaluation, and deployment options.

Generated pages created:

- `concepts/Google Agent Development Kit (ADK).md` - Covers ADK's multi-language support (Python, TypeScript, Go, Java), progressive complexity model, open model support, structured context management, evaluation framework, and Google Cloud deployment.

Generated pages updated:

- `concepts/Agent SDKs and Codex Automation.md` — Added `raw/Agent SDK overview.md` to frontmatter sources.
- `index.md` — Added two new raw sources to frontmatter; added Google ADK concept link and raw source descriptions.
- `log.md`

Important decisions:

- Updated the existing Agent SDKs concept page rather than creating a new one for the Claude Agent SDK overview, since the SDK was already covered and the new raw source provides supplementary official documentation details.
- Created a dedicated concept page for Google ADK as a distinct multi-agent framework, cross-linked to the existing orchestration and validation concept pages.

## [2026-05-01] ingest | LangChain ecosystem and n8n workflow automation

Processed three newly added raw articles covering LLM application frameworks and workflow automation platforms.

Raw source notes processed:

- `raw/LangChain vs LangGraph vs LangSmith vs LangFlow Key Differences Explained.md` - DataCamp article comparing the four LangChain ecosystem components with code examples for LCEL, structured outputs, tool calling, and memory.
- `raw/n8n A Guide to Workflow Automation.md` - DigitalOcean guide covering n8n's node-based workflow architecture, deployment options, best practices, and comparison to Zapier.
- `raw/Deploy n8n on Cloud Run  Google Cloud Blog.md` - Google Cloud blog on serverless n8n deployment with Cloud SQL persistence and Gemini AI integration.

Generated pages created:

- `concepts/LangChain Ecosystem Components.md` - Synthesizes LangChain (LCEL foundation), LangGraph (graph orchestration), LangSmith (tracing/evaluation), and LangFlow (visual builder) with a decision heuristic and historical timeline. Cross-linked to existing orchestration and validation concept pages.
- `concepts/n8n Workflow Automation.md` - Covers n8n's core components (triggers, actions, logic, code nodes), deployment options (Cloud, self-hosted, Cloud Run, DigitalOcean), AI/LLM workflow capabilities, best practices, and positioning relative to Zapier and code-based frameworks.

Generated pages updated:

- `index.md` — Added three new raw sources to frontmatter; added two concept article links and raw source descriptions.
- `log.md`

Important decisions:

- Created a single LangChain ecosystem page rather than separate pages for each component because the source article's core value is the comparative framework showing how the four pieces fit together.
- Combined both n8n articles into one concept page because they cover complementary aspects (architecture/guide vs. cloud deployment) of the same tool.
- Positioned n8n as a visual workflow automation layer distinct from code-based agent frameworks (LangGraph, Microsoft Agent Framework) while noting overlapping AI orchestration use cases.

## [2026-05-01] ingest | OpenAI AGI Progression Framework

Processed the remaining uningested raw article from the 2026-04-30 batch.

Raw source note processed:

- `raw/OpenAI's 5 Levels Of 'Super AI' (AGI To Outperform Human Capability).md` - Forbes article (Jodie Cook, 2024-07-16) describing OpenAI's five-level AGI framework.

Generated pages created:

- `concepts/OpenAI AGI Progression Framework.md` - Summarizes the 5 levels (conversational → reasoners → agents → innovators → organizations) with a capability table and wiki-relevant context for agent skill design.

Generated pages updated:

- `index.md` — Added new raw source to frontmatter and source list; added concept link.
- `log.md`

Important decisions:

- Created a dedicated concept page rather than folding into an existing page because AGI progression is a distinct topic from the wiki's core Agent Skills focus.
- Added a "Context for This Wiki" section connecting the framework to Agent Skills maturity and skill design implications, keeping it relevant to the wiki's scope.

## [2026-05-01] ingest | Full wiki review, linkages, and new concept pages

Comprehensive review of the entire wiki after a wave of new additions. Processed all remaining uningested raw sources, created new concept pages, and established cross-linkages throughout the wiki.

Raw source notes processed (previously added to disk but not yet ingested):

- `raw/Deep Dive into LLMs like ChatGPT.md` - Andrej Karpathy's video transcript covering the full LLM pipeline: data collection, tokenization (BPE), transformer training, RLHF, and autoregressive inference.
- `raw/VILA-LabDive-into-Claude-Code A Systematic Analysis and Discussion of Claude Code for Designing Today's and Future AI Agent Systems.md` - arXiv 2604.14228: source-level analysis of Claude Code v2.1.88 (~512K lines, ~1,900 TypeScript files).
- `raw/OpenAI API Responses vs. Chat Completions.md` - Simon Willison analysis of the Responses API introduction.
- `raw/Why we built the Responses API.md` - OpenAI developer blog on Responses API design rationale for reasoning models.

Generated pages created:

- `concepts/Claude Code Architecture Deep Dive.md` (created in prior session, now logged) — Source-level architectural analysis: 98.4% infrastructure / 1.6% AI, 7 safety layers, 5 compaction stages, 4 extensibility mechanisms (Hooks → Skills → Plugins → MCP), 7 permission modes, 27 hook events, 13 design principles. Includes design guide for agent builders.
- `concepts/OpenAI Responses API.md` — Covers the API evolution (Completions → Chat → Assistants → Responses), key differences (state management, reasoning preservation, hosted tools, polymorphic outputs), design rationale (encrypted reasoning, agentic loop), and implications for Agent Skills.
- `concepts/LLM Fundamentals.md` — Mental models for how LLMs work: pretraining data pipeline, BPE tokenization, transformer architecture, RLHF fine-tuning, and autoregressive inference. Connects fundamentals to why skills need precise wording, progressive disclosure, and systematic evaluation.
- `lesson-plan/AI Fundamentals to Agent Skills.md` (created in prior session, now logged) — 16-module curriculum (~40-60 hours) organized in 4 phases: AI Foundations → Building with LLMs → Agents and Skills → Advanced Topics. Includes three learning pathways (Skill Author ~25-35h, Agent Developer ~40-60h, Quick Start ~20-30h).

Cross-linkages established:

- `concepts/Agent Skills.md` — Added links to Claude Code Architecture Deep Dive, LLM Fundamentals, and OpenAI Responses API.
- `concepts/Agent Frameworks and Orchestration.md` — Added links to Claude Code Architecture Deep Dive (concrete harness reference) and OpenAI Responses API (built-in agentic loop).
- `concepts/Discovery Conventions.md` — Added link to Claude Code Architecture Deep Dive (4-level CLAUDE.md hierarchy at source level).
- `concepts/Plugin-Based Agent Extensions.md` — Added link to Claude Code Architecture Deep Dive (plugin manifest accepts 10 component types, extensibility spectrum).
- `concepts/Skill Distribution and Installation.md` — Added link to Claude Code Architecture Deep Dive (graduated extensibility spectrum).
- `concepts/Agent SDKs and Codex Automation.md` — Already had link to Claude Code Architecture Deep Dive; verified.
- `concepts/MCP and Tool-Integration Architecture.md` — Verified existing linkages; no addition needed (MCP page already references extensibility spectrum).
- `concepts/LLM Fundamentals.md` — Added links to LLM Provider Selection, AI Coding Plans, Progressive Disclosure, Validation and Evaluation, MCP, OpenAI Responses API, and the lesson plan.

Updated:

- `index.md` — Added 3 new concept articles, 1 lesson plan section, 4 new raw sources to frontmatter, 5 new raw source descriptions.
- `log.md`

Important decisions:

- Treated Claude Code Architecture Deep Dive as a reference-grade page rather than a core Agent Skills page — it provides implementation evidence that informs many other concepts but is not itself about skills.
- Created LLM Fundamentals as a standalone concept page because Karpathy's video is the foundational mental-model resource for the entire wiki; all higher-level concepts (skills, tools, orchestration) assume an understanding of what LLMs are.
- Created OpenAI Responses API as a separate concept page because it represents a shift in how OpenAI's API layer handles agentic work — this overlaps with but is distinct from orchestration frameworks.
- Did not create a separate concept page for the Karpathy video's raw transcript; instead synthesized the key mental models into LLM Fundamentals with explicit connections to skill design.

Follow-ups:

- Consider adding a model-level benchmark page once target AI tools and evaluation tasks are known (was a follow-up from the 2026-04-26 LLM provider ingest).
- If the Responses API gains a migration guide or best-practice document specifically for Agent Skills integration, add a dedicated section.
- The lesson plan references several modules that could become standalone concept pages if learners need more depth (e.g., Prompt Engineering Fundamentals, Tool Use and Function Calling as a standalone from Module 6).

## [2026-05-02] ingest | Karpathy: From Vibe Coding to Agentic Engineering

Processed the Sequoia Capital AI Ascent 2026 interview transcript with user's personal reflections and blog post draft as the primary synthesis material.

Raw source note processed:

- `raw/Andrej Karpathy From Vibe Coding to Agentic Engineering.md` - Karpathy on Software 3.0 (prompting as programming), vibe coding vs agentic engineering, verifiability and jagged intelligence, the rising ceiling for AI-native engineers, and why understanding cannot be outsourced.

Generated pages created:

- `concepts/Software 3.0.md` — Karpathy's paradigm: Software 1.0 → 2.0 → 3.0, context window as programming surface, OpenClaw installer and MenuGen examples, and the "new things not just faster things" argument.
- `concepts/Agentic Engineering vs Vibe Coding.md` — Vibe coding (exploration, raises the floor) vs agentic engineering (production, preserves the ceiling), intern analogy, spec > plan mode, and the Stripe/email failure.
- `concepts/The AI-Native Engineer and the Rising Ceiling.md` — The 10x engineer is outdated, shallow vs deep AI use, setup investment in the agentic era, and why hiring should change from puzzles to real projects with agents.
- `concepts/Understanding as the Human Bottleneck.md` — "You can outsource your thinking, but you can't outsource your understanding." Syntax vs concepts, the hidden risk of obedient agents, and LLM knowledge bases as comprehension tools.

Generated pages updated:

- `index.md` — Added new raw source to frontmatter and source list; added concept article entry.
- `log.md`

Important decisions:

- Split the user's blog post into four separate concept pages rather than keeping it as one combined page. Each concept page focuses on a single idea with its own cross-links, keeping the wiki organized by concept rather than by source.
- Did not create separate concept pages for jagged intelligence, verifiability, or the "ghosts vs animals" framing because those are adjacent to this wiki's core Agent Skills focus. They are captured in the raw transcript and can be extracted if a future concept requires them.
- Positioned the concept page as a personal reflection layer rather than a purely technical summary, matching the wiki's existing pattern (e.g., README.md notes this is an "LLM-maintained wiki" built from personal raw sources).

Follow-ups:

- If the user's blog post is published externally, consider adding the publication URL to the concept page source section.
- The "what is my MenuGen?" question could become a recurring journal entry if the user wants to track obsolete projects over time.
- Consider adding a jagged intelligence concept page if future raw sources expand on the verifiability + RL training data argument.

## [2026-05-04] ingest | Debois: Context Is the New Code

Processed Patrick Debois's AI Engineer World's Fair talk on the Context Development Lifecycle.

Raw source note processed:

- `raw/Context Is the New Code — Patrick Debois, Tessl.md` - DevOps-inspired lifecycle for context: Generate → Evaluate → Distribute → Observe. Covers context flywheel, eval non-determinism and error budgets, context dependency hell, AI SBOM, context filters, sandbox security, and harness engineering observability.

Generated pages created:

- `concepts/Context Development Lifecycle.md` — Four-stage lifecycle modelled on SDLC/DevOps infinity loop. Two nested loops (library authoring and organizational). Context flywheel. "Context is fuel, LLMs are engine."
- `concepts/Context Observability and Feedback.md` — Observe stage in detail: agent logs, PR feedback as context feedback, production failure capture, sandbox security testing, context filters as WAF for prompt injections, AI SBOM, and harness engineering observability.

Generated pages updated:

- `concepts/Skill Authoring Workflow.md` — Added Debois source and "Context Generation Methods" section covering voice coding, documentation pull, external context pull, spec-driven development, code-to-skills transformation.
- `concepts/Validation and Evaluation.md` — Added Debois source and sections on non-determinism/error budgets for CI/CD evals, and end-to-end testing with judge agents that execute code in sandboxes.
- `concepts/Skill Distribution and Installation.md` — Added Debois source and "Dependency Management and Context Security" section covering context dependency hell, AI SBOM, credential scanning, and context filters.
- `index.md` — Added new raw source and two concept articles.
- `log.md`

Important decisions:

- Created two new concept pages rather than one combined page. The Context Development Lifecycle is the overarching framework; Context Observability and Feedback is the deep-dive into the Observe stage, which has enough distinct content (security, logs, production monitoring, sandboxing, filters) to warrant its own page.
- Folded Debois Generate material into Skill Authoring Workflow rather than creating a separate page, since it extends the existing authoring patterns.
- Folded Debois Evaluate material into Validation and Evaluation, since the existing page already covers the evaluation ladder and Debois adds practical concerns (non-determinism, error budgets, judge-as-agent).
- Folded Debois Distribute material into Skill Distribution and Installation, since it adds security and dependency concerns to the existing distribution picture.
- Positioned the "context as fuel, LLMs as engine" framing as the conceptual anchor: most engineers cannot change the model, but they can optimize context systematically.

Follow-ups:

- If the wiki later tracks concrete CI/CD tools for context evals, create a dedicated "Context CI/CD" section or page.
- The AI SBOM concept could become its own page if the wiki accumulates more sources on skill provenance, signing, and supply-chain trust.
- Context filters (WAF for prompts) is an emerging pattern — revisit if tooling matures around this.

## [2026-05-10] ingest | Official Claude docs + Skill security research

Processed 4 newly added raw articles: two official Claude Skills documentation/cookbook sources, and two security research articles covering indirect prompt injection and the Snyk ToxicSkills supply chain audit.

Raw source notes processed:

- `raw/Agent Skills.md` - Official platform.claude.com docs: VM architecture, beta API requirements (3 beta headers), progressive disclosure token budgets (~100/<5k/unlimited), runtime constraints per surface (API vs claude.ai vs Claude Code), ZDR ineligibility notice, name/description field requirements, and "treat like installing software" security guidance.
- `raw/Introduction to Claude Skills.md` - Official Jupyter cookbook: Excel/PPT/PDF generation via beta API with code execution tool, token optimization (98% savings on initial context), versioning strategy (use "latest" for Anthropic skills), generation time expectations (40s-2min), and troubleshooting guide.
- `raw/Indirect Prompt Injection Attacks Hidden AI Risks.md` - CrowdStrike blog: indirect prompt injection as OWASP #1 GenAI risk, 300K+ adversarial prompts analyzed, 150+ techniques tracked, shadow AI problem (45% BYO AI without IT knowledge), real-world examples (AI hiring platform manipulation, LinkedIn bio injection), and 6-layer defense framework.
- `raw/Snyk Finds Prompt Injection in 36%, 1467 Malicious Payloads in a ToxicSkills Study of Agent Skills Supply Chain Compromise.md` - Snyk security audit of 3,984 skills from ClawHub/skills.sh (Feb 2026): 13.4% critical issues (534 skills), 36.82% any flaw (1,467 skills), 76 confirmed malicious payloads (credential theft, backdoors, exfiltration), 91% of malicious skills combine prompt injection + traditional malware, 8 threat actors identified, 3 attack techniques (external malware distribution, obfuscated exfiltration, security disablement), and mcp-scan open-source defense tool.

Generated pages created:

- `Agent Skills (platform docs).md` — Source summary of official platform docs with VM architecture, API requirements, runtime constraints, and security guidance.
- `Introduction to Claude Skills (cookbook).md` — Source summary of official Jupyter cookbook with token optimization, versioning, and troubleshooting.
- `Indirect Prompt Injection Attacks (CrowdStrike).md` — Source summary of CrowdStrike analysis on indirect prompt injection threat landscape.
- `Snyk ToxicSkills Research.md` — Source summary of Snyk ToxicSkills security audit with threat taxonomy, attack techniques, and defense recommendations.
- `concepts/Skill Security and Supply Chain Risk.md` — New concept page synthesizing security research from Snyk and CrowdStrike: landscape overview, why Agent Skills are worse than traditional package risks, attack techniques, indirect injection vectors, defense layers, and runtime constraint implications.

Generated pages updated:

- `concepts/Agent Skills.md` — Added 2 new sources to frontmatter; added platform docs and cookbook to Connections with brief descriptions; added Skill Security concept link.
- `index.md` — Added 4 new raw sources to frontmatter and source list; added new concept article entry; added 4 new source summaries.
- `log.md`

Important decisions:

- Created a dedicated "Skill Security and Supply Chain Risk" concept page rather than folding into Skill Governance and Metrics. The security research has enough distinct content (ThreatSkills taxonomy, indirect injection, attack techniques, defense layers, runtime constraint analysis) to warrant its own page. Skill Governance focuses on ownership, review, and quality metrics; Skill Security focuses on attack surfaces, malware, and supply chain compromise.
- Did not create source summaries for the two security articles as separate entries — each security source got its own source summary page because they have different scopes (CrowdStrike = broader prompt injection threat landscape; Snyk = Agent Skills-specific supply chain audit).
- Positioned the Snyk ToxicSkills data as the primary evidence for the new Skill Security concept page, with CrowdStrike providing the broader indirect injection context and Anthropic's own security guidance providing the platform-level baseline.

Follow-ups:

- The ToxicSkills research mentions `mcp-scan` as an open-source scanning tool — consider adding a practical "how to audit your installed skills" section to the Skill Security page if this becomes a recurring operational need.
- The 8 identified threat actors and malicious skill URLs should be tracked if this wiki later maintains a "known bad" indicator list.
- CrowdStrike's mention of OWASP 2025 Top 10 and the Pangea acquisition context could be worth tracking if OWASP publishes formal Agent Skills security guidance.

## [2026-05-10] ingest | Agent Skills official sources (Anthropic blog + agentskills.io)

Processed two newly added raw articles covering the official Anthropic engineering introduction to Agent Skills and the agentskills.io open standard homepage.

Raw source notes processed:

- `raw/Equipping agents for the real world with Agent Skills.md` - Anthropic engineering blog: official Agent Skills introduction using the PDF skill as a walk-through example. Covers skill anatomy, progressive disclosure with context window diagrams, code execution as tools, skill development guidelines (start with eval, structure for scale, think from Claude's perspective, iterate with Claude), security considerations, and future roadmap (agent self-creation, MCP complement).
- `raw/Agent Skills Overview.md` - agentskills.io official homepage: open standard definition, canonical three-stage loading (Discovery, Activation, Execution), folder structure template, and cross-product reuse as the core value proposition.

Generated pages created:

- `Equipping Agents for the Real World with Agent Skills.md` — Source summary of the Anthropic engineering article with key points, quotes, and cross-links.
- `Agent Skills Overview (agentskills.io).md` — Source summary of the agentskills.io open standard homepage.

Generated pages updated:

- `concepts/Agent Skills.md` — Added both new sources to frontmatter; added "Skill Development Guidelines" section with Anthropic's four guidelines; added source links to Connections.
- `concepts/Progressive Disclosure.md` — Added both new sources to frontmatter; added agentskills.io canonical stage names (Discovery, Activation, Execution) and Anthropic's context window visualization reference.
- `index.md` — Added two new raw sources to frontmatter and source list; added Source Summaries section with both new entries.
- `log.md`

Important decisions:

- Created two dedicated source-summary pages rather than folding content only into concept pages, because both sources are foundational references for the wiki's core topic and deserve standalone summaries.
- Did not create new concept pages since the content reinforced existing concepts (Agent Skills, Progressive Disclosure) rather than introducing new ones.
- Positioned the agentskills.io "Discovery/Activation/Execution" terminology as the canonical three-stage naming, supplementing the existing descriptive progressive disclosure content.

Follow-ups:

- The security considerations from the Anthropic article (malicious skills, data exfiltration, auditing) could warrant a dedicated "Skill Security and Trust" concept page if more sources accumulate on this topic (currently referenced in Skill Governance and MCP security pages).
- The Anthropic article's mention of agent self-creation/evaluation of skills is a forward-looking claim worth tracking if the ecosystem develops tooling in that direction.

## [2026-05-10] ingest | Meta-Meta-Prompting (Garry Tan) + Agent Skills Overview update

Processed one new raw article and an updated wiki page.

Raw sources processed:

- `raw/Meta-Meta-Prompting The Secret to Making AI Agents Work.md` - Garry Tan's "fat skills, fat code, thin harness" architecture: Skillify meta-skill that creates skills from repeated work, book-mirror workflow, 100K-page structured brain, GBrain/OpenClaw/Hermes Agent stack, compounding personal AI system. Part of his Fat Skills series.
- `raw/Introduction to Claude Skills.md` - Updated raw source (full Jupyter notebook export). Existing wiki summary already captures key points; no changes needed.

Updated pages:

- `Agent Skills Overview (agentskills.io).md` - Updated with Advantages section (core benefits, team/enterprise value, ecosystem), Problems Agent Skills Solve table, and Sources section with 10 external references.

Generated pages created:

- `Meta-Meta-Prompting The Secret to Making AI Agents Work.md` — Source summary of Garry Tan's article with architecture breakdown, Skillify workflow, brain schema, and getting-started guide.

Updated files:

- `index.md` — Added new raw source to frontmatter and source list; added Source Summaries entry.
- `log.md`

Important decisions:

- Did not create new concept pages — the article reinforces existing concepts (Harness Engineering, Skill Authoring Workflow, Replacing Code with Skills, Context Development Lifecycle) rather than introducing new ones.
- Positioned "Skillify" as a concrete example of the skill authoring workflow — the meta-skill that extracts patterns from repeated work into reusable skills.

Follow-ups:

- The GBrain project (github.com/garrytan/gbrain) ships 39 installable skills and claims 97.6% recall on LongMemEval — worth revisiting if this wiki later covers retrieval architectures or brain-style personal knowledge systems.
- The "cross-modal eval" pattern (running output through multiple models for quality checking) could be a useful addition to the Validation and Evaluation concept page.

## [2026-05-10] maintenance | Organize source summaries into sources/ folder

Moved all 7 source-summary pages from root into `sources/` to keep root clean.

Files moved:

- `sources/Agent Skills (platform docs).md`
- `sources/Agent Skills Overview (agentskills.io).md`
- `sources/Equipping Agents for the Real World with Agent Skills.md`
- `sources/Indirect Prompt Injection Attacks (CrowdStrike).md`
- `sources/Introduction to Claude Skills (cookbook).md`
- `sources/Meta-Meta-Prompting The Secret to Making AI Agents Work.md`
- `sources/Snyk ToxicSkills Research.md`

Also:

- Deleted empty `.codex` stray file
- Created `.gitignore` to exclude `.claude/settings.local.json`
- Moved misplaced `courses/from-agents-to-skills/raw/2026-05-10 Skill Authoring Patterns Cross-Project Research.md` → `raw/`
- Updated `AGENTS.md` to document `sources/` and `concepts/` folder roles

Important decisions:

- Obsidian wikilinks are filename-based, not path-based, so existing links continue to resolve without changes.
- `README.md` and `image.png` remain in root as legitimate project-level files.

## [2026-05-10] ingest | Matt Pocock Skills for Real Engineers (updated snapshot)

Processed updated snapshot of mattpocock/skills repo — significantly different from the earlier snapshot already in `raw/`.

Key differences from earlier snapshot (`mattpocockskills My personal directory of skills...`):

- **Design philosophy now explicit**: four common agent failure modes (misalignment, verbosity, broken code, ball of mud) mapped to skill solutions
- **Shared language / CONTEXT.md**: New emphasis on DDD-style ubiquitous language as a concision tool — agents spend fewer tokens, name consistently, navigate easier
- **New skills**: diagnose (debugging loop), grill-with-docs (grilling + CONTEXT.md/ADR updates), triage (state machine), setup-matt-pocock-skills (per-repo config scaffold), zoom-out (contextual explanation), prototype (throwaway exploration), caveman (ultra-compressed comms)
- **Removed/renamed skills**: design-an-interface, request-refactor-plan, triage-issue, edit-article, ubiquitous-language, obsidian-vault
- **Installer**: `npx skills@latest add mattpocock/skills` with interactive `/setup-matt-pocock-skills` wizard

No new concept page created — content reinforces existing pages (Agent Skills, Skill Authoring Workflow, Skill Distribution, Skill Repository Tooling).

Updated:

- `index.md` — Added new raw source to frontmatter and source list
- `concepts/Agent Skills.md` — Added new source to frontmatter
- `concepts/Skill Authoring Workflow.md` — Added new source to frontmatter
- `concepts/Skill Distribution and Installation.md` — Added new source to frontmatter
- `concepts/Skill Repository Tooling.md` — Added new source to frontmatter
- `log.md`

## [2026-05-11] ingest | Self-improving skills, autonomous research, meta-skills

Processed three newly added raw articles covering autonomous skill improvement, Karpathy's autoresearch, and Garry Tan's skillification architecture.

Raw source notes processed:

- `raw/Build Self-Improving Claude Code Skills. The Results Are Crazy.md` - Simon Scrapes video transcript: applying Karpathy's autoresearch loop to Claude Code skills, binary assertions for automated scoring, two-layer self-improvement.
- `raw/karpathyautoresearch AI agents running research on single-GPU nanochat training automatically.md` - Karpathy's autoresearch README: fixed 5-min time budgets, single-file agent editing, autonomous iteration loop, ~100 experiments/night.

Generated pages created:

- `concepts/Self-Improving Skills.md` — Autonomous improvement loops using binary assertions, Karpathy pattern adapted to skills, two layers (description optimization + output quality), eval structure, limitations.
- `concepts/Autonomous Research Agents.md` — Karpathy's autoresearch project: prepare.py/train.py/program.md triad, fixed time budget design, autonomy protocol, platform tuning for smaller GPUs.
- `concepts/Meta-Skills and Skillification.md` — Skills that create skills (skillify), fat skills/thin harness architecture, skill composition, GBrain/GStack systems, compounding personal AI infrastructure.

Generated pages updated:

- `concepts/Skill Authoring Workflow.md` — Added cross-project research section: SKILL.md structure convergence, description design rules, constraint patterns, TDD-for-skills testing methodology, voice guidelines. Updated sources and tags.
- `concepts/SKILL.md Package Anatomy.md` — Added Matt Pocock patterns: failure modes addressed, skill categories, CONTEXT.md as companion file. Updated sources.
- `concepts/Validation and Evaluation.md` — Added binary assertions reference with cross-link to Self-Improving Skills.

Updated:

- `index.md` — Added 3 new concept articles, 2 new raw sources to frontmatter and source list.
- `log.md`

Important decisions:

- Created a dedicated "Autonomous Research Agents" concept page rather than folding into Self-Improving Skills, because autoresearch is a distinct pattern that predates and inspired the skill self-improvement application.
- Created "Meta-Skills and Skillification" as a standalone concept because the GBrain/GStack architecture (skillify, brain pages, compounding infrastructure) is architecturally distinct from both skill authoring and self-improvement.
- Folded the 2026-05-10 Skill Authoring Patterns cross-project research into Skill Authoring Workflow and SKILL.md Package Anatomy rather than creating a standalone page, because it is a synthesis of existing projects that reinforces existing concepts.

## [2026-05-11] lint | Full wiki health check

Ran a comprehensive lint pass across all 45 concept pages, raw sources, index.md, and log.md.

Issues found and fixed:

1. **Medium**: `index.md` was missing entries for 3 new concept pages (Self-Improving Skills, Autonomous Research Agents, Meta-Skills and Skillification). Added with descriptions.
2. **Low**: `index.md` frontmatter was missing 2 new raw sources. Added.
3. **Low**: `index.md` and `log.md` updated dates were stale (2026-05-10). Bumped to 2026-05-11.
4. **Low**: Added log entry for 2026-05-11 ingest.

No broken wikilinks detected. All concept pages have valid frontmatter with type/created/updated fields. No duplicate pages requiring consolidation. All index entries verified against disk.

## [2026-05-11] lint | Wiki navigation and link health

Checked generated wiki pages, source summaries, concept pages, course docs, and local skill artifacts for link health and index coverage.

What changed:

- Added a `Development Artifacts` section to `index.md` for presentation design specs and implementation plans under `docs/superpowers/`.
- Left `raw/` untouched.

Files updated:

- `index.md`
- `log.md`

Findings:

- No real broken Obsidian wikilinks were found after accounting for filename-based resolution and raw-source references.
- The only index coverage gap found was the four `docs/superpowers/` planning/spec files, now linked from the index.
- Duplicate `lesson-plan.md` filenames exist under separate course folders; this is acceptable but can be confusing in Obsidian filename-only lookup, so future course pages should use path-qualified links or more specific page names when cross-linking lesson plans.

Follow-ups:

- Decide whether `.claude/skills/presentation-slides/SKILL.md` should be documented as a wiki artifact or treated as local tooling only. I left it out of `index.md` for now because it is a large operational skill file rather than a generated knowledge page.

## [2026-05-11] ingest | Tokenmaxxing and AI-native engineering orgs

Processed two newly added raw YouTube transcript clippings:

- `raw/Tokenmaxxing How Top Builders Use AI To Do The Work Of 400 Engineers.md` - Garry Tan / Y Combinator on tokenmaxxing, GStack, model cross-review, Playwright QA automation, personal AI ownership, and using tokens to buy back scarce human time.
- `raw/Running an AI-native engineering org.md` - Fiona Fung / Claude on shifted bottlenecks, JIT planning, code review, ownership, hiring, flat orgs, dogfooding, and killing stale processes in AI-native engineering teams.

Generated pages created:

- `sources/Tokenmaxxing How Top Builders Use AI To Do The Work Of 400 Engineers.md`
- `sources/Running an AI-native engineering org.md`
- `concepts/Tokenmaxxing.md`
- `concepts/AI-Native Engineering Organizations.md`

Generated pages updated:

- `concepts/The AI-Native Engineer and the Rising Ceiling.md` - Added tokenmaxxing as a mechanism for the rising ceiling and AI-native org implications for hiring/team design.
- `concepts/Harness Engineering Principles.md` - Added tokenmaxxing and org-process sections.
- `concepts/Collaborative AI Engineering.md` - Added org norms for faster teams.
- `concepts/Validation and Evaluation.md` - Added verification-as-new-bottleneck section.
- `index.md` - Added new raw sources, concept pages, and source summaries.
- `log.md`

Important decisions:

- Created `Tokenmaxxing` as a standalone concept because it is broader than skillification: it covers a spend-machine-time-to-buy-context-and-human-time strategy across research, coding, QA, and personal AI.
- Created `AI-Native Engineering Organizations` as a standalone concept because Fiona Fung's talk is about management and operating-model changes, not only individual agentic engineering or repository harnesses.
- Did not update `raw/Build Self-Improving Claude Code Skills. The Results Are Crazy.md`; git showed only a line-ending warning and no substantive diff.

## [2026-05-11] ingest | AI-native work archetypes

Processed one newly added raw Substack clipping:

- `raw/There will only be four jobs.md` - Yoni Rechtman on the claim that AI-native companies will organize around working styles rather than traditional product/design/engineering output categories.

Generated pages created:

- `sources/There will only be four jobs.md`
- `concepts/AI-Native Work Archetypes.md`

Generated pages updated:

- `concepts/AI-Native Engineering Organizations.md` - Added work-archetypes section connecting acceleration, stabilization, governance, and interface roles to AI-native org design.
- `concepts/The AI-Native Engineer and the Rising Ceiling.md` - Added beyond-the-engineer-title section for cross-functional AI-native builders.
- `index.md` - Added new raw source, concept page, and source-summary entry.
- `log.md`

Important decisions:

- Created `AI-Native Work Archetypes` as a standalone concept because the source is about cross-functional working styles, not only engineering teams.
- Treated the source's labels as intentionally memetic and preserved the underlying durable functions: acceleration, stabilization, governance, and interface.

## [2026-05-11] lint | Wiki health check after new ingests

Checked 77 raw files, 48 concept pages, 10 source summaries, 3 course pages, and 4 docs pages.

What changed:

- Appended this lint entry to `log.md`.
- Left `raw/` untouched.
- Did not repair ambiguous links in this pass because the request was to lint, not repair.

Findings:

- No generated pages are missing from `index.md` by path or title check.
- All `index.md` wikilinks resolve.
- All raw markdown files are listed in `index.md`.
- No broken wikilinks were found in generated pages (`concepts/`, `sources/`, `courses/`, `docs/`).
- All concept and source pages have basic frontmatter fields (`type`, `created`, `updated`, `status`).
- All concept and source pages include an obvious source reference.
- Duplicate markdown basenames exist where raw files and generated source summaries share titles. This is expected for source summaries but can make unqualified Obsidian links ambiguous.
- Medium navigation risk: `raw/Agent Skills.md` and `concepts/Agent Skills.md` share the same basename, and several generated pages link to `[[Agent Skills]]` without a path or alias. These should be rewritten to `[[concepts/Agent Skills|Agent Skills]]`.
- Low navigation risk: source-summary entries in `index.md` link by basename for pages that also exist in `raw/`; path-qualified `[[sources/...|...]]` links would be less ambiguous.
- Low orphan risk: the course article/lesson plans, superpowers docs, and `sources/Meta-Meta-Prompting The Secret to Making AI Agents Work.md` have low inbound link counts beyond the index. This appears acceptable for docs/source-summary artifacts, but adding backlinks from related concept pages would improve navigation.

Recommended fixes:

1. Path-qualify generated-page links to `Agent Skills` so they target `concepts/Agent Skills.md`.
2. Path-qualify `index.md` source-summary links where raw/source basename duplicates exist.
3. Optionally add a backlink from `concepts/Meta-Skills and Skillification.md` to the `Meta-Meta-Prompting` source summary.

## [2026-05-11] maintenance | Repair ambiguous wiki links

Repaired the navigation issues found in the previous lint pass.

What changed:

- Path-qualified ambiguous `[[Agent Skills]]` links in generated concept pages so they resolve to `[[concepts/Agent Skills|Agent Skills]]`.
- Path-qualified the `Source Summaries` section in `index.md` so source-summary links resolve under `sources/` rather than competing with same-basename raw files.
- Added a backlink from `concepts/Meta-Skills and Skillification.md` to `sources/Meta-Meta-Prompting The Secret to Making AI Agents Work.md`.

Files updated:

- `concepts/Skill Distribution and Installation.md`
- `concepts/Discovery Conventions.md`
- `concepts/Agent SDKs and Codex Automation.md`
- `concepts/Agent Frameworks and Orchestration.md`
- `concepts/Plugin-Based Agent Extensions.md`
- `concepts/MCP and Tool-Integration Architecture.md`
- `concepts/Skill Authoring Workflow.md`
- `concepts/Meta-Skills and Skillification.md`
- `index.md`
- `log.md`

Verification:

- Follow-up link checks found no remaining unqualified `[[Agent Skills]]` links in generated pages.
- `index.md` source-summary links now use path-qualified `sources/` targets.
