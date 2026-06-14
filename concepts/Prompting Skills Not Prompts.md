---
type: concept
created: 2026-06-06
updated: 2026-06-06
status: active
sources:
  - "raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md"
  - "raw/Why We’ll Still Be Employed When AI Can Do Everything.md"
  - "raw/Lessons from building Claude Code How we use skills.md"
tags: [skills, prompting, mental-model, workflow, anthropic]
---

# Prompting Skills, Not Prompts

## Summary

The central mental model shift for effective AI-agent use: stop writing ad-hoc prompts for every task and start building reusable skills. When you prompt Claude directly, the prompt dies when you close the chat. When you prompt through a skill, the skill persists — and every session makes it sharper. This is the difference between reinventing the wheel each time and building a compounding system.

The idea has three parts: (1) the mental shift from per-task prompts to reusable procedures, (2) the three-layer architecture of a well-built skill (description, instructions, tools), and (3) the composability principle — small focused skills that chain together beat monolithic ones.

Source: Austin Marchese's analysis of Anthropic engineering practices, `raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md`. Confirmed by Anthropic's own engineering blog, `raw/Lessons from building Claude Code How we use skills.md`.

## The Mental Model Shift

Most people start using AI by writing a new prompt for every task. This works for one-off problems but creates waste for recurring work: the same prompt gets rewritten, refined, and lost across sessions.

The shift is to think at the **skill layer** — Layer 3 in Anthropic's model:

| Layer | What It Is | Example |
|---|---|---|
| Layer 1 | The AI model | Claude, GPT, Gemini |
| Layer 2 | Agents and prompts | A single chat with a specific prompt |
| Layer 3 | Skills | Reusable, invocable procedures |

Anthropic builds the phone (Layer 1). Users interact through apps (Layer 2). But the durable value is in the apps you build yourself (Layer 3). A `/draft-email` skill that knows your voice, tone, and writing style is more valuable than rewriting the email prompt each time.

The practical trigger: when you find yourself writing the same kind of prompt for the third time, it should already be a skill.

## The Three-Layer Skill Architecture

A well-built skill has three layers, and most people stop too early:

1. **Description** — What Claude checks to decide whether to use the skill. Think of it as the label on a folder. If the label is vague, Claude won't know when to reach for it. If it's specific, Claude can auto-invoke it without an explicit slash command.

2. **Instructions** — The step-by-step playbook Claude follows once the skill is activated. This is what most people focus on when authoring skills.

3. **Tools** — Code scripts, API calls, reference files. This is where the leverage lives, but most people stop at instructions. As Eric from Anthropic noted: "people put a lot of effort into creating beautiful, detailed prompts, and then the tools they give the model are incredibly bare-bones."

The tools layer is what transforms a skill from a prompt-in-a-folder into a genuine capability. A domain-checking skill with a programmatic verification script can scan 10,000+ domains — something no amount of prompt text could achieve.

## Composability Over Monoliths

Small, focused, reusable skills that chain together beat one massive skill that does everything. The benefits:

- **Issues are easy to spot.** When a focused skill breaks, you know exactly where to look.
- **Improvements compound.** Update one skill and every workflow that uses it gets better.
- **Reuse beats rebuilding.** A domain-checking skill plugs into any workflow without re-implementation.

The anti-pattern is the monolithic `/content-creation` skill that handles ideas, scripts, social posts, and distribution all at once. When something breaks, the cause is unclear. When you fix one part, you may break another. Split into focused skills (`/youtube-idea-research`, `/youtube-script-writer`, `/linkedin-post`) and each can call the others.

## The Compounding Loop

Skills get smarter every session — if you update them. The loop:

1. Run a skill.
2. The output isn't quite right.
3. Ask: "Is this a one-time fix or should it be in the skill forever?"
4. If forever, update the skill — add the rule, example, or edge case.
5. Next session starts smarter than the last.

This is the manual version of [[Self-Improving Skills|autonomous self-improvement]]. The difference is that manual updates are guided by human judgment about what matters, while autonomous loops optimize against binary assertions.

Most users skip step 4. They run the skill, get output, and move on. Anthropic engineers treat every imperfection as a signal to improve the skill itself.

## Practical Implications

- **Skill description design matters.** A precise description lets Claude auto-invoke the skill. A vague one means you always need explicit slash commands.
- **Save scripts inside skills.** When Claude writes the same code repeatedly, save it as a tool. Deterministic code is cheaper, faster, and more repeatable than AI inference. "If you can use code instead of AI, you should."
- **Invocation control.** Two flags shape who can use a skill: `user_invocable: false` (agent-only, for internal tools) and `disable_model_invocation` (human-only, for high-risk actions like deployments).
- **Start with failure modes.** The best skills address recurring agent failures, not just recurring tasks.
- **Ask your agent what it needs.** Naveen Naidu's workflow (from `raw/Why We’ll Still Be Employed When AI Can Do Everything.md`) shows a practical discovery method: "What tools can I give you so you can work more quickly?" The agent identifies its own inefficiencies, then you build the focused skill it describes. His rule of thumb: "Don't download any skills. Start interacting with the agent, see where it is inefficient, and then ask it to create skills."

## Connections

- [[concepts/Agent Skills]] — Defines what skills are; this concept is about the mental shift to using them.
- [[concepts/Skill Authoring Workflow]] — The three-layer model and scripts-inside-skills pattern are concrete authoring guidance.
- [[concepts/Progressive Disclosure]] — The three layers map to discovery (description), activation (instructions), and execution (tools).
- [[concepts/Self-Improving Skills]] — Rule 4 (skills get smarter every session) is the manual precursor to autonomous self-improvement.
- [[concepts/Meta-Skills and Skillification]] — Composable skills are the prerequisite for skillification — skills that create skills.
- [[concepts/Harness Engineering Principles]] — Skills are harness components; invocation control flags are guardrails.
- [[concepts/Comprehension-Driven Development]] — The shift from ad-hoc prompts to skills parallels the shift from code generation to comprehension.
- [[concepts/The Compute Cost Tradeoff]] — "If you can use code instead of AI, you should" is the skill-design expression of the compute cost tradeoff.

## Contradictions or Tensions

- "If you can use code instead of AI, you should" tensions with [[concepts/Tokenmaxxing|tokenmaxxing]] — spending more model time for better results. The right balance depends on whether the task is deterministic or creative.
- Auto-invocation by description matching may over-trigger or under-trigger. Description tuning becomes its own maintenance task.
- Composability has limits. At some point, coordinating many small skills creates overhead that exceeds the benefit of modularity.

## Open Questions

- What is the practical ceiling on skill composability before coordination costs dominate?
- How should skill updates be reviewed — informally after each session, or through a formal eval cycle?
- Do invocation control flags compose cleanly with plugin-level permissions and MCP approval policies?
- Can the "save scripts inside skills" pattern scale beyond single-file utilities to complex multi-file codebases?
