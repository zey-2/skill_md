---
type: raw-source
created: 2026-04-26
source_type: web
source_url: "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"
accessed: 2026-04-26
status: raw-notes
tags: [agent-evals, anthropic, graders, reliability]
---

# Anthropic evals for AI agents

## Source Identity

Anthropic's engineering article "Demystifying evals for AI agents" gives current practice for evaluating multi-turn agents, including grader types, transcripts, reliability metrics, and long-term eval maintenance.

## Relevant Extracted Facts

- Anthropic defines an eval as a test for an AI system: give an input, then apply grading logic to measure success.
- Agent evals are harder than single-turn evals because agents use tools across many turns, modify environment state, and can compound mistakes.
- A task is one test case with inputs and success criteria.
- A trial is one attempt at a task; multiple trials help measure nondeterministic behavior.
- A grader scores some aspect of performance and may contain multiple assertions.
- A transcript, trace, or trajectory is the full record of the trial, including outputs, tool calls, reasoning, intermediate results, and interactions.
- The outcome is the final environment state, which can differ from the agent's final statement.
- An evaluation harness runs tasks, provides instructions and tools, records steps, grades outputs, and aggregates results.
- Anthropic distinguishes capability or quality evals from regression evals. Capability evals should have room to improve; regression evals should protect known working behavior.
- Agent evaluations often combine code-based, model-based, and human graders.
- Code-based graders can include string checks, tests, static analysis, outcome verification, tool-call verification, and transcript analysis.
- Model-based graders can include rubric scoring, natural-language assertions, pairwise comparison, reference-based evaluation, and multi-judge consensus.
- Human graders remain useful for expert review, calibration, A/B testing, and spot checks.
- Anthropic recommends deterministic graders where possible, LLM graders where necessary, and human graders judiciously.
- The article cautions against overly rigid path-based grading because agents may find valid solutions the evaluator did not anticipate.
- The article recommends grading outcomes more than exact action sequences when the path can vary.
- It recommends reading transcripts to verify that failures are fair and that graders are measuring what matters.
- It recommends starting with 20-50 simple tasks from real failures or manual checks.
- Good tasks should be unambiguous, solvable by a capable agent, and backed by reference solutions where possible.
- Balanced problem sets should include cases where a behavior should occur and cases where it should not occur.
- Anthropic highlights pass@k for measuring whether at least one attempt succeeds, and pass^k for measuring whether all k trials succeed.
- Eval suites are living artifacts that need ownership, product/domain-expert contributions, and maintenance as products and models change.

## Relevance to Skill Validation and Evaluation

This source supplies the clearest vocabulary for evaluating agent skills as behavior-changing artifacts: task, trial, grader, transcript, outcome, harness, capability suite, regression suite, pass@k, and pass^k. It also warns against overfitting to exact tool-call paths when the skill goal is broader than a single prescribed sequence.

## Open Questions

- For portable skills, the same task may need separate harness adapters for Codex, Claude Code, Gemini CLI, GitHub Copilot, and other clients.
