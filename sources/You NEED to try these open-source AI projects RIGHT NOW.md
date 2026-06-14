---
type: source-summary
created: 2026-06-14
updated: 2026-06-14
status: active
sources:
  - "raw/You NEED to try these open-source AI projects RIGHT NOW.md"
tags: [open-source, skills, context-compression, tokenmaxxing, search, tools]
---

# You NEED to try these open-source AI projects RIGHT NOW

**Source**: YouTube, `https://www.youtube.com/watch?v=zjFE-dBzP_E`
**Author**: Matthew Berman
**Published**: 2026-06-13

## Summary

Matthew Berman showcases four free open-source GitHub projects: (1) **Last30Days** — a skill-based search engine that aggregates trending content from Reddit, HN, Poly Market, GitHub, X, YouTube, and TikTok scored by human engagement; (2) **Open Notebook** — a fully local, open-source NotebookLM clone with podcast generation; (3) **Agent Skills** — a seven-slash-command engineering workflow skill (interview, spec, plan, build, test, review, ship); and (4) **Headroom** — a context compression wrapper that reduces token usage by 47–92% across Claude Code, Cursor, and Codex without quality degradation.

## Key Points

### Last30Days: Skills as Search Interfaces

- A skill that functions as a new type of search engine. Instead of serving links and ads, it queries Reddit upvotes, HN stories, Poly Market odds, X likes, YouTube transcripts, and TikTok engagement.
- "It is what is trending lately on the internet, and it gives you that information" — scored by human voting, not an algorithm.
- The V3 engine resolves where to search before the search begins (e.g., "openclaw" resolves to Peter Steinberger's Twitter and relevant subreddits).
- Can emit HTML briefs for sharing. Install by pasting the GitHub URL into your agent.
- By Matt Van Horn, co-founder of the company that became Lyft. 40K+ GitHub stars.

### Open Notebook: Local NotebookLM

- Free, open-source, fully local NotebookLM clone. Upload PDFs/documents, ask questions, generate podcasts.
- Can be powered by hosted models (OpenAI) or completely local models (Ollama, LM Studio).
- Features: insights extraction, dense summaries, paper analysis, reflection questions, table of contents.
- Podcast generation is customizable: multi-host, different tones, script editing.
- 30K GitHub stars.

### Agent Skills: Seven-Stage Engineering Workflow

- A skill with seven slash commands mapping to engineering stages: `/interview-me`, spec, plan, build, test, review, code, simplify, ship.
- Similar to GStack by Garry Tan but focused specifically on engineering workflow rather than company building.
- `/interview-me` conducts a step-by-step interview to extract what the user wants to build, structures it as markdown.
- 56K GitHub stars.

### Headroom: Context Compression

- Compresses everything the AI agent reads — tool outputs, logs, RAG chunks, files, conversation history — before it reaches the LLM.
- "Same answers, fraction of the tokens."
- Concrete savings:
  - Code search with 100 results: 17,000 → 1,400 tokens (92% savings)
  - Incident debugging: 65,000 → 5,000 tokens (92% savings)
  - GitHub issue tracking: 54,000 → 14,000 tokens (73% savings)
  - Codebase exploration: 78,000 → 41,000 tokens (47% savings)
- Tested on GSM8K, TruthfulQA, SQuAD v2, and BFCL — accuracy preserved.
- `headroom perf` command shows per-model savings breakdown, cache performance, optimization overhead.
- `headroom learn` mines failed sessions and writes corrections to CLAUDE.md and AGENTS.md.
- Works with Claude Code, Cursor, and Codex.
- 24K GitHub stars, exploding in June 2026.
- Caveat: installs "serena" by default and has telemetry enabled by default — disable with `--no-sa` and `--no-telemetry` flags.

## Evidence

- Last30Days: 40K+ GitHub stars, built by Matt Van Horn (Lyft co-founder company).
- Open Notebook: 30K GitHub stars, podcast generation demonstrated on a "Long Humans" essay.
- Agent Skills: 56K GitHub stars, `/interview-me` demonstrated live.
- Headroom: 24K GitHub stars with June 2026 star explosion, concrete token savings percentages across four use cases, accuracy preserved on four benchmarks.
- Berman demonstrates installing each skill by pasting the GitHub URL directly into the agent.

## Connections

- [[concepts/Tokenmaxxing]] — Headroom is a direct tokenmaxxing tool: it compresses context to get the same answers with fewer tokens, effectively multiplying the token budget. `headroom learn` is a self-improvement pattern that mines failed sessions.
- [[concepts/Context Rot]] — Headroom's compression addresses context rot by reducing the amount of noise and redundancy before it reaches the model. The 60% quality-drop threshold from Kilo Code becomes less relevant when compression keeps effective context well below that threshold.
- [[concepts/Progressive Disclosure]] — Last30Days is a skill that functions as a search interface — it loads context on demand based on the query, rather than dumping everything into context. This is progressive disclosure applied to information retrieval.
- [[concepts/Prompting Skills Not Prompts]] — All four projects are installable as skills with simple URL-based installation. Agent Skills maps the engineering workflow into composable slash commands.
- [[concepts/Skill Distribution and Installation]] — The "paste URL and say install" pattern is demonstrated across all four projects, confirming the skill-as-package distribution model.
- [[concepts/Self-Improving Skills]] — `headroom learn` is a concrete self-improvement pattern: mining failed sessions and writing corrections to CLAUDE.md/AGENTS.md.
- [[concepts/Parallel Agent Management]] — Headroom enables more parallel agents by reducing per-agent token consumption, potentially allowing more agents within the same budget.
- [[concepts/Software Economics]] — Open-source tools that compress costs and provide free alternatives to hosted services (Open Notebook vs. NotebookLM) reinforce the abundance thesis.
- [[concepts/Context Development Lifecycle]] — Headroom's compression and learn features are tools for the Generate and Observe stages of the context lifecycle.

## Contradictions or Tensions

- Headroom claims "same answers, fraction of the tokens" and passes four benchmarks, but the benchmarks are standard NLP benchmarks, not coding-agent benchmarks. The real-world savings on complex multi-turn coding tasks may differ.
- Headroom installs serena and enables telemetry by default — Berman explicitly flags this as "kind of annoying" and advises disabling both. This is a trust/supply-chain concern relevant to [[concepts/Skill Security and Supply Chain Risk]].
- The "install by pasting URL" pattern works for open-source skills but doesn't address governance, versioning, or security auditing — all concerns raised by the Snyk ToxicSkills research.
