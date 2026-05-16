---
type: concept
created: 2026-05-16
updated: 2026-05-16
status: active
sources:
  - "raw/Building a Second Brain Vivian Balakrishnan AI Engineer Singapore.md"
tags: [memory-systems, graph-memory, embeddings, personal-knowledge, agent-memory]
---

# Graph-Based Memory for AI Agents

## Summary

The emerging pattern that persistent memory for AI agents should be graph-based — storing entities, relationships (causal, temporal, semantic), and embeddings — rather than flat databases or keyword indexes. Graph memory enables semantic search, relationship discovery, and contextual reasoning that flat storage cannot support. This is "the frontier" for personal and enterprise agent design.

## Key Points

- **Graph memory stores relationships, not just facts** — Entities connected by edges representing causality, temporal relationships, and semantic similarity. This allows the agent to traverse relationships ("what else is connected to this person?") rather than just look up keywords.
- **Semantic search over keyword search** — Local embedding models (e.g., Ollama) enable the agent to find relevant information even when the user's query uses different vocabulary than the stored content.
- **Multiple edge types enable different queries** — Causal edges support "why did this happen?" queries. Temporal edges support "what changed since last time?" queries. Semantic edges support "what's similar to this?" queries.
- **Local embeddings preserve privacy** — Running embeddings locally (Ollama) means raw content never leaves the device, even if the LLM API is cloud-based.
- **Memory is the differentiator** — The LLM's knowledge is frozen at training time. The agent's personal knowledge — curated, graph-structured, continuously updated — is what makes it individually useful.
- **Multiple tools competing** — Neoman (used by Balakrishnan), Zep, Graphiti, Mem0, and other memory systems are all converging on the graph+embedding pattern. No clear winner yet.

## Evidence

- Dr. Balakrishnan's personal agent uses Neoman, a graph-based memory system with entities, causality, temporal relationships, and semantic edges, combined with local Ollama embeddings for semantic search.
- He reports the system is "incredibly useful" for meeting preparation, travel, speech drafting, and parliamentary questions — use cases that require connecting disparate pieces of information.
- The combination with Obsidian (wiki UI) and iCloud (sync) creates a personal cloud knowledge base accessible across devices.

## Memory Architecture Layers

| Layer | Example | Purpose |
|-------|---------|---------|
| Storage | Graph database | Entities, relationships (causal, temporal, semantic) |
| Embeddings | Ollama (local) | Semantic search vectors |
| Ingestion | LLM extraction | Curate material → extract entities → store in graph |
| Retrieval | Semantic + graph traversal | Query → embed → find similar → traverse relationships |
| Interface | Obsidian, chat UI | Human-readable navigation and query |
| Sync | iCloud, local filesystem | Cross-device availability |

## Connections

- [[concepts/Personal AI Agents and Memory Systems]] — Graph memory is a core component of the personal agent pattern.
- [[concepts/LLM Fundamentals]] — LLMs have no persistent memory between sessions. Graph memory solves this architectural gap.
- [[concepts/Context Development Lifecycle]] — Memory is the "Distribute" and "Observe" layer: extracted knowledge is stored, then retrieved and evaluated.
- [[concepts/Self-Improving Skills]] — Memory systems could feed eval results back into skill improvement loops.
- [[concepts/Progressive Disclosure]] — Graph traversal can be a progressive disclosure mechanism: start with a broad entity, then traverse deeper as context budget allows.

## Contradictions or Tensions

- **Graph complexity vs. practical value** — Graph databases with four edge types (causal, temporal, semantic, entity) are significantly more complex to build and maintain than flat vector stores. The ROI of causal edges specifically is unproven.
- **Local vs. cloud embeddings** — Local embeddings (Ollama) preserve privacy but use lower-quality embedding models than cloud alternatives. The quality gap affects semantic search accuracy.
- **Who curates the memory** — Balakrishnan's system is personally curated (speeches, transcripts, curated material). For enterprise agents, the curation burden is much higher — who decides what goes into the organizational memory graph?
- **Memory decay** — Graph memory accumulates over time but does not automatically prune outdated or contradicted information. Unlike LLM weights, graph data is mutable but has no natural forgetting mechanism.

## Open Questions

- How do Neoman, Zep, Graphiti, and Mem0 compare in practice? Which edge types actually drive agent quality?
- Can graph memory be shared between agents (agent-to-agent knowledge transfer)?
- How should contradictions between stored facts be represented in the graph?
- Is there a role for Agent Skills in standardizing memory ingestion patterns (what to extract, how to structure entities)?
- What is the minimum viable graph? Can a simple entity+semantic-edge system work without causal and temporal edges?
