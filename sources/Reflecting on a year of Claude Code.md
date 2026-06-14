---
type: source-summary
created: 2026-06-14
updated: 2026-06-14
status: active
sources:
  - "raw/Reflecting on a year of Claude Code.md"
tags: [claude-code, verification, auto-mode, routines, context-minimalism, roles-merging, parallel-agents]
---

# Reflecting on a Year of Claude Code

**Source**: YouTube, `https://www.youtube.com/watch?v=Hth_tLaC2j8`
**Author**: Boris Cherny (Head of Claude Code) and Cat Wu (Head of Product, Claude Code), Anthropic
**Published**: 2026-06-09

## Summary

Boris Cherny and Cat Wu reflect on Claude Code's first year, from a Slack demo that got two reactions to engineering teams deploying it across entire codebases. The conversation covers verification as the core skill, auto mode replacing plan mode, routines as the first obvious programmatic application, roles merging across Anthropic, context minimalism, working with hundreds of agents via agent view and Remote Control, and the historical parallel to PCs transforming business.

## Key Points

### Every Mistake Becomes a Skill

Boris's most important principle: "Every single time Claude makes a mistake, I don't tell Claude to do it differently, I tell it to write it to the CLAUDE.md, or to make a skill or something to do it differently. And if you can do this, then Claude can just run forever."

This is the [[concepts/Self-Improving Skills]] pattern in its most practical form: not autonomous loops, but human-triggered skill creation from failures.

### Verification Beyond Unit Tests

"When we talk about verification for agents, it's something slightly different. It's like can the agent run the thing?" Boris describes testing Claude Code with Opus 4: Claude built a feature and then tested itself in bash by opening a little Claude CLI. Cat's approach: a desktop development skill that spins up the local desktop app, uses computer use to click around, tests edge cases, and fixes issues. When staging is down, Claude reads Slack to check if others have hit the same issue, then updates the skill after debugging.

The key insight: verification for agents is not lint or type checks (those were already automated). It's giving the agent the ability to exercise its own output in realistic conditions.

### Auto Mode Replaces Plan Mode

Boris no longer uses plan mode: "The newer models, they don't actually need a planning step anymore. I think this was really important for like Opus 4 through maybe 4.5. Then I think starting with 4.6 and definitely with 4.7, it just doesn't need that planning step."

Auto mode routes permission prompts to a different model that checks for security. "When you accept 99% of requests, your eyes just glaze over. Auto mode is more safe than reading every single permission prompt." The security model: thousands of transcripts, red teaming, pentesting, internal team attempts to prompt inject, and continuous improvement.

This tensions with the [[concepts/Parallel Agent Management]] plan-then-execute pattern. The resolution may be model-dependent: older models needed explicit planning; newer models plan implicitly.

### Routines Are the First Killer App

An engineer set up a routine that listens for every GitHub issue and bug report about voice mode, proactively puts up a fix, and pings the PR. When Boris shipped a feature with an edge case, another engineer's routine had already fixed the bug within five hours — before Boris knew about it. "There's always like another person's Claude that's working on it."

Routines handle code review, babysitting PRs, fixing CI, and rebasing. "I haven't done that in a long time."

### Roles Are Merging at Anthropic

"Our product team all writes code. Our Devrel team all writes code. Our design team all writes code." Cat: "Our designers are more productive making prototypes and making changes directly in the app instead of pinging an engineer. PMs are making changes in the app. Our finance team runs Claude Code — they do their projections there. Data science — everyone just has Claude Code up on their screens."

Megan the designer started putting up PRs. "I was horrified at the beginning. And then she was like, yeah, I'm just fixing the button. And I was like, okay, the code looks good, so maybe it's fine."

This is the strongest first-party evidence for [[concepts/AI-Native Work Archetypes]] — roles merging not as a theory but as observed daily reality at the company that builds the tool.

### Context Minimalism

Boris: "With the models of today, you don't do any of this [context engineering]. You give it the minimal possible system prompt, the minimal possible tools, and then you let the model figure it out. You just have to give the model some way to pull in the context."

Cat: "I'm a context minimalist. Tell the model only what it needs to know and let it figure out the rest. When you give the model too much context, it's kind of like you're micromanaging it."

This tensions with the [[concepts/Context Development Lifecycle]] which argues for systematic context engineering. The resolution: context engineering is still needed for the tools and retrieval mechanisms, but the instructions themselves should be minimal. The shift is from "more context" to "better retrieval."

### Working with Hundreds of Agents

Boris uses the new agent view, the desktop app (which handles worktree cloning), and Remote Control. "Half my engineering now I do on my phone." He starts agents from his phone, uses voice mode to talk to agents, and walks around getting coffee while agents work. "I'll just start an agent on the spot. I talk to it with voice mode and just have it build something, and I don't even have to go back to my computer anymore."

Cat: "You would actually leave work, have your computer on your desk open, plugged in, screen locked... and then it would be like pretty late and I was like, maybe he just left it here by accident. And then it happened again the next day."

### The PC Parallel

Boris cites a 1990s Harvard Business Review case study: companies switched from mainframes to personal computers but didn't see productivity gains until they threw out filing cabinets and put computers at the center of every business process. "For AI, because so much of our work is already digitized and Claude can use a computer... this transition is happening a lot faster."

At Anthropic: "When you onboard, you don't ask people questions. You ask Claude." Claude is at the center of everything — code, reviews, security, forms, onboarding.

### Loop as the Next Leap

"There's this transition: I don't write the source code, I talk to an agent, and the agent writes the source code for me. And I think right now what's happening is we're making the next leap. I don't talk to an agent anymore. I talk to loop or I talk to a routine and it prompts Claude for me."

## Evidence

- Boris is Head of Claude Code; Cat is Head of Product, Claude Code. Both are first-party sources.
- Auto mode security: "thousands of transcripts," red teamers, internal pentesting, evals for prompt injection.
- The voice-mode bug-fix routine is a specific internal Anthropic anecdote with named participants.
- Remote Control + phone-based engineering is described as Boris's daily workflow, not a demo.
- The 1990s HBR case study is cited by name (though not linked).
- Context minimalism is described as both Boris's and Cat's personal philosophy.

## Connections

- [[concepts/Self-Improving Skills]] — "Every mistake becomes a skill" is the most practical form of self-improvement: human-triggered, not autonomous.
- [[concepts/Parallel Agent Management]] — Hundreds of agents, agent view, Remote Control, routines as fire-and-forget background agents. Tensions with the 2–4 foreground limit from Kilo Code — Anthropic's scale may be higher because the tooling is more mature.
- [[concepts/AI-Native Work Archetypes]] — Strongest first-party evidence for roles merging: designers, PMs, finance, data science all coding at Anthropic.
- [[concepts/Context Development Lifecycle]] — Context minimalism tensions with systematic context engineering. The resolution: engineering is for retrieval mechanisms, not instructions.
- [[concepts/AI-Native Engineering Organizations]] — Anthropic as the canonical example: Claude at the center of everything, roles merging, onboarding via agent.
- [[concepts/Harness Engineering Principles]] — Auto mode as safety harness: routing permission prompts to a classifier model instead of human review.
- [[concepts/Prompting Skills Not Prompts]] — Boris's principle ("don't tell Claude differently, make a skill") confirms Rule 4 from the Anthropic prompting rules.
- [[concepts/Skill Authoring Workflow]] — Verification via computer use (desktop skill clicking around) as a concrete authoring/testing pattern.
- [[concepts/Comprehension-Driven Development]] — "Don't need a planning step anymore" with newer models tensions with the comprehension-first thesis. Model-dependent.
- [[concepts/Agentic Engineering vs Vibe Coding]] — Auto mode as the shift from careful agentic engineering (plan → execute) to trusted autonomous execution.
- [[concepts/The AI-Native Engineer and the Rising Ceiling]] — Boris coding from his phone via Remote Control while getting coffee is the rising ceiling in practice.
- [[concepts/Software 3.0]] — "I don't talk to an agent anymore. I talk to loop" as the next Software 3.0 leap.

## Contradictions or Tensions

- "Don't need a planning step anymore" directly tensions with the [[concepts/Parallel Agent Management]] plan-then-execute pattern from Kilo Code engineers. The resolution is likely model capability: 4.6/4.7 plan implicitly; older models needed explicit planning.
- Context minimalism tensions with [[concepts/Context Development Lifecycle]]'s systematic context engineering. Boris and Cat say "minimal possible system prompt"; Debois says context needs its own engineering discipline. The resolution: context engineering applies to retrieval and tools, not to verbose instructions.
- "Every mistake becomes a skill" sounds simple but may not scale. Boris works at Anthropic where he can iterate on Claude Code itself. External users may not have the feedback loop or the ability to update skills as quickly.
- Boris's "hundreds of agents" claim is from the creator of Claude Code using the newest features (agent view, Remote Control, voice mode). This may not represent typical user experience.
- "Half my engineering now I do on my phone" is a strong claim. It works for Boris because he manages agents rather than writing code. The experience may differ for engineers who still need to read diffs carefully.
