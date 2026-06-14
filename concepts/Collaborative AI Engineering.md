---
type: concept
created: 2026-05-03
updated: 2026-06-14
status: active
sources:
  - "raw/Collaborative AI Engineering One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md"
  - "raw/Running an AI-native engineering org.md"
  - "raw/after-automation.pdf"
tags: [collaboration, alignment, multiplayer, agent-collaboration, github-next, ace]
---

# Collaborative AI Engineering

## Key Points

Collaborative AI Engineering addresses the alignment gap that emerges when individual agent productivity outpaces team coordination. When everyone directs agents in isolation with no shared context, teams get duplicate work, conflicting changes, surprise features, and coordination debt. The bottleneck shifts from "how to build it" to "should we build it" — and alignment must happen before agents start working, not after.

## The Solo Productivity Trap

The popular narrative of one developer with a fleet of agents doing the work of an entire team is fundamentally flawed. Software is not made by one person in a vacuum — it is a team sport. Scaling individual output without coordination doesn't solve team problems; it makes them worse. More individual output without alignment is "nine women make a baby in one month" logic.

## Alignment Is the New Bottleneck

When implementation becomes fast, cheap, and increasingly high-quality, the hard question is no longer *how* to build something but *whether* it should be built. When production is cheap, **opportunity cost becomes the real cost** — you can't build everything, and whatever you pick comes at the cost of everything else.

### Why Existing Tools Fail

Traditional coordination tools (GitHub PRs, Slack, Jira, Linear) were not designed for agentic development. The development process used to have alignment touchpoints throughout — planning discussions, draft PR reviews, team feedback — because implementation was slow enough to allow conversation. But the implementation window has now collapsed:

- The time between logging an issue and an agent opening a PR is minutes
- Agent plan modes are local and unshared with the team
- The weight of alignment falls entirely on the PR, which was never designed for that role
- Most checkpoints now happen *after* implementation, when it's too late

### Consequences of Speed Without Alignment

- **Wasted work** — Features nobody asked for that don't solve real problems
- **Post-implementation rework** — Critical feedback arrives after the code is done, requiring complete rewrites
- **Coordination debt** — Merge conflicts from agents touching the same files, duplicate work when two people independently tackle the same task
- **Review backlog** — Giant stacks of PRs with no context for reviewers

## ACE: Agent Collaboration Environment

GitHub Next built a research prototype called **ACE** (Agent Collaboration Environment) to explore solutions:

### Sessions as Multiplayer Workspaces

Each session is both a multiplayer chat (like Slack) and a sandboxed micro VM in the cloud on its own Git branch. Multiple humans and agents share the same session, prompting the same agent, seeing the same live preview, and running the same terminal commands.

### Key Design Decisions

- **Shared prompting** — Any team member can prompt the agent; the entire conversation history is fed as agent context
- **Cloud VMs, not local machines** — Close your laptop, work continues. No "doesn't work on my machine" problems. No need for always-on local hardware
- **Collaborative plan editing** — For complex features, the agent writes a plan and the team edits it together in real-time before execution
- **Instant session switching** — Jump into any teammate's session to see what they're doing, including full prompting history
- **Accessible interface** — Non-developers (PMs, designers, customer support) can participate because it's chat-like, not a terminal

### Proactive Agents

Instead of humans checking what's happening, agents summarize what teammates have been working on, prompt you to pick up unfinished work, and notify you when someone is about to extend a feature you originally built. When all conversations around code are available to agents, they gain access to a **social information fabric** that helps keep the team oriented.

## The Human Sandwich

Dan Shipper describes the core collaboration pattern at Every: "You're responsible for managing the agents at the start and end of each one of their tasks, making sure it's done well, and finding the next piece of work to do. Kieran calls this the human 'sandwich' — we're the bread on either end of the AI's work."

The engineers at Every spend all day going back and forth with agents: planning features, reviewing work, tuning the system. This extends beyond coding — Shipper composes writing in Proof inside Codex (with subagents for drafts, research, copy editing) and does email in Cora inside Codex's in-app browser.

The human sandwich is a concrete operationalization of the alignment problem: the human sets the frame at the start and evaluates the result at the end. The agent executes in between.

Source: `raw/after-automation.pdf`.

## The Philosophical Shift

### Reclaim Time for Craftsmanship

Before agents, teams shipped software they weren't proud of because implementation consumed all the time and energy. Agents gift that time back. The opportunity is to make *better* software through more rigorous thinking and planning, not just a giant pile of the same mediocre output faster.

### Quality Is the New Differentiator

The bar is being set much higher. Craftsmanship separates exceptional software from "vibe-coded slop." But craft still costs time — teams need to **do fewer things better**, which requires strong alignment.

### The Goal

Agentic tools should create environments where teams can *think rigorously together* about hard problems, get aligned faster, and build a few exceptional things rather than a thousand mediocre ones.

## Org Norms for Faster Teams

Fiona Fung's "Running an AI-native engineering org" adds concrete operating norms to this collaboration problem. When code generation is cheap, teams can use prototypes and PR variants as shared debate artifacts, but they must prevent "last person to check in wins" culture. Planning can become more just-in-time, while alignment, verification, product sense, and explicit process cleanup become more important.

Source: `raw/Running an AI-native engineering org.md`.

## Connections

- [[concepts/AI-Native Engineering Organizations]] — Concrete management and process patterns for AI-native teams.
- [[concepts/Harness Engineering Principles]] — Harness engineering optimizes single-agent environments; collaborative engineering extends to team-level alignment.
- [[concepts/Symphony Orchestration]] — Symphony coordinates agents via issue trackers; collaborative engineering coordinates humans *and* agents via shared workspaces.
- [[concepts/Agent Legibility]] — Making codebases legible to agents is one side; making team context legible to both humans and agents is the other.
- [[concepts/Agentic Engineering vs Vibe Coding]] — Agentic engineering at team scale requires alignment infrastructure, not just individual discipline.
- [[sources/After Automation]] — The "human sandwich" pattern as a concrete collaboration model.
- [[concepts/Replacing Code with Skills]] — The best-of command is a form of collaborative comparison: humans evaluate multiple model outputs on the same task and compose the best pieces together.

## Source

- [[raw/Collaborative AI Engineering One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]]
- [[raw/Running an AI-native engineering org]]
