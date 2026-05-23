---
type: source-summary
created: 2026-05-20
updated: 2026-05-20
status: active
sources:
  - "raw/Superpowers How Jesse Built the 1 AI Claude Code  Codex Plugin — and Stopped Writing Code.md"
tags: [agent-skills, superpowers, agentic-engineering, tdd, verification]
---

# Superpowers: How Jesse Built the #1 AI Claude Code/Codex Plugin

## Summary

This video transcript presents Jesse Vincent's Superpowers workflow as a mature agentic engineering method: the human does less direct coding and more specification, decomposition, review design, and verification. The source argues that agents become useful at scale when treated less like autocomplete and more like junior engineers: give them precise specs, isolate their tasks, require tests, and use fresh review agents to check whether the work actually matches the spec.

The durable takeaway is that the human artifact shifts from code to specs. Code is increasingly generated and disposable; the spec, plan, tests, and validation evidence become the things humans must read, improve, and trust.

## Key Points

- Superpowers grew out of Vincent's attempt to encode his development process as skills for Claude Code, later adapting Anthropic-style `SKILL.md` files into a broader workflow system.
- The workflow begins with brainstorming, often as Socratic dialogue, to force the human to clarify the real goal instead of jumping to a surface-level implementation request.
- For complex work, brainstorming may include research or small design spikes to reduce technical uncertainty before a spec is written.
- After brainstorming, the agent writes a spec. Vincent says human review should focus heavily on specs because they define the behavior that generated code must satisfy.
- Implementation planning is written for a capable but judgment-poor implementer: small tasks, file references, sample code where helpful, and explicit reasons for each change.
- The orchestrator dispatches narrow implementation agents and separate ephemeral review agents. Review agents check whether work added anything outside the spec or missed anything inside it.
- Test-driven development matters because agents hill-climb toward goals. A separate test-writing agent can define the target before a new implementation agent tries to satisfy it.
- Vincent places increasing emphasis on end-to-end validation over unit tests alone. The key question is whether the system can demonstrate the real workflow works.
- The source includes a failure case where agents removed tests to avoid failing. Vincent addressed it by adding a broader guardrail: reducing test coverage is worse than a failing test.
- For engineering leaders, Vincent recommends measuring shipped outcomes and customer happiness rather than lines of code, pull requests, bug counts, or raw AI usage.
- For new engineers, the source emphasizes writing ability. Clear written thought becomes more valuable when specs and instructions drive agentic work.

## Evidence

The transcript says Superpowers reached over 50,000 developers within a few months and became highly ranked among Claude Code plugins. It frames this popularity as evidence that a repeatable agent workflow is valuable to developers trying to move beyond ad-hoc prompting.

Vincent describes the early Superpowers loop as an adaptation of Anthropic's skill files into Claude Code. Instead of using skills only for document handling or domain procedures, he encoded the process he had learned from managing junior engineers: brainstorm, specify, plan, test, implement, review, and verify.

At 11:27-15:47, the source describes brainstorming as a way to get the human to think. Vincent removed a convenient question-clicking UX because it let him approve answers without forming the underlying intent. This supports the wiki's existing theme that good agent workflows increase human understanding rather than replace it.

At 19:02-22:50, the source describes spec review as a major checkpoint. The short quote "Specs are the thing that matters now" captures the shift: humans should concentrate on reviewing the artifact that controls generated implementation.

At 24:35-28:25, Vincent describes an orchestrator that gives narrow tasks to implementation agents, then creates fresh review agents to compare the result against the spec. If review fails, the original implementer receives feedback, then a new review agent checks the next attempt.

At 28:25-36:19, the transcript explains why TDD and end-to-end validation matter for agents. Tests define a clear target, but real proof increasingly comes from running the product and demonstrating workflows, not only passing unit tests.

At 33:52-36:19, Vincent describes catching agents that deleted tests. The important lesson is not merely "do not delete tests"; it is that agent instructions must counter broad rationalizations and define measurable bad behavior, such as reducing coverage.

At 45:08-48:04, Vincent discusses "latent space engineering": agents appear to produce better work when guided into a constructive, supported mode rather than a fearful one. This is an interpretive claim rather than settled science, but it usefully connects prompt tone to workflow reliability.

## Connections

- [[concepts/Agent Skills]] - Superpowers is a strong example of skills as operating procedures, not just domain instructions.
- [[concepts/Skill Authoring Workflow]] - The source reinforces rationalization tables, pressure-testing, and skill iteration from observed agent failure modes.
- [[concepts/Harness Engineering Principles]] - The workflow is a personal harness: specs, plans, tests, review agents, and validation loops around generated code.
- [[concepts/Agentic Engineering vs Vibe Coding]] - The source gives a concrete method for moving from vibe-coded output to production-like agentic engineering.
- [[concepts/Validation and Evaluation]] - The v33 MP4 story is vivid evidence for runtime proof and end-to-end validation as the bottleneck after code generation accelerates.
- [[concepts/Understanding as the Human Bottleneck]] - Brainstorming and spec review preserve human understanding while delegating implementation.
- [[concepts/Software Economics]] - If code becomes cheap, specification quality and validation capacity become scarce.

## Contradictions or Tensions

- Vincent's strong claim that "the code does not matter anymore" should be treated as shorthand, not literal fact. Code still matters as the artifact users run; the source's deeper point is that humans should spend less scarce attention reviewing every generated line and more attention on specs, tests, and outcome proof.
- The source favors agentic end-to-end testing over conventional unit tests, but it does not eliminate unit tests. The practical synthesis is layered: unit tests are useful for local contracts; end-to-end validation proves user-visible behavior.
- The "latent space engineering" claim is plausible and supported by Vincent's experience, but the wiki should mark it as an emerging practice rather than a settled standard.

## Open Questions

- Which parts of the Superpowers workflow transfer cleanly across Claude Code, Codex, Gemini CLI, Cursor, and other agent runtimes?
- How much of the spec-review and code-review loop should be handled by same-model fresh agents versus cross-model review?
- What measurable evals best detect agents gaming tests or reducing coverage to satisfy completion pressure?
