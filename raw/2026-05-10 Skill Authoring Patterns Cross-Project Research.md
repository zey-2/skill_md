# Skill Authoring Patterns: Cross-Project Research

## Sources Investigated

1. **obra/superpowers** (v5.1.0) - 14 skills, official Claude plugin.
2. **mattpocock/skills** - Personal skill directory, installable via `npx skills@latest add`.
3. **garrytan/gstack** - 23 opinionated tools/skills acting as a virtual development team.
4. **garrytan/gbrain** - Compiled intelligence system with skill-based workflows.

---

## 1. Overview of Each Skill's Approach

### 1.1 obra/superpowers - A Complete Software Development Methodology

**Philosophy:** Not a loose collection of skills — a complete, sequential development methodology. Skills chain: brainstorming → using-git-worktrees → writing-plans → subagent-driven-development → verification-before-completion → finishing-a-development-branch. Each skill knows about the others and dispatches to the next.

**Key distinguishing features:**
- **TDD applied to skill creation itself.** The `writing-skills` skill mandates that every skill must be tested with subagent pressure scenarios before deployment. The "Iron Law": "NO SKILL WITHOUT A FAILING TEST FIRST."
- **Flowchart-driven process.** Every skill uses Graphviz `digraph` diagrams to show decision trees.
- **Rationalization tables.** Tables mapping agent excuses to reality counters, based on actual baseline testing observations.
- **Iron Laws.** Critical constraints as non-negotiable declarations: "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST."
- **Red Flags sections.** Specific thought patterns that signal the agent is rationalizing — "ALL of these mean: STOP."

### 1.2 mattpocock/skills - Personal, Vertical-Slice Tooling

**Philosophy:** Curated personal skills, each addressing a specific recurring task. Focus on developer tooling and workflow automation.

**Key distinguishing features:**
- **Composable and independent.** Skills installed individually, not sequential chains.
- **Strong naming:** `to-prd`, `to-issues`, `grill-me`, `design-an-interface`, `write-a-skill`, `ubiquitous-language`.
- **GitHub integration focus:** Skills synthesize output into GitHub issues.
- **DDD influence:** `ubiquitous-language` extracts a glossary from conversations.
- **Meta-skill included:** `write-a-skill` for creating new skills with proper structure.

### 1.3 garrytan/gstack - A Virtual Development Team

**Philosophy:** Each skill is a specialist role on a virtual dev team — CEO, Engineering Manager, Staff Engineer, Debugger, Designer, etc.

**Key distinguishing features:**
- **Preamble system.** Every skill starts with a bash preamble handling updates, session management, config, telemetry, and routing.
- **AskUserQuestion format.** Every interactive decision follows a structured brief: header, ELI10 explanation, stakes, recommendation with reason, completeness score, pros/cons.
- **"Boil the Lake" principle.** AI makes completeness cheap — do the complete thing. Completeness scores (N/10) accompany options.
- **Fix-First Review.** Auto-fix issues first, then ask about the rest.
- **Specialist dispatch ("Review Army").** Parallel specialist subagents (Testing, Security, Performance) merged with confidence gates.
- **Voice guidelines.** Forbids corporate/academic tone, em dashes, and AI vocabulary (delve, crucial, robust, comprehensive, nuanced).
- **Continuous checkpoint mode.** Auto-commits with `WIP:` prefix including context blocks.
- **Context recovery.** Reads artifacts, checkpoints, reviews, and timeline data at session start.

### 1.4 garrytan/gbrain - Knowledge as Infrastructure

**Philosophy:** Compiled intelligence system. Every page is an intelligence assessment with "compiled truth" above the line and "timeline" (append-only evidence trail) below.

**Key distinguishing features:**
- **Skill Development Cycle.** "If you have to ask your agent for something twice, it should already be a skill running on a cron. First time is discovery. Second time is system failure." 5-step cycle: Concept → Run manually (3-10 items) → Evaluate output → Codify into SKILL.md → Add to cron.
- **MECE discipline.** Each entity type has exactly ONE owner skill. Two skills creating the same brain page = violation.
- **Quality bar checklist.** Must be tested on 3-10 real items with user approval before deployment. SKILL.md under 500 lines. Citation enforcement. No stubs.

---

## 2. Cross-Cutting Patterns and Best Practices

### 2.1 SKILL.md Structure

All three projects converge on a common skeleton:

```yaml
---
name: skill-name          # letters, numbers, hyphens only
description: Use when [triggering conditions]
---
```

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

### 2.2 Description Field Design

**The most important cross-cutting insight:**

The `description` field should describe ONLY triggering conditions, NOT what the skill does. When descriptions summarize workflow, Claude follows the description instead of reading the full skill content.

```yaml
# BAD: Summarizes workflow
description: Use when executing plans - dispatches subagent per task with code review

# GOOD: Just triggering conditions
description: Use when executing implementation plans with independent tasks in the current session
```

Gstack extends this with a `triggers` array listing specific phrases that activate the skill.

### 2.3 Progressive Disclosure Patterns

**Three-tier disclosure model:**

1. **Tier 1 (Metadata):** YAML frontmatter `name` + `description` — pre-loaded at startup.
2. **Tier 2 (SKILL.md body):** Core principles, process steps, red flags — loaded when triggered. Target: under 500 lines.
3. **Tier 3 (Reference files):** Heavy API docs, examples, scripts — loaded on-demand.

**Critical constraint:** Keep references one level deep from SKILL.md. Nested references (SKILL.md → advanced.md → details.md) cause agents to use partial reads instead of loading complete files.

### 2.4 Constraint Design: What NOT to Do

All projects use similar patterns for specifying prohibitions:

1. **Iron Laws** (Superpowers): `NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST`
2. **STOP points** (Gstack): Named checkpoints where workflow must pause for user input.
3. **Red Flags lists:** Explicit thought patterns to watch for — "ALL of these mean: STOP. Return to Phase 1."
4. **Rationalization tables:** Mapping agent excuses to reality counters.
5. **Explicit negation:** "Don't just state the rule — forbid specific workarounds."
6. **Foundational principle early:** "Violating the letter of the rules is violating the spirit of the rules."

### 2.5 Scripts vs LLM Instructions

**What goes into scripts (deterministic):**
- Environment setup, file system operations, telemetry, config reading/writing, validation

**What stays as LLM instructions (judgment-required):**
- Design decisions, code review findings, debugging strategy, prioritization

### 2.6 Cross-Referencing Between Skills

**Superpowers convention:** Uses `superpowers:skill-name` syntax with explicit requirement markers. Does NOT use `@` file links (force-loads and burns context).

**Gstack convention:** Comprehensive routing table in each skill body listing which user patterns trigger which skill.

---

## 3. Concrete Takeaways for Skill Authors

### 3.1 Writing the Description (The Most Important Field)

1. Start with "Use when..." to focus on triggering conditions.
2. Include specific symptoms, situations, and contexts.
3. NEVER summarize the skill's process or workflow in the description.
4. Write in third person (injected into system prompt).
5. Add keywords: error messages, symptoms, tool names.
6. Keep under 500 characters.

### 3.2 Structuring the Body

1. **Overview:** Core principle in 1-2 sentences. Lead with the most important insight.
2. **When to Use:** Bullet list with symptoms. When NOT to use.
3. **Process:** Numbered steps or flowchart for non-obvious decisions.
4. **Constraints:** Iron Law declaration, Red Flags, rationalization table.
5. **Examples:** One excellent example beats many mediocre ones. Show Good vs Bad.
6. **References:** Link to supporting files for heavy content. Keep references one level deep.

### 3.3 Testing Before Deployment

From superpowers' TDD-for-skills methodology:
1. Run the task WITHOUT the skill first. Watch the agent fail.
2. Document the exact rationalizations the agent uses verbatim.
3. Write the skill to address those specific failures.
4. Re-run the task WITH the skill. Verify compliance.
5. If agent finds new rationalizations, add counters and re-test.
6. Repeat until bulletproof under maximum combined pressure.

### 3.4 Choosing the Right Freedom Level

- **Low freedom** (specific scripts, exact commands): Database migrations, deployment sequences.
- **Medium freedom** (pseudocode with parameters): Report generation, data analysis.
- **High freedom** (text-based instructions): Code review, design decisions.

### 3.5 Voice and Tone

Gstack's explicit voice guidelines:
- Direct, concrete, builder-to-builder.
- Name the file, function, command, and user-visible impact.
- No em dashes. No AI vocabulary (delve, crucial, robust, comprehensive, nuanced).
- Short paragraphs. End with what to do.

---

## 4. Framework: A Reusable Methodology for Creating Skills

### Phase 1: Discovery

1. **Identify the repeating task.** If you've asked your agent for something twice, it should be a skill.
2. **Complete the task without a skill first.** Note where you repeatedly provide context, explain preferences, or share procedural knowledge.
3. **Extract the reusable pattern.** What information would make future instances succeed without additional guidance?

### Phase 2: Baseline Testing (RED)

1. **Create pressure scenarios** (3+ combined pressures: time, sunk cost, authority, exhaustion).
2. **Run WITHOUT the skill.** Give agents the realistic task with pressures.
3. **Document exact failures and rationalizations** word-for-word.
4. **Identify patterns** — which excuses appear repeatedly?

### Phase 3: Author the Skill (GREEN)

1. **Write frontmatter:**
   ```yaml
   ---
   name: active-verb-noun      # gerund form preferred
   description: Use when [triggering conditions, not workflow summary]
   ---
   ```
2. **Write the body:**
   - Overview with core principle
   - When to Use (symptoms, when NOT to use)
   - Process steps or flowchart
   - Iron Law / constraints
   - Red Flags list
   - Rationalization table (from baseline testing)
   - One excellent example (Good vs Bad)
   - References to supporting files
3. **Keep SKILL.md under 500 lines.** Move heavy content to separate files.
4. **References one level deep only.** No nested references.

### Phase 4: Validate (VERIFY GREEN)

1. Run the same pressure scenarios WITH the skill.
2. Verify agent complies under pressure.
3. If agent still fails: The skill is unclear or incomplete. Revise.

### Phase 5: Close Loopholes (REFACTOR)

1. For each new rationalization found in testing:
   - Add explicit negation in rules
   - Add entry to rationalization table
   - Add to Red Flags list
   - Update description with violation symptoms
2. Re-test same scenarios. Repeat until bulletproof.

### Phase 6: Deploy

1. **Verify checklist:**
   - [ ] Description is specific, includes key terms
   - [ ] Description includes triggering conditions only
   - [ ] SKILL.md body is under 500 lines
   - [ ] Additional details in separate files
   - [ ] No time-sensitive information
   - [ ] Consistent terminology
   - [ ] Concrete examples
   - [ ] File references one level deep
   - [ ] Agent follows rule under maximum pressure
2. **Commit to git.**
