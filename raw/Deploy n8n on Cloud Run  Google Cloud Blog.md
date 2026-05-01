---
title: "Deploy n8n on Cloud Run | Google Cloud Blog"
source: "https://cloud.google.com/blog/topics/developers-practitioners/deploy-n8n-on-cloud-run"
author:
  - "[[Ryan Pei]]"
published: 2025-11-08
created: 2026-05-01
description: "With just a few commands, you can deploy n8n to Cloud Run and have it up and running, ready to supercharge your business with AI workflows that can manage spreadsheets, read and draft emails, and more."
tags:
  - "clippings"
---
Developers & Practitioners

## Easy AI workflow automation: Deploy n8n on Cloud Run

##### Ryan Pei

Product Manager

##### Try Gemini Enterprise Business Edition today

The front door to AI in the workplace

[Try now](https://business.gemini.google/?utm_source=cloud.google.com/blog&utm_medium=et&utm_campaign=FY26-Q2-GLOBAL-GLO27877-physicalevent-er-next26-mc-105752)

[n8n](https://n8n.io/) is a powerful yet easy-to-use workflow and automation tool for multi-step AI agents, and many teams want a simple, scalable, and cost-effective way to self-host it. With just a few commands, you can deploy n8n to Cloud Run and have it up and running, ready to supercharge your business with AI workflows that can manage spreadsheets, read and draft emails, and more. The [n8n docs](https://docs.n8n.io/hosting/installation/server-setups/google-cloud-run) now tell you how to deploy the official n8n Docker image to our serverless platform, connect it to Cloud SQL for persistent data storage, call Gemini as the agents’ LLM, and (optionally) connect your workflows directly to Google Workspace.

### Deploy n8n to Cloud Run in minutes

You can deploy the official n8n image directly to Cloud Run. This gives you a managed, serverless environment that automatically scales from zero to handle any workload, so you only pay for what you use. That means whenever you’re not actively using n8n, you’re not paying for any compute and your n8n data is persisted in Cloud SQL.

To first try out n8n quickly on Cloud Run, deploy it with this one command:

```
gcloud run deploy --image=n8nio/n8n \
```

```
--allow-unauthenticated \
```

```
--port=5678 \
```

```
--no-cpu-throttling \
```

```
--memory=2Gi
```

This gives you a running instance of n8n that you can use to try out n8n and all its awesome features for workflow automation with the power of AI. Connect your first n8n agent to Gemini (provide your Gemini API key for the “Google Gemini Chat Model” credentials) and see it in action.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/1_-_basic_n8n_setup.max-1200x1200.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/1_-_basic_n8n_setup.max-1200x1200.png)

Then when you’re ready to use n8n for actual workflows, you can follow the steps in the [n8n docs](https://docs.n8n.io/hosting/installation/server-setups/google-cloud-run/#durable-mode) for a more durable, secure setup (using Cloud SQL, Secrets Manager, etc.). You can either use a Terraform script or follow along step-by-step through each gcloud command in the instructions.

### Connect Google Workspace tools

A key benefit of hosting on Google Cloud is the ability to easily connect n8n to your Google Workspace tools. The [n8n docs](https://docs.n8n.io/hosting/installation/server-setups/google-cloud-run/#optional-enabling-google-workspace-services-as-n8n-tools) walk you through the steps to configure OAuth for Google Cloud, allowing your n8n workflows to securely access and automate tasks using Google tools like Gmail, Google Calendar, and Google Drive.

Here’s a demo showing an n8n instance on Cloud Run that uses Gmail and Google Calendar to schedule appointments on your behalf whenever an email hits your inbox with a request to meet:

The two AI agents in this n8n workflow call Gemini to do the following:

- The **Text Classifier** reads your incoming emails to see which ones are asking for time to meet
- The **Agent** checks your calendar for your availability, and sends a response with a suggested time

### Cloud Run is great for all AI apps

Cloud Run is a versatile, easy-to-use runtime for all your AI application needs. Whether your agentic app was made with n8n, [LangChain](https://cloud.google.com/blog/products/ai-machine-learning/deploy-langchain-on-cloud-run-with-langserve), [ADK](https://google.github.io/adk-docs/deploy/cloud-run/), or no framework at all, you can deploy it to Cloud Run. This collaboration on Cloud Run and n8n is another example of how we aim to simplify the process for developers to build and deploy intelligent applications.

### Next steps

- Read more about [Cloud Run](https://cloud.run/) (or just [try it out in the web console](https://console.cloud.google.com/run)!)
- Explore [n8n](https://n8n.io/)