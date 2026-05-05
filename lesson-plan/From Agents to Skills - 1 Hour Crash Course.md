---
type: lesson-plan
created: 2026-05-05
updated: 2026-05-05
status: draft
tags: [lesson-plan, curriculum, agent-skills, quick-start]
---

# From Agents to Skills: A 1-Hour Crash Course

## Guiding Principles

**Why this order:** Start with a quick agent recap to ground the terminology, then immediately move into what skills are and how to build one. Every minute targets the practical outcome: by the end, learners have drafted a real SKILL.md for a task they actually do.

**Target outcome:** Learners can explain what an AI agent is, describe what a skill does, and author a complete SKILL.md for a recurring task.

**Time estimate:** ~60 minutes total.

---

## Part 1: What Is an AI Agent? (~5 min)

> **Goal:** Pin down the term "agent" in one concrete mental model before building on it.

**Key idea:** An AI agent is an LLM that can **use tools in a loop** to achieve a goal. It is not just a chatbot — it can act on the world.

- **The formula:** Agent = LLM + tools + loop + goals
- **The ReAct pattern:** The agent reasons about what to do, acts (calls a tool), observes the result, and repeats until the goal is met
- **Tools:** File operations, web search, code execution, database queries, API calls — anything the LLM can request to run externally
- **The loop:** Unlike a single API call, an agent runs multiple turns: think → act → observe → think again
- **What separates agents from regular LLM calls:** persistence across turns, tool access, and goal-directed behavior

**Quick check:** Ask yourself — what's the minimum difference between asking ChatGPT a question and running an agent? (Answer: the agent can take actions, not just produce text.)

---

## Part 2: What Is an Agent Skill? (~10 min)

> **Goal:** Understand why skills exist and what problem they solve.

**The problem:** Agents are powerful but inconsistent. The same agent will do a recurring task differently each time, because it has no packaged knowledge of *how your team* wants it done.

**The solution:** A skill is a **reusable operating procedure** for an agent. It tells the agent:

1. **When** to use it (trigger conditions, keywords)
2. **What** steps to follow (workflow, process knowledge)
3. **What** files or scripts are available (supporting resources)
4. **What** constraints matter (safety, style, scope boundaries)

**Skills vs. tools vs. frameworks:**

| Concept | Role | Example |
|---------|------|---------|
| Tool / MCP Server | Exposes an action the agent can call | `read_file`, `search_codebase` |
| Skill | Packages reusable knowledge about *how* to do a task | "When reviewing PRs, check for X, Y, Z" |
| Framework | Coordinates multiple agents, state, and control flow | LangGraph, OpenAI Agents SDK |

**Real-world examples of skills:** PR description generation, code review checklists, TDD workflow enforcement, debugging playbooks, safety guardrails.

---

## Part 3: SKILL.md Anatomy & Progressive Disclosure (~10 min)

> **Goal:** Know exactly what a skill package looks like and why it's structured this way.

### Package Structure

```
my-skill/
├── SKILL.md          # Main instruction file (required)
├── references/       # Longer background docs, API schemas
├── scripts/          # Deterministic helper code
└── assets/           # Templates, images, static files
```

### SKILL.md Essentials

The main file contains:
- **Front matter** (YAML): `name`, `description` — these two fields determine routing
- **Instructions** (Markdown): when to use it, steps to follow, constraints, examples

### Progressive Disclosure

Skills use a layered loading model because agent context is limited:

1. **Layer 1 — Metadata (~100 tokens):** The agent first sees `name` and `description` to decide if the skill applies
2. **Layer 2 — SKILL.md body (~500 lines max):** Full instructions, steps, constraints
3. **Layer 3 — References/scripts/assets:** Loaded on-demand only when the task needs them

**Key rule:** If a detail is too long for the main file, put it in `references/`. The SKILL.md should link to it, not inline it.

---

## Part 4: Authoring Workflow (~15 min)

> **Goal:** Learn the repeatable process for turning a recurring task into a skill.

### Step-by-step:

1. **Collect a concrete use case** — What task do you (or your team) repeat regularly? What fragile steps keep going wrong?
2. **Draft the SKILL.md core** — Write name, description, and the essential instructions. Keep it under 500 lines.
3. **Move bulk to references** — If any section feels long, split it into `references/`.
4. **Add scripts where determinism matters** — If a step needs exact, reproducible logic (not LLM judgment), write a script.
5. **Test the skill** — Does it trigger on the right inputs? Stay silent on wrong ones? Produce complete, correct output?
6. **Iterate** — Fix vague triggers, tighten constraints, add missing examples.

### Writing good descriptions

A good `description` says what the skill does and when to use it, using concrete keywords the agent can match on:

- Bad: "Helps with code stuff"
- Good: "Generate a structured PR description from git diff, including change summary, risk assessment, and test plan. Trigger when the user asks to write or generate a PR/commit description."

### Common mistakes

- Vague triggers ("use this sometimes")
- Oversized instructions (putting 2000+ lines in SKILL.md)
- Missing examples (no "here's what good looks like")
- No scope boundary (when should the skill *not* apply?)

---

## Part 5: Hands-On — Draft Your First Skill (~15 min)

> **Goal:** Author a complete SKILL.md for a task you actually perform.

### Exercise

Pick **one** recurring task you do regularly. Examples:

- Write PR descriptions from git diffs
- Review code for security issues
- Generate test cases from a function signature
- Summarize meeting notes into action items
- Convert a bug report into a reproducible test case

### Template to fill in

```markdown
---
name: your-skill-name
description: One sentence: what it does and when to use it
---

## When to use this skill

[2-3 bullet points with concrete trigger conditions]

## Steps

1. [First step the agent should take]
2. [Second step]
3. [And so on...]

## Constraints

- [What the agent should NOT do]
- [Style or quality requirements]

## Examples

**Input:** [What the user might ask]
**Output:** [What good output looks like]
```

### Validation checklist

- [ ] The `description` says what the skill does and when to use it (under 100 tokens)
- [ ] The SKILL.md body is under 500 lines
- [ ] There are at least 2 concrete trigger conditions
- [ ] There is at least 1 constraint ("do NOT do X")
- [ ] There is at least 1 example of input → expected output

---

## Part 6: Wrap-Up & Next Steps (~5 min)

> **Goal:** Know where to go from here.

### What you covered today

1. AI agents = LLMs that use tools in a loop to achieve goals
2. Skills = packaged operating procedures that make agent behavior consistent
3. SKILL.md = the main skill file, kept concise via progressive disclosure
4. Authoring = identify a recurring task, draft instructions, test, iterate

### Where to go deeper

| Topic | Wiki Concept Article |
|-------|---------------------|
| Skill package details | [[concepts/SKILL.md Package Anatomy]] |
| Cross-platform metadata | [[concepts/Portable Skill Core]] |
| Context management | [[concepts/Progressive Disclosure]] |
| Full authoring workflow | [[concepts/Skill Authoring Workflow]] |
| Testing skills | [[concepts/Validation and Evaluation]] |
| Sharing skills | [[concepts/Skill Distribution and Installation]] |

### Next step

Take your drafted skill, test it with an agent, and refine it based on the output. The best skills emerge from real usage, not first drafts.