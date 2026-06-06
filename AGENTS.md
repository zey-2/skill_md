# LLM Wiki Agent Instructions

This repository is an LLM-maintained personal knowledge base. Treat the wiki like a codebase: sources are immutable inputs, generated markdown pages are maintained artifacts, and every update should leave the system easier to navigate than before.

## Project Layout

- `skill_md/` is the Obsidian vault and wiki root.
- `skill_md/raw/` contains raw source material. Do not modify, rewrite, summarize in place, rename, or delete files in `raw/` unless the user explicitly asks.
- `skill_md/raw/assets/` may contain downloaded images or attachments referenced by raw sources.
- Generated wiki pages live under `skill_md/`, outside `raw/`.
  - `skill_md/sources/` contains source-summary pages — one per raw source with key points, quotes, and cross-links.
  - `skill_md/concepts/` contains concept pages synthesized across multiple sources.
- `skill_md/index.md` is the content catalog. Create it if missing.
- `skill_md/log.md` is the append-only activity log. Create it if missing.
- `skill_md/.obsidian/` contains Obsidian settings. Do not edit it unless the user asks for vault configuration changes.

If a future reorganization adds folders such as `sources/`, `entities/`, `concepts/`, `syntheses/`, or `queries/`, follow the local structure already present and update this file when conventions change.

## Operating Principles

- The human curates sources, asks questions, and guides judgment.
- The LLM maintains the wiki: summaries, links, entities, concepts, contradictions, indexes, and logs.
- Prefer persistent wiki updates over one-off chat answers when the result is useful beyond the current conversation.
- Preserve provenance. Every substantive claim added to the wiki should be traceable to a source page, raw source, or logged inference.
- Keep raw sources immutable. The wiki may interpret sources, but it must not silently alter them.
- Keep pages interlinked with Obsidian wikilinks such as `[[Page Name]]`.
- When evidence conflicts, record the disagreement instead of smoothing it away.
- When uncertain, mark uncertainty explicitly and suggest what source would resolve it.

## Page Conventions

Use plain Markdown with Obsidian-compatible links.

Recommended frontmatter for generated pages:

```yaml
---
type: source-summary | entity | concept | synthesis | query-answer | index | log
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active
sources:
  - "[[Source Page Name]]"
tags: []
---
```

For pages where frontmatter would add friction, keep the page simple and prioritize clear content. Consistency is useful, but useful knowledge is the goal.

Recommended page sections:

- `# Title`
- `## Summary` for the durable takeaway.
- `## Key Points` for concise claims.
- `## Evidence` for source-grounded details.
- `## Connections` for links to related pages.
- `## Contradictions or Tensions` when sources disagree.
- `## Open Questions` for unresolved gaps.

Use stable, descriptive page names. Prefer `Title Case` for entities and concepts. Avoid duplicate pages for the same subject; merge or cross-link when overlap appears.

## Citations and Evidence

- Cite wiki pages with wikilinks.
- Cite raw files with relative paths when no generated source page exists, for example `raw/article-name.md`.
- For PDFs, note the file path and page number when available.
- For web-derived sources already clipped into `raw/`, cite the local source first.
- Do not invent citations. If the wiki lacks evidence, say so and propose an ingest or search step.
- Separate source claims from agent inference. Use phrases such as "The source states..." versus "A reasonable inference is..."

## `index.md`

`index.md` is the wiki map. Read it before answering non-trivial queries, and update it after every ingest or significant page creation.

Suggested structure:

```markdown
# Index

## Sources
- [[Source Title]] - One-line summary.

## Entities
- [[Entity Name]] - One-line summary.

## Concepts
- [[Concept Name]] - One-line summary.

## Syntheses
- [[Synthesis Title]] - One-line summary.

## Query Answers
- [[Question or Answer Title]] - One-line summary.
```

Keep entries short. The index is for navigation, not full summaries.

## `log.md`

`log.md` is chronological and append-only. Add an entry for every ingest, substantial query, lint pass, reorganization, or schema change.

Use this parseable heading format:

```markdown
## [YYYY-MM-DD] ingest | Source Title
## [YYYY-MM-DD] query | Question Title
## [YYYY-MM-DD] lint | Scope
## [YYYY-MM-DD] maintenance | Change Summary
```

Each log entry should include:

- What changed.
- Files created or updated.
- Important decisions, uncertainties, or follow-ups.

Do not rewrite old log entries except to fix obvious formatting errors.

## Ingest Workflow

When the user asks to ingest a source:

1. Identify the raw source file and inspect it without modifying it.
2. Read `skill_md/index.md` and recent entries in `skill_md/log.md` if present.
3. Create or update a source-summary page for the new source.
4. Extract durable entities, concepts, dates, claims, and useful quotes or data points.
5. Update existing entity, concept, and synthesis pages touched by the source.
6. Add new pages only when the concept or entity is likely to be reused.
7. Record contradictions, confirmations, and changes in confidence.
8. Update `index.md`.
9. Append a `log.md` entry with files changed and follow-ups.

Prefer ingesting one source at a time when the user is actively reviewing. For batch ingests, keep summaries more mechanical and log the batch boundaries clearly.

## Query Workflow

When answering a question against the wiki:

1. Read `index.md` first if it exists.
2. Search the wiki with `rg` for relevant terms, names, aliases, and concepts.
3. Read the relevant generated pages before raw sources.
4. Use raw sources when the wiki is thin, ambiguous, or the answer needs verification.
5. Answer with citations to wiki pages and source files.
6. If the answer is durable, ask whether to file it or proactively create a query-answer page when the user has asked for wiki maintenance.
7. If a new page is created, update `index.md` and append to `log.md`.

Good query outputs may include a concise answer, comparison table, synthesis page, outline, chart, or slide-ready markdown. Choose the simplest durable format that fits the question.

## Lint Workflow

When asked to lint or health-check the wiki, inspect for:

- Pages missing from `index.md`.
- `index.md` entries pointing to missing pages.
- Orphan pages with few or no inbound links.
- Important entities or concepts mentioned repeatedly but lacking pages.
- Contradictions between pages.
- Claims that newer sources supersede.
- Missing citations or weak provenance.
- Duplicated pages covering the same subject.
- Stale open questions that can now be answered.

Produce a short report with recommended fixes. If the user asked you to repair the wiki, make the edits, update `index.md`, and append a `log.md` entry.

## Image and Attachment Handling

- Markdown image links in raw sources may point to local attachments.
- Read the text first, then inspect images only when they materially affect the summary or answer.
- Do not rely on remote image URLs when local assets exist.
- If an image supports an important claim, mention the asset path in the relevant page.

## Maintenance Rules

- Before editing, check for existing pages that should be updated instead of creating duplicates.
- Keep edits scoped to the requested operation and directly related maintenance.
- Do not erase useful older interpretations. If a newer source changes the view, note the update and preserve the history when relevant.
- Prefer small, well-linked pages over giant catch-all documents.
- Use tables for comparisons and timelines when they improve scanability.
- Keep summaries concise enough to be useful as navigation surfaces.
- Avoid dumping long source excerpts into generated pages.
- If a workflow convention changes, update `AGENTS.md` and log the schema change.

## Presentation Output

All generated presentation HTML files (e.g., from `/presentation-slides` or similar skills) must be deposited in the `courses/` folder at the repo root, following the naming convention:

```
courses/presentation-{topic-slug}.html
```

Do NOT place presentations under `content/`, `skill_md/`, or any other directory. The `courses/` folder is the canonical output location for all slide decks and presentation artifacts.

## Tooling Preferences

- Use `rg` or `rg --files` for search when available.
- Use standard filesystem reads for markdown and text sources.
- For PDFs, use an appropriate PDF extraction workflow and cite page numbers when available.
- Use Obsidian-compatible Markdown and wikilinks.
- Optional future search tools such as `qmd` may be added when the wiki grows beyond what `index.md` plus `rg` can handle.
- **Git commit messages**: The Bash tool runs in bash, not PowerShell. Do not use PowerShell here-strings (`@'...'@` or `@"..."@`) for multi-line commit messages — bash will split them on newlines and pass each line as a separate argument, causing `error: pathspec` failures. Use a single-line `-m "..."` flag instead, or use the `&&` operator to chain `git add` and `git commit` in a single call.

## Completion Checklist

For ingest or maintenance work, finish with:

- Relevant pages created or updated.
- `index.md` updated.
- `log.md` appended.
- Contradictions or open questions recorded.
- A concise summary to the user naming the changed files.

For query-only work, finish with:

- A cited answer.
- Any uncertainty clearly marked.
- A recommendation on whether the answer should be filed into the wiki.
