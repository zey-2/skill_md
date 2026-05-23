---
type: concept
created: 2026-05-01
updated: 2026-05-01
status: active
sources:
  - "raw/VILA-LabDive-into-Claude-Code A Systematic Analysis and Discussion of Claude Code for Designing Today's and Future AI Agent Systems.md"
tags: [claude-code, architecture, harness-engineering, agent-design, safety, context-management]
---

# Claude Code Architecture Deep Dive

## Key Points

VILA-Lab's **Dive into Claude Code** (arXiv 2604.14228) is a source-level architectural analysis of Claude Code v2.1.88 (~1,900 TypeScript files, ~512K lines). Its central finding: **only 1.6% of Claude Code's codebase is AI decision logic; the other 98.4% is deterministic infrastructure** (permission gates, context management, tool routing, recovery).

## Core Architecture

### Four Design Questions

| Question | Claude Code's Answer |
|----------|---------------------|
| Where does reasoning live? | Model reasons; harness enforces. ~1.6% AI, 98.4% infrastructure. |
| How many execution engines? | One `queryLoop` for all interfaces (CLI, SDK, IDE). |
| Default safety posture? | Deny-first: deny > ask > allow. Strictest rule wins. |
| Binding resource constraint? | ~200K (older) / 1M (Claude 4.6 series) context window. 5 compaction layers before every model call. |

### 5-Layer Decomposition

User → Interfaces → Agent Loop → Permission System → Tools → State & Persistence → Execution Environment

### The Agentic Query Loop

- **ReAct-pattern while-loop**: assemble context → call model → dispatch tools → check permissions → execute → repeat
- **9-step pipeline per turn**: Settings resolution → State init → Context assembly → 5 pre-model shapers → Model call → Tool dispatch → Permission gate → Tool execution → Stop condition
- **5 compaction shapers** (cheapest first): Budget Reduction → Snip → Microcompact → Context Collapse → Auto-Compact
- **Two execution paths**: `StreamingToolExecutor` (latency-optimized) and fallback `runTools` (concurrent-safe vs exclusive classification)
- **5 stop conditions**: No tool use, max turns, context overflow, hook intervention, explicit abort

## Safety and Permissions

### 7 Permission Modes (Graduated Trust Spectrum)

`plan` → `default` → `acceptEdits` → `auto` (ML classifier) → `dontAsk` → `bypassPermissions` (+ internal `bubble`)

### 7 Independent Safety Layers

From tool pre-filtering through shell sandboxing to hook interception. **Deny-first**: a broad deny always overrides a narrow allow. **Permissions are never restored on resume** — trust is re-established per session.

### Shared Failure Modes

Defense-in-depth degrades when layers share constraints. Per-subcommand parsing causes event-loop starvation — commands exceeding 50 subcommands bypass security analysis entirely to prevent REPL freeze.

### Pre-Trust Execution Window

Hooks and MCP servers execute during initialization **before** the trust dialog appears, creating a structurally privileged attack window outside the deny-first pipeline (2 patched CVEs share this root cause).

## Extensibility

**Four mechanisms at graduated context costs:** Hooks (zero) → Skills (low) → Plugins (medium) → MCP (high)

**Three injection points** in the agent loop:
- **assemble()** — what the model sees
- **model()** — what it can reach
- **execute()** — whether/how actions run

**27 hook events** across 5 categories with 4 execution types (shell, LLM-evaluated, webhook, subagent verifier)

**Plugin manifest** accepts 10 component types: commands, agents, skills, hooks, MCP servers, LSP servers, output styles, channels, settings, user config

## Context and Memory

**9 ordered sources** build the context window. CLAUDE.md instructions are delivered as **user context** (probabilistic compliance), not system prompt (deterministic).

**4-level CLAUDE.md hierarchy:** Managed (`/etc/`) → User (`~/.claude/`) → Project (`CLAUDE.md`, `.claude/rules/`) → Local (`CLAUDE.local.md`, gitignored)

**Memory is file-based** (no vector DB) — fully inspectable, editable, version-controllable. LLM-based scan of memory-file headers selects up to 5 relevant files.

## Subagent Delegation

**6 built-in types** (Explore, Plan, General-purpose, Guide, Verification, Statusline) + custom agents via `.claude/agents/*.md`

**Sidechain transcripts**: only summaries return to parent (parent's context is *protected* from subagent verbosity)

**Three isolation modes:** worktree, remote, in-process. Coordination via POSIX `flock()`.

**SkillTool vs AgentTool:** SkillTool injects into current context (cheap). AgentTool spawns isolated context (expensive, but prevents context explosion).

## Session Persistence

Three channels: append-only JSONL transcripts, global prompt history, subagent sidechains. Chain patching records `headUuid`/`anchorUuid`/`tailUuid` — nothing is destructively edited on disk. File-history checkpoints for `--rewind-files`.

## Values → Principles → Implementation

| Value | Core Idea |
|-------|-----------|
| **Human Decision Authority** | Humans retain control via principal hierarchy. Restructure boundaries, not add warnings. |
| **Safety, Security, Privacy** | System protects even when human vigilance lapses. 7 independent safety layers. |
| **Reliable Execution** | Gather-act-verify loop. Graceful recovery. |
| **Capability Amplification** | "A Unix utility, not a product." 98.4% deterministic infrastructure. |
| **Contextual Adaptability** | CLAUDE.md hierarchy, graduated extensibility, trust trajectories that evolve. |

**13 Design Principles:** deny-first, graduated trust spectrum, defense in depth, externalized programmable policy, context as scarce resource, append-only durable state, minimal scaffolding/maximal harness, values over rules, composable multi-mechanism extensibility, reversibility-weighted risk assessment, transparent file-based config, isolated subagent boundaries, graceful recovery.

## Design Guide for Agent Builders

The paper extracts 6 key design decisions every production agent must navigate:

| Decision | Key Insight |
|----------|------------|
| **Reasoning placement** | As models converge, the harness becomes the differentiator. |
| **Safety posture** | Defense-in-depth fails when layers share failure modes. |
| **Context management** | Design for context scarcity from day one. Graduated > single-pass. |
| **Extensibility** | Not all extensions need to consume context tokens. |
| **Subagent architecture** | Agent teams in plan mode cost ~7× tokens. Summary-only returns prevent context blow-up. |
| **Session persistence** | Never restore permissions on resume. Auditability > query power. |

## Curated Resources Map

The repo also curates: official Anthropic research/engineering blogs, architecture analyses from multiple reverse-engineering projects, open-source reimplementations (Rust port, Python rebuild, buildable research forks), learning guides, harness engineering courses, and a broad map of notable 2025–2026 AI agent projects (OpenClaw, OpenCode, Hermes Agent, MiroFish, nanobot, OpenHarness, OpenAI Symphony, karpathy/autoresearch, CLI-Anything, etc.).

## Relationship to This Wiki

This article provides the most detailed source-level view of a coding agent's internal architecture available in this wiki. It directly informs:
- [[concepts/Agent Skills]] — explains the Hooks → Skills → Plugins → MCP extensibility spectrum at source level, showing where skills sit in Claude Code's architecture
- [[concepts/Agent SDKs and Codex Automation]] — explains the `queryLoop` that the Agent SDK exposes programmatically
- [[concepts/MCP and Tool-Integration Architecture]] — shows how MCP fits into the 5-step tool pool assembly and the execute() injection point
- [[concepts/Agent Frameworks and Orchestration]] — provides a concrete implementation reference for the harness design principles discussed abstractly there
- [[concepts/Discovery Conventions]] — explains the 4-level CLAUDE.md hierarchy and skill/plugin discovery at source level
- [[concepts/Skill Distribution and Installation]] — shows how Skills fit into the extensibility spectrum (Hooks → Skills → Plugins → MCP)
- [[concepts/Validation and Evaluation]] — safety layers and permission modes provide concrete examples of governance boundaries

## Source

- VILA-Lab/Dive-into-Claude-Code GitHub repo and arXiv paper 2604.14228
- [[raw/VILA-LabDive-into-Claude-Code A Systematic Analysis and Discussion of Claude Code for Designing Today's and Future AI Agent Systems]]
