---
type: concept
created: 2026-05-03
updated: 2026-06-14
status: active
sources:
  - "raw/Harness engineering leveraging Codex in an agent-first world.md"
  - "raw/Harness Engineering How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"
  - "raw/Tokenmaxxing How Top Builders Use AI To Do The Work Of 400 Engineers.md"
  - "raw/Running an AI-native engineering org.md"
  - "raw/new_economics_of_software.md"
  - "raw/Superpowers How Jesse Built the 1 AI Claude Code  Codex Plugin — and Stopped Writing Code.md"
  - "raw/How the engineer behind Claude Cowork actually uses Claude  Felix Rieseberg (Anthropic).md"
  - "raw/after-automation.pdf"
tags: [harness-engineering, agent-first, code-is-free, scarcity, software-economics, openai]
---

# Harness Engineering Principles

## Key Points

Harness engineering is the discipline of building the environments, guardrails, and feedback loops that enable coding agents to do reliable work. When implementation is no longer the bottleneck (code is free), the scarce resources shift to human time, human/model attention, and model context windows. Engineers become staff-level architects who design systems rather than write code.

## Code Is Free

Implementation capacity is effectively infinite. The models can produce, maintain, refactor, and delete code at a scale that makes code itself no longer a scarce resource. This means:

- All P3 tasks can be kicked off in parallel immediately
- Internal tools can have full i18n, accessibility, and polish from day one
- Large-scale migrations can be completed by firing 15 agents simultaneously
- Code becomes a disposable build artifact — like compiled x86 instructions

The constraint is no longer "can we build this?" but "can we specify what good looks like well enough for the agent to build it?"

## Scarce Resources

In an agent-first workflow, three resources remain scarce:

1. **Human time and attention** — The highest-leverage activity is defining work, prioritizing, and validating outcomes
2. **Model attention** — What the model focuses on during a turn
3. **Model context window** — Tokens available for instructions, code, and reasoning

Every harness design decision should optimize for preserving these scarce resources. When code is free, spending human time on a P2 task that an agent could handle is the real cost.

## The Engineer as Staff-Level Architect

Every engineer with agents becomes a staff engineer. The role shifts from:
- Writing code → Defining work and success criteria
- Reviewing PRs → Encoding guardrails that prevent classes of errors
- Managing implementations → Managing systems, delegation, and orchestration

The skill set shifts toward systems thinking, system design, and delegation.

## Defining "A Good Job"

Agents have seen trillions of lines of code making every possible choice of non-functional requirements. It's the human's job to specify which choices are acceptable:

- Write down non-functional requirements explicitly (timeouts, retries, error handling patterns)
- Document what good code review looks like per persona (security, reliability, scalability)
- Use failing tests and lints with remediation instructions, not just error messages
- Don't accept slop — take short-term velocity hits to encode guardrails permanently

The Superpowers workflow makes this concrete at the individual-developer level. The human's highest-leverage job becomes defining the spec, acceptance criteria, and proof of completion. Implementation agents can then work on small tasks, while fresh review agents compare the result against the spec. The source's shorthand is that specs matter more than code review line-by-line; the more precise reading is that the spec is the artifact that makes generated code governable.

## Prompt Injection via Infrastructure

A good harness surfaces the right instructions at the right time:

- **AGENTS.md and docs** → Persistent guidance in the repository
- **Reviewer agents** → Persona-specific review (security, reliability, QA) on every push
- **Custom lints** → Error messages that include remediation steps as prompts
- **Test failures** → Source-level tests (e.g., file size limits) that adapt the codebase to model constraints
- **CI gates** → Just-in-time instructions that fire after the agent has done the work

The key insight: don't frontload all instructions. Let the agent prototype, then enforce constraints at lint/test time when the agent can see both the work it has done and the requirements simultaneously.

## LLMs as Fuzzy Compilers

Code in an agent-first repository is like compiled output from an LLM compiler. All the context, guardrails, and documentation are optimization passes that constrain which code is acceptable. Swapping models is like changing the code generation backend (LLVM to Cranelift) — the constraints should still produce valid output regardless of which model generates it.

## Every Human Interaction Is a Harness Failure

If a human must type "continue" to an agent, the harness failed to provide enough context for the agent to reach completion on its own. The goal is to define work well enough that agents can run 24/7 without human babysitting.

## Tokenmaxxing Needs Harnesses

The Tokenmaxxing source reinforces that abundant model work is useful only when the workflow can absorb it. More tokens can buy deeper research, more role-specific reviews, more generated tests, and more automated QA. But without a harness that routes those passes into acceptance criteria, test suites, reviewer agents, and reusable skills, the extra output becomes a larger verification burden.

Jesse Vincent's orchestrator pattern is a small-scale harness: brainstorming creates intent, spec review checks the target, planning decomposes work, TDD defines pass/fail targets, implementation agents edit the code, and ephemeral review agents verify conformance. This loop turns abundant model work into controlled progress rather than a flood of unreviewed changes.

## Org Processes as Harnesses

Fiona Fung's "Running an AI-native engineering org" talk extends harness thinking from repo infrastructure to team process. Planning, review, ownership, hiring, onboarding, and org shape are all part of the harness. When coding is no longer the slow part, stale processes can become the new failure mode; teams need explicit permission to automate or remove them.

## Async Design and Output-Based Trust

Felix Rieseberg adds two harness insights from building Claude Cowork and Claude Code Desktop:

**Async as a design principle.** Products with built-in latency (like agent execution) should embrace asynchrony rather than fight it. Users are comfortable waiting if the end quality is high. The Cowork interface deliberately lets users continue other work while the agent runs in the background — it chitchats and shows progress rather than demanding attention. This is a harness choice: the human should not watch the agent work; the agent should do annoying things in the background to free up the human's creative energy.

**Output-based trust.** Rieseberg describes moving from "reading every single line that Claude writes" to "only judging it on its impact." This is a harness maturity pattern: early users inspect the process; experienced users evaluate the outcome. The harness must be reliable enough that the human can step away. This connects to the "every human interaction is a harness failure" principle — if you need to supervise closely, the spec or guardrails are insufficient.

## The Biggest Gap: Problem Recognition, Not Capability

Rieseberg observes that the biggest barrier to AI adoption is not model capability — "it is literally people being able to understand that almost any problem can go into these tools." This is a harness design challenge: the human-model interface needs to make it obvious which problems are solvable, not just powerful when a problem is already framed.

The practical advice is simple: "Whenever you do something that you find annoying and you're not enjoying and it doesn't feel creative — that is a good time to pause for a second and wonder, is there a way I can use AI to do this?" This is the [[concepts/Anti-To-Do List and Abstraction Layering]] pattern in practice.

## Harnesses as the Expert Response to Cheap Competence

Shipper's "After Automation" provides the mechanism: when AI floods the system with cheap competence, human experts move in two directions. Some use AI to do bigger work; others "build systems that absorb and leverage the flood of new work: review queues, evals, harnesses, repo rules, Claude and Codex instruction files, continuous integration (CI), permissions, and workflows that turn first attempts into great work."

This is exactly what harness engineering describes. The harness is the expert response to the slop cycle: when everyone can generate code, the scarce work becomes defining what good looks like and building systems that enforce it.

Concrete cost evidence: Every's PowerPoint automation = 24 skills + 18 scripts + $62 in tokens per deck. The maintenance burden of agent systems is itself a harness engineering challenge.

Source: `raw/after-automation.pdf`.

## Economic Framing: Scarcity to Abundance

Max Buckley's "New Economics of Software" frames harness engineering's "code is free" insight as a broader economic shift. The collapse of development costs means SaaS moats built on code alone erode — competitive advantage moves to brand, data, ML models, and integration. Bottlenecks shift from implementation to attention and governance: any idea can be built quickly, so the scarce resource becomes discernment (which ideas matter) and validation (can humans evaluate agent output fast enough). This economic lens reinforces why harness design is the critical skill — it is the infrastructure that makes abundance usable rather than overwhelming.

## Connections

- [[concepts/Tokenmaxxing]] — Aggressive token spend needs tests, review, and reusable workflows to compound.
- [[concepts/AI-Native Engineering Organizations]] — Org-level harness design for planning, review, hiring, and process cleanup.
- [[concepts/Agentic Engineering vs Vibe Coding]] — Harness engineering operationalizes agentic engineering at scale.
- [[concepts/Agent Legibility]] — Harnesses make applications and codebases legible to agents.
- [[concepts/Progressive Disclosure]] — Good harnesses surface instructions just-in-time, not all at once.
- [[concepts/Agent Skills]] — Skills are one mechanism for encoding reusable harness patterns.
- [[concepts/Symphony Orchestration]] — Symphony extends harness principles from single-agent to multi-agent orchestration.
- [[concepts/Collaborative AI Engineering]] — Harness engineering optimizes single-agent environments; collaborative engineering extends to team-level alignment.
- [[concepts/Replacing Code with Skills]] — The cursor worktree skill shows a harness boundary shift: hard-coded filesystem isolation replaced by prompt-based instructions backed by evals.
- [[concepts/Context Development Lifecycle]] — Debois frames harness engineering observability as the Observe stage of the context lifecycle, where logs, traces, and feedback close the improvement loop.
- [[concepts/Context Observability and Feedback]] — Covers the specific observability patterns (agent logs, production monitoring, context filters) that complement harness guardrails.
- [[concepts/Neuro-Symbolic AI Architecture]] — Deterministic guardrails (lints, tests, CI gates) are the symbolic layer around the LLM's neural generation.
- [[concepts/Tool Assembly as a Skill]] — Assembling harness tools (AGENTS.md, reviewer agents, custom lints) is itself a form of tool assembly.
- [[concepts/Anti-To-Do List and Abstraction Layering]] — The behavioral discipline of eliminating tedious tasks by going up abstraction layers.
- [[concepts/Zeno's Paradox of AI]] — Harnesses are the expert response to the cheap competence cycle: review queues, evals, CI, and workflows that turn first attempts into great work.
- [[sources/After Automation]] — Shipper's "expert systems to absorb the flood" description matches harness engineering exactly.
- [[sources/Superpowers How Jesse Built the 1 AI Claude Code Codex Plugin]] — Superpowers as a personal harness for spec-first coding, review-agent loops, TDD, and runtime proof.

## Source

- [[raw/Harness engineering leveraging Codex in an agent-first world]]
- [[raw/Harness Engineering How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]]
- [[raw/Tokenmaxxing How Top Builders Use AI To Do The Work Of 400 Engineers]]
- [[raw/Running an AI-native engineering org]]
- [[raw/Superpowers How Jesse Built the 1 AI Claude Code  Codex Plugin — and Stopped Writing Code]]
- [[raw/How the engineer behind Claude Cowork actually uses Claude  Felix Rieseberg (Anthropic)]]
