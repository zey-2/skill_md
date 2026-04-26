# DeepSeek API LLM provider source

Captured: 2026-04-26

Primary sources:

- DeepSeek API docs: https://api-docs.deepseek.com/
- Azure Foundry Models source mentioning DeepSeek availability: https://azure.microsoft.com/en-us/products/ai-foundry/models/

## Source Summary

DeepSeek is a popular model provider whose models are available directly through DeepSeek API docs and indirectly through major model hubs such as Azure Foundry Models and several open-model inference providers. The DeepSeek quickstart says the API uses a format compatible with OpenAI and Anthropic, with OpenAI and Anthropic base URLs.

For powering AI tools, DeepSeek is relevant for cost-sensitive reasoning and coding workloads, but production use should pay close attention to hosting path, data handling, reliability, and geopolitical/procurement constraints.

## Provider Notes

- DeepSeek appears in Azure Foundry's curated catalog and Serverless API availability list.
- Open-model inference providers such as Together AI and Hugging Face route or host DeepSeek-family models.
- DeepSeek's quickstart lists `deepseek-v4-flash` and `deepseek-v4-pro` as current model names.
- The same quickstart says `deepseek-chat` and `deepseek-reasoner` are scheduled for deprecation on 2026-07-24, with compatibility mappings to non-thinking and thinking modes of `deepseek-v4-flash`.
- Example API calls use the OpenAI-style `/chat/completions` path, `reasoning_effort`, and an extra `thinking` body field for thinking mode.
- The best implementation path may be direct DeepSeek API, Azure Foundry, Together, Hugging Face routing, Fireworks, or another host depending on governance requirements.

## AI Tool Fit

- Strong candidate to benchmark for coding, reasoning, and cost-sensitive workloads.
- Often more practical through a trusted cloud or inference hub when procurement, regional control, or unified billing is required.
- Useful as a secondary or fallback model if quality and latency are acceptable.

## Open Questions

- The direct API docs should be rechecked for current model IDs, pricing, and rate limits before implementation.
- Verify data residency, retention, and compliance requirements carefully before sending sensitive data.
