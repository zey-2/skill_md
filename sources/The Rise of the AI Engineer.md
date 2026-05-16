---
type: source-summary
created: 2026-05-16
updated: 2026-05-16
status: active
sources:
  - "raw/The Rise of the AI Engineer.md"
tags: [ai-engineer, job-roles, software-3-0, prompt-engineering, latent-space]
---

# The Rise of the AI Engineer

**Source**: Latent Space, `https://www.latent.space/p/ai-engineer`
**Author**: swyx (Latent Space)
**Published**: 2023-07-01
**Venue**: Latent Space newsletter

## Summary

Foundational article coining "AI Engineer" as an emerging job title distinct from ML Engineer and Prompt Engineer. Argues that foundation models created a "shift right" of applied AI — tasks that once required 5 years and a research team now require API docs and an afternoon. Predicts AI Engineer will become the highest-demand engineering job of the decade.

## Key Points

- **"Shift right" of applied AI** — Foundation models moved AI capabilities across a permeable API line. AI Engineers work on the application side; ML/Research Engineers work on the model side. Both sides are permeable.
- **AI Engineer vs ML Engineer** — ML Engineers train models; AI Engineers build atop APIs. Predicted AI Engineer jobs would outnumber ML Engineer jobs within 5 years. No PhD required; "when it comes to shipping AI products, you want engineers, not researchers."
- **Why now** — Few-shot learning and in-context transfer mean model creators don't fully know model capabilities. Frontier labs corner research talent, making it rentable via API. "Fire, ready, aim" workflow: prompt-validated prototypes move 1,000-10,000x cheaper than traditional ML.
- **AI is Agile** — Analogy to Waterfall vs Agile. Traditional ML: laborious data collection, train one domain model, deploy. AI Engineering: prompt LLM, validate product idea, then fine-tune with specific data if needed.
- **Software 3.0** — Karpathy's Software 2.0 (neural networks) evolves to Software 3.0: English as the hottest new programming language, with human-written code orchestrating LLM power. Distinction between "software atop intelligence" vs "intelligent software."
- **Code is re-emerging** — After the Prompt Engineering hype, 2023 saw re-emergence of Software 1.0 paradigms: LangChain, Voyager (code generation/reuse), Codium AI. The primary architectural divide is between applications built around code vs applications built around LLM generation.
- **Python + JavaScript expansion** — AI Engineering tools expanding from Python-only (LangChain, LlamaIndex) to JavaScript (LangChain.js, Transformers.js, Vercel AI SDK), doubling the addressable developer base.
- **Generative AI vs Classifier ML** — Where ML focused on fraud detection, recommendations, anomaly detection, AI Engineers build writing apps, personalized learning tools, natural language interfaces.
- **Community convergence** — `#discuss-ai` Slack channels turning into formal teams. Independent hackers, startup engineers, and big-tech developers converging on "AI Engineer" as the least cringe title.

## Evidence

- Karpathy quote: "In numbers, there's probably going to be significantly more AI Engineers than there are ML engineers / LLM engineers. One can be quite successful in this role without ever training anything."
- Examples of AI Engineers at Microsoft, Google, Figma (via Diagram), Vercel (RoomGPT), Notion (Notion AI), Anthropic ($300k/yr prompt engineering), OpenAI ($900k salaries).
- AI Engineer Summit announced as first independently-run, builder-oriented AI conference.
- HN discussion on "How to Break into AI Engineering" — top answers still recommended ML/Data Engineering prerequisites, which the author argues no effective AI Engineer actually followed.

## Connections

- [[concepts/Software 3.0]] — The article introduced Software 3.0 as the evolution beyond Karpathy's Software 2.0, with English as the programming surface.
- [[concepts/Agentic Engineering vs Vibe Coding]] — The "fire, ready, aim" workflow is an early articulation of what became vibe coding vs agentic engineering.
- [[concepts/The AI-Native Engineer and the Rising Ceiling]] — The AI Engineer role is the predecessor to the AI-native engineer concept.
- [[concepts/Harness Engineering Principles]] — "You want engineers, not researchers" is an early statement of the harness engineering thesis.
- [[concepts/Replacing Code with Skills]] — The article's "code core vs LLM shell" architectural divide is the precursor to the skills-vs-code discussion.
- [[concepts/LLM Fundamentals]] — The article argues you don't need to understand transformers to be an AI Engineer — experience with models is sufficient. This tension (fundamentals vs practical use) is central to LLM Fundamentals.
