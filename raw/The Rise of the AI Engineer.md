---
title: "The Rise of the AI Engineer"
source: "https://www.latent.space/p/ai-engineer"
author:
  - "[[Latent.Space]]"
published: 2023-07-01
created: 2026-05-16
description: "Emergent capabilities are creating an emerging job title beyond the Prompt Engineer."
tags:
  - "clippings"
---
### Emergent capabilities are creating an emerging title: to wield them, we'll have to go beyond the Prompt Engineer and write \*software\*, and AI that writes software.

**We are observing a once in a generation “shift right” of applied AI**, fueled by the emergent capabilities and open source/API availability of Foundation Models.

A wide range of AI tasks that used to take [5 years and a research team](https://xkcd.com/1425/) to accomplish in **2013**, now just require API docs and a spare afternoon in **2023**.

![](https://substackcdn.com/image/fetch/$s_!Bojh!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa81555af-0b76-4a61-9b53-595e3d47580a_1005x317.png)

Important: the API line is permeable - AI Engineers can go left to finetune/host models and Research Engineers go right to build atop APIs too! This diagram has also been criticized for the placement of evals and data; we certainly agree evals are an important part of the job! MLR/MLEs handle foundation model concerns - aka pretrain scale data and general benchmark evals; but AI Engineers should certainly view product-specific data and evals as their job.

> *“In numbers, there's probably going to be significantly more AI Engineers than there are ML engineers / LLM engineers. One can be quite successful in this role without ever training anything.”* - [Andrej Karpathy](https://twitter.com/karpathy/status/1674873002314563584)

However, the devil is in the details - there are no end of challenges in successfully evaluating, applying and productizing AI:

- **Models:** From evaluating the largest GPT-4 and Claude models, down to the smallest open source Huggingface, LLaMA, and other models
- **Tools**: From the most popular chaining, retrieval and vector search tools like LangChain, LlamaIndex, and Pinecone to the emerging field of autonomous agents like [Auto-GPT and BabyAGI](https://www.latent.space/p/agents) (must-read recap from [Lilian Weng here](https://lilianweng.github.io/posts/2023-06-23-agent/))
- **Research/Progress**: On top of this, the sheer volume of papers and models and techniques published each day is [exponentially increasing](https://twitter.com/JackSoslow/status/1600552300392480768?s=20) with interest and funding, so much so that keeping on top of it all is almost a full time job.

I take this seriously and literally. **I think it** ***is*** **a full time job**. I think software engineering will spawn a new subdiscipline, specializing in applications of AI and wielding the emerging stack effectively, just as “ [site reliability engineer](https://www.enov8.com/blog/the-history-of-sre/) ”, “ [devops engineer](https://www.bunnyshell.com/blog/history-of-devops/) ”, “ [data engineer](https://www.freecodecamp.org/news/the-rise-of-the-data-engineer-91be18f1e603/) ” and “ [analytics engineer](https://www.holistics.io/blog/analytics-engineering-what-we-know/) ” emerged.

The emerging (and least cringe) [^1] version of this role seems to be: **AI Engineer**.

Every startup I know of has some kind of `#discuss-ai` Slack channel. Those channels will turn from informal groups into formal teams, as [Amplitude](https://www.latent.space/p/amplitude), [Replit](https://www.latent.space/p/reza-shabani#details) and [Notion](https://www.latent.space/p/ai-interfaces-and-notion#details) have done. The thousands of Software Engineers working on productionizing AI APIs and OSS models, whether on company time or on nights and weekends, in corporate Slacks or indie Discords, will professionalize and converge on a title - the AI Engineer. **This will likely be the highest-demand engineering job of the decade.**

AI Engineers can be found everywhere from the largest companies like Microsoft and Google, to leading edge startups like Figma (via [Diagram acquisition](https://www.figma.com/blog/ai-the-next-chapter-in-design/)), Vercel (eg [Hassan El Mghari’s viral RoomGPT](https://twitter.com/nutlope)) and Notion (eg [Ivan Zhao and Simon Last with Notion AI](https://www.latent.space/p/ai-interfaces-and-notion#details)) to independent hackers like [Simon Willison](https://www.latent.space/p/function-agents#details), [Pieter Levels](https://twitter.com/levelsio) (of [Photo/InteriorAI](https://twitter.com/ayushtweetshere/status/1673310909979033600)) and [Riley Goodside](https://twitter.com/goodside) (now at Scale AI). They are [making $300k/yr doing prompt engineering](https://twitter.com/swyx/status/1616541173996482560?lang=en) at Anthropic and [$900k building software at OpenAI](https://news.ycombinator.com/item?id=36460082). They are spending free weekends [hacking on ideas at AGI House](https://twitter.com/swyx/status/1672686090589990912) and sharing tips on [/r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) [^2]. What is common among them all is they are taking AI advancements and shaping them into real products used by millions, virtually overnight.

Not a single PhD in sight. **When it comes to shipping AI products, you want engineers, not researchers**.

## The AI vs ML Engineer Flippening

I am calling attention to this trend rather than starting it. There are 10x as many [ML Engineer jobs](https://www.indeed.com/jobs?q=%22machine+learning+engineer%22&l=&vjk=92db5c6fe7c47a89) as [AI Engineer jobs](https://www.indeed.com/jobs?q=%22ai+engineer%22&l=&vjk=9d645e42687689ae) on Indeed, but the higher growth rate of “AI” leads me to predict that this ratio will invert in 5 years.

![](https://substackcdn.com/image/fetch/$s_!UGaw!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28975621-0539-4b0b-9b3c-186d240513e2_600x400.svg)

Monthly job trends per HN Who’s Hiring

All job titles are flawed, but some are useful. We are both wary and weary of the endless semantic debates on the difference between AI and ML, and are well aware that regular “software engineer” roles are perfectly capable of building AI software. However a recent [Ask HN question on How to Break into AI Engineering](https://news.ycombinator.com/item?id=36432598) illustrates the fundamental perception that still persists in the market:

![](https://substackcdn.com/image/fetch/$s_!GQGh!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffdceef7d-fac9-4660-8bf4-fb5944ff17ab_806x992.png)

Jun 2023 screenshot: top voted answers for “How to break into AI Engineering”

Most people still consider AI Engineering as a form of either Machine Learning or Data Engineering, so they recommend the same prerequisites. But I *guarantee* you that *none* of the highly effective AI Engineers I named above have done the equivalent work of the Andrew Ng Coursera courses, nor do they know PyTorch, nor do they know the difference between a Data Lake or Data Warehouse [^3].

**In the near future, nobody will recommend** ***[starting](https://news.ycombinator.com/item?id=36432772)*** **[in AI Engineering by reading Attention is All You Need](https://news.ycombinator.com/item?id=36432772),** just like you do not start driving by reading the schematics for the Ford Model T. Sure, understanding fundamentals and history is always helpful, and does help you find ideas and efficiency/capability gains that are not yet in common consciousness. But sometimes you can just *use* products and learn their qualities through experience.

I don’t expect this “flippening” of the curriculum to happen overnight. It is human nature to want to stuff a resume, fill out a market map, and stand out by citing deeper topics with more authority. In other words, Prompt Engineering and AI Engineering will feel inferior to people with good Data Science/ML backgrounds for a *long* while. However, I think sheer demand-and-supply economics will prevail.

## Why AI Engineers are Emerging Now

- **Foundation Models** are “ [few shot learners](https://arxiv.org/abs/2005.14165) ”, exhibiting [in-context learning](https://twitter.com/karpathy/status/1627366413840322562?s=20) and even [zero shot transfer](https://arxiv.org/pdf/2304.02643.pdf) capabilities that generalize beyond the original intent of model trainers. In other words, *the people creating the models don’t fully know what they are capable of*. People who *aren’t* LLM researchers are able to find and exploit capabilities simply by spending more time with the models, and applying them to a domain that is undervalued by research (e.g. Jasper with copywriting).
- **Microsoft, Google, Meta, and the large Foundation Model labs have cornered scarce research talent** to essentially deliver “AI Research as a Service” APIs. You can’t hire them, but you can rent them — if you have software engineers on the other end who know how to work with them. There are ~5000 LLM researchers in the world, but ~50m software engineers. Supply constraints dictate that an “in-between” class of AI Engineers will rise to meet demand.
- **GPU hoarding**. Of course [OpenAI/Microsoft was first](https://news.microsoft.com/source/features/ai/openai-azure-supercomputer/), but Stability AI kicked off the startup GPU arms race by emphasizing their [^4] 4,000 GPU cluster.
	![](https://substackcdn.com/image/fetch/$s_!C_Uv!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a5b2c3c-4c5b-44cb-af75-818946b1adc5_1464x694.png)
	remember October 2022?
	Since then it has become commonplace for new startups like [Inflection](https://www.forbes.com/sites/alexkonrad/2023/06/29/inflection-ai-raises-1-billion-for-chatbot-pi/) ($1.3b), [Mistral](https://news.ycombinator.com/item?id=36326706) ($113m), [Reka](https://reka.ai/announcing-our-58m-funding-to-build-generative-models-and-advance-ai-research/) ($58m), [Poolside](https://www.newcomer.co/p/former-github-cto-jason-warner-raises) ($26m) and [Contextual](https://contextual.ai/announcing-next-generation-language-models/) ($20m) to raise huge seed rounds in order to own their own hardware. Dan Gross and Nat Friedman [^5] even announced [Andromeda](https://twitter.com/natfriedman/status/1668650915505803266), their $100m, 10 exaflop GPU cluster exclusively for startups they invest in. The global chip shortage [^6] is [reflexively](https://www.swyx.io/mimicry-reflexivity) creating even more shortage. There will be much more capacity for AI Engineers on the other side of the API line to *use* models, rather than train them.
- **Fire, ready, aim.** Instead of requiring *data scientists/ML engineers* do a laborious data collection exercise before training a single domain specific model that is then put into production, a *product manager/software engineer* can prompt an LLM, and build/validate a product idea, before getting specific data to finetune.
	![](https://substackcdn.com/image/fetch/$s_!r_7t!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6035ddd2-418d-421d-aebd-6893c32bb6dd_1579x266.png)
	Let’s say there are 100-1000x more of the latter than the former, and the “fire, ready, aim” workflow of prompted LLM prototypes lets you move 10-100x faster than traditional ML. So AI Engineers will be able to validate AI products say 1,000-10,000x cheaper. It’s Waterfall vs Agile, all over again. AI is Agile.
- **Python + JavaScript**. Data/AI is traditionally extremely Python centric, and the first AI Engineering tools like LangChain, LlamaIndex and Guardrails arose out of that same community. However, there are at least as many JavaScript developers as Python developers, so now tools are increasingly catering to this widely expanded audience, from [LangChain.js](https://github.com/hwchase17/langchainjs) and [Transformers.js](https://huggingface.co/docs/transformers.js/index) to [Vercel’s new AI SDK](https://sdk.vercel.ai/docs). The TAM expansion and opportunity is at least 100% bigger.
- **Generative AI vs Classifier ML**. “Generative AI” [^7] as a term has fallen out of favor, giving way to other analogies like “ [reasoning engine](https://every.to/chain-of-thought/gpt-4-is-a-reasoning-engine) ”, but is still useful in concisely articulating the difference between the existing group of MLOps tools and ML practitioners, and the rising, starkly different kind of persona that is best wielding LLMs and text to image generators. Where the existing generation of ML might have been focused on [fraud risk, recommendation systems, anomaly detection, and feature stores](https://applyingml.com/papers/), the AI Engineers are building [writing apps, personalized learning tools, natural language spreadsheets, and Factorio-like visual programming languages](https://www.latent.space/p/build-ai-ux).[^8]

Whenever a subgroup arises that has a completely different background, speaks a different language, produces a completely different set of products, and uses a completely different set of tools, they eventually split out into their own group.

## 1+2=3: The Role of Code in the evolution from Software 2.0 to Software 3.0

6 years ago, Andrej Karpathy wrote a very influential essay describing [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) - contrasting the “classical stack” of hand-coded programming languages that precisely model logic against the new stack of “machine learned” neural networks that approximate logic, enabling software to solve a lot more problems than could humanly be modeled. In 2023, he now notes that [the hottest new programming language is English](https://twitter.com/karpathy/status/1617979122625712128?lang=en), finally filling out the gray area in his diagram that was left unlabeled in the original essay - **moving from Software 2.0 to something… a LOT broader.**

![](https://substackcdn.com/image/fetch/$s_!A8CX!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F094e6082-1e2d-46de-ba73-f555341bcd34_895x519.png)

> Update: [Andrej responds! with some disagreement](https://twitter.com/karpathy/status/1674873002314563584)!

Last year, Prompt Engineering was the [memetic take](https://twitter.com/karpathy/status/1273788774422441984) on how jobs would change as people began to put GPT-3 and Stable Diffusion to work. People derided AI startups as “OpenAI Wrappers”, and fretted as LLM apps proved susceptible to [prompt injection and reverse prompt engineering](https://www.latent.space/p/reverse-prompt-eng). No moat to be found?

But one of the biggest themes of 2023 has very much been about **re-establishing the role of human-written code** to orchestrate and supplant LLM power, from [the >$200m behemoth Langchain](https://www.businessinsider.com/sequoia-leads-funding-round-generative-artificial-intelligence-startup-langchain-2023-4), to [Nvidia-backed Voyager](https://twitter.com/swyx/status/1666542199209869312?s=20) showing the unmistakable importance of code generation and reuse (I recently took part in a [Chains vs Agents webinar](https://www.youtube.com/watch?v=bYLHklxEd_k) with Harrison where I expanded on the thesis of Code Core vs LLM Core applications).

![Image](https://substackcdn.com/image/fetch/$s_!hXuc!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55d13fad-b282-4d9c-9258-d63a507ee002_2736x1494.jpeg)

The primary architectural divide: “software atop intelligence” vs “intelligent software”

Prompt Engineering was both [overhyped](https://www.latent.space/p/why-prompt-engineering-and-generative) *and* here to stay, but the re-emergence of Software 1.0 paradigms in Software 3.0 applications is both an area of mass opportunity/confusion, and created white space for a mess of startups:

![](https://substackcdn.com/image/fetch/$s_!gvfb!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a51a8e5-59d3-4e36-a0b7-d8f88ba5c028_1196x861.png)

are you even a VC if you don’t market map?

It’s not going to be *just* human-written code, of course. My recent adventures with [smol-developer](https://twitter.com/swyx/status/1657892220492738560), the larger scoped [gpt-engineer](https://twitter.com/antonosika/status/1667641038104674306), and other code generation agents like [Codium AI](https://www.latent.space/p/codium-agents#details), [Codegen.ai](https://codegen.ai/) and [Morph/Rift](https://morph.so/) will increasingly be a part of the AI Engineer toolkit. As human Engineers learn to harness AI, AIs will increasingly do Engineering as well, until a distant future when we look up one day and can no longer tell the difference.

## It’s Time To Converge - AI Engineer Summit

Builders need a place to talk turpentine. This is why, after [months of organizing small meetups](https://www.latent.space/i/115665083/events), we are now announcing the first independently run, builder oriented AI conference: **[The AI Engineer Summit](https://www.ai.engineer/summit)**!

![](https://substackcdn.com/image/fetch/$s_!ZFTW!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25e79b47-293b-42f8-8770-70ca1b59e67b_500x308.png)

check out our nifty domain - ai.engineer!

If everything in this post is resonating with you, we aim to convene all the top AI Engineers, founders, and investors together to learn about the state of the art, attend/teach workshops and find everything from the great new tool they’ll use at work, to their next new hire/cofounder/round.

**The definitive conference** to discuss everything that we’ve covered in the past year on this newsletter and our podcast, and more:

- AI UX
- AI Devtools
- AI Infra
- AI Agents
- New LLM Tools, including Langchain, Vector DBs, and more
- Open Source Models (training, finetuning, inferencing, evaling)

I have a [fair amount of experience](https://twitter.com/swyx/status/1480968467360595968) running community, but have never run a 500 person conference, so I have teamed up with [Ben Dunphy](https://twitter.com/benghamine) of [Reactathon](https://www.reactathon.com/) to put on the best AI Engineer conference in San Francisco (and online - his last conference had 20,000+ tuning in remotely).

**Join us at [ai.engineer](https://www.ai.engineer/summit)!**

*We are accepting both [speaker CFPs](https://docs.google.com/forms/d/e/1FAIpQLSdVCTSSDPkcIBjJeqZqq1Ox-PWS6cCxzxdZ9BbZ1z5z56C8eA/viewform) and [sponsors](mailto:sponsors@ai.engineer) (get in touch!).*

## We are the Builders

Keen observers will have noticed that we’ve gradually [the Latent Space podcast and newsletter](https://www.latent.space/about) to cater to the AI Engineer persona. What excites me most about serving this audience is **the combination of techno-optimism and practicality**. [Marc Andreesen recently wrote](https://a16z.com/2023/06/06/ai-will-save-the-world/) about how the vast majority of public AI discourse has been “hysterical fear and paranoia”, calling out that there is a whole profession of “AI safety expert”, “AI ethicist”, “AI risk researcher” paid to be doomers, but no corresponding role for builders and [foomers](https://www.latent.space/p/ok-foomer). On the other end of the spectrum, there are many [unserious accelerationists](https://www.latent.space/p/geohot#details) and [intolerable foomer threadbois](https://www.latent.space/p/ok-foomer) who spend all day on Twitter talking about a distant Utopian future, but it’s unclear what they are doing to bring it about.

**AI Engineers will tame and ride Shoggoth**.

Let’s make this a thing.

---

*Thanks for the many comments and questions on [HN](https://news.ycombinator.com/item?id=36538423) and [Twitter](https://twitter.com/karpathy/status/1674873002314563584)! We convened a snap Twitter Space to talk it through and >1,000 AI Engineers [tuned in](https://twitter.com/swyx/status/1674895620870651909). The Rise of the AI Engineer has also been covered in [other podcasts](https://www.latent.space/p/aies-podrocket).*

***Author’s note**: I am especially grateful to my cohost [Alessio Fanelli](https://twitter.com/fanahova) of [Decibel](https://www.decibel.vc/) and [Sarah Guo](https://twitter.com/saranormous/) and [Pranav Reddy](https://twitter.com/prnvrdy) of [Conviction](http://conviction.com/) for reviewing drafts of this post and providing critical feedback and invaluable support. And of course, [Ben Dunphy](https://twitter.com/benghamine) for agreeing to cofound [the AI Engineer conference](https://ai.engineer/) series and network. Thank you!*

---

[^1]: Alternatives considered: “Foundation Model Engineer”, “AI API Developer”, “LLM Engineer”, but it doesn’t quite roll off the tongue, whereas “Prompt Engineer” is also too limited for the [Code Core, LLM Shell](https://www.latent.space/p/function-agents#%C2%A7llm-core-code-shell) we are seeing emerge. There is also “ [MLOps Engineer](https://www.indeed.com/jobs?q=%22MLops%22&l=&from=searchOnHP&vjk=9841ad5da95d4c6e) ”, but this is a [well established community](https://mlops.community/) historically focused on lower level ML concerns — a distinction we discuss later in this piece. Lastly, “ [AI Tinkerer](https://twitter.com/alexgraveley/status/1626627645495443460?lang=en) ” has been popularized by Alex Gravely (([disputed?](https://twitter.com/jdan/status/1671333866915635201)) creator of Copilot), but unfortunately doesn’t seem titleworthy.

[^2]: My full list of AI [podcasts, newsletters](https://github.com/sw-yx/ai-notes/blob/main/Resources/Good%20AI%20Podcasts%20and%20Newsletters.md), and [communities](https://github.com/swyxio/ai-notes#communities) is maintained on GitHub.

[^3]: And probably could not [explain transformers on a whiteboard](https://twitter.com/WillManidis/status/1649097024388878337).

[^4]: Stability and AWS’ relationship on the cluster is a matter of active debate, so it is best to [hear from Emad in his own words](https://news.ycombinator.com/item?id=36514375) on this.

[^5]: I’m workshopping numeronyms for them. g12n?

[^6]: More accurately, this is an Nvidia chip shortage. This is why [George Hotz’s Tinycorp](https://www.latent.space/p/geohot) is so important in being able to run popular open source models on AMD cards. [Mosaic’s LLMFoundry](https://www.latent.space/p/mosaic-mpt-7b) also [reports](https://twitter.com/vitaliychiley/status/1674797832992333827?s=20) AMD compatibility.

[^7]: And, thank goodness, “Gen AI”.

[^8]: Of course, when you can combine both disciplines well, you have outlier results like [Character.ai](https://twitter.com/zackhargett/status/1674106749547315202), founded by a coauthor on the Transformers paper but finding a great use for the generative aspect of LLMs.