---
type: concept
created: 2026-04-26
updated: 2026-05-04
status: active
sources:
  - "raw/skill.md for AI Agents.md"
  - "raw/2026-04-26 Agent Skills specification evaluation and description optimization.md"
  - "raw/2026-04-26 OpenAI agent evaluation and trace grading docs.md"
  - "raw/2026-04-26 Anthropic evals for AI agents.md"
  - "raw/2026-04-26 LangSmith AgentEvals trajectory evaluation docs.md"
  - "raw/2026-04-26 tau-bench tool-agent reliability benchmark.md"
  - "raw/Context Is the New Code — Patrick Debois, Tessl.md"
tags: [agent-skills, validation, evaluation, context]
---

# Validation and Evaluation

## Summary

Validation checks whether a skill package is structurally correct. Evaluation checks whether it actually helps an agent do the task well. A repository needs both.

In plain language: validation asks, "Is the skill well formed?" Evaluation asks, "Does the skill work?"

The newer sources add two important layers between those questions: trigger evaluation asks whether the agent loads the skill at the right time, and trace or trajectory evaluation asks how the skill changed the agent's actual behavior.

Sources: `raw/skill.md for AI Agents.md`, `raw/2026-04-26 Agent Skills specification evaluation and description optimization.md`, `raw/2026-04-26 OpenAI agent evaluation and trace grading docs.md`, `raw/2026-04-26 Anthropic evals for AI agents.md`, `raw/2026-04-26 LangSmith AgentEvals trajectory evaluation docs.md`, and `raw/2026-04-26 tau-bench tool-agent reliability benchmark.md`.

## Key Ideas and Evidence

The earlier raw source says a serious repository should validate syntax, structure, and execution quality. At minimum, it recommends checking that:

- YAML front matter parses cleanly.
- `name` and `description` exist.
- names are unique and follow naming rules.
- referenced files actually exist.
- generated vendor adapters match the canonical package.
- evaluation prompts still pass after a change.

The source also connects evaluation to operational metrics such as task success rate, trigger precision, trigger recall, and eval pass rate.

The Agent Skills specification makes the validation layer more concrete. It requires `SKILL.md`, YAML frontmatter, a valid `name`, and a valid `description`. It also recommends the `skills-ref validate ./my-skill` command for checking frontmatter and naming conventions. This is necessary but not enough: a skill can pass schema validation while never being triggered or while producing weak outputs.

## Evaluation Ladder

Use a layered evaluation ladder for agent skills:

| Layer | Question | Typical Evidence |
|---|---|---|
| Structural validation | Is the skill package valid? | `SKILL.md` exists, frontmatter parses, `name` matches folder, file references resolve. |
| Trigger evaluation | Does the skill load when it should and stay quiet when it should not? | Balanced `should_trigger` and `should_not_trigger` prompts, repeated runs, trigger rate, train/validation split. |
| Output evaluation | Does the skill improve task results? | Skill-specific `evals/evals.json`, assertions, with-skill vs baseline comparison, pass rate, human review. |
| Trace or trajectory evaluation | Did the agent follow the intended behavioral route? | Trace grading, tool-call checks, trajectory match, subset/superset tool-call checks, transcript review. |
| Outcome evaluation | Did the final state become correct? | Tests, generated artifacts, database state, file state, state checks, reference solution comparison. |
| Reliability evaluation | Does it work consistently across trials? | Multiple trials, pass@k, pass^k, variance, flaky-task investigation. |
| Maintenance evaluation | Does the eval suite stay useful over time? | Regression suite, saturated capability eval detection, task/grader audits, ownership and update cadence. |

## Trigger Evaluation

Trigger evaluation deserves separate attention because the `description` field controls whether the agent loads the skill. The Agent Skills description guide recommends realistic labeled prompts, including positive cases that should trigger and near-miss negative cases that share keywords but require a different capability.

Because agent behavior is nondeterministic, a single prompt run is weak evidence. A stronger approach runs each query multiple times and computes a trigger rate. Positive cases should exceed the chosen threshold; negative cases should stay below it. Train/validation splits reduce overfitting when improving the description.

For a skill repository, trigger precision and trigger recall are not abstract governance metrics. They are the first behavioral proof that the skill can be discovered and used correctly.

## Output and Outcome Evaluation

The Agent Skills output-quality guide recommends writing skill-local test cases with a prompt, expected output, and optional input files. It also recommends comparing runs with the skill against a baseline without the skill or against a previous skill version.

Good assertions are concrete and observable: file exists, JSON is valid, chart has labeled axes, report includes at least three recommendations. Mechanical assertions should use scripts where possible. LLM graders and human reviewers are better suited for judgment-heavy qualities such as clarity, polish, completeness, and usefulness.

Anthropic's agent-eval guidance adds a useful distinction: grade the outcome when the path can vary. For many skills, the exact sequence of tool calls is less important than whether the final artifact, environment state, or user-facing answer is correct. Path checks are still useful when the skill is specifically about a required procedure or tool boundary.

## Trace and Trajectory Evaluation

OpenAI's trace-grading docs frame traces as end-to-end records of decisions, tool calls, and reasoning steps. LangSmith's trajectory-eval docs focus on the sequence of messages and tool calls. Both are useful for skills because a skill often changes what the agent does internally, not just what it says at the end.

Trajectory matching is useful when the expected workflow is fixed. Subset and superset checks are safer when only certain tool calls matter. LLM-as-judge trajectory grading can help when there are multiple reasonable paths, but its rubric should be clear and periodically checked against human judgment.

Transcript review remains important. Anthropic warns that unfair graders, ambiguous tasks, and overly rigid expected paths can make a good agent look bad. Reading transcripts helps distinguish a real skill failure from a broken eval.

## Reliability Metrics

Agent skills should be evaluated across repeated trials, not only one lucky run. Anthropic and tau-bench both highlight the difference between:

- `pass@k`: the chance that at least one of k attempts succeeds.
- `pass^k`: the chance that all k attempts succeed.

For creative or exploratory skills, `pass@k` may be acceptable because one good candidate can be enough. For procedural, compliance, customer-support, finance, legal, deployment, or safety-sensitive skills, `pass^k` is often the stricter and more relevant metric because users need consistent behavior.

## Non-Determinism and Error Budgets

Debois highlights a practical challenge with running context evals in CI/CD: LLMs are non-deterministic. Running an eval twice may produce different results. This means:

- A single pass/fail result is unreliable. Instead, run each test multiple times and track the success rate.
- **Error budgets** are a useful model: give a set of tests an allowed failure rate. Critical tests have tight budgets; convenience tests can tolerate more variance.
- Context changes influence which tests pass or fail, so tracking which specific tests become flaky after a context edit helps isolate the problem.

## End-to-End Testing with Judge Agents

Beyond checking generated code against rules, Debois describes giving the judge LLM tool access so it becomes an agent that can execute the code in a sandbox. This creates true end-to-end tests: the judge runs the endpoint, performs a curl, checks the response, and judges whether the behavior matches expectations. This is significantly stronger than regex or static checks because it validates runtime behavior.

Given a specific commit and context, this approach can answer: "did this context change make a difference, yes or no?" And the judge agent can use the feedback to automatically suggest context improvements.

## Practical Minimum for a Skill Repository

For each reusable skill, keep at least:

- a structural validation check;
- 8-10 realistic should-trigger prompts;
- 8-10 realistic should-not-trigger prompts;
- 2-5 output eval tasks with expected outputs and assertions;
- a baseline comparison against no skill or the prior skill version;
- transcript or trace samples from failures;
- a small regression suite for behaviors that must not break.

As the skill becomes important, add more trials per task, outcome-state checks, token and latency measurements, human review samples, and a maintenance owner.

## Where Sources Agree

The sources agree that skills need checks before release. The Agent Skills specification emphasizes YAML correctness, required fields, naming rules, progressive disclosure, and `skills-ref` validation. OpenAI emphasizes traces, graders, datasets, and eval runs. Anthropic emphasizes tasks, trials, graders, transcripts, outcomes, and long-term eval ownership. LangSmith emphasizes trajectory evaluation for tool-using agents. tau-bench emphasizes final state and reliability across trials.

They agree that a skill can be syntactically valid but still not useful. That is why evaluation is separate from validation.

## Where Sources Disagree

The ecosystem still does not establish one universal public conformance benchmark for skill triggering and execution. In other words, there is agreement that evaluation matters, but incompleteness around exactly how every platform should measure it.

The likely reason is that agent runtimes differ. A skill that routes well in one environment may behave differently in another if tool access, context handling, invocation policy, or activation logic differs.

There is also a tension between path grading and outcome grading. Some sources support trajectory checks because tool use matters. Anthropic cautions that overly strict path checks can punish valid alternative solutions. The practical compromise is to grade exact trajectories only when the procedure itself is the requirement; otherwise prefer outcome checks plus lightweight trajectory constraints.

## Connections

- [[Portable Skill Core]] explains why `name` and `description` need special validation attention.
- [[Vendor Adapters]] explains adapter drift checks.
- [[Skill Authoring Workflow]] explains when validation fits in the lifecycle.
- [[Skill Governance and Metrics]] explains operational KPIs.
- [[Progressive Disclosure]] explains why description quality matters for triggering.
- [[concepts/Replacing Code with Skills]] — Cursor's evals (headless CLI with dual scorers checking worktree compliance vs. primary checkout leakage) show how evals directly drive prompt improvement and RL training for skills.
- [[Context Development Lifecycle]] frames evaluation as the Evaluate stage within the broader Generate → Evaluate → Distribute → Observe loop, including error budgets and CI/CD for context.

## Open Questions

- What pass-rate and trigger-rate thresholds should be used for personal, team, and production skill repositories?
- Should each vendor publish standardized test prompts or trace schemas for portable skills?
- How should portable skill evals normalize differences between clients such as Codex, Claude Code, Gemini CLI, VS Code, and GitHub Copilot?
