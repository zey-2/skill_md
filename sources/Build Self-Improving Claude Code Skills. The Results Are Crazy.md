---
type: source-summary
created: 2026-05-16
updated: 2026-05-16
status: active
sources:
  - "raw/Build Self-Improving Claude Code Skills. The Results Are Crazy.md"
tags: [self-improving-skills, binary-assertions, skill-evals, autoresearch, skill-creator]
---

# Build Self-Improving Claude Code Skills. The Results Are Crazy.

**Source**: YouTube, `https://www.youtube.com/watch?v=wQ0duoTeAAU`
**Author**: Simon Scrapes
**Published**: 2026-03-14

## Summary

Tutorial on applying Karpathy's autoresearch loop to Claude Code skills for autonomous overnight improvement. Two-layer approach: (1) skill creator's built-in description optimization loop for trigger accuracy, and (2) binary assertion-based output quality loop for structural correctness.

## Key Points

- **Two layers of self-improvement**:
  - Layer 1: Skill creator's description improvement loop tests whether Claude activates the skill at the right time (trigger accuracy, reported as low as 20% with vague descriptions).
  - Layer 2: Binary assertion loop tests output quality against true/false structural criteria (format, word count, forbidden patterns).
- **Binary assertions are critical** — must be objectively verifiable true/false statements (e.g., "does not contain m-dashes", "under 300 words", "first line is standalone"). Subjective criteria like "compelling subject line" cannot be automated.
- **Setup**: Create `evals/` folder in skill package with `evals.json` containing test prompts, expected outputs, and binary assertions. Ask skill creator to generate the assertions from the SKILL.md.
- **Autonomous loop logic**: Run tests → if any assertion fails, make one change to SKILL.md → rerun → if score improved, `git commit` and keep; if dropped, `git reset` and try different change.
- **Instruction to Claude**: "Do not ask for my permissions. Keep looping until I interrupt you or you hit a perfect score."
- **Results example**: Marketing copywriting skill scored 23/24 (95.8%) on first run. The one failure was a rule in `tone-of-voice.md` but not in `SKILL.md` — conflicting information. After adding the missing rule, achieved perfect score on second iteration.
- **Limitations**: Binary loop handles structure, format, word counts, forbidden patterns. Does NOT handle tone of voice, creative quality, or proper use of reference files — those still need human judgment via the skill creator's qualitative dashboard.
- **Evals.json can be auto-generated**: Ask Claude Code to "spin up an evals.json file with assertions that can be validated by true or false questions based on your skill.md."

## Evidence

- The author tested with a marketing copywriting skill that had 25 binary assertions across 5 tests, each testing different prompts against structural rules from reference files (tone of voice guide, persuasion toolkit, examples).
- First iteration caught a real gap: conflicting information between `tone-of-voice.md` (which said "don't end with a question") and `SKILL.md` (which didn't have that rule).
- The agent autonomously fixed this by adding: "LinkedIn post must not end with a question, close with declarative statement, CTA, or a punchy fragment."

## Connections

- [[concepts/Self-Improving Skills]] — Primary evidence for the concept page on autonomous skill improvement.
- [[concepts/Autonomous Research Agents]] — Karpathy's autoresearch is the original pattern this adapts.
- [[concepts/Validation and Evaluation]] — Binary assertions are a specific evaluation methodology for skill outputs.
- [[concepts/Skill Authoring Workflow]] — The evals.json generation and iterative improvement loop as part of authoring.

## Contradictions or Tensions

- The binary loop is presented as "self-improving" but is actually limited to structural/format assertions. Creative quality, tone, and reference-file usage still require human review — this is an important boundary that the video title may overstate.
- The example achieved perfect score in only 2 iterations, but the author acknowledges this was already version 5 of the skill (had gone through comprehensive manual iterations). Fresh skills may take many more cycles.

## Open Questions

- What is the maximum reasonable number of iterations before diminishing returns or degradation?
- Can the binary assertion approach be extended to code-generating skills, not just copywriting?
- How does the agent decide *what* change to make to SKILL.md when an assertion fails? Is this itself guided by a prompt?
