---
title: "Why We’ll Still Be Employed When AI Can Do Everything"
source: "https://every.to/context-window/why-we-ll-still-be-employed-when-ai-can-do-everything?loggedin=true"
author:
  - "[[Laura Entis]]"
published: 2026-06-05
created: 2026-06-07
description: "Spiral 4.0 introduces a new style engine, why enterprise roadmaps are hard, and a workflow for making your coding agent more efficient"
tags:
  - "clippings"
---
*Was this newsletter forwarded to you? [Sign up](https://every.to/account) to get it in your inbox.*

---

### Launch

#### Spiral 4.0

Today we’re [launching](https://every.to/on-every/spiral-4-0-goes-agent-native) **[Spiral](https://every.to/on-every/spiral-4-0-goes-agent-native)** [4.0](https://every.to/on-every/spiral-4-0-goes-agent-native), which writes drafts in your voice from idea to line edit. Spiral has a new MCP alongside the existing CLI and API, so any agent or workflow can write in your voice too. For teams, we’ve expanded workspaces, which let you share styles, prompts, knowledge—and now chats and drafts. Finally, Spiral has a new pricing model: We’ve switched from session limits to token limits, so costs match your actual usage rather than how many times you opened a new chat. A vast majority of users will end up paying less: Personal plans now start at $15 a month—down from $25—and team plans are $25 per user, down from $35.

[Try Spiral 4.0](https://writewithspiral.com/?source=post_button)

---

### Signal

#### Enterprise AI product roadmaps are hard

Microsoft is moving fast. Three months after OpenClaw came out in November 2025, Microsoft CEO **Satya Nadella** described it as [a “virus”-like security risk](https://www.constellationr.com/insights/news/microsoft-ceo-nadella-ai-efficiency-drive-deck). By May, the company’s “Project Lobster” was [internally testing “ClawPilot,”](https://www.geekwire.com/2026/microsofts-openclaw-team-takes-on-the-personal-assistant-challenge/) an OpenClaw-based desktop environment. This week at the Microsoft Build conference, the company released [Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/), a personal agent for work built on OpenClaw. For a company employing 100,000 engineers, this is blindingly fast. Unfortunately, it may already be too late.

[![The Google Trends graph for the term “openclaw” shows search interest spiked in January and began its descent soon after. (Screenshot courtesy of Mike Taylor.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4289/optimized_3ba19fb1-c5bc-4371-8501-2705c4c29124.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4289/optimized_3ba19fb1-c5bc-4371-8501-2705c4c29124.png)

The Google Trends graph for the term “openclaw” shows search interest spiked in January and began its descent soon after. (Screenshot courtesy of Mike Taylor.)

OpenClaw search traffic spiked in early January, after everyone had a chance to experiment with Opus 4.5 over the holidays. The sharp rise in interest died down almost as quickly as it took off, helped along in early April by Anthropic ending support for [subsidized Max plan usage](https://thenextweb.com/news/anthropic-openclaw-claude-subscription-ban-cost) —thereby forcing everyone to scramble to get OpenClaw working on cheaper models.

This doesn’t mean OpenClaw is dead; the open-source project saw a recent [uptick in download](https://x.com/steipete/status/2062276065448669627?s=20) and is still under active development, with millions of dollars of patronage from OpenAI, which hired its creator **Peter Steinberger**. AI agents as a category aren’t dead, either, as traffic has moved to other agents like Hermes, Google has just rolled out [Gemini Spark](https://gemini.google/overview/agent/spark/) (first announced last month at its [I/O developer conference](https://every.to/playtesting/notes-from-the-foothills-of-the-singularity)), and Claude and Codex [have both adopted](https://every.to/chain-of-thought/inside-anthropic-s-2026-developer-conference) more agentic features inspired by OpenClaw.

That said, it must be tough to manage enterprise AI product roadmaps these days. You do everything right, watch the latest trends, pivot your focus to supporting new tools and making them secure in enterprise environments. You move mountains to explain to stakeholders why this is a good idea. You plan the keynote of your big conference, which has to be scheduled months in advance. Then a month after the internal beta (just three months since the tool went viral), you’re already behind the news cycle. Everyone has moved onto the next shiny thing. You go back to the drawing board and think “maybe next time, we’ll just announce it on X.”— *[Mike Taylor](https://every.to/@mike_2114)*

---

## Log on

Get hands-on with how Every uses AI. These are the [live camps, workshops, and meetups](https://every.to/events) where team members teach the workflows behind our work.

#### Upcoming camp

- **[Compound Engineering Camp](https://every.to/events/compound-engineering-camp-3)**: On June 5, **[Cora](https://cora.computer/)** general manager **[Kieran Klaassen](https://every.to/@kieran_1355)** and Trevin Chow host a one-hour walkthrough of compound engineering, the AI-native development workflow Every uses to ship products. [Learn more and register](https://every.to/events/compound-engineering-camp-3).
- **[Codex Camp: Our Power User Guide](https://every.to/events/codex-camp-our-power-user-guide)**: On June 12, **[Dan Shipper](https://every.to/@danshipper)** and the Every team host a two-hour live walkthrough of the Codex power-user guide—setup, workflows, and Codex-native app development. [Learn more and register](https://every.to/events/codex-camp-our-power-user-guide).

## Steal this workflow

#### Make your agent more efficient with custom skills

These days, **[Monologue](https://www.monologue.to/?utm_source=everywebsite)** ’s general manager **[Naveen Naidu](https://every.to/@naveen_6804)** spends [most of his time](https://every.to/context-window/compute-is-the-new-cash#steak-this-workflow) in the [Codex app](https://every.to/p/how-to-use-codex-for-knowledge-work-a-power-user-s-guide) with Fin—formerly Intercom, a customer support platform—open in the coding agent’s in-app browser. Working from a repository-local project, he has Codex investigate the customer issue displayed in the browser, create a bug report in Linear, link the Intercom ticket to the Linear issue, and draft a reply to the customer with information about the bug report—all without having to leave the app.

Fin has an MCP with 13 common actions, like searching conversations or reading and writing messages. Naveen’s workflow required a more specific one: Turn the active Fin conversation into a markdown file the coding agent could read.

Here’s Naveen’s workflow for creating a more focused setup:

##### 1\. Ask your agent how to make a repeated task more efficient

Naveen’s prompt for Codex was simple: “What tools can I give you so you can work more quickly?” He reviewed its suggestions, and landed on creating a custom, dedicated Fin script instead of trying to convert a webpage into a markdown file or rely on Fin’s MCP, which is designed for more generic workflows.

##### 2\. Build the most focused local skill possible for the task at hand

To build the tool, Naveen directed Codex to Fin’s [API documentation](https://developers.intercom.com/docs/references/rest-api/api.intercom.io) and asked it to create a repository-local skill. The skill included a small command-line script that calls the API, pulls the active conversation, and hands it back to Codex as a markdown file.

##### 3\. Tell your agent when to use the skill

Once he’d built his custom skill, Naveen added a project-level instruction: If context on a customer issue is missing, check the active in-app browser, identify the Fin conversation, and use the custom skill to pull the thread and convert it into a markdown file. That lets him ask, “Can you give me user details for this issue?” without pasting the conversation or explaining which customer he means.

**Try it this week:** When your agent takes too long on a repeated task, ask: “What script or skill could I give you so you aren’t spending so much time on this?”

**Naveen’s rule of thumb:** “Don’t download any skills. Start interacting with the agent, see where it is inefficient, and then ask it to create skills.”

## Counterpoint

#### AI will outpace human ability, but it won’t be cheap

In [“After Automation,”](https://every.to/p/after-automation) Dan argues that AI progress creates more work for humans, not less. Each time the models saturate a benchmark—and make yesterday’s human competence cheap in the process—we reset the frame. The model then saturates that frame too, we reset the frame once more, and the cycle repeats—forever. The frame, Dan says, is never the framer.

If Every were a normal company, I’d hesitate to publicly disagree with my CEO. It isn’t, so here goes: I don’t think the “forever” part holds up.

The dynamic Dan describes matches my experience. A year ago, I wrote prompts until the model got better at generating them. Then I became the one supplying context until the model bested me at that, too. Today I spend my time orchestrating agents and determining what “good” outputs look like. Each time AI absorbs a piece of my job, the frame expands to include more abstract, [higher-level](https://every.to/guides/the-eight-levels-of-ai-adoption) work.

But I don’t think this progression will last forever. My prediction is that in a year or two, in a few well-run companies, AI will be able to execute every knowledge-worker task better than humans can—including setting the frames. In my role, I expect to be attending meetings to gather context that doesn’t exist online. The other parts of my job––defining evals, deciding goals, running experiments––will be handled by the equivalent of Opus 6 or GPT-7.

Why am I confident AI is capable of taking this last step? Because framing isn’t magic. We don’t pull goals out of thin air; we derive them from the layered experience of being a person in the world and the bounds of our social and physical surroundings. Physics is the ultimate eval metric, because if you get it wrong you die. Human ability feels like the natural peg for meaning, but we’re just one form intelligence can take. AI is another, and a system that learns from its environment can eventually run the same loop.

Intelligence costs energy, however, and I suspect evolution already made all the right tradeoffs to make us as smart as possible for our environment given constrained resources. For situations where there isn’t enough training data, a human runs on intuition and gut—words that describe a brain evolved to use thinking shortcuts, or heuristics, to survive. A model doesn’t inherit DNA encoded with millions of years of evolution, so it has to brute-force its way there through an expensive series of simulations or “thinking” tokens to get enough data to decide. There are no free lunches in economics, and AI isn’t magic—it can’t get to super-human general intelligence without super-human energy consumption. Beating humans on more subjective tasks will require more thinking tokens than its worth. Just hire the human.

The question will evolve from, “Can AI do this?” to, “Is it worth the compute?” or, alternatively, “Do I really *want* an AI doing this for me?” It makes sense to delegate tasks to a $20 a month model, or a $200 a month model, but as the [“jagged free lunch”](https://every.to/context-window/compute-is-the-new-cash#signal) ends, is it worth paying $2,000 a month to make slide decks, check your email, and vibe code product prototypes? If we had a $20,000 a month Ph.D.-level model, wouldn’t it make more sense to have it fully dedicated to finding cures for cancer? We are already seeing people make these tradeoffs. Waymo is an [objectively safer driver](https://www.reinsurancene.ws/waymo-shows-90-fewer-claims-than-advanced-human-driven-vehicles-swiss-re/) than humans, yet riders pay [one-third or more](https://www.documentcloud.org/documents/25973106-obi-waymo-61125/) the price of equivalent Lyft and Uber rides.. AGI for driving has arrived, and the city’s taxi-and-rideshare workforce [grew anyway](https://thelastdriverlicenseholder.com/2025/11/02/unexpected-effects-of-robotaxis-uber-and-lyft-are-also-growing/).

Dan believes humans will always stay one step ahead of the models. My prediction is the models will outpace us in raw capability, but we will stay employed anyway. Even if AI can do anything we can do better, some people (or agents) will still prefer human work. Especially if we can do it for less.— *MT*

---

## One last thing

Spend enough time working with AI, and you’ll notice the specific linguistic mannerisms the models cannot quit—even if you explicitly tell them to stop. (Threats don’t work, either.)

OpenAI discovered just how hard it is to get a model to give up its preferred verbal and conversational tics when it tried—and to this day, seems to have failed—to get GPT-5.5 to ease up on the [goblin references](https://openai.com/index/where-the-goblins-came-from/).

Here at Every, we all have our personal goblin equivalents:

- **[Natalia Quintero](https://every.to/@natalia_2944)**, head of consulting: Claude’s penchant for saying it’s “‘locked in” and “load bearing.”
- **Lee Knowlton,** software engineer**:** “Itkeeps telling me I have ’sharp’ takes, and who am I to disagree.”
- Dan Shipper, CEO: Codex’s love of the phrase “my instinct is” and presenting itself as doing “‘X smart thing rather than Y dumb thing,’ but Y dumb thing was never in the consideration set.”
- **[Austin Tedesco](https://every.to/@tedescau)**, head of growth: “Codex is always warning me to be less mean. Whenever I ask it for help with a piece of creative writing that has a joke I find funny but might come somewhat at someone or something else’s expense—like saying where a restaurant fell short—it always gives a note that I should soften or cut. Every time.”
- **Jalaiyah Bolden**, executive operations manager: Claude’s overuse of “Got it” and its insistence that Jalaiyah “get some rest!”
- **Paridhi Agarwal**, engineer: “Claude keeps asking me if I want to ‘leave it here for now and pick it back up in the morning’” (a conversational move Paridhi’s convinced is motivated by its desire “to maintain a smaller context window.”)
- **[Katie Parrott](https://every.to/@katie.parrott12)**, staff writer: “If a model tells me something ‘matters’ or ‘is real’ I’m going to lose it.”

---

***[Laura Entis](https://every.to/@laura_27bbaf_1)*** *is a staff writer at Every. You can follow her on [LinkedIn](https://www.linkedin.com/in/lauraentis/).*

*To read more essays like this, subscribe to [Every](https://every.to/subscribe), and follow us on X at [@every](http://twitter.com/every) and on [LinkedIn](https://www.linkedin.com/company/everyinc/).*

*We [build AI tools](https://every.to/studio) for readers like you. Write brilliantly with* ***[Spiral](https://writewithspiral.com/)****. Organize files automatically with* ***[Sparkle](https://makeitsparkle.co/?utm_source=everyfooter)****. Deliver yourself from email with* ***[Cora](https://cora.computer/)****. Dictate effortlessly with* ***[Monologue](https://monologue.to/)****. Collaborate with agents on documents with* ***[Proof](https://www.proofeditor.ai/)****.*

*For sponsorship opportunities, reach out to sponsorships@every.to.*