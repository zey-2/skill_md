---
type: source-summary
created: 2026-06-08
updated: 2026-06-08
status: active
sources:
  - "raw/Lessons from building Claude Code How we use skills.md"
tags: [claude-code, skills, anthropic, authoring, distribution, skill-categories, progressive-disclosure]
---

# Lessons from building Claude Code: How we use skills

**Source**: Anthropic engineering blog, `https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills`
**Author**: Thariq Shihipar (member of technical staff, Anthropic, working on Claude Code)
**Published**: 2026-06-03

## Summary

Thariq Shihipar shares lessons from scaling hundreds of skills internally at Anthropic. The article catalogs nine skill categories, debunks the "skills are just markdown files" misconception, and provides concrete authoring and distribution guidance. Key themes: skills are folders (not just SKILL.md), the gotchas section is the highest-signal content, progressive disclosure via the file system, avoid railroading Claude, write descriptions for the model (not humans), and skills should improve through iterative gotcha accumulation.

## Key Points

### Skills Are Folders, Not Just Markdown

- A common misconception: skills are "just markdown files." They're actually **folders** that can include scripts, assets, data, etc. that the agent can discover, explore, and manipulate.
- Claude Code skills have a wide variety of configuration options including registering dynamic hooks.
- The most effective skills use configuration options and folder structure effectively.

### Nine Skill Categories

After cataloging all internal skills at Anthropic, the team found they cluster into nine categories:

| Category | Purpose | Example |
|---|---|---|
| 1. Library and API reference | Correct library/CLI/SDK usage, edge cases, gotchas | `billing-lib`, `internal-platform-cli`, `sandbox-proxy` |
| 2. Product verification | Test or verify code works; paired with Playwright, tmux, etc. | `signup-flow-driver`, `checkout-verifier`, `tmux-cli-driver` |
| 3. Data fetching and analysis | Connect to data/monitoring stacks | `funnel-query`, `cohort-compare`, `grafana`, `datadog` |
| 4. Business process and team automation | Automate repetitive workflows into one command | `standup-post`, `create-ticket`, `weekly-recap` |
| 5. Code scaffolding and templates | Generate framework boilerplate with natural-language requirements | `new-workflow`, `new-migration`, `create-app` |
| 6. Code quality and review | Enforce code quality; can run as hooks or GitHub Actions | `adversarial-review`, `code-style`, `testing-practices` |
| 7. CI/CD and deployment | Fetch, push, deploy code | `babysit-pr`, `deploy-service`, `cherry-pick-prod` |
| 8. Runbooks | Take a symptom, walk through investigation, produce structured report | `service-debugging`, `oncall-runner`, `log-correlator` |
| 9. Infrastructure operations | Routine maintenance with guardrails for destructive actions | `resource-orphans`, `dependency-management`, `cost-investigation` |

- **Product verification skills have had the most measurable impact on Claude's output quality internally.** "It can be worth having an engineer spend a week just making your verification skills excellent."
- The best skills fit cleanly into one category. Skills that try to do too much straddle several and confuse the agent.

### Don't State the Obvious

- Claude already knows how to code and read your codebase. A skill that restates what Claude would do by default adds context without adding value.
- Focus on information that **pushes Claude out of its normal way of thinking**.
- Example: the frontend design skill was built by iterating with customers to improve Claude's design taste, avoiding classic patterns like the Inter font and purple gradients.

### The Gotchas Section Is the Highest-Signal Content

- The highest-signal content in any skill is the Gotchas section.
- Gotchas should be built from common failure points that Claude runs into when using the skill.
- Example gotchas: "The `subscriptions` table is append-only. The row you want is the one with the highest version, not the most recent `created_at`." "This field is called `@request_id` in the API gateway and `trace_id` in the billing service. They're the same value." "Staging returns 200 even when the Stripe webhook didn't actually process. Check `payment_events` for the real state."

### Use the File System and Progressive Disclosure

- Think of the entire file system as a form of context engineering and progressive disclosure.
- Tell Claude what files are in your skill, and it will read them at appropriate times.
- Simplest form: point to other markdown files for detailed function signatures and usage examples (e.g., `references/api.md`).
- You can have folders of references, scripts, examples, etc.

### Avoid Railroading Claude

- Skills are reusable, so be careful of being too specific. Give Claude the information it needs but flexibility to adapt.
- Example: a skill that prompts the user if a Slack channel is not configured, rather than hardcoding a channel.

### Config.json for Setup

- Some skills need context from the user (e.g., which Slack channel to post to).
- Good pattern: store setup information in a `config.json` in the skill directory. If not set up, the agent asks the user.
- Can instruct Claude to use the AskUserQuestion tool for structured, multiple-choice questions.

### Write Descriptions for the Model, Not for Humans

- When Claude Code starts a session, it builds a listing of every available skill with its description. This listing is what Claude scans to decide "is there a skill for this request?"
- The description field is not a summary — it's a description of **when to trigger** this skill.
- Include trigger words in the description (e.g., "babysit" for the babysit-pr skill).

### Help Claude Remember

- Skills can include a form of memory by storing data within them — append-only text log files, JSON files, or SQLite databases.
- Example: a `standup-post` skill keeps a `standups.log` with every post it's written. Next time, Claude reads its own history and can tell what's changed since yesterday.
- Use `${CLAUDE_PLUGIN_DATA}` env variable for a stable persistent data directory.

### Store Scripts and Generate Code

- Giving Claude scripts and libraries lets it spend turns on composition rather than reconstructing boilerplate.
- Example: a `data-science` skill with a library of functions to fetch data. Claude generates scripts on the fly to compose this functionality for prompts like "What happened on Tuesday?"

### On-Demand Hooks

- Skills can include hooks that are only activated when the skill is called and last only for the session duration.
- Use for opinionated hooks you don't want running all the time:
  - `/careful` — blocks `rm -rf`, `DROP TABLE`, force-push, `kubectl delete` via PreToolUse matcher on Bash.
  - `/freeze` — blocks any Edit/Write outside a specific directory.

### Distributing Skills

Two distribution methods:
1. **Check into repo** (`.claude/skills`) — works well for small teams, but every skill adds to model context.
2. **Plugin marketplace** — as you scale, an internal marketplace lets team members choose which skills to install, with a setup flow.

### Managing a Skills Marketplace

- At Anthropic, no centralized team decides. Skills are shared organically — upload to a sandbox folder in GitHub, point people to it in Slack.
- Once a skill gets traction, the owner can PR it into the marketplace.

### Composing Skills

- Skills can depend on each other by referencing other skills by name. The model will invoke them if installed.
- Dependency management is not natively built into marketplaces or skills yet.

### Measuring Skills

- Use a PreToolUse hook to log skill usage within the company.
- This reveals which skills are popular or under-triggering compared to expectations.

## Evidence

- Anthropic has "hundreds of skills in active use" internally.
- The nine-category taxonomy came from cataloging all internal skills.
- Product verification skills had "the most measurable impact on Claude's output quality internally."
- The frontend design skill was built by an Anthropic engineer by iterating with customers.
- Example gotchas are quoted directly from the article as patterns for skill authors to emulate.
- The `standup-post` memory pattern uses `${CLAUDE_PLUGIN_DATA}` for persistent storage.
- On-demand hooks (`/careful`, `/freeze`) are described as internal Anthropic patterns.
- PreToolUse hook for skill usage measurement is shared with a link to example code.

## Connections

- [[concepts/Agent Skills]] — Skills as folders (not just SKILL.md) and the nine-category taxonomy expand the definition.
- [[concepts/Skill Authoring Workflow]] — Gotchas as highest-signal content, descriptions for models, config.json setup, progressive disclosure via file system, and on-demand hooks are concrete authoring patterns.
- [[concepts/Progressive Disclosure]] — The file system as progressive disclosure (point to references, scripts, examples) is a concrete implementation.
- [[concepts/Skill Distribution and Installation]] — Repo check-in vs. plugin marketplace, organic marketplace discovery, and skill composition.
- [[concepts/Skill Governance and Metrics]] — PreToolUse hook for measuring skill usage, marketplace organic governance.
- [[concepts/Self-Improving Skills]] — Iterative gotcha accumulation as a manual self-improvement pattern.
- [[concepts/Prompting Skills Not Prompts]] — Descriptions for models (not humans), three-layer architecture, and scripts inside skills confirm the Anthropic-internal rules.
- [[concepts/Skill Authoring Workflow]] — Nine categories as a gap-analysis framework for identifying missing skills.
- [[concepts/Meta-Skills and Skillification]] — Skill composition (skills referencing other skills) as the foundation for skillification.

## Contradictions or Tensions

- The article says skills are "not just markdown files" and emphasizes folders, scripts, and configuration — but many wiki sources (and the SKILL.md spec) center on the markdown file as the core. This is a framing difference: the spec defines the minimum, while Anthropic's internal practice shows the effective maximum.
- "Don't state the obvious" tensions with the advice from other sources to be thorough and explicit in skill instructions. The right balance depends on model capability — as models improve, less obvious restatement is needed.
- The organic marketplace governance (no centralized team, PR when ready) tensions with the security concerns from Snyk ToxicSkills research. Organic discovery works at Anthropic's scale and trust level but may not scale to public marketplaces.
- "Descriptions for the model, not humans" is a stronger claim than the cross-project research's "describe triggering conditions." Anthropic's version says the description is literally what Claude scans to decide — it's a routing instruction, not documentation.

## Open Questions

- How do the nine categories map to the existing wiki's skill taxonomy? Should the wiki adopt this categorization?
- What is the practical limit on skill composition before coordination overhead exceeds benefit?
- How does the PreToolUse hook for usage measurement interact with plugin-level permissions and MCP approval policies?
- Can the "store scripts inside skills" pattern scale to complex multi-file codebases, or is it best for single-file utilities?
- How should the gotchas section be structured for maximum agent consumption — prose, bullet points, or structured key-value pairs?
