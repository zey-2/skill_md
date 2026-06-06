---
type: source-summary
created: 2026-06-06
updated: 2026-06-06
status: active
sources:
  - "raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md"
tags: [claude-code, skills, prompting, composable-skills, self-improvement, anthropic]
---

# How Anthropic Engineers ACTUALLY Prompt Claude Code

**Source**: YouTube, `https://www.youtube.com/watch?v=qOvc9IUKEIc`
**Author**: Austin Marchese (BuildPartner.ai / The Incubator)
**Published**: 2026-05-16
**Created**: 2026-06-06

## Summary

Austin Marchese distills four rules from studying how Anthropic engineers prompt Claude Code, drawn from the AI Code Summit and published Anthropic engineering materials. The core thesis is that most users are prompting wrong — they write ad-hoc prompts for every task instead of building reusable skills. The four rules form a progression: (1) prompt skills, not Claude, (2) skills are more than prompts — they have three layers (description, instructions, tools), (3) build composable skills, not monolithic ones, and (4) skills get smarter every session through deliberate updates.

## Key Points

- **Rule 1: Prompt skills, not Claude.** Stop writing new prompts for every task. Create reusable skills and invoke them via slash commands. Skills sit at Layer 3 (the application layer) above the model (Layer 1) and agents/prompts (Layer 2).
- **Rule 2: Skills are more than prompts.** A skill has three layers: (1) description — what Claude checks to decide whether to use the skill, (2) instructions — the step-by-step playbook, (3) tools — code scripts, API calls, reference files. Most people obsess over instructions and neglect tools, but tools are where the leverage lives.
- **Rule 3: Build composable skills, not custom skills.** Small, focused, reusable skills that chain together beat one massive skill. Benefits: issues are easy to spot, improvements compound across workflows, and skills are reusable without rebuilding.
- **Pattern 1: Save scripts inside skills.** When Claude writes the same Python script repeatedly, save it inside the skill as a tool. Code is deterministic — same input, same output — trading AI tokens for cheaper, faster, repeatable compute. "If you can use code instead of AI, you should."
- **Pattern 2: Control who invokes what.** Two flags: `user_invocable: false` hides a skill from the slash menu (agent-only); `disable_model_invocation` prevents the model from running it (human-only, for high-risk actions like deployments).
- **Rule 4: Skills get smarter every session.** A prompt dies when you close the chat; a skill persists. Every time you use a skill and the output isn't right, ask: "Is this a one-time fix or should it be in the skill forever?" If forever, update the skill. This creates a compounding improvement loop.
- **Three-layer mental model**: Layer 1 = AI model, Layer 2 = agents and prompts, Layer 3 = skills (the application layer). Anthropic builds the phone; users build the apps.
- **Claude auto-invokes skills.** If a skill's description is specific enough, Claude will automatically use it when relevant — no explicit slash command needed.

## Evidence

- Marchese references the Anthropic AI Code Summit presentations by Barry and Eric from the Anthropic team.
- Eric from Anthropic noted the common mistake: "people will put a lot of effort into creating these really beautiful, detailed prompts, and then the tools that they make to give the model are incredibly bare-bones."
- Barry described saving a Python slide-styling script inside a skill so Claude stops rewriting it each session.
- The composable skills example: splitting a monolithic `/content-creation` skill into separate YouTube idea research, YouTube script writer, and LinkedIn post skills.
- Domain-checking example: a custom skill with programmatic domain verification replaced manual back-and-forth, enabling 10 sub-agents to scan 10,000+ domains.

## Connections

- [[concepts/Agent Skills]] — Defines skills as reusable agent operating procedures; this source provides practical rules for authoring them.
- [[concepts/Skill Authoring Workflow]] — Rule 2's three-layer model (description, instructions, tools) and the scripts-inside-skills pattern are concrete authoring guidance.
- [[concepts/Progressive Disclosure]] — The three-layer model maps to progressive disclosure: description for discovery, instructions for activation, tools for execution.
- [[concepts/Self-Improving Skills]] — Rule 4 (skills get smarter every session) is the manual version of the autonomous self-improvement loop.
- [[concepts/Meta-Skills and Skillification]] — Composable skills that chain together are the prerequisite for skillification.
- [[concepts/Comprehension-Driven Development]] — The shift from ad-hoc prompts to skills mirrors the shift from code generation to comprehension.
- [[concepts/Harness Engineering Principles]] — Skills are harness components; invocation control flags are guardrails.

## Contradictions or Tensions

- Marchese presents these as "how Anthropic engineers actually prompt," but the source material is a public presentation aimed at adoption, not internal engineering documentation. The rules may be aspirational guidance rather than consistent internal practice.
- The "if you can use code instead of AI, you should" rule tensions with the tokenmaxxing philosophy of spending more model time for better results. The right balance depends on task determinism.
- Auto-invocation by description matching may over-trigger or under-trigger in practice, creating a maintenance burden for description tuning.

## Open Questions

- How do Anthropic engineers actually version and test skill updates after each session? Is there a formal review step or is it purely informal?
- What is the practical limit on skill composability before coordination overhead exceeds the benefit?
- How do invocation control flags interact with plugin-level permissions and MCP approval policies?
- Can the "save scripts inside skills" pattern scale to complex multi-file codebases, or is it best for single-file utilities?
