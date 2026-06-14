---
title: "After Automation"
source: "https://every.to/p/after-automation"
author:
  - "[[The Every Team]]"
published:
created: 2026-06-14
description: "AI progress creates more work for humans, not less"
tags:
  - "clippings"
---
## ##Explainer

Dan Shipper's essay **After Automation** starts from a paradox. At Every, we use Codex, Claude Code, OpenClaw, and frontier models across coding, writing, design, customer support, and operations. But the human job has not disappeared. It has moved up a level in expertise.

Agent Mode turns the essay into a working session: connect your coding agent to the companion repo, inspect the arguments, and apply it into your own workflows.

## ##How to use this

1. Copy the setup prompt below.
2. Paste it into Codex, Claude Code, OpenClaw, or another coding agent.
3. Let your agent open the companion repo and read the core files.
4. Choose one starter prompt to push deeper

## ##Connect your agent

Paste this into Codex, Claude Code, OpenClaw, or the coding agent of your choosing once.

```
You are helping me read and use Dan Shipper's Every essay, "After Automation."
https://every.to/p/after-automation

Use this companion GitHub repo as your source of truth:
https://github.com/EveryInc/after-automation-agent-mode

If you can access GitHub or run shell commands, clone or open that repo first. Then read:
- README.md
- AGENTS.md
- claims.md
- prompts/starter-prompts.md
- prompts/objections-and-responses.md
- case-studies/every-ai-native-workflows.md

Only read after-automation.md or files in sources/ when I ask for deeper evidence or source work.

Do not answer from the essay alone. Use the repo to understand the argument, inspect the evidence, and turn it into a workflow I can try.

Start by giving me:
1. the cleanest version of the core claim;
2. the part of the argument most relevant to what you know about me;
3. if you have enough context, one prompt I should run next based on my work, context, and goals; otherwise, one useful prompt from the repo to start with.

If I ask you to apply the essay to my work and you can inspect my workspace, inspect available context before interviewing me: recent project files, README or AGENTS instructions, docs, notes, commits, issue lists, calendars, or other connected tools that show how I actually work.

If you cannot access GitHub directly, tell me what repo files you need me to paste or upload before you continue.
```

## ##Prompts

### Understand the argument

Engage with the cleanest version of Dan's thesis.

### Inspect the evidence

Choose a claim, audit the sources, and grapple with the strongest open questions.

### Apply it to my work

Use my available context first, then turn the essay into one workflow.

### Work through objections

Steelman a counterargument, test Dan's answer, and apply it to a real workflow.