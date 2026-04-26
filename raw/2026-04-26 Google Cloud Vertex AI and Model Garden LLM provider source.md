# Google Cloud Vertex AI and Model Garden LLM provider source

Captured: 2026-04-26

Primary sources:

- Google Cloud Model Garden: https://cloud.google.com/model-garden
- Google Cloud generative AI model docs: https://cloud.google.com/vertex-ai/generative-ai/docs/models

## Source Summary

Google Cloud positions Vertex AI / Model Garden as an enterprise model hub for discovering, customizing, and deploying models from Google and selected partners. The current Model Garden page describes a curated set of 200+ models and emphasizes model choice, customization with customer data, one-click deployment, and end-to-end MLOps.

For powering AI tools, Google Cloud is most relevant when the project already uses Google Cloud, needs Gemini first-party models, or wants managed access to open and third-party models under cloud governance.

## Provider Notes

- First-party model families include Gemini for language, multimodal reasoning, and coding; Imagen for image generation; Veo for video; and Chirp for speech-to-text.
- Open-model access includes Gemma, CodeGemma, PaliGemma, Meta Llama, Mistral AI, AI21, Falcon, BERT, T5-FLAN, ViT, and EfficientNet.
- Third-party model support explicitly includes Anthropic Claude.
- The platform pitch is less about a single API model and more about model discovery, customization, deployment, and ML operations inside Google Cloud.

## AI Tool Fit

- Strong candidate for enterprise AI tools that need cloud IAM, governance, model evaluation, and deployment controls.
- Natural fit for teams already standardized on Google Cloud or BigQuery/Vertex workflows.
- Particularly attractive for Gemini-native tools and multimodal use cases.

## Open Questions

- Pricing, regional availability, and per-model quota should be checked at implementation time because model availability changes frequently.
- Confirm whether the target AI tool needs the Google Gen AI API directly or the Vertex AI managed API surface.
