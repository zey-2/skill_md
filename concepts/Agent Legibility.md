---
type: concept
created: 2026-05-03
updated: 2026-05-03
status: active
sources:
  - "raw/Harness engineering leveraging Codex in an agent-first world.md"
tags: [agent-legibility, context-management, repository-design, openai]
---

# Agent Legibility

## Key Points

Agent legibility means organizing a codebase so agents can reason about the full business domain directly from the repository itself. Anything an agent cannot access in-context effectively doesn't exist. Knowledge in Google Docs, Slack, or people's heads is invisible to the agent — the same way it would be unknown to a new hire.

## Repository as the System of Record

The repository's knowledge base lives in a structured `docs/` directory treated as the system of record. A short `AGENTS.md` (~100 lines) serves as a table of contents with pointers to deeper sources of truth:

```
AGENTS.md
ARCHITECTURE.md
docs/
├── design-docs/        # Indexed design documents with verification status
├── exec-plans/         # Active and completed plans, tech debt tracker
├── generated/          # Auto-generated docs (e.g., db-schema.md)
├── product-specs/      # Indexed product specs
├── references/         # External docs converted to llms.txt format
├── DESIGN.md
├── FRONTEND.md
├── PLANS.md
├── PRODUCT_SENSE.md
├── QUALITY_SCORE.md
├── RELIABILITY.md
└── SECURITY.md
```

## Progressive Disclosure for Agents

Agents start with a small, stable entry point and are taught where to look next, rather than being overwhelmed up front. This enables:

- **Plan artifacts are versioned** — Active plans, completed plans, and technical debt are co-located in the repo
- **Knowledge is indexed** — Design documents include core beliefs, verification status, and decision logs
- **Documentation is mechanically enforced** — Dedicated linters and CI jobs validate that the knowledge base is up to date and cross-linked
- **Doc-gardening agents** scan for stale documentation and open fix-up pull requests

## The AGENTS.md Anti-Pattern

The "one big AGENTS.md" approach fails in predictable ways:

- **Context is scarce** — A giant instruction file crowds out the task, the code, and relevant docs
- **Too much guidance becomes non-guidance** — When everything is important, nothing is
- **It rots instantly** — A monolithic manual becomes a graveyard of stale rules
- **It's hard to verify** — A single blob doesn't lend itself to mechanical checks

Instead, `AGENTS.md` should be the table of contents, not the encyclopedia.

## Agent-Optimized Architecture

Because the repository is agent-generated, it's optimized first for the agent's legibility:

- **"Boring" technologies** are preferred — easier for agents to model due to composability, API stability, and training set representation
- **Internal reimplementation** can be cheaper than opaque upstream libraries — e.g., implementing a map-with-concurrency helper instead of pulling `p-limit` for tighter OpenTelemetry integration
- **Strict architectural boundaries** — Each business domain divided into fixed layers (Types → Config → Repo → Service → Runtime → UI) with validated dependency directions
- **Custom linters** inject remediation instructions into agent context

## Application Legibility

Beyond code legibility, agents need to see and interact with the application itself:

- **Chrome DevTools Protocol** wired into the agent runtime — agents can drive the app, take DOM snapshots and screenshots, navigate, and validate UI behavior
- **Per-worktree bootable app** — Codex can launch one instance per change
- **Local observability stack** — Ephemeral per worktree, with Vector fanning logs/metrics/traces to Victoria Logs, Metrics, and Traces
- **PromQL/LogQL/TraceQL access** — Prompts like "ensure service startup completes in under 800ms" become tractable

## Connections

- [[concepts/Progressive Disclosure]] — Agent legibility uses progressive disclosure to manage context efficiently.
- [[concepts/Harness Engineering Principles]] — Legibility is a core harness engineering technique.
- [[concepts/Skill Repository Architecture]] — Skills are one form of repository knowledge that agents can discover.
- [[concepts/Replacing Code with Skills]] — Skills encode rules in markdown that agents can read and follow; worktree skills make agent isolation state legible to the UI and other agents.

## Source

- [[raw/Harness engineering leveraging Codex in an agent-first world]]
