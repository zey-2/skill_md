---
type: log
created: 2026-04-26
updated: 2026-07-01
status: active
sources:
  - "raw/research-context-window-degradation.md"
  - "raw/Making AI Work Leadership, Lab, and Crowd.md"
  - "raw/after-automation.pdf"
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
  - "raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md"
  - "raw/Lessons from building Claude Code How we use skills.md"
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

## [2026-05-16] ingest | Building a Second Brain — Vivian Balakrishnan at AI Engineer Singapore

Processed one new raw source: a keynote transcript from Singapore's Minister for Foreign Affairs sharing his 3-month experience building a personal AI agent without writing code.

Raw source note processed:

- `raw/Building a Second Brain Vivian Balakrishnan AI Engineer Singapore.md` - Dr. Balakrishnan's keynote: three key messages (personal understanding cannot be outsourced, real value is created at ground level, barriers have collapsed), tech stack (NanoClaw, Neoman, Ollama, Whisper, Obsidian, Claude, Raspberry Pi), and policy arguments for decentralized deployment and neuro-symbolic future.

Generated pages created:

- `sources/Building a Second Brain Vivian Balakrishnan AI Engineer Singapore.md` — Source summary with key points, tech stack table, and connections.
- `concepts/Personal AI Agents and Memory Systems.md` — New concept page on the emerging pattern of individuals building personal AI agents with graph-based memory, local deployment, and tool assembly.

Generated pages updated:

- `concepts/Understanding as the Human Bottleneck.md` — Added Balakrishnan source (direct alignment: "personal understanding cannot be outsourced").
- `concepts/Self-Improving Skills.md` — Updated timestamp.
- `index.md` — Added new raw source to frontmatter, new concept article, and 2 new source summaries.
- `log.md`

Important decisions:

- Created "Personal AI Agents and Memory Systems" as a standalone concept because the combination of graph-based personal memory, local deployment, tool assembly, and neuro-symbolic argument forms a distinct pattern from the wiki's existing focus on developer-facing agent skills.
- Included a detailed tech stack table because the specific tool choices (NanoClaw, Neoman, Ollama, Whisper, Obsidian) are the concrete evidence for the "tool assembly" claim.
- Noted the accessibility tension: "barriers have fallen" is true for a technically curious tinkerer but may overstate accessibility for non-technical users.

## [2026-05-16] ingest | Build Self-Improving Claude Code Skills (full transcript)

Processed updated raw source — went from short placeholder to full YouTube transcript with detailed tutorial on applying Karpathy's autoresearch to Claude Code skills.

Raw source note processed:

- `raw/Build Self-Improving Claude Code Skills. The Results Are Crazy.md` - Full transcript of Simon Scrapes tutorial: two-layer self-improvement (description optimization + binary assertion output quality), evals.json setup, autonomous loop logic, marketing copywriting example (23/24 → 25/25), and limitations.

Generated pages created:

- `sources/Build Self-Improving Claude Code Skills. The Results Are Crazy.md` — Source summary with two-layer architecture, binary assertion methodology, concrete results, and limitations.

Generated pages updated:

- `concepts/Self-Improving Skills.md` — Updated timestamp (already had this source in frontmatter).
- `index.md` — Added new source summary entry.
- `log.md`

Important decisions:

- Previously ingested this source only at the concept level; now created a proper source summary because the full transcript has significantly more detail (specific evals.json structure, concrete results, limitation boundaries).

## [2026-05-18] ingest | Ramp and Block enterprise AI adoption sources

Ingested new raw materials into the wiki as source summaries and a reusable synthesis concept about company-wide AI adoption.

Raw sources ingested:

- `raw/How to get your company AI pilled - geoffintech.md`
- `raw/How Block is becoming the most AI-native enterprise in the world  Dhanji R. Prasanna.md`

Generated pages created:

- `sources/How to get your company AI pilled.md`
- `sources/How Block is becoming the most AI-native enterprise in the world.md`
- `concepts/Enterprise AI Adoption Flywheel.md`

Generated pages updated:

- `concepts/AI-Native Engineering Organizations.md` — Added enterprise adoption pattern and links to Ramp/Block evidence.
- `concepts/AI-Native Work Archetypes.md` — Added enterprise case evidence showing non-engineers as builders and the continuing need for stabilizers, adults, and interface work.
- `index.md` — Added the Block raw source, new concept, and new source summaries.
- `log.md`

Important decisions:

- Treated Ramp and Block as complementary case studies: Ramp emphasizes cultural pressure, broad access, Glass/Dojo, and leaderboards; Block emphasizes functional org design, Goose/MCP, open tooling, and executive dogfooding.
- Created a new synthesis concept because the material extends beyond engineering-team norms into whole-company adoption.

## [2026-05-18] ingest | How to get your company AI pilled

Created a raw source capture from a user-provided X post by @geoffintech about Ramp's company-wide AI adoption playbook.

Files created:

- `raw/How to get your company AI pilled - geoffintech.md`

Files updated:

- `index.md` — Added the raw source to frontmatter and Raw Sources.
- `log.md`

Important decisions:

- Treated this as raw-source capture only, not a full synthesized source summary.
- Published date is inferred from the X status ID timestamp; the post text itself was supplied by the user.

## [2026-05-16] ingest | There will only be four jobs (full transcript)

Processed updated raw source — went from short placeholder to full Substack article with "Some Stray Notes" section.

No new pages created. Existing source summary (`sources/There will only be four jobs.md`) already captured the main points well from the earlier version.

Generated pages updated:

- `sources/There will only be four jobs.md` — Updated timestamp.
- `index.md` — Updated frontmatter date.
- `log.md`

Important decisions:

- Did not modify the source summary because the existing summary already covered all key archetypes, the working-styles-vs-titles distinction, and the product/design/eng replacement thesis. The full article adds illustrative examples (OpenAI/TBPN deal, GLP-1 company) but no new structural claims.

## [2026-05-16] extract | Three new concept pages from ingested material

Extracted three standalone concept pages from ideas that were previously captured only as bullet points in `Personal AI Agents and Memory Systems.md`.

Generated pages created:

- `concepts/Neuro-Symbolic AI Architecture.md` — Pure LLMs as pattern recognition vs. hybrid neural+symbolic systems. LeCun's critique, biological efficiency argument, token economics, and the already-working neuro-symbolic pattern in self-improving skills.
- `concepts/Graph-Based Memory for AI Agents.md` — Graph memory architecture: entities, causal/temporal/semantic edges, local embeddings, privacy preservation. Memory tool landscape (Neoman, Zep, Graphiti, Mem0). Architecture layers table.
- `concepts/Tool Assembly as a Skill.md` — Tool assembly as distinct capability between vibe coding and agentic engineering. Evidence from Balakrishnan's personal agent. Comparison table vs. vibe coding, agentic engineering, software engineering.

Generated pages updated (cross-references):

- `concepts/Personal AI Agents and Memory Systems.md` — Added connections to all three new pages.
- `concepts/LLM Fundamentals.md` — Added neuro-symbolic and graph-memory connections.
- `concepts/Agentic Engineering vs Vibe Coding.md` — Added tool assembly as third pattern.
- `concepts/Harness Engineering Principles.md` — Added neuro-symbolic (guardrails as symbolic layer) and tool assembly connections.
- `index.md` — Added three new concept articles.
- `log.md`

## [2026-05-16] enhance | Understanding as the Human Bottleneck — accountability dimension

Added the accountability dimension to the concept page after user emphasis on Dr. Balakrishnan's full quote: "you can delegate work. You can't delegate accountability."

What changed:

- Added full quote including accountability.
- Added "What Can and Cannot Be Outsourced" table.
- Added "Understanding and Accountability" section.
- Added connections to AI-Native Work Archetypes and Harness Engineering.
- Added new raw source capturing the tweet.

Files updated:

- `concepts/Understanding as the Human Bottleneck.md`
- `index.md` — Added new raw source to frontmatter.
- `log.md`

Files created:

- `raw/You can outsource your thinking but not your understanding - Yacine MTB.md`

## [2026-05-17] lint | Full wiki health check

Ran a comprehensive lint pass across all concept pages, raw sources, source summaries, courses, and docs.

Issues found and fixed:

1. **Critical**: 3 concept pages missing from `index.md` — `Software Economics`, `The New Meta - Measurement, Ideation, Iteration`, `AI agency`. Added with descriptions to the Concept Articles section.
2. **Critical**: `raw/new_economics_of_software.md` missing from `index.md` — referenced by Software Economics and The New Meta frontmatter but absent from both frontmatter and Raw Sources body. Added to both.
3. **Critical**: 4 new raw files about AI agency not in `index.md` — `A Formal Model of How Artificial Intelligence Erodes Human Agency`, `AI Agent Autonomy Levels`, `Six Levels of Agenticness`, `The Philosophy of Agentic AI Agency`. Added to frontmatter and Raw Sources section.
4. **Critical**: `sources/The New Economics of Software (AI Engineer Singapore 2026).md` missing from Source Summaries section. Added.
5. **Critical**: `raw/You can outsource your thinking but not your understanding - Yacine MTB.md` was in frontmatter only, never added to Raw Sources body section. Added.
6. **Medium**: Duplicate raw source entries removed from Raw Sources section — `2026-04-30 AI Coding Plans Comparison 2026.md` and `2026-04-30 Claude Code Third-Party LLM Provider Configuration.md` appeared twice (lines ~174-175 and ~201-202).
7. **Medium**: `concepts/AI agency.md` frontmatter used non-standard `name:/metadata:` format instead of `type:/created:/updated:`. Fixed to match wiki convention with proper source references.
8. **Low**: 2 new course HTML files (`courses/presentation-agency.html`, `courses/presentation-the-human-bottleneck.html`) missing from index. Added a Presentations section.

Verification:

- All concept pages now listed in `index.md` Concept Articles.
- All raw markdown files in `raw/` now listed in frontmatter and Raw Sources body.
- All source summaries in `sources/` now listed in Source Summaries section.
- No broken wikilinks detected in new concept pages — all referenced pages exist.
- Duplicate frontmatter entries for AI Coding Plans and Third-Party Provider Configuration remain in frontmatter (they were added in separate ingests); deduplicated only in the body section to avoid breaking existing source citations.

## [2026-05-20] ingest | Superpowers: How Jesse Built the #1 AI Claude Code/Codex Plugin

Ingested the new video transcript raw source on Jesse Vincent's Superpowers workflow.

Generated pages created:

- `sources/Superpowers How Jesse Built the 1 AI Claude Code Codex Plugin.md` — Source summary covering spec-first development, Socratic brainstorming, implementation planning, TDD, ephemeral review agents, end-to-end validation, and latent space engineering.

Generated pages updated:

- `concepts/Agent Skills.md` — Added Superpowers as evidence that skills can package a full operating procedure, not just task instructions.
- `concepts/Skill Authoring Workflow.md` — Added the test-deletion story as evidence for rationalization-aware skill authoring.
- `concepts/Harness Engineering Principles.md` — Added Superpowers as a personal harness pattern using specs, plans, tests, review agents, and validation loops.
- `concepts/Validation and Evaluation.md` — Added the v33 MP4 story and test-gaming warning as evidence for runtime proof and coverage-preserving verification.
- `concepts/Agentic Engineering vs Vibe Coding.md` — Added Superpowers as an operating loop that turns agentic engineering from posture into practice.
- `index.md` — Added the raw source and source summary entries.
- `log.md`

Important decisions and open questions:

- Did not create a new concept page because the material fit existing pages well.
- Recorded the "code does not matter anymore" claim as shorthand rather than literal doctrine: generated code still matters as the runnable artifact, but specs and proof artifacts are the scarce human-review layer.
- Open question: which parts of the Superpowers workflow transfer cleanly across Claude Code, Codex, Gemini CLI, Cursor, and other agent runtimes?

## [2026-05-23] ingest | The tokenmaxxing math nobody wants to admit

Ingested a new Agentmail article as a separate raw source and source-summary page, without merging it into the prior Y Combinator/Garry Tan tokenmaxxing article.

Files created:

- `raw/The tokenmaxxing math nobody wants to admit.md`
- `sources/The tokenmaxxing math nobody wants to admit.md`
- `concepts/Context Rot.md`

Files updated:

- `concepts/Tokenmaxxing.md` - Added Agentmail's output-over-tokens critique as a distinct tension beside the positive leverage framing.
- `concepts/Validation and Evaluation.md` - Added metric-gaming and output-ratio guidance.
- `concepts/Skill Governance and Metrics.md` - Added caution that token footprint must be paired with outcome metrics.
- `index.md` - Added the raw source, source summary, and Context Rot concept.
- `log.md`

Important decisions and open questions:

- Kept the Agentmail article distinct from `raw/Tokenmaxxing How Top Builders Use AI To Do The Work Of 400 Engineers.md`.
- Treated claims about Meta, Amazon, Google, and long-context accuracy as source claims, not independently verified facts.
- Open question: which concrete output metrics best normalize token spend across coding, research, sales, support, and personal-agent workflows?

## [2026-05-23] lint | Full wiki health check

Ran a read-only lint pass across generated wiki pages, raw sources, source summaries, courses, docs, `index.md`, and wikilinks.

Files updated:

- `log.md`

Findings:

- `index.md` coverage is healthy: all concept pages, source-summary pages, raw markdown files, course markdown files, and docs markdown files are listed or linked.
- All `index.md` wikilinks resolve.
- No generated concept/source pages are missing basic frontmatter.
- No indexed generated pages appear orphaned by the current path/title link check.
- One real broken generated-page wikilink was found: `concepts/Claude Code Architecture Deep Dive.md` links to `raw/VILA-labDive-into-Claude-Code...`, but the actual raw file is `raw/VILA-LabDive-into-Claude-Code...`.
- Template/example wikilinks in `AGENTS.md` and a placeholder historical link in `log.md` were ignored as non-content issues.
- Source-summary coverage is incomplete: 18 `sources/` pages exist for 89 raw markdown sources, leaving 71 raw sources without dedicated source-summary pages.
- `sources/Snyk ToxicSkills Research.md` is well sourced but uses `## Key Findings` rather than the recommended `## Key Points` / `## Evidence` pattern.
- Duplicate basenames remain where raw files and source-summary pages intentionally share titles; current ambiguous unqualified `[[Agent Skills]]` links appear only in historical log entries, not active generated pages.

Recommended fixes:

1. Repair the case-mismatched VILA raw-source wikilink in `concepts/Claude Code Architecture Deep Dive.md`.
2. Decide whether the vault should enforce "one source-summary page per raw source"; if yes, backfill the 71 missing source-summary pages in batches.
3. Optionally normalize `sources/Snyk ToxicSkills Research.md` headings to match the recommended source-summary structure.

## [2026-05-23] maintenance | Repair wiki lint findings

Repaired the actionable issues from the full wiki health check.

Files created:

- `sources/2026-04-26 Agent orchestration frameworks source.md`
- `sources/2026-04-26 Agent Skills specification evaluation and description optimization.md`
- `sources/2026-04-26 agentskills.io Agent Skills overview and quickstart.md`
- `sources/2026-04-26 Anthropic Claude API LLM provider source.md`
- `sources/2026-04-26 Anthropic evals for AI agents.md`
- `sources/2026-04-26 AWS Amazon Bedrock LLM provider source.md`
- `sources/2026-04-26 Azure AI Foundry Models LLM provider source.md`
- `sources/2026-04-26 Claude Agent SDK source.md`
- `sources/2026-04-26 Claude Code Agent Skills docs.md`
- `sources/2026-04-26 Claude Code Plugins docs.md`
- `sources/2026-04-26 Cohere LLM provider source.md`
- `sources/2026-04-26 Cursor Agent Skills support sources.md`
- `sources/2026-04-26 DeepSeek API LLM provider source.md`
- `sources/2026-04-26 Gemini CLI Agent Skills docs.md`
- `sources/2026-04-26 GitHub Copilot and VS Code Agent Skills docs.md`
- `sources/2026-04-26 Google Cloud Vertex AI and Model Garden LLM provider source.md`
- `sources/2026-04-26 LangSmith AgentEvals trajectory evaluation docs.md`
- `sources/2026-04-26 MCP architecture and Agent Skills integration source.md`
- `sources/2026-04-26 MCP security and authorization source.md`
- `sources/2026-04-26 Microsoft Agent Framework Agent Skills docs.md`
- `sources/2026-04-26 Mistral AI LLM provider source.md`
- `sources/2026-04-26 Open model inference providers source.md`
- `sources/2026-04-26 OpenAI agent evaluation and trace grading docs.md`
- `sources/2026-04-26 OpenAI Agents SDK official source.md`
- `sources/2026-04-26 OpenAI Agents SDK tools MCP and orchestration source.md`
- `sources/2026-04-26 OpenAI API LLM provider source.md`
- `sources/2026-04-26 OpenAI Codex Agent Skills docs.md`
- `sources/2026-04-26 OpenAI Codex Plugins docs.md`
- `sources/2026-04-26 OpenAI Codex SDK and App Server source.md`
- `sources/2026-04-26 OpenClaw Skills docs.md`
- `sources/2026-04-26 OpenCode Agent Skills docs.md`
- `sources/2026-04-26 OpenRouter LLM provider router source.md`
- `sources/2026-04-26 Perplexity Sonar API LLM provider source.md`
- `sources/2026-04-26 tau-bench tool-agent reliability benchmark.md`
- `sources/2026-04-26 Windsurf Cascade Skills docs.md`
- `sources/2026-04-26 xAI Grok API LLM provider source.md`
- `sources/2026-04-30 AI Coding Plans Comparison 2026.md`
- `sources/2026-04-30 Claude Code Third-Party LLM Provider Configuration.md`
- `sources/2026-04-30 Microsoft Copilot SKILL.md support roadmap.md`
- `sources/2026-05-10 Skill Authoring Patterns Cross-Project Research.md`
- `sources/A Formal Model of How Artificial Intelligence Erodes Human Agency.md`
- `sources/Agent Development Kit (ADK).md`
- `sources/Agent SDK overview.md`
- `sources/AI Agent Autonomy Levels From Assistive to Fully Autonomous.md`
- `sources/An open-source spec for Codex orchestration Symphony.md`
- `sources/Andrej Karpathy From Vibe Coding to Agentic Engineering.md`
- `sources/anthropicsskills Public repository for Agent Skills.md`
- `sources/Collaborative AI Engineering One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md`
- `sources/Context Is the New Code — Patrick Debois, Tessl.md`
- `sources/Deep Dive into LLMs like ChatGPT.md`
- `sources/Deploy n8n on Cloud Run  Google Cloud Blog.md`
- `sources/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md`
- `sources/Harness Engineering How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md`
- `sources/Harness engineering leveraging Codex in an agent-first world.md`
- `sources/karpathyautoresearch AI agents running research on single-GPU nanochat training automatically.md`
- `sources/LangChain vs LangGraph vs LangSmith vs LangFlow Key Differences Explained.md`
- `sources/mattpocockskills My personal directory of skills, straight from my .claude directory.md`
- `sources/mattpocockskills Skills for Real Engineers. Straight from my .claude directory.md`
- `sources/n8n A Guide to Workflow Automation.md`
- `sources/obrasuperpowers An agentic skills framework & software development methodology that works.md`
- `sources/OpenAI API Responses vs. Chat Completions.md`
- `sources/openaiskills Skills Catalog for Codex.md`
- `sources/OpenAI’s 5 Levels Of ‘Super AI’ (AGI To Outperform Human Capability).md`
- `sources/Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md`
- `sources/Six Levels of Agenticness Scoring AI Agency.md`
- `sources/skill.md for AI Agents.md`
- `sources/The Philosophy of Agentic AI Agency Autonomy and Moral Responsibility.md`
- `sources/VILA-LabDive-into-Claude-Code A Systematic Analysis and Discussion of Claude Code for Designing Today's and Future AI Agent Systems.md`
- `sources/VoltAgentawesome-agent-skills A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.md`
- `sources/Why we built the Responses API.md`
- `sources/You can outsource your thinking but not your understanding - Yacine MTB.md`

Files updated:

- `concepts/Claude Code Architecture Deep Dive.md` - Fixed the case-mismatched VILA raw-source reference.
- `sources/Agent Skills (platform docs).md` - Added an Evidence section and refreshed `updated`.
- `sources/Agent Skills Overview (agentskills.io).md` - Added an Evidence section and refreshed `updated`.
- `sources/Equipping Agents for the Real World with Agent Skills.md` - Added an Evidence section and refreshed `updated`.
- `sources/Indirect Prompt Injection Attacks (CrowdStrike).md` - Added an Evidence section and refreshed `updated`.
- `sources/Introduction to Claude Skills (cookbook).md` - Added an Evidence section and refreshed `updated`.
- `sources/Meta-Meta-Prompting The Secret to Making AI Agents Work.md` - Added an Evidence section and refreshed `updated`.
- `sources/Snyk ToxicSkills Research.md` - Normalized source-summary headings and added an Evidence section.
- `sources/The New Economics of Software (AI Engineer Singapore 2026).md` - Added an Evidence section and refreshed `updated`.
- `index.md` - Added source-summary backfill entries for raw sources that lacked dedicated `sources/` pages.
- `log.md`

Important decisions and follow-ups:

- Created 71 initial source-summary pages from existing `index.md` raw-source catalog descriptions rather than inventing deeper summaries without a focused ingest pass.
- These backfill pages are intentionally marked as navigational summaries and include open questions for fuller future ingestion.
- Follow-up: prioritize full ingest passes for the most reused raw sources if richer quotes, contradictions, or cross-links are needed.

## [2026-05-28] ingest | The AI paradox: More automation, more humans, more work

Ingested Dan Shipper's Lenny's Podcast / YouTube transcript from `raw/The AI paradox More automation, more humans, more work  Dan Shipper.md`.

Files created:

- `sources/The AI paradox More automation, more humans, more work  Dan Shipper.md`

Files updated:

- `concepts/AI-Native Engineering Organizations.md` - Added automation-as-management-work and agent-management bottlenecks.
- `concepts/AI-Native Work Archetypes.md` - Added PMs, full-stack designers, and forward deployed engineers as concrete AI-native role forecasts.
- `concepts/Software Economics.md` - Added agent-native SaaS as a counterpoint to pure SaaS-moat erosion.
- `index.md` - Added the raw source and source-summary catalog entry.
- `log.md`

Important decisions and follow-ups:

- Recorded a tension between Shipper's SaaS optimism and the existing software-economics thesis that cheap software erodes SaaS moats.
- Treated the "automation is a lie" claim as an operating-model insight rather than a literal rejection of automation.
- Follow-up: gather more evidence on whether agent-native SaaS pricing will support bring-your-own-model-token workflows.

## [2026-06-06] ingest | How Anthropic Engineers ACTUALLY Prompt Claude Code + fix index gaps

Ingested Austin Marchese's video transcript on four rules from Anthropic engineers for prompting Claude Code. Also fixed 3 raw sources that had source-summary pages but were missing from `index.md`.

Raw source processed:

- `raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md` - YouTube transcript: four rules (prompt skills not Claude, skills have three layers, build composable skills, skills improve every session) plus two patterns (save scripts inside skills, control invocation flags).

Raw sources added to index (previously missing):

- `raw/How the engineer behind Claude Cowork actually uses Claude  Felix Rieseberg (Anthropic).md`
- `raw/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md`
- `raw/Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic).md`

Files created:

- `sources/How Anthropic Engineers ACTUALLY Prompt Claude Code.md` — Source summary with four rules, three-layer skill architecture, composability principle, and compounding improvement loop.
- `concepts/Prompting Skills Not Prompts.md` — New concept page for the mental model shift from ad-hoc prompts to reusable skills, three-layer architecture, composability, and the compounding loop.

Files updated:

- `concepts/Self-Improving Skills.md` — Added Anthropic source and "Manual Self-Improvement" section documenting Rule 4 as the manual version of the autonomous loop.
- `concepts/Meta-Skills and Skillification.md` — Added composability evidence from Anthropic's Rule 3 (build composable, not custom).
- `concepts/Skill Authoring Workflow.md` — Added "Save Scripts Inside Skills" and "Invocation Control Flags" sections.
- `concepts/Progressive Disclosure.md` — Added Anthropic's three-layer model (description, instructions, tools) as mapping to the Discovery/Activation/Execution stages.
- `concepts/Comprehension-Driven Development.md` — Already existed from prior ingestion; no changes needed.
- `index.md` — Added 4 raw sources to frontmatter and Raw Sources; added new concept page and source summary entries; added 3 previously-missing source summaries (Felix Rieseberg, Priscila, Thariq).

Important decisions:

- Created "Prompting Skills, Not Prompts" as a standalone concept rather than folding into Agent Skills, because it captures a mental model shift (how to think about prompting) rather than a definition (what skills are).
- Did not create concept pages for "Ride the Models" or "Anti-To-Do List" despite those being referenced by existing source summaries — those are pre-existing broken links from prior ingestions, not part of this source.
- The 3 partially-ingested files (Felix Rieseberg, Priscila, Thariq) already had source-summary pages and concept-page cross-references from commit `051e0bd`; only the `index.md` entries were missing.

Follow-ups:

- The `[[concepts/Ride the Models]]` and `[[concepts/Anti-To-Do List and Abstraction Layering]]` links in existing source summaries point to non-existent concept pages — consider creating them or redirecting to the course article.
- The `[[concepts/HTML as AI Spec Format]]` link in the Thariq source summary points to a non-existent concept page.
- The `[[concepts/Ride the Models]]` link in the new source summary also points to a non-existent concept page (exists only as a course article).

## [2026-06-07] ingest | Why We'll Still Be Employed When AI Can Do Everything

Ingested Every newsletter (Laura Entis, 2026-06-05). Also noted that `raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md` had a line-ending-only change — no content re-ingestion needed.

Files created or updated:

- `sources/Why We'll Still Be Employed When AI Can Do Everything.md` — New source summary covering enterprise AI roadmap difficulty (Microsoft/OpenClaw), Naveen Naidu's custom skill workflow, the frame-reset cycle (Dan Shipper), and the compute cost tradeoff counterpoint (MT).
- `concepts/The Compute Cost Tradeoff.md` — New concept: AI capability ≠ AI adoption because intelligence costs energy. The question shifts from "Can AI do this?" to "Is it worth the compute?" Uses Waymo as empirical evidence.
- `concepts/Software Economics.md` — Added "The Compute Cost Ceiling" section with Waymo evidence and the "jagged free lunch" framing.
- `concepts/AI-Native Work Archetypes.md` — Added "The Frame-Reset Cycle" section showing how AI creates more work (prompts → context → orchestration → evals).
- `concepts/Enterprise AI Adoption Flywheel.md` — Added "The Speed Mismatch Problem" section with Microsoft/OpenClaw timeline (Nov 2025 viral → Jun 2026 Scout launch, already behind the news cycle).
- `concepts/Prompting Skills Not Prompts.md` — Added Naveen's "ask your agent what it needs" workflow to Practical Implications.
- `index.md` — Added new concept page, source summary, and raw source entry.

Important decisions:

- Created "The Compute Cost Tradeoff" as a standalone concept rather than folding into Software Economics, because it represents a distinct constraint (energy/compute) that applies beyond software development.
- Did not create a concept page for the "frame-reset cycle" — it fits naturally as a section in AI-Native Work Archetypes rather than standing alone.
- Did not create concept pages for the OpenClaw timeline or model linguistic quirks — these are evidence/color rather than reusable concepts.

Follow-ups:

- The compute cost argument assumes energy costs stay high. If inference costs continue declining at historical rates, the concept may need revision.
- The Dan Shipper vs MT debate is a direct contradiction published in the same newsletter — worth tracking as a source of tension in the wiki.
- Naveen's "don't download skills" advice could be its own short concept if the skill marketplace pattern becomes more prominent.

## [2026-06-07] ingest | Geoffrey Huntley (PyCon Lithuania) + Kilo Code parallel agents

Ingested two new raw sources. Also confirmed that `raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md` has only a line-ending change — no content re-ingestion needed. `raw/Why We’ll Still Be Employed When AI Can Do Everything.md` was already ingested in the prior entry.

Files created or updated:

- `sources/Geoffrey Huntley - Software Development Now Costs Less Than Minimum Wage.md` — New source summary: PyCon Lithuania talk on $10.42/hour software development, knowledge scarcity→abundance, model-first companies, middle management collapse, identity erasure, $800K in tokens, "build your damn agent."
- `sources/How 7 Kilo Code Engineers Run Up to 20 Parallel Agents and Still Ship Clean Code.md` — New source summary: foreground (2–4) vs. background (20+) agents, 60% context quality drop, plan-with-thinking/execute-with-fast pattern, cross-agent verification loops, software as gardening.
- `concepts/Parallel Agent Management.md` — New concept: the foreground/background split, context window Goldilocks zone, plan-then-execute pattern, verification loops, and software-as-gardening metaphor.
- `concepts/Software Economics.md` — Added "Concrete Unit Economics" ($10.42/hour) and "Model-First Companies" sections.
- `concepts/AI-Native Engineering Organizations.md` — Added "Model-First Companies" section (5–20 people, middle management collapse, compressed timelines) and "Parallel Agent Workflows" section.
- `concepts/Tokenmaxxing.md` — Added "Hyper-Engineer Communities" section ($20K/month gated community, $800K personal spend).
- `concepts/Context Rot.md` — Added Kilo Code evidence: quality drops at 60% context fill, well before 95% compaction.
- `concepts/The AI-Native Engineer and the Rising Ceiling.md` — Added "Consumer vs. Builder" section (cursor user vs. agent builder as the new hiring line).
- `concepts/Self-Improving Skills.md` — Added Geoffrey Huntley source for recursive self-improvement pattern.
- `index.md` — Added 2 raw sources, 2 source summaries, 1 concept page.
- `log.md` — This entry.

Important decisions:

- Created "Parallel Agent Management" as a standalone concept because it captures a distinct practical workflow (foreground/background, task sizing, verification loops) not reducible to existing concepts.
- Did not create a separate concept for "model-first companies" — it fits as a section in both Software Economics and AI-Native Engineering Organizations.
- Did not create a concept for "identity erasure" — it's a symptom of Software 3.0 and the rising ceiling, not a standalone idea.
- The Geoffrey Huntley source directly contradicts the [[concepts/The Compute Cost Tradeoff|compute cost tradeoff]] — Huntley says compute is already cheap enough to disrupt; the Every newsletter argues it's the ceiling. Recorded as tension in both source summaries.

Follow-ups:

- The "agile is waste" claim from Huntley is strong. Consider whether it warrants a concept page or fits as evidence in existing process-related concepts.
- The consumer-vs-builder hiring line could become its own concept if more sources adopt this framing.
- The 60% context quality drop from Kilo Code is a concrete number that should be cross-referenced with any future benchmark data on context rot.

## [2026-06-08] ingest | Lessons from building Claude Code: How we use skills

Ingested Anthropic's engineering blog by Thariq Shihipar on internal skill practices at Anthropic. This was the one remaining uningested raw source from the 2026-06-07 batch.

Raw source processed:

- `raw/Lessons from building Claude Code How we use skills.md` — Anthropic engineering blog: nine skill categories from internal catalog, skills as folders (not just SKILL.md), gotchas as highest-signal content, progressive disclosure via file system, config.json for setup, descriptions for models not humans, memory via log files, scripts inside skills, on-demand hooks, repo vs marketplace distribution, skill composition, usage measurement via PreToolUse hooks.

Files created:

- `sources/Lessons from building Claude Code How we use skills.md` — Source summary with nine-category taxonomy, gotchas pattern, progressive disclosure, config.json, on-demand hooks, marketplace governance, and skill composition.

Files updated:

- `concepts/Skill Authoring Workflow.md` — Added nine skill categories as a gap-analysis framework, gotchas as highest-signal content, config.json setup pattern, and on-demand hooks.
- `concepts/Skill Distribution and Installation.md` — Added repo check-in vs plugin marketplace (Anthropic internal), organic marketplace governance, and skill composition.
- `concepts/Skill Governance and Metrics.md` — Added PreToolUse hook for measuring skill usage and organic marketplace governance.
- `concepts/Self-Improving Skills.md` — Added iterative gotcha accumulation as a manual self-improvement pattern.
- `index.md` — Added new raw source to frontmatter and Raw Sources; added source summary to Source Summaries.
- `log.md` — This entry.

Important decisions:

- Did not create a new concept page for the nine skill categories — they fit as a section in Skill Authoring Workflow as a gap-analysis framework.
- Did not create a concept page for "skills are folders" — it reinforces the existing SKILL.md Package Anatomy concept rather than standing alone.
- Recorded the "descriptions for the model, not humans" claim as a stronger version of the cross-project research's "describe triggering conditions" — Anthropic's version says the description is literally what Claude scans to decide.
- The "don't state the obvious" advice tensions with other sources recommending thoroughness. Recorded as a model-capability-dependent tradeoff.

Follow-ups:

- The nine-category taxonomy could become the wiki's standard categorization if other sources adopt it.
- The PreToolUse hook for usage measurement has example code linked in the article — consider adding a practical governance section if this becomes a recurring pattern.
- The "skills are folders" framing could warrant updating SKILL.md Package Anatomy if the misconception persists in other sources.

## [2026-06-14] ingest | Ideation process + open-source AI projects (Matthew Berman)

Ingested two new raw sources: a structured ideation methodology and a video showcasing four open-source projects including context compression tooling.

Raw sources processed:

- `raw/The Ideation Process from Problems to Practical Solutions.md` — ChatGPT-generated guide: seven-stage pipeline (Understand → Explore → Generate → Combine → Evaluate → Prototype → Learn), methods (SCAMPER, Crazy 8s, brainwriting, analogy thinking), impact-effort prioritisation, and iteration loop.
- `raw/You NEED to try these open-source AI projects RIGHT NOW.md` — Matthew Berman video: Last30Days (skill-based trending search from Reddit/HN/Poly Market/X/YouTube/TikTok), Open Notebook (local NotebookLM clone with podcast generation), Agent Skills (seven-stage engineering workflow with `/interview-me`), and Headroom (context compression wrapper with 47–92% token savings and `headroom learn` self-improvement).

Files created:

- `sources/The Ideation Process from Problems to Practical Solutions.md` — Source summary with seven-stage pipeline, iteration loop, and connections to skill authoring.
- `sources/You NEED to try these open-source AI projects RIGHT NOW.md` — Source summary covering all four projects with concrete token savings evidence for Headroom.

Files updated:

- `concepts/Skill Authoring Workflow.md` — Added "Ideation Pipeline for Skill Design" section mapping the seven-stage ideation process to skill authoring. Added source to frontmatter.
- `concepts/Tokenmaxxing.md` — Added "Context Compression as Tokenmaxxing" section with Headroom's concrete token savings table (47–92%) and `headroom learn` self-improvement loop. Added source to frontmatter.
- `concepts/Context Rot.md` — Added Headroom as context compression evidence: tools that compress context before it reaches the model mitigate context rot by keeping effective context below the 60% quality-drop threshold. Added source to frontmatter.
- `index.md` — Added 2 raw sources to frontmatter and Raw Sources; added 2 source summaries to Source Summaries.
- `log.md` — This entry.

Important decisions:

- Did not create new concept pages for either source. The ideation methodology maps naturally to the existing Skill Authoring Workflow. The Berman video projects reinforce existing concepts (Tokenmaxxing, Context Rot, Progressive Disclosure) rather than introducing new ones.
- Did not create a standalone concept for "context compression" — it fits as a section in Tokenmaxxing (it's a tokenmaxxing tool) and evidence in Context Rot (it mitigates the problem).
- Did not create a concept for Last30Days as "skills as search interfaces" — interesting pattern but not enough evidence for a standalone page yet.
- Recorded Headroom's default telemetry and bundled "serena" installation as a supply-chain concern in the source summary, linking to existing Skill Security concept.

Follow-ups:

- Headroom's `headroom learn` pattern (mining failed sessions → writing corrections to CLAUDE.md/AGENTS.md) is a concrete self-improvement tool worth cross-referencing with Self-Improving Skills if more tools adopt this pattern.
- Last30Days's "skill as search interface" pattern could become a concept if more skills emerge that function as information retrieval interfaces rather than task workflows.
- Open Notebook's local-first architecture connects to Personal AI Agents and Memory Systems — worth revisiting if that concept page expands.

## [2026-06-14] ingest | After Automation + Reflecting on a Year of Claude Code

Ingested two new raw sources: Dan Shipper's Agent Mode interactive essay and Boris Cherny & Cat Wu's Claude Code first-year retrospective.

Raw sources processed:

- `raw/After Automation.md` — Dan Shipper's Every essay repackaged as an Agent Mode interactive article with companion GitHub repo (`EveryInc/after-automation-agent-mode`), setup prompts for Codex/Claude Code/OpenClaw, claims.md, objections-and-responses.md, and starter prompts.
- `raw/Reflecting on a year of Claude Code.md` — Boris Cherny (Head of Claude Code) and Cat Wu (Head of Product) on: every mistake becomes a skill, verification beyond unit tests (agent tests itself in bash, computer use), auto mode replacing plan mode (4.6/4.7 don't need planning), routines as the first programmatic application (bug-fix routines, proactive issue resolution), roles merging at Anthropic (designers/PMs/finance/data science all coding), context minimalism (minimal prompt, let model figure it out), hundreds of agents via agent view + Remote Control + voice mode, and loop as the next leap.

Files created:

- `sources/After Automation.md` — Source summary covering Agent Mode as a publishing format, core claim, and interactive engagement pattern.
- `sources/Reflecting on a year of Claude Code.md` — Source summary with 10 key points covering verification, auto mode, routines, roles merging, context minimalism, hundreds of agents, and the PC parallel.

Files updated:

- `concepts/AI-Native Work Archetypes.md` — Added "Roles Merging at Anthropic" section: designers, PMs, finance, and data science all coding. Strongest first-party evidence for the archetypes thesis. Added sources to frontmatter.
- `concepts/Self-Improving Skills.md` — Added "Every Mistake Becomes a Skill" section: Boris's human-triggered skill creation from failures as the most practical self-improvement pattern. Added source to frontmatter.
- `concepts/Parallel Agent Management.md` — Added three new sections: "Routines" (event-driven background agents), "Hundreds of Agents" (agent view, Remote Control, voice mode), and "Auto Mode" (permission model evolution). Added source to frontmatter.
- `concepts/Context Development Lifecycle.md` — Added "Context Minimalism: A Counterpoint" section: Boris and Cat advocate minimal prompts, tension with Debois's systematic context engineering. Resolution: engineering applies to retrieval, not instructions. Added source to frontmatter.
- `index.md` — Added 2 raw sources to frontmatter and Raw Sources; added 2 source summaries to Source Summaries.
- `log.md` — This entry.

Important decisions:

- Did not create new concept pages. Both sources reinforce existing concepts with stronger evidence rather than introducing new ideas.
- The "After Automation" essay is a different format (interactive Agent Mode) from the Lenny's Podcast source but covers the same thesis. Captured the format novelty (agent-readable publishing) without duplicating the argument.
- Recorded context minimalism as a tension with Context Development Lifecycle rather than a contradiction. The resolution (engineering for retrieval, minimalism for instructions) preserves both frameworks.
- Boris's "hundreds of agents" contradicts the Kilo Code "2–4 foreground" finding. Recorded as tooling-dependent: agent view + Remote Control + routines raise the practical limit.
- Boris's "auto mode replaces plan mode" tensions with the plan-then-execute pattern. Recorded as model-dependent: 4.6/4.7 plan implicitly.

Follow-ups:

- Boris's "every mistake becomes a skill" could become its own short concept if more sources adopt this framing. Currently it fits well as a section in Self-Improving Skills.
- The Agent Mode publishing format (companion repo + interactive prompts) could become a concept about agent-readable content if the pattern spreads.
- Context minimalism vs. context engineering is a live debate worth tracking as models improve and retrieval tooling matures.

## [2026-06-14] ingest | Making AI Work: Leadership, Lab, and Crowd (Ethan Mollick)

Ingested Ethan Mollick's One Useful Thing article on why individual AI productivity gains don't translate to organizational performance, and the Leadership/Lab/Crowd framework for closing the gap.

Raw source processed:

- `raw/Making AI Work Leadership, Lab, and Crowd.md` — Mollick's four facts (AI boosts work, 40% adoption, more gains available, companies not capturing them), the Leadership/Lab/Crowd framework, Secret Cyborgs (20% official vs 40% actual adoption), cross-functional "vibework" teams, org-specific benchmarking, and the organizational innovation gap thesis.

Files created:

- `sources/Making AI Work Leadership, Lab, and Crowd.md` — Source summary with four facts, three-lever framework, empirical evidence, and connections.

Files updated:

- `concepts/Enterprise AI Adoption Flywheel.md` — Added Leadership/Lab/Crowd framework as a more detailed model mapping to the flywheel stages. Added source to frontmatter.
- `concepts/AI-Native Engineering Organizations.md` — Added "The Organizational Innovation Gap" section with empirical adoption data and the Secret Cyborgs dynamic. Added source to frontmatter.
- `index.md` — Added new raw source to frontmatter, Raw Sources, and Source Summaries.

Important decisions:

- Did not create a new concept page for the Leadership/Lab/Crowd framework — it maps naturally to the existing Enterprise AI Adoption Flywheel concept as a more detailed model.
- Did not create a separate concept for "Secret Cyborgs" — it fits as evidence in both the flywheel and AI-native org pages.
- The Mollick article (May 2025) predates the agent era but aged well: the "build things that don't work yet" Lab advice predicted the rapid improvement cycle that made agents viable within months.

Follow-ups:

- The 20% → 40% adoption gap was measured Dec 2024–Apr 2025. Worth tracking whether the gap has widened or narrowed as agent tools became mainstream.
- The "vibework" pattern (dispersed cross-functional teams building in days) could become its own concept if more sources adopt this framing.
- Mollick's article references Manus agent capabilities — worth revisiting if the wiki later covers agent benchmarking.

## [2026-06-14] ingest | After Automation — full essay ingest from PDF

Discovered that the existing `raw/After Automation.md` was only the Agent Mode setup page (prompts and instructions), not the full essay. The PDF (`raw/after-automation.pdf`, 26 pages, 9.5MB) contains the complete article with substantial frameworks never captured in the wiki.

Raw source processed:

- `raw/after-automation.pdf` — Shipper's full essay: two modes of working with agents (employees vs. collaboration), named agents at Every (Claudie, Andy, Viktor, Fin with metrics), the human sandwich, Codex as OS for work, the 5-step cheap competence cycle, Zeno's Paradox of AI, chart psychosis, Senior Engineer benchmark (GPT-5.5 = 62/100), GDPval and smuggled intelligence, frame vs. framer, agents without agency (toddler thought experiment), AGI definition, Rabbi Hanokh parable.

Files created:

- `concepts/Zeno's Paradox of AI.md` — New concept: the 5-step cycle (cheap competence → rapid adoption → sameness → demand for difference → demand for experts), chart psychosis, benchmark saturation, frame vs. framer, smuggled intelligence.

Files updated:

- `sources/After Automation.md` — Complete rewrite from setup-page summary to full essay summary with all 19 sections, concrete evidence, and connections.
- `concepts/Software Economics.md` — Added "The Cheap Competence Cycle" section with the 5-step mechanism. Added source and Zeno's Paradox connection.
- `concepts/AI Slop and Garbage Collection.md` — Added "What Slop Actually Is" section with Shipper's precise definition ("visible sameness, repeated ad nauseam"). Added source and connections.
- `concepts/Harness Engineering Principles.md` — Added "Harnesses as the Expert Response to Cheap Competence" section. Added $62/token PowerPoint evidence and source.
- `concepts/Collaborative AI Engineering.md` — Added "The Human Sandwich" section with the collaboration pattern. Added source and connections.
- `concepts/AI agency.md` — Added "The Toddler Thought Experiment" section (agency = wanting for oneself). Added Connections section with Zeno's Paradox link.
- `index.md` — Added `raw/after-automation.pdf` to frontmatter; added Zeno's Paradox concept page; updated source summary description; added PDF to Raw Sources.
- `log.md` — This entry.

Important decisions:

- Kept `raw/After Automation.md` as-is (the setup page) because it is a distinct artifact — the agent-readable companion instructions. The PDF is the primary essay source.
- Created a dedicated Zeno's Paradox concept page rather than folding into Software Economics because the framework is original, self-contained, and has broad cross-wiki implications (benchmarks, slop, agency, harnesses).
- Did not create a separate concept page for "agents as employees" / "coworker agents" — the taxonomy fits as evidence in the source summary and connects to existing Agent Skills and AI-Native Engineering Organizations concepts.
- The toddler thought experiment was added to AI Agency rather than creating a new page because it extends the existing agent/agency distinction with a concrete illustration.

Follow-ups:

- The frame-vs-framer argument has implications for skill design: skills are frames, skill authors are framers. This could become a section in Skill Authoring Workflow if more sources adopt this framing.
- The $62/token PowerPoint deck is a concrete maintenance cost that should be cross-referenced with future token economics data.
- Shipper's AGI definition (economically viable continuous agent) is measurable — worth tracking against current system capabilities.
- The "smuggled intelligence" in benchmarks should inform how the wiki cites benchmark data going forward.

## [2026-06-27] ingest | How to keep AI spend flat — Brian Armstrong (Coinbase)

Processed a tweet by Coinbase CEO Brian Armstrong on keeping AI spend flat while token usage grows exponentially.

Raw source note processed:

- `raw/How to keep AI spend flat while token usage grows - Brian Armstrong.md` - Coinbase playbook: cheaper defaults (GLM 5.2, Kimi 2.7 via LLM gateway), prompt routing, cache awareness (5% → 60% hit rate), context hygiene, and visibility over friction. Claims nearly halved AI spend while token usage continued to grow.

Generated pages created:

- `sources/How to keep AI spend flat while token usage grows - Brian Armstrong.md` — Source summary with five-part playbook, metrics, and cross-links.

Generated pages updated:

- `concepts/Tokenmaxxing.md` — Added Armstrong's approach as the organizational counterweight to individual tokenmaxxing: enable high usage, manage cost through infrastructure. Added to Contradictions and Connections.
- `concepts/AI-Native Engineering Organizations.md` — Added "AI Cost Management as Infrastructure" section covering Coinbase's five-part playbook. Added to Connections.
- `index.md` — Added raw source to frontmatter and Raw Sources; added source summary to Source Summaries.
- `log.md`

Important decisions:

- Did not create a new concept page — the material fits naturally into Tokenmaxxing (cost vs. usage tension) and AI-Native Engineering Organizations (org-level operating model).
- Positioned "visibility over friction" as the key insight: engineers self-regulate when usage is visible, making caps unnecessary.
- The "humans shouldn't choose models" claim is notable and connects to the LLM Provider Selection concept but was not added there as it's a Coinbase-specific operational claim rather than general guidance.

Follow-ups:

- Track whether Coinbase's LLM gateway approach becomes a pattern adopted by other large engineering orgs.
- The 5% → 60% cache hit rate improvement is a concrete metric worth citing in future caching/optimization discussions.
- If more sources emerge on model routing as infrastructure, consider a dedicated concept page on prompt routing and model selection automation.

## [2026-07-01] ingest | Claude Sonnet 5 launch

Processed Anthropic's Claude Sonnet 5 launch announcement.

Raw source note processed:

- `raw/Introducing Claude Sonnet 5.md` - Anthropic's Sonnet 5: performance close to Opus 4.8 at lower prices, updated tokenizer, safety improvements over Sonnet 4.6, poorer cybersecurity than Opus 4.8, now default for Free/Pro plans.

Generated pages created:

- `sources/Introducing Claude Sonnet 5.md` — Source summary with pricing, benchmarks, safety, and the "narrowing gap" pattern analysis.

Generated pages updated:

- `concepts/The Compute Cost Tradeoff.md` — Added "The Narrowing Gap Pattern" section documenting the recurring pattern where mid-tier models absorb frontier capabilities within months at 40–60% of the price. Sonnet 5 as concrete evidence. Added to sources, connections, and contradictions.
- `index.md` — Added raw source to frontmatter and Raw Sources; added source summary to Source Summaries.
- `log.md`

Important decisions:

- Did not create a new concept page for "model tier convergence" — the pattern is documented within The Compute Cost Tradeoff as the "narrowing gap" section. If more sources accumulate on this pattern, it could become its own concept.
- Positioned Sonnet 5 as evidence for the recurring pattern (user's observation: "This keeps happening") rather than as a standalone model review.
- The updated tokenizer (1.0–1.35× more tokens per input) is notable for cost calculations — flagged in the source summary open questions.

Follow-ups:

- Track whether the narrowing gap pattern continues with future Sonnet/Opus releases and competing model families (GPT, Gemini).
- If the tokenizer change significantly affects real-world costs for coding workflows, update the AI Coding Plans concept page.
- The cybersecurity capability gap between Sonnet and Opus is a concrete example of where frontier models retain durable advantage — worth tracking if this pattern holds.

## [2026-07-01] research | LLM Prompt Caching

Researched prompt caching across Anthropic, OpenAI, and AWS Bedrock. Fetched current documentation from all three providers and synthesized into a cross-provider concept page.

Generated pages created:

- `concepts/LLM Prompt Caching.md` — Cross-provider synthesis covering mechanism, pricing, TTL, prompt structuring guidelines, production benchmarks, and reasoning token interaction.

Generated pages updated:

- `index.md` — Added new concept article entry.

Sources consulted (web fetches, not raw files):

- Anthropic prompt caching documentation (platform.claude.com/docs)
- OpenAI prompt caching documentation (developers.openai.com)
- OpenAI API pricing page (developers.openai.com/api/docs/pricing)
- Anthropic prompt caching blog post (claude.com/blog/prompt-caching)
- Anthropic extended thinking documentation
- OpenAI reasoning models documentation
- AWS Bedrock prompt caching documentation

Important decisions:

- Created a single cross-provider concept page rather than separate pages per provider because the core mechanism (KV cache reuse for identical prefixes) is the same, and the comparison table is more useful than isolated pages.
- Included Coinbase production data (5% to 60% cache hit rate) from the already-ingested Armstrong source as real-world benchmark evidence.
- Positioned reasoning token interaction as a distinct section because it is a common source of confusion (reasoning tokens are output, not input, so they do not benefit from caching).
- Did not create raw source notes for the web-fetched documentation pages because they are living documentation that changes frequently; the concept page captures the durable patterns.

Follow-ups:

- Track whether Anthropic's 1-hour TTL or OpenAI's 24-hour extended retention becomes the dominant pattern for agent workflows.
- If Google Gemini or other providers add prompt caching, expand the cross-provider comparison table.
- The Coinbase cache hit rate improvement (5% to 60%) is from a single data point; more production benchmarks would strengthen the guidance.

## [2026-07-01] query | LLM Effort Levels and Reasoning Budget Controls

Files created:
- `concepts/LLM Effort Levels and Reasoning Budget Controls.md`

Files updated:
- `index.md` (added concept entry)

Summary:

Researched Anthropic's `effort` parameter and OpenAI's `reasoning_effort` parameter from official documentation. Created a cross-provider concept page covering:

- Anthropic effort levels: `low`, `medium`, `high`, `xhigh`, `max` with model-specific guidance for Sonnet 5, Sonnet 4.6, Opus 4.7/4.8, and Fable 5.
- OpenAI reasoning effort levels: `none`, `minimal`, `low`, `medium`, `high`, `xhigh` with per-level use case guidance.
- Key difference: Anthropic's effort affects all tokens (text + tools + thinking); OpenAI's primarily controls reasoning chain depth.
- Both parameters are behavioral signals, not strict token budgets -- models adaptively allocate regardless of setting.
- Approximate token scaling: `low` ~1/5th of `high`, `medium` ~1/3rd of `high`, `xhigh` 1.5-3x of `high`, `max` 2-5x+ of `high`.
- On easy tasks (MMLU-level), effort level has minimal quality impact; on hard tasks (SWE-bench-level), higher effort matters significantly.
- Both providers bill reasoning/thinking tokens as output tokens.

Important decisions:

- Created a single cross-provider concept page rather than separate pages per provider, following the same pattern as the LLM Prompt Caching page.
- Included the full effort level definition tables from both providers' official docs.
- Did not create raw source notes for web-fetched documentation pages because they are living documentation; the concept page captures the durable patterns.
- Token scaling ratios are approximate (documented behavior, not published exact multipliers).

Follow-ups:

- Neither provider publishes exact token multipliers between effort levels. If community benchmarks emerge with precise measurements, update the scaling table.
- Track how effort interacts with prompt caching efficiency across both providers.
- Monitor whether effort levels converge to a standard or continue to diverge across providers.

## [2026-07-01] research | LLM Context Window Degradation

Researched context window degradation and context rot across academic benchmarks and provider documentation.

Files created:
- `raw/research-context-window-degradation.md` -- Comprehensive research compilation with RULER benchmark data, Lost in the Middle findings, attention sink mechanism, model-by-model comparison, provider best practices, and academic citations.

Files updated:
- `concepts/Context Rot.md` -- Major expansion: added RULER benchmark table (5 models with 4K/128K scores), Lost in the Middle findings, mechanism section (attention dilution, positional encoding limits, training distribution bias, attention sink disruption, retrieval vs. reasoning), practical thresholds, academic citations, and provider-reported performance data.
- `index.md` -- Added raw source to frontmatter and Raw Sources section; updated Context Rot description.

Key findings:

- **No universal "60% drop" threshold exists.** The 60% figure from Kilo Code is a practical observation for coding agents, not a benchmark-derived constant. Actual degradation depends on model capability, task type, and information position.
- **RULER benchmark (46 models):** Top models (Gemini-1.5-pro, Jamba-1.5-large) lose only 1-2 points across 4K-128K. GPT-4 loses 15 points. Many open models lose 30-95+ points. Effective context is typically 25-50% of claimed context for weaker models.
- **Lost in the Middle:** U-shaped performance curve -- information at beginning and end is retrieved more reliably than in the middle.
- **Mechanisms:** Attention dilution (n-squared scaling), positional encoding interpolation limits, training distribution bias, and attention sink disruption.
- **Provider strategies:** Anthropic recommends compaction, sub-agents, and structured note-taking. OpenAI recommends prompt caching and RAG. Google recommends placement at end of prompt and context caching.

Important decisions:

- Treated the "60% quality drop" claim from Kilo Code as a practical observation rather than a universal benchmark, because RULER data shows highly variable degradation across models.
- Did not create separate concept pages for individual benchmarks (RULER, LongBench, Lost in the Middle) -- the data is synthesized into the Context Rot concept page and the raw research file.
- Academic citations are included in both the raw research file and the Context Rot concept page for traceability.

Follow-ups:

- Track RULER benchmark results for newer models (Claude Sonnet 5, GPT-4.1, Gemini 2.0) as they become available.
- Investigate whether attention sink patterns can be deliberately exploited for better context utilization.
- Monitor if any provider publishes explicit degradation curves for their production models.
