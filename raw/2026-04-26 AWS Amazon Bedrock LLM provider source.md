# AWS Amazon Bedrock LLM provider source

Captured: 2026-04-26

Primary sources:

- Amazon Bedrock foundation model information: https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models-reference.html
- Supported foundation models in Amazon Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html

## Source Summary

Amazon Bedrock is AWS's managed foundation-model service. AWS documentation describes Bedrock as a place to run inference, evaluate models, set up knowledge bases, create agents, customize models, and purchase provisioned throughput.

For powering AI tools, Bedrock is most relevant when AWS governance, private networking, IAM, regional controls, and multi-provider access matter more than direct access to one model vendor.

## Provider Notes

- Bedrock supports first-party Amazon models, including Nova, Titan, and Amazon Rerank.
- Bedrock also lists major third-party model providers, including Anthropic Claude, Cohere, DeepSeek, Meta Llama, Mistral AI, OpenAI open-weight models, and others depending on region and feature.
- The supported model table tracks provider, model ID, regional support, input/output modalities, streaming support, and inference parameters.
- Bedrock exposes agent, knowledge-base, evaluation, customization, and provisioned-throughput workflows around the model catalog.

## AI Tool Fit

- Strong candidate for enterprise AI tools already hosted on AWS.
- Useful when the tool may need to switch between several foundation model providers through one cloud control plane.
- Good fit for production workloads needing AWS security posture, procurement, and operational controls.

## Open Questions

- The exact model set varies by region and deployment mode; confirm target regions before committing.
- Some providers or models may require additional approval, use-case details, or provisioned throughput.
