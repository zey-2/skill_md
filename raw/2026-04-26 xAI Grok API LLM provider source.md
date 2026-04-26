# xAI Grok API LLM provider source

Captured: 2026-04-26

Primary sources:

- xAI models and pricing: https://docs.x.ai/developers/models
- xAI API introduction: https://docs.x.ai/docs/introduction

## Source Summary

xAI offers developer API access to Grok models. The current models page says xAI offers models for multiple use cases and modalities and recommends Grok 4.20 for chat and coding through the API. The docs also describe Voice API and Imagine API for audio, image, and video capabilities.

For powering AI tools, xAI is most relevant when Grok's model behavior, coding capability, X/search integration, or multimodal roadmap is specifically useful.

## Provider Notes

- The current docs present Grok 4.20 as the recommended general model for API callers.
- xAI describes dedicated APIs for chat, voice, image, and video.
- Tool pricing applies to xAI-provided server-side tools, with costs based on token usage and tool invocations.
- The docs mention server-side tools such as web search, X search, code execution, and collection search.
- The API is distinct from Grok in grok.com, mobile apps, and X.

## AI Tool Fit

- Candidate for tools that need Grok specifically, especially where X search or xAI server-side tools matter.
- Good to evaluate for coding assistants because xAI documents code-editor integrations and recommends Grok 4.20 for coding.
- Less proven than AWS/Azure/GCP/OpenAI/Anthropic for conservative enterprise procurement unless the organization has a specific reason to choose it.

## Open Questions

- Confirm enterprise controls, regional endpoints, support posture, and data handling before regulated workloads.
- Benchmark hallucination behavior, tool reliability, and cost because xAI is evolving quickly.
