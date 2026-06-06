---
type: concept
created: 2026-05-11
updated: 2026-06-06
status: active
sources:
  - "raw/Build Self-Improving Claude Code Skills. The Results Are Crazy.md"
  - "raw/karpathyautoresearch AI agents running research on single-GPU nanochat training automatically.md"
  - "raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md"
tags: [agent-skills, self-improvement, evaluation, autonomous-loops]
---

# Self-Improving Skills

## Summary

Self-improving skills are agent skills that autonomously test, score, and refine themselves through iterative loops. Inspired by Karpathy's autoresearch pattern, the agent reads its own skill definition, makes a change, runs an evaluation, keeps the change if the score improves, and reverts if it gets worse — looping indefinitely until interrupted or a perfect score is reached.

Sources: Simon Scrapes' "Build Self-Improving Claude Code Skills" video and Karpathy's autoresearch project.

## Key Ideas and Evidence

### The Autoresearch Pattern (Karpathy)

Karpathy's autoresearch gives an AI agent a small but real LLM training setup and lets it experiment autonomously. The core loop is:

1. Read the current `program.md` (instructions) and `train.py` (code).
2. Make a change to the code based on the instructions.
3. Run a training experiment with a fixed time budget (5 minutes).
4. Check if the metric (`val_bpb`, validation bits per byte) improved.
5. If improved: keep the change and advance the git branch.
6. If worse: reset to the previous commit and try a different change.
7. Never stop — do not ask the human for permission to continue.

Key design choices:
- **Single file to modify.** The agent only touches one file (`train.py`), keeping scope manageable and diffs reviewable.
- **Fixed time budget.** All experiments run for exactly 5 minutes, making results comparable regardless of what the agent changes.
- **Full autonomy.** Once the loop begins, the agent works indefinitely without pausing for human approval.

### Applying Autoresearch to Skills (Simon Scrapes)

The same pattern applies to Claude Code skills with one key substitution: instead of editing code and measuring a training metric, the agent edits `SKILL.md` and measures output quality against **binary assertions**.

The loop is nearly identical:

| Autoresearch | Self-Improving Skills |
|---|---|
| Read `train.py` | Read `SKILL.md` |
| Change a hyperparameter or architecture | Change a rule, instruction, or constraint |
| Run training (5 min) | Run test prompts through the skill |
| Check `val_bpb` metric | Check pass rate against binary assertions |
| Keep if improved, revert if worse | Keep if improved, revert if worse |
| Loop indefinitely | Loop until perfect score or interrupted |

### Binary Assertions

The word "binary" is critical. Assertions must be true/false statements, not subjective judgments.

**Binary (good for automation):**
- Does not contain em dashes.
- Total word count under 300.
- First line is a standalone sentence.
- Final line is not a question.
- Contains at least one specific number or statistic.

**Non-binary (bad for automation):**
- Does it have a compelling subject line?
- Is the tone appropriate?
- Does it use curiosity effectively?

Binary assertions enable fully automated scoring: the agent can validate each assertion as true or false without human judgment, calculate a pass rate, and make deterministic decisions about whether to keep or revert changes.

### Two Layers of Self-Improvement

There are two distinct layers to skill self-improvement:

**Layer 1: Description Optimization (built into Anthropic's skill creator)**
- Tests whether the skill triggers at the right time.
- Runs test queries, checks trigger accuracy, proposes a better description.
- Focus: getting the skill to activate when it should.

**Layer 2: Output Quality Improvement (Karpathy-style loop)**
- Tests whether the skill produces correct outputs when triggered.
- Runs test prompts through the skill, checks binary assertions, makes one change to `SKILL.md` if any assertion fails.
- Focus: getting the skill to produce structurally correct outputs.

### Eval Structure

The eval file (`evals/evals.json`) contains test cases, each with:
- A prompt to feed the skill.
- An expected output description.
- A list of binary assertions (true/false checks).

Example assertions for a marketing copywriting skill:
- Does the first line appear as a standalone sentence?
- Does it contain at least one specific number or statistic?
- Is the final line not a question?
- Is the total word count under 300?

A typical eval might have 25 binary assertions across 5 tests. The agent scores each run (e.g., 23/24 = 95.8%), identifies the failing assertion, makes one targeted change to `SKILL.md`, re-runs, and keeps the change if the score improved.

### Limitations

The binary loop handles structural concerns well:
- Format, layout, word counts
- Forbidden patterns (em dashes, specific phrases)
- Rule compliance (must include X, must not end with Y)

It does **not** handle:
- Tone of voice or creative quality
- Whether the skill uses reference files properly
- Subjective judgment calls

These still require human review, which is where Layer 1 (the skill creator's qualitative eval dashboard) complements the binary loop.

### Practical Results

In the documented example, a marketing copywriting skill that had already gone through five manual iterations scored 23/24 (95.8%) on the first automated run. The single failure revealed a contradiction: a rule existed in `tone-of-voice.md` but not in `SKILL.md`. The agent added the missing rule, re-ran, and achieved a perfect score on the second iteration.

This demonstrates a key value: self-improving loops surface inconsistencies between reference files and skill instructions that humans miss during manual review.

## Manual Self-Improvement (Anthropic Practice)

Anthropic engineers practice a manual version of this loop. Rule 4 from their Claude Code prompting methodology: "Skills get smarter every session." After every skill run where the output isn't right, the engineer asks: "Is this a one-time fix or should it be in the skill forever?" If forever, the skill is updated immediately — adding the rule, example, or edge case. This creates a compounding loop where each session starts smarter than the last.

The manual approach trades automation for human judgment. The engineer decides what matters; the autonomous loop optimizes against assertions. Both share the same core insight: skills are living documents, not static files. Source: `raw/How Anthropic Engineers ACTUALLY Prompt Claude Code.md`.

## Connections

- [[Validation and Evaluation]] — binary assertions are a specific type of output evaluation.
- [[Skill Authoring Workflow]] — the self-improvement loop is an automated extension of the manual authoring cycle.
- [[Autonomous Research Agents]] — Karpathy's autoresearch is the origin pattern.
- [[Context Development Lifecycle]] — self-improving skills operationalize the Observe and Evaluate stages into a continuous loop.
- [[Prompting Skills Not Prompts]] — Rule 4 (skills get smarter every session) is the manual version of this concept.
- [[sources/How Anthropic Engineers ACTUALLY Prompt Claude Code]] — source for the manual self-improvement practice at Anthropic.

## Open Questions

- How many iterations before diminishing returns? When should the loop be stopped?
- Can binary assertions be generated automatically from `SKILL.md` content?
- What happens when multiple agents run self-improvement loops on the same skill simultaneously?
- How do you prevent overfitting to the eval assertions at the expense of real-world quality?
