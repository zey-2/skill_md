---
type: source-summary
created: 2026-06-01
updated: 2026-06-01
status: active
sources:
  - "raw/How the engineer behind Claude Cowork actually uses Claude  Felix Rieseberg (Anthropic).md"
tags: [claude-cowork, model-selection, personal-agents, anti-todo-list, hardware-agents]
---

# How the engineer behind Claude Cowork actually uses Claude — Felix Rieseberg

**Source**: How I AI podcast / YouTube, `https://www.youtube.com/watch?v=-tdNsYi8AXs`  
**Speaker**: Felix Rieseberg (engineering lead for Claude Cowork, Claude Code, Claude Desktop at Anthropic)  
**Published**: 2026-05-25  
**Created**: 2026-06-01

## Summary

Felix Rieseberg, engineering lead for Claude Cowork and Claude Code Desktop at Anthropic, shares how he uses Claude products in his personal and professional life. Key patterns include: using email as a source of truth for personal inventory (furniture, purchases), going "one abstraction layer up" when facing tedious tasks (the anti-to-do list), building interactive 3D furniture planners from floor plans, creating personal live-artifact dashboards, and connecting Claude to $20 IoT hardware devices. He also provides a practical heuristic for model selection: reach for Opus when you don't know what you're asking for; Sonnet 4.6 is sufficient for well-scoped problems.

## Key Points

- **Model selection heuristic**: Sonnet 4.6 handles most daily tasks well. Reach for Opus when the problem itself is ambiguous — when you need help figuring out what question to ask. The distinction is about problem decomposition, not technical complexity.
- **The biggest gap is not capabilities, it's imagination.** Most people don't realize that almost any problem can go into AI tools.
- **Pre-convergent era**: We're in the "time right before we came up with the glass pebble as the correct shape for a phone." Multiple form factors (Code, Cowork, Chrome, Desktop) exist because different tasks need different entry points.
- **Anti-to-do list**: When doing something tedious, stop and ask: can Claude do this? Then go another layer up: how can I never have to do this again?
- **Email as personal inventory source**: Claude can read purchase emails to build a furniture inventory, eliminating manual data entry.
- **Going one abstraction layer up**: Instead of manually entering furniture dimensions, tell Claude to figure out what furniture you have. Instead of tracking promises manually, have Claude read your messages and track them.
- **Judging by impact, not process**: Rieseberg is getting comfortable not supervising Claude closely, judging only on output quality. This is harder for control freaks but necessary for scale.
- **Politeness to Claude is about human humanity**: Being nice to Claude is good for the human's mental health and communication habits, not because Claude cares.
- **"I know it's possible" prompting**: Telling Claude you know something is possible (even if you don't know how) gives it confidence and preempts pushback.
- **Async design makes latency delightful**: Get users comfortable with asynchronous tasks. People are fine waiting if the quality at the end is very good.
- **AI should free creative energy**: "AI is used poorly if it just needs to move the mouse cursor for you." The vision is AI doing annoying things in the background so humans can focus on creative ideas.
- **$20 hardware Claude buddy**: Built a tiny IoT device ($19) with Wi-Fi and Bluetooth that acts as a physical approval button and cheerleader for Claude. Claude Code built all the firmware in one shot.
- **Kids are magical AI users**: They've never learned what not to ask for. They don't have the "mind prison" of things not working.
- **When Claude goes off rails**: Debug the workflow, not the model. Ask Claude what went wrong and how to prevent it. Usually the fix is in the harness, prompt, or data source — not in giving up.
- **Thumbs up/down buttons matter**: They end up on the product team's desk and are used in model and product training.

## Evidence

- Rieseberg built an interactive 3D furniture planner from a marketing floor plan by uploading the plan to Cowork and asking for units. Claude figured out garage dimensions from a permit document and built the 3D model without being asked.
- He created a personal live-artifact dashboard pulling from Spotify, Gmail, Calendar, and Notion connectors, with a refresh button for live data.
- His 9-year-old is a daily active Claude user who uses the terminal to discover device IDs and explore cybersecurity.
- The $20 hardware device (IoT with LCD screen, Wi-Fi, Bluetooth) was programmed entirely by Claude Code in one shot with no corrections needed.

## Connections

- [[concepts/Ride the Models]] — Rieseberg's role evolution and continuous experimentation with new Claude features.
- [[concepts/Anti-To-Do List and Abstraction Layering]] — Primary source for the "go one abstraction layer up" pattern.
- [[concepts/Understanding as the Human Bottleneck]] — "The biggest gap is not capabilities, it's imagination" — people need to understand what problems AI can solve.
- [[concepts/Personal AI Agents and Memory Systems]] — Email as personal inventory source, promise tracker, furniture planner — all personal agent patterns.
- [[concepts/Harness Engineering Principles]] — Debugging the harness, not the model, when things go wrong.

## Contradictions or Tensions

- Rieseberg says he doesn't closely supervise Claude, but as the engineering lead for these products, he has deep knowledge of capabilities and limitations that average users lack.
- The "politeness to Claude" advice is explicitly about human psychology, not model behavior — though others (like Thariq Shihipar) report better outcomes from trust-based prompting.
- The "I know it's possible" prompting technique may encourage models to attempt things that are genuinely not possible, wasting compute.

## Open Questions

- How can the "anti-to-do list" pattern be encoded as a reusable skill?
- What are the privacy implications of using email as a personal inventory source?
- Will hardware-Claude integrations become a new category of personal agent interfaces?
- How do we bridge the gap between "almost any problem can go into AI tools" and the lack of user imagination about what to ask?
