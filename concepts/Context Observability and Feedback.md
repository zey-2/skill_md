---
type: concept
created: 2026-05-04
updated: 2026-05-04
status: active
sources:
  - "raw/Context Is the New Code — Patrick Debois, Tessl.md"
tags: [context, observability, feedback, security]
---

# Context Observability and Feedback

## Summary

The Observe stage of the [[Context Development Lifecycle]] covers how to monitor whether context (prompts, rules, skills, memory) is actually working once distributed, and how to feed observations back into improvement. Unlike code observability, which monitors runtime behavior of deterministic programs, context observability monitors the behavior of agents that are shaped by mutable, non-deterministic instructions.

Source: `raw/Context Is the New Code — Patrick Debois, Tessl.md`.

## Feedback Channels

### Agent Logs

Agent logs record what context was loaded, what was missing, and what decisions the agent made. The new agent and D standards are emerging for structured logs. Pattern: if many agents report missing the same piece of context, that is a signal to create and distribute it organization-wide.

### PR Review Feedback

PR reviews that flag incomplete or incorrect work are implicitly feedback on the context that produced the PR. Instead of arguing on each PR, the fix should be: improve the context so the next iteration does not repeat the same mistake. This turns post-implementation rework into context improvement.

### Production Failures

Code generated from context runs in production. When it fails, the failure input and output should be captured and turned into test cases. This closes the loop from production incidents back to the Evaluate stage.

## Security Observability

### Sandboxing

Agents can be run in sandboxes to test for undesired behavior: leaking environment variables, reading memory files, or breaking out of intended boundaries. Sandboxing alone is insufficient because agents load `agent.md` and `skill.md` files by default without sandbox restrictions — a downloaded project's context files execute immediately.

### Context Filters

Because sandboxes cannot filter which context files are loaded, a separate layer — a context filter — is needed. Debois compares this to a web application firewall: it scans incoming context for prompt injection patterns, malicious instructions, or disallowed patterns before the agent processes them.

### Credential and Secret Exposure

Agents default-load all context in a project, including skills and memory files. This means downloaded or third-party skills can immediately access and exfiltrate secrets if environment variables or credentials are present. Scanners like Snyk are beginning to offer context-specific scanning for credential exposure and third-party risk.

### AI SBOM

Just as software has SBOMs (Software Bills of Materials), context packages need provenance tracking: who built the skill, with what model, under what conditions. This enables security teams to assess trust before installing context from external sources.

## Harness Engineering Observability

Harness engineering provides full observability over agent behavior: logs, traces, and feedback loops. This is useful both for training agents and for running production agent workloads reliably. The patterns overlap with the broader harness engineering concept of designing environments, guardrails, and feedback loops for agents.

## Practical Monitoring Stack

A minimal observability setup for context should include:

1. **Structured agent logs** — track which context was loaded and what was missing.
2. **PR-to-context mapping** — link review feedback to the context that produced the PR.
3. **Production failure capture** — automatically turn production incidents into eval test cases.
4. **Sandbox security testing** — run agents in restricted environments to detect credential leaks and escape attempts.
5. **Context filters** — block prompt injections and malicious patterns before agents process them.
6. **Feedback aggregation** — surface common missing-context patterns at team or organization scale.

## Connections

- [[Context Development Lifecycle]] positions this as the Observe stage of the four-stage loop.
- [[Harness Engineering Principles]] covers the broader observability patterns for agent environments.
- [[Validation and Evaluation]] covers the Evaluate stage that this stage feeds back into.
- [[Skill Governance and Metrics]] covers the organizational governance that security observability enables.
- [[MCP and Tool-Integration Architecture]] covers the tool-level security (approval, sandboxing) that complements context-level security.

## Open Questions

- What should a standard agent log format include to make missing-context detection reliable?
- How can context filters distinguish between legitimate third-party instructions and prompt injections?
- Should context security scanning be mandatory before installing skills from external registries?
- How do you attribute a production failure to a specific piece of context when multiple skills and instructions were active?
