---
type: raw-source
created: 2026-04-26
source_type: web
source_url: "https://docs.langchain.com/langsmith/trajectory-evals"
accessed: 2026-04-26
status: raw-notes
tags: [agent-evals, langsmith, trajectories, tool-calls]
---

# LangSmith AgentEvals trajectory evaluation docs

## Source Identity

LangSmith documentation describes trajectory evaluations using the open-source `agentevals` package and LangSmith.

## Relevant Extracted Facts

- Some agent behaviors only appear when running a real LLM, such as tool choice, response formatting, and whole execution trajectory changes after prompt edits.
- Agent trajectories are the exact sequence of messages, including tool calls.
- AgentEvals supports trajectory matching and LLM-as-judge evaluation.
- A trajectory match compares an actual run against a reference trajectory.
- Strict trajectory matching is appropriate when a workflow has a well-defined expected path.
- Subset and superset modes focus on which tools were called rather than exact order.
- Subset mode helps ensure the agent did not call irrelevant or unnecessary tools.
- Superset mode helps verify key required tools were called while allowing additional calls.
- LLM-as-judge trajectory grading can evaluate reasonableness or quality when exact trajectory matching is too rigid.

## Relevance to Skill Validation and Evaluation

Trajectory evaluation is useful for agent skills because many skills change the route an agent takes, not just the final answer. A skill eval can check whether the agent loaded the skill, called the expected helper script, avoided unrelated tools, or followed a multi-step procedure.

## Open Questions

- Trajectory matching can be brittle if a skill intentionally permits multiple valid paths; in those cases, subset/superset checks or outcome grading are better.
