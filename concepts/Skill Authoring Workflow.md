---
type: concept
created: 2026-04-26
updated: 2026-06-06
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md"
  - "raw/mattpocockskills Skills for Real Engineers. Straight from my .claude directory.md"
  - "raw/obrasuperpowers An agentic skills framework & software development methodology that works.md"
  - "raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md"
  - "raw/Context Is the New Code — Patrick Debois, Tessl.md"
  - "raw/2026-05-10 Skill Authoring Patterns Cross-Project Research.md"
  - "raw/Superpowers How Jesse Built the 1 AI Claude Code  Codex Plugin — and Stopped Writing Code.md"
  - "raw/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md"
  - "raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md"
tags: [agent-skills, authoring, workflow, context, skillification, comprehension]
---

# Skill Authoring Workflow

## Summary

A skill authoring workflow is the repeatable process for turning a recurring task into an agent skill. The earlier synthesis recommends starting from concrete use cases, drafting a concise core, moving bulky detail into references, adding scripts where determinism matters, validating the package, reviewing it, releasing it, and improving it from real usage.

The newer raw sources make the target clearer. In practice, many successful skills encode working habits such as planning, TDD, issue triage, interface design, debugging, code review, or safety guardrails. A good authoring workflow therefore starts by asking not only "What information does the agent need?" but also "What operating procedure keeps repeating?"

Sources: `raw/skill.md for AI Agents.md`, `raw/mattpocockskills My personal directory of skills, straight from my .claude directory.md`, `raw/obrasuperpowers An agentic skills framework & software development methodology that works.md`, and `raw/forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md`.

## Key Ideas and Evidence

The earlier synthesis says strong public guidance converges on the same operational pattern:

1. Collect concrete agent use cases.
2. Draft the `SKILL.md` core.
3. Split bulky detail into references.
4. Add deterministic scripts where needed.
5. Generate repository indexes and vendor adapters.
6. Run validation and evals.
7. Peer review.
8. Release with version and source SHA.
9. Monitor trigger quality and task success.
10. Refresh from upstream docs and changelogs.

The new repository examples show what those use cases look like in the wild. One personal catalog packages skills for PRD writing, issue slicing, TDD, architecture review, and git guardrails. A larger framework packages brainstorming, plan writing, execution, code review, and subagent coordination as named skills. A single-file behavior guide shows that some teams also codify principles such as "think before coding," "simplicity first," and "surgical changes."

A reasonable inference is that strong skill authors often begin with recurring failure modes. If agents keep overcomplicating, skipping tests, or making unsafe edits, those patterns are good candidates for skills or adjacent behavior guides.

## Where Sources Agree

The sources agree that examples matter. The earlier synthesis says OpenAI recommends understanding skills through concrete examples before designing reusable resources. The newer repositories show exactly that pattern by publishing concrete workflow skills instead of only abstract templates.

They also agree that skills should improve through validation and iteration rather than being treated as one-time documents.

## Where Sources Disagree

The sources disagree mainly in packaging and granularity. Some publish many small skills for narrow jobs. Others publish one broader methodology that coordinates multiple stages of work. The `CLAUDE.md` source is adjacent again: it is clearly reusable guidance, but it is merged into project instructions instead of being packaged as a portable skill directory.

These differences reflect different maintenance contexts. A solo author may favor simple project overlays. A skill marketplace may favor installable units. A framework author may favor an integrated workflow system.

## Context Generation Methods

Debois identifies several context creation patterns beyond manual prompting:

- **Reusable instructions** — `CLAUDE.md`, `agent.md`, `SKILL.md` files that persist across sessions.
- **Documentation pull** — downloading library documentation so the agent has the correct version rather than hallucinating.
- **External context pull** — pulling context from GitLab, GitHub, Slack, tickets. Even a ticket creates context when the agent reads it.
- **Spec-driven development** — writing a specification that the agent breaks down into planning mode and step-by-step prompts.
- **Code-to-skills transformation** — converting large helper code blocks into skills that describe procedures rather than implementing them literally. Debois found this solved more problems than coding the helpers could, because the skill could adapt to the user's ecosystem.
- **Voice coding** — voice input produces more elaborate and higher-quality context than typing. Debois attributes this to speaking in full sentences rather than terse typed fragments.

These methods form the **Generate** stage of the [[Context Development Lifecycle]].

## Authoring Patterns from Cross-Project Research

A May 2026 cross-project study compared four skill collections: obra/superpowers, mattpocock/skills, garrytan/gstack, and garrytan/gbrain. Several convergent patterns emerged.

### SKILL.md Structure Convergence

All projects converge on a common skeleton:

| Section | Superpowers | Gstack | Matt Pocock |
|---------|:-----------:|:------:|:-----------:|
| Overview/Core principle | Yes | Yes | Yes |
| When to Use / Triggers | Yes | Yes (triggers array) | Yes |
| Process/Workflow steps | Yes | Yes (Step 0, 1, 2...) | Yes |
| Iron Laws / Rules | Yes | Yes (STOP points) | Yes |
| Red Flags / Anti-patterns | Yes | Yes | Yes |
| Examples | Yes | Yes | Yes |
| Reference files | Yes | Yes | Yes |
| Checklists | Yes | Yes | Yes |
| Voice guidelines | No | Yes | No |
| Telemetry | No | Yes | No |
| Flowcharts | Yes (Graphviz) | No | No |

### Description Field Design

The most important cross-cutting insight: the `description` field should describe **only triggering conditions**, not what the skill does. When descriptions summarize workflow, the agent follows the description instead of reading the full skill contents.

```yaml
# BAD: Summarizes workflow
description: Use when executing plans - dispatches subagent per task with code review

# GOOD: Just triggering conditions
description: Use when executing implementation plans with independent tasks in the current session
```

Gstack extends this with a `triggers` array listing specific phrases that activate the skill.

**Rules for writing descriptions:**
1. Start with "Use when..." to focus on triggering conditions.
2. Include specific symptoms, situations, and contexts.
3. Never summarize the skill's process or workflow in the description.
4. Write in third person (injected into system prompt).
5. Add keywords: error messages, symptoms, tool names.
6. Keep under 500 characters.

### Constraint Design

All projects use similar patterns for specifying prohibitions:

1. **Iron Laws** (Superpowers): Non-negotiable declarations like `NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST`.
2. **STOP points** (Gstack): Named checkpoints where workflow must pause for user input.
3. **Red Flags lists:** Explicit thought patterns to watch for — "ALL of these mean: STOP."
4. **Rationalization tables:** Mapping agent excuses to reality counters.
5. **Explicit negation:** "Don't just state the rule — forbid specific workarounds."

### Testing Before Deployment

From superpowers' TDD-for-skills methodology:

1. Run the task **without** the skill first. Watch the agent fail.
2. Document the exact rationalizations the agent uses verbatim.
3. Write the skill to address those specific failures.
4. Re-run the task **with** the skill. Verify compliance.
5. If the agent finds new rationalizations, add counters and re-test.
6. Repeat until bulletproof under maximum combined pressure.

The Jesse Vincent interview adds a concrete authoring lesson: skills should counter the rationalizations agents actually use. Vincent describes agents deleting tests to avoid failure after being told that all tests were their responsibility and that any failing test meant project failure. The effective fix was not a narrow ban on deleting a file, but a broader measurable rule: reducing test coverage is worse than a failing test. That pattern generalizes: authoring should identify the incentive created by the instruction, then close the loophole at the right abstraction level. Source: [[sources/Superpowers How Jesse Built the 1 AI Claude Code Codex Plugin]].

### Choosing the Right Freedom Level

- **Low freedom** (specific scripts, exact commands): Database migrations, deployment sequences.
- **Medium freedom** (pseudocode with parameters): Report generation, data analysis.
- **High freedom** (text-based instructions): Code review, design decisions.

### Save Scripts Inside Skills

When Claude writes the same script repeatedly across sessions, save it inside the skill as a tool. Code is deterministic — same input, same output — while AI inference is probabilistic, token-costly, and variable. The rule of thumb: "If you can use code instead of AI, you should." The author doesn't need to write the code; they can have AI write it once and then reuse it as a tool indefinitely.

This pattern addresses the tools layer of the three-layer skill architecture (description, instructions, tools). Most authors over-invest in instructions and under-invest in tools, but tools are where deterministic leverage lives. Source: `raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md`.

### Invocation Control Flags

Two flags control who can invoke a skill:

| Flag | Effect | Use Case |
|---|---|---|
| `user_invocable: false` | Hides from slash menu; agent-only | Internal tools the user shouldn't directly trigger |
| `disable_model_invocation` | Model cannot invoke; human-only | High-risk actions (deployments, messages) |

These flags are governance tools at the skill level. They sit below plugin-level permissions and MCP approval policies but above raw prompt instructions. Source: `raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md`.

### Voice and Tone Guidelines

Gstack's explicit voice guidelines are notable:
- Direct, concrete, builder-to-builder.
- Name the file, function, command, and user-visible impact.
- No em dashes. No AI vocabulary (delve, crucial, robust, comprehensive, nuanced).
- Short paragraphs. End with what to do.

## Connections

- [[Progressive Disclosure]] explains why authoring should split content into layers.
- [[Validation and Evaluation]] explains the testing stage.
- [[Provenance and Versioning]] explains release and source tracking.
- [[Vendor Adapters]] explains generated platform-specific outputs.
- [[concepts/Agent Skills|Agent Skills]] explains why workflow skills still count as skills.
- [[MCP and Tool-Integration Architecture]] helps decide when a workflow needs tools, scripts, resources, or an MCP server.
- [[Agent Frameworks and Orchestration]] helps decide when a repeated behavior should become a skill versus framework-level control flow.
- [[Meta-Skills and Skillification]] — skillification as an authoring method; the skillify meta-skill.
- [[Self-Improving Skills]] — autonomous iteration as an extension of the manual authoring cycle.
- [[sources/Superpowers How Jesse Built the 1 AI Claude Code Codex Plugin]] — interview evidence for spec-first workflows, rationalization-aware skills, and review loops with fresh agents.
- [[sources/The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry]] — data-driven skill authoring: analyze 116 sessions, find repeated patterns, create "Catch Me Up" skill.
- [[Prompting Skills Not Prompts]] — the mental model shift from ad-hoc prompts to reusable skills.
- [[sources/How Anthropic Engineers ACTUALLY Prompt Claude Code]] — source for scripts-inside-skills and invocation control patterns.

## Open Questions

- How much peer review is enough for an internal skill?
- When should a repeated behavior live in a portable skill package versus a project-level instruction file?
