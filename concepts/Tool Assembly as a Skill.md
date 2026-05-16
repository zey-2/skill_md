---
type: concept
created: 2026-05-16
updated: 2026-05-16
status: active
sources:
  - "raw/Building a Second Brain Vivian Balakrishnan AI Engineer Singapore.md"
tags: [tool-assembly, no-code, agent-building, accessibility, personal-agents]
---

# Tool Assembly as a Skill

## Summary

Building functional AI systems no longer requires writing code — the skill is selecting, configuring, and connecting existing tools. Tool assembly sits between vibe coding (prompting to generate code you don't fully understand) and agentic engineering (designing specs, evals, and harnesses for agents). It is a distinct capability: technical literacy without coding.

## Key Points

- **No glue code needed** — Dr. Balakrishnan built a personal agent connecting NanoClaw, Neoman, Ollama, Whisper, and Obsidian "without writing any glue code." The tools integrated through their existing interfaces.
- **Tool selection is the skill** — The value is not in building tools but in knowing which tools exist, what each does well, how they connect, and which combination serves the use case.
- **Containerization matters** — "There's no such thing as a routine operation and things will go wrong. When they do break, hopefully you want them to break within barriers." Containerized tools (NanoClaw) isolate failures.
- **Short codebases build trust** — "The fact that NanoClaw has a very short code base which even an idiot like me can read and sort of understand" — understandability matters even if you don't write code.
- **Bash approval as learning** — NanoClaw insists on bash approval for every command. Scanning through these approvals builds understanding of what the agent is doing, even without coding ability.
- **Learn by doing** — "It's not enough to sit down and read, get the headlines, get the summaries done. If you're interested in anything, get your hands wet."
- **You cannot govern technology you have only been briefed on** — Technical literacy (reading code, understanding tool behavior) is different from coding ability but equally necessary for accountability.

## Evidence

- Dr. Balakrishnan assembled a production personal agent in 3 months, running on a 2-3 year old Raspberry Pi with 8GB RAM, without writing any code.
- The agent communicates via WhatsApp, has graph-based memory, local embeddings, speech-to-text, and wiki generation — a genuinely functional system.
- "I have not dared to switch it off" — the system is practically useful, not a toy.
- NanoClaw v1→v2 transition was rough; he kept v1 running and put v2 on another computer — demonstrating independent system management ability.

## Tool Assembly vs. Adjacent Patterns

| Pattern | What it is | Who does it | Output |
|---------|------------|-------------|--------|
| **Tool Assembly** | Select, configure, connect existing tools | Anyone with technical literacy | Functional system |
| **Vibe Coding** | Prompt LLM to generate code you don't fully understand | Anyone with access to LLM | Code (may be fragile) |
| **Agentic Engineering** | Design specs, evals, harnesses for agents | Engineers | Production agent system |
| **Software Engineering** | Write, test, deploy, maintain code | Software engineers | Software |

Tool assembly trades flexibility for speed and accessibility. The assembled system is constrained by what the tools can do and how they connect. But for many use cases, the existing tool surface is sufficient.

## Connections

- [[concepts/Personal AI Agents and Memory Systems]] — Tool assembly is the method by which personal agents are built.
- [[concepts/Agentic Engineering vs Vibe Coding]] — Tool assembly is a third pattern: neither vibe coding (no code generated) nor agentic engineering (no specs/evals designed), but genuine system building.
- [[concepts/Harness Engineering Principles]] — Assembling tools is a form of harness: building scaffolding around AI capabilities.
- [[concepts/Understanding as the Human Bottleneck]] — "You cannot govern a technology you have only been briefed on" — tool assembly requires understanding, not just briefing.
- [[concepts/Skill Authoring Workflow]] — Skills themselves can be seen as tool assembly: combining LLM instructions, reference files, and scripts into a reusable package.

## Contradictions or Tensions

- **Accessibility vs. technical literacy** — Tool assembly is presented as accessible to non-coders, but Dr. Balakrishnan is a retired eye surgeon who assembles watches and reprograms appliances. The minimum technical literacy (understanding containers, reading code for comprehension, scanning bash approvals) is real and non-trivial.
- **Flexibility ceiling** — Tool assembly is constrained by the tools available and their integration points. When no tool exists for a specific need, coding becomes necessary. The "ceiling" is the tool ecosystem's coverage.
- **Maintenance burden** — Assembling tools means maintaining the connections between them. When one tool updates (NanoClaw v1→v2), the entire assembly may break. This is the integration tax of tool assembly.

## Open Questions

- What is the minimum technical literacy needed for effective tool assembly? Can it be taught systematically?
- Which tool combinations have emerged as stable "stacks" for common use cases?
- Can tool assembly be formalized into reusable patterns (e.g., "agent + memory + interface" as a template)?
- How does tool assembly relate to Agent Skills? Are skills a form of tool assembly, or a different layer entirely?
- At what point does a tool-assembled system need to transition to coded integration?
