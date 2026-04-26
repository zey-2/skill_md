# Open model inference providers source

Captured: 2026-04-26

Primary sources:

- Together AI serverless models: https://docs.together.ai/docs/serverless-models
- Groq supported models: https://console.groq.com/docs/models
- Fireworks AI model overview: https://docs.fireworks.ai/models/overview
- Hugging Face Inference Providers: https://huggingface.co/docs/inference-providers/index

## Source Summary

Several popular providers focus on hosting open or third-party models with fast, OpenAI-compatible, or unified inference APIs. These providers are useful when an AI tool needs model variety, low latency, lower cost, or access to open model families without running GPU infrastructure.

This category includes Together AI, Groq, Fireworks AI, and Hugging Face Inference Providers.

## Provider Notes

### Together AI

- Together AI's serverless model catalog includes chat, image, vision, video, audio, embedding, rerank, and moderation models.
- The chat-model list includes MiniMax, Qwen, Moonshot/Kimi, Z.ai, OpenAI GPT-OSS, DeepSeek, and other model families.
- The docs point to recommended models, OpenAI compatibility, function calling, structured outputs, and dedicated inference options.

### Groq

- GroqCloud lists production models and systems, including Llama 3.1/3.3, OpenAI GPT-OSS, Whisper, and Groq Compound.
- Groq emphasizes token speed, production/preview status, context windows, and OpenAI-compatible model listing.
- Groq Compound is described as an AI system powered by openly available models that can selectively use built-in tools such as web search and code execution.

### Fireworks AI

- Fireworks models can be served through serverless inference or dedicated deployments.
- Fireworks describes serverless inference as shared, per-token, and best-effort, while dedicated deployments provide more control and performance guarantees.
- Fireworks states that it does not log or store prompt/generated data except for metadata required to operate the service, with documented exceptions for certain proprietary or opt-in features.

### Hugging Face Inference Providers

- Hugging Face provides a unified proxy layer across multiple inference providers.
- The provider-selection docs describe automatic provider selection, explicit provider selection, failover, unified billing, and OpenAI-compatible chat-completions routing.
- Listed partner capabilities include LLM chat providers such as Cerebras, Cohere, Fireworks, Groq, Hugging Face Inference, Hyperbolic, Nebius, Novita, SambaNova, Scaleway, Together, Z.ai, and others.

## AI Tool Fit

- Strong candidate category for prototypes, open-model experiments, high-throughput inference, model fallback, and cost-sensitive applications.
- Useful when a tool wants OpenAI-compatible APIs but not necessarily OpenAI-hosted models.
- Less ideal as the first choice for conservative enterprise governance unless the provider's security, support, uptime, and data policies match the workload.

## Open Questions

- Benchmark latency and quality with the exact model and deployment mode; provider-level claims are not enough.
- Check whether serverless deployments have uptime or latency guarantees; dedicated deployments may be needed for production.
- Confirm data retention and training policies for each provider before using sensitive user data.
