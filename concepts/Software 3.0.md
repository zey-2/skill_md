---
type: concept
created: 2026-05-02
updated: 2026-05-02
status: active
sources:
  - "raw/Andrej Karpathy From Vibe Coding to Agentic Engineering.md"
tags: [software-3-0, prompting, context-window, karpathy]
---

# Software 3.0: Prompting as Programming

## Key Points

Software 3.0 is a new computing paradigm where the context window becomes the programming surface. Instructions, examples, files, logs, specifications, errors, constraints, and goals are placed into context, and the model acts on them. Prompting is not merely communication — it becomes a form of programming.

This paradigm enables capabilities that were not possible before, not just faster versions of old workflows.

## The Paradigm Shift

| Paradigm | Programming Surface | Mechanism |
|----------|-------------------|-----------|
| Software 1.0 | Explicit code | Humans write instructions line by line |
| Software 2.0 | Data and objectives | Humans arrange datasets, define loss functions, train networks |
| Software 3.0 | Context window | Humans place information into context; the LLM interprets and computes |

## Examples

**OpenClaw installer.** In Software 1.0, installation logic is a shell script that must handle operating systems, missing dependencies, environment differences, path issues, permissions, network failures, and every edge case explicitly. In Software 3.0, the installer is a block of text given to an agent. The agent reads the environment, identifies errors, adapts commands, debugs itself, and continues. The script does not need to encode every branch because the agent contributes intelligence at execution time.

**MenuGen.** Karpathy built a Vercel app to OCR restaurant menus and generate food photos — a real stack with real implementation work. Later, he realised that Gemini plus Nano Banana could accomplish much of the same task directly through one prompt. The intermediate application became unnecessary. The neural network itself replaced the app layer.

**LLM knowledge bases.** A traditional program can store notes, index documents, and display pages. But there was no conventional code that could convert a pile of facts into different useful projections: a wiki, a comparison table, a glossary, a timeline, a study guide, or a question map. The model itself becomes the new capability.

## The MenuGen Question

The important personal question this raises is: **what is my MenuGen?** Which systems have I built in the old style that may already be obsolete? More importantly, what can now be built that was not possible before?

AI should not only be framed as a speedup for existing workflows. Some capabilities are genuinely new.

## Context for This Wiki

Software 3.0 explains why [[concepts/Agent Skills]] are structured the way they are. Skills are operating procedures designed for the context window — they package the instructions, examples, and constraints that guide agents. The paradigm also connects to [[concepts/MCP and Tool-Integration Architecture]] because the agent's intelligence at execution time depends on the tools and resources available to it through MCP.

## Connections

- [[concepts/LLM Fundamentals]] — Understanding how LLMs work (tokenization, transformer architecture, RLHF) explains why the context window behaves as it does and why skills need precise wording and progressive disclosure.
- [[concepts/OpenAI Responses API]] — The Responses API represents OpenAI's API-layer shift toward the Software 3.0 model, with preserved reasoning state and server-side agentic loops.
- [[concepts/Agent Skills]] — Skills are the structured knowledge packages that populate the context window in Software 3.0.

## Source

- [[raw/Andrej Karpathy From Vibe Coding to Agentic Engineering]]
