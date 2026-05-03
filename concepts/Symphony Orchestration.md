---
type: concept
created: 2026-05-03
updated: 2026-05-03
status: active
sources:
  - "raw/An open-source spec for Codex orchestration Symphony.md"
tags: [orchestration, symphony, issue-tracker, multi-agent, openai, linear]
---

# Symphony Orchestration

## Key Points

Symphony is an open-source spec for Codex orchestration that turns an issue tracker (like Linear) into a control plane for coding agents. Every open task gets a dedicated agent, agents run continuously, and humans review the results. It achieves a 500% increase in landed pull requests on some teams by eliminating the bottleneck of human context switching.

## The Interactive Agent Ceiling

Coding agents are still interactive tools. Engineers can comfortably manage 3-5 Codex sessions at a time before context switching becomes painful. Beyond that:

- Engineers forget which session is doing what
- They jump between terminals to nudge agents back on track
- They debug long-running tasks that stalled halfway through

The agents are fast, but human attention is the system bottleneck. Teams effectively built a team of extremely capable junior engineers, then assigned human engineers to micromanaging them.

## Issue Tracker as Control Plane

Symphony decouples work from sessions and pull requests. Instead of supervising agents directly, agents pull work from the task tracker:

- Each open Linear issue maps to a dedicated agent workspace
- Symphony continuously watches the task board, ensuring every active task has an agent running
- If an agent crashes or stalls, Symphony restarts it
- If new work appears, Symphony picks it up automatically

## Key Workflow Patterns

### Ticket Statuses as State Machine

Workflows are organized around ticket statuses. Symphony uses the task manager as a state machine, but agents are given **objectives** rather than strict transitions — much like a good manager assigning a goal to a direct report.

### Complex Work Decomposition

- File a task asking the agent to analyze the codebase and produce an implementation plan
- Once approved, the agent generates a tree of tasks with dependencies (a DAG)
- Agents only start working on unblocked tasks, so execution unfolds naturally in parallel
- Example: React upgrade blocked on Vite migration — agents started React work only after Vite was complete

### Agents Creating Work

During implementation or review, agents notice improvements outside scope (performance issues, refactoring opportunities) and file new issues. Many of these follow-up tasks also get picked up by agents automatically.

## The Cognitive Cost Shift

When engineers no longer spend time supervising Codex sessions, the economics of code changes completely change:

- The perceived cost of each change drops (no human effort driving implementation)
- It becomes trivial to spin up speculative tasks — try an idea, explore a refactor, test a hypothesis
- Non-engineers (PMs, designers) can file feature requests directly without managing sessions
- Engineers focus on a single hard problem instead of context-switching across small tasks

## Symphony Building Symphony

Symphony is technically just a `SPEC.md` file — a definition of the problem and intended solution. The reference implementation was built by Codex in Elixir (chosen for its concurrency primitives), and the spec was validated by having Codex implement it in TypeScript, Go, Rust, Java, and Python to identify ambiguities.

## Symphony Spec Architecture

The spec defines these abstraction layers:

1. **Policy Layer** (repo-defined) — `WORKFLOW.md` prompt body and team-specific rules
2. **Configuration Layer** (typed getters) — Parses front matter into typed runtime settings
3. **Coordination Layer** (orchestrator) — Polling loop, issue eligibility, concurrency, retries
4. **Execution Layer** (workspace + agent subprocess) — Filesystem lifecycle, coding-agent protocol
5. **Integration Layer** (Linear adapter) — API calls and normalization for tracker data
6. **Observability Layer** (logs + optional status surface) — Operator visibility

### Core Components

- **Workflow Loader** — Reads `WORKFLOW.md`, parses YAML front matter and prompt body
- **Orchestrator** — Owns the poll tick, in-memory runtime state, dispatch/retry/reconciliation decisions
- **Workspace Manager** — Maps issue identifiers to workspace paths, manages lifecycle hooks
- **Agent Runner** — Creates workspace, builds prompt, launches coding agent app-server

### State Machine

Issues progress through: `Unclaimed` → `Claimed` → `Running` → `RetryQueued` → `Released`

The orchestrator manages global concurrency limits, per-state concurrency limits, exponential backoff retries, and stall detection.

### Codex App Server Integration

Symphony uses Codex in [app server mode](https://developers.openai.com/codex/app-server/) — a headless JSON-RPC API over stdio for starting threads, running turns, and handling approvals. This is more scalable than CLI or tmux sessions.

## Lessons and Tradeoffs

- **Lost mid-flight nudging** — Moving from interactive to ticket-level supervision means you can't course-correct during execution. Failures revealed gaps that were addressed with better guardrails
- **Not every task fits** — Ambiguous problems or work requiring strong judgment still need interactive sessions
- **Rigid state machines don't work** — Early versions only asked agents to implement tasks. Giving agents broader tools (gh CLI, CI log reading) let them handle PR management, conflict resolution, and more
- **Spec-driven development works** — Codex built Symphony from its own spec, iteratively improving both

## Connections

- [[concepts/Harness Engineering Principles]] — Symphony extends single-agent harness principles to multi-agent orchestration.
- [[concepts/Agent Frameworks and Orchestration]] — Symphony is a concrete orchestration pattern built on top of existing agent SDKs.
- [[concepts/Agent Skills]] — Skills are used within Symphony workspaces to give agents domain-specific capabilities.
- [[concepts/Collaborative AI Engineering]] — Symphony coordinates agents via issue trackers; collaborative engineering addresses the human alignment gap that orchestration alone doesn't solve.
- [[concepts/Replacing Code with Skills]] — Symphony itself is a spec (`SPEC.md`) implemented by agents; the worktree skill demonstrates the same pattern of prompt-as-implementation at a smaller scale.

## Source

- [[raw/An open-source spec for Codex orchestration Symphony]]
