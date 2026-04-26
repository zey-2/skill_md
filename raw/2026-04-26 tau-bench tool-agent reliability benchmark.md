---
type: raw-source
created: 2026-04-26
source_type: web
source_url:
  - "https://huggingface.co/papers/2406.12045"
  - "https://arxiv.org/abs/2406.12045"
accessed: 2026-04-26
status: raw-notes
tags: [agent-benchmarks, tool-use, reliability, pass-k]
---

# tau-bench tool-agent reliability benchmark

## Source Identity

The tau-bench paper evaluates tool-using agents in realistic domains with simulated users, API tools, policy guidelines, and outcome-state grading.

## Relevant Extracted Facts

- tau-bench targets tool-agent-user interaction in realistic domains.
- The benchmark emulates conversations between a user simulator and a language agent.
- The agent receives domain-specific API tools and policy guidelines.
- Evaluation compares the final database state at the end of the conversation with an annotated goal state.
- The paper proposes pass^k to measure reliability across multiple trials.
- The Hugging Face paper summary reports that contemporary function-calling agents were inconsistent, with pass^8 below 25% in the retail domain in the reported experiments.
- The benchmark emphasizes consistency and rule-following, not just one-off success.

## Relevance to Skill Validation and Evaluation

Agent skills often package policy, procedure, and tool-use instructions. tau-bench is relevant because it evaluates whether an agent follows domain rules and achieves the correct end state across realistic multi-turn interactions. Its pass^k framing is especially useful when a skill must work reliably every time rather than occasionally.

## Open Questions

- tau-bench is a benchmark for agents, not specifically for portable `SKILL.md` packages. A skill repository would need to adapt the benchmark idea into skill-specific task suites.
