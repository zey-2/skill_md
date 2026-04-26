---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://agentskills.io/specification"
  - "https://agentskills.io/skill-creation/optimizing-descriptions"
  - "https://agentskills.io/skill-creation/evaluating-skills"
accessed: 2026-04-26
status: raw-notes
tags: [agent-skills, validation, evaluation, trigger-evals]
---

# Agent Skills specification evaluation and description optimization

## Source Identity

AgentSkills.io documents the Agent Skills open format, including the `SKILL.md` specification, validation expectations, description optimization, and output-quality evaluation workflow.

## Relevant Extracted Facts

- The specification requires a skill directory to contain `SKILL.md`.
- `SKILL.md` must include YAML frontmatter followed by Markdown instructions.
- Required frontmatter fields are `name` and `description`.
- `name` must be 1-64 characters, lowercase alphanumeric plus hyphens, must not start or end with a hyphen, must not contain consecutive hyphens, and must match the parent directory name.
- `description` must be 1-1024 characters, should explain what the skill does and when to use it, and should include task-matching keywords.
- Optional fields include `license`, `compatibility`, `metadata`, and experimental `allowed-tools`.
- The specification recommends progressive disclosure: startup metadata, full `SKILL.md` on activation, and supporting resources only as needed.
- The specification recommends `skills-ref validate ./my-skill` for frontmatter and naming validation.
- The description guide says the `description` field is the primary mechanism agents use to decide whether to load a skill.
- Trigger evaluation should use realistic prompts labeled `should_trigger: true` or `false`.
- The guide recommends around 20 trigger queries, balanced between positive and negative cases, with near-miss negatives that share vocabulary but require a different skill.
- Because model behavior is nondeterministic, the guide recommends running each trigger query multiple times and computing trigger rate.
- The guide recommends train/validation splits to avoid overfitting the description to known failed prompts.
- The output-quality guide recommends test cases with prompt, expected output, and optional input files in `evals/evals.json`.
- The output-quality guide recommends running each task with the skill and against a baseline without the skill or against the previous skill version.
- Evaluation workspaces should capture outputs, timing, grading, and aggregated benchmark results per iteration.
- Assertions should be specific and verifiable; vague assertions such as "the output is good" are weak.
- Mechanical checks should use scripts when possible; LLM grading is useful for more subjective assertions.
- The output-quality guide recommends human review because assertions only test what the maintainer anticipated.
- Iteration should use failed assertions, human feedback, and execution transcripts to improve the `SKILL.md`.

## Relevance to Skill Validation and Evaluation

This is direct primary evidence for separating structural validation from behavioral evaluation. It also adds a missing middle layer: trigger evaluation of the `description`, which determines whether a valid skill is actually loaded when useful and avoided when irrelevant.

## Open Questions

- `skills-ref` validates structure and naming, but behavioral trigger and output evals still need agent-client-specific harnesses.
- The guide shows example workflows, but individual teams must define thresholds for acceptable trigger rate, pass rate, token cost, and runtime.
