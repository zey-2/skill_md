---
title: "Building a 'Second Brain': Opportunities, Risks, and Implications for AI Adoption in Singapore"
source: "https://www.youtube.com/watch?v=t-4a20_iYhg"
author:
  - "[[Vivian Balakrishnan]]"
published: 2026-05-16
created: 2026-05-16
description: "Dr. Vivian Balakrishnan, Singapore's Minister for Foreign Affairs, delivers a keynote at AI Engineer Singapore (organized by 65Labs). He shares his 3-month experience building a personal AI agent using NanoClaw, Neoman memory system, Ollama, Whisper, and Obsidian — assembled entirely without writing code. Three key messages: you cannot outsource personal understanding or delegate accountability; real value is created workflow-by-workflow at the ground level; the barriers to entry have collapsed. Argues for democratization of AI tools, decentralized deployment at the edge, and a neuro-symbolic future over pure LLM reliance."
tags:
  - "clippings"
  - "ai-adoption"
  - "personal-agents"
  - "second-brain"
  - "singapore"
---

![](https://www.youtube.com/watch?v=t-4a20_iYhg)

## Transcript

### Introduction

**0:00** · I am absolutely honored to introduce our keynote speaker and a builder himself, Singapore's Minister for Foreign Affairs, Dr. Vivian Bala Krishnan.

**0:20** · Hi, good morning everyone. You know, we can be a bit more informal in Singapore. So, good morning. I know it's raining, but Singapore's usually sunny. I feel like an impostor here. For those of you who don't know me, I'm actually a retired eye surgeon. Took a detour into politics for perhaps too long. But I've always retained an interest in getting things done, building things, fixing things. And since I don't get to operate on eyes anymore, I assemble watches, I reprogram appliances, and now there's some other stuff which is what I'm going to talk about today.

### Three Key Messages

**1:20** · Let me jump to the end, and to say these are the three key messages which you can forget everything I've said but just bear these things in mind.

**1:29** · We're now at an age when you can outsource a lot of stuff — calculations, computation, memory, replication, dissemination of knowledge. The one thing which you cannot outsource is your personal understanding. And if you are in a position of authority, you can delegate work. You can't delegate accountability. So remember the personal element in that understanding and accountability.

**2:08** · The next point — I would refer you to a nice short letter published in the Financial Times by Professor Neil Lawrence, University of Cambridge. He's the professor of machine learning. And you know there's a lot of hype about AI models, data centers, top-down systems, rules, governments. That's macro. But his hypothesis is that real value for the economy and society is created at the ground level — workflow by workflow, sector by sector, department by department, and in fact at the individual level. What this means is that, look, I know you guys are great and I know the guys working on frontier models are incredible, but the real payoff is when ordinary people — teachers, lawyers, technicians, managers, doctors, lawyers, or even ministers — are actually using the tools which are already available, already invented. People who know their jobs and are empowered by these tools. That's how you create real value for society and for the economy.

**3:42** · So I'm looking at decentralization, individualization, bespoke models. I'm talking about making yourself better at what your day job is and even better still re-engineering the workflows of your life. That's where the real value boost is. And the third takeaway — and that's why I'm making this presentation — is that I sincerely believe the barriers for achieving all this have collapsed. The tools have already been availed. It's a matter of getting people to understand what tools are out there, assemble their own tools, and put ourselves on a completely different trajectory.

### Building a Personal Agent

**4:34** · Now my personal agent first came to life almost exactly 3 months ago. Yes, I got caught up by the OpenClaw hype but immediately given my job I knew that was not practical because security was an issue. And then someone else then pointed to NanoClaw, and I think we are going to hear from Gabriel after this. As a geek and as a tinkerer myself, I like stuff which I can grasp. So the fact that NanoClaw has a very short code base which even an idiot like me can read and sort of understand, the fact that it's containerized — and as a surgeon I know that there's no such thing as a routine operation and things will go wrong, things will break, and when they do break hopefully you want them to break within barriers — so the containerization part, the understandability part was vital for me.

**5:47** · Anyway, simple: go to GitHub, download the stuff. And the other attractive part about it is there are no configs. There in fact, because you rely on an LLM to do all the bespoke tailor customizations. In fact, you realize everyone running an instance of NanoClaw is running an individualized system. Now, that's both good and also has its share of complications.

**6:25** · NanoClaw provides the platform. It allows me to communicate through WhatsApp with my agent. That part's not rocket science. The thing which I was really after was how could I use it for my daily life. Let me give you an idea of my daily life. This month I'm visiting 12 countries. I will therefore have to meet hundreds of people. I will have to understand the country's economy, geography, culture, history, war and peace. I need to know people as individuals and not just something I from a brief, and there's a huge cognitive overload on every single diplomat. And the question is: how can I turbocharge this process so that if I need a fact or a factoid, I can get it, I can get it anywhere, and I can go down the rabbit hole if need be.

**7:42** · The LLMs are useful for analysis, for abstraction, for expression, and certainly for drafting briefs, drafting speeches, formulating answers to questions — including I must add parliamentary questions. And 3 months ago, which includes the whole debates in parliament, it was extremely impressive to see both the questions and the answers which generated, and with due respect to all my colleagues in parliament, some of the AI generated debates far more incisive shall I say.

**8:29** · But anyway, so it communicates with me through WhatsApp. So there's this bit of software called Bailey's. I suspect it's probably not entirely in keeping with what Meta or WhatsApp would like us to do because it's actually simulating the way we get WhatsApp to work in our browsers or on our laptops. So it's a pseudo terminal in a sense.

**8:58** · Then the bit which I believe is the real frontier for people like me is memory, and fortunately I came across this obscure piece of software called Neoman. I still haven't met the developers so I don't really know, but a memory system with graphs. So it's got entities. The edges are entities, causality, temporal relationships, and semantic. And also because I didn't want to be confined to just keyword searches, the fact that I could run Ollama locally with an embedding model means I also have semantic search built in.

**9:50** · Whisper is the part that's easy because with WhatsApp, I didn't want to only have to type. I wanted to be able to speak and it can speak back to me. And of course, my dream is one day to just have my agent answer supplementary questions in parliament. I'm not sure about the legality of that, but if it happens, you'll know that I shared the idea with you first.

**10:13** · But the point is I was now able to curate material — speeches, transcripts, particularly of my own contributions — get it into the system, digested, extracted, put into that memory database. And then around the same time, Andrej Karpathy came up with his LLM supervised wiki generation, so I added that in as well. And then for the UX, the user interface, I used Obsidian partly also because Obsidian allows me to use the Apple iCloud and that therefore immediately means I've got a personal cloud, and all the wikis which are extracted from this personally curated database becomes available to me — because remember I started off by saying the key is personal understanding.

**11:14** · So I've got a memory system, I've got a communication system, I've got an analysis system, but all nice in theory. But what I'm here to share with you is that in the last 3 months, I found it incredibly useful — meeting people, traveling, first drafts, first cut of a speech. Even today's presentation, even the slides actually were generated by Claude. You know, it's turbocharged the pace at which things can be done. And as a practitioner — so not as an engineer but as a practitioner with a day job — it's useful, and I can attest to its usefulness because I can honestly tell you I have not dared to switch it off. And NanoClaw unfortunately has moved from version 1 to version 2. When version 2 came on, because their transition is not at all smooth, I've left version 1 working and I put version 2 on another computer. And I should also add, all this stuff — one of my most daily used agents is running off a Raspberry Pi which is at least 2 or 3 years old. All it has is 8 GB of RAM. You see my point about accessibility, personalization, relevance, use.

### The Barriers Have Fallen

**12:48** · Let's go on to the next slide. And this is my point: the barriers have fallen because I did this. I did this without writing Claude, Bailey's, Neoman, Whisper, or the credentialing system. You know, there's this whole thing about vibe coding. I won't even dare to claim I was vibe coding. I was just assembling tools. It's just tool assembly. I didn't write any glue. I can honestly say, yes, I have gone through the code. NanoClaw insists that you approve every time you give bash access to the agent. So I do scan through it. But it does help here. It does help if you don't understand coding — you understand what's going on even if you're not actually typing and editing code in the raw.

**14:05** · In a sense, my approach to all this has been to learn by doing. It's not enough to sit down and read, get the headlines, get the summaries done. If you're interested in anything, get your hands wet. Learn and you learn best by doing. And because the barriers for entry have come down so dramatically, everyone should embark on their personal experiments.

**14:40** · And you know, Claude came up with this quote which I got a bit suspicious about — you know who has said it before and says it, it claims no one else has. But actually I kind of agreed with it, and this is a shout out to my government colleagues: you cannot govern a technology that you have only been briefed on. You better get your hands dirty and then you understand both the potential and the limits and the problems.

### Constraints and the Future

**15:16** · A few other digressions. There are constraints. So for instance, depending on LLMs — and quite frankly, I mean, the prices for which the AI majors are currently charging us, I think we all know we're enjoying in effect a subsidy. Tokens are not cheap. Compute power is limited. Electricity prices have risen. Wars do not help. And we should beware of just trying to throw every problem and every step in a solution at an LLM. It reminds me of the old proverb: for a man with a hammer, everything looks like a nail. And in fact there are good both economic and design advantages so that you use LLMs but do not forget there is still a role for deterministic systems. There is still a role for expert rule-based systems. And my personal belief as a biologist: in the end, some kind of neuro-symbolic system rather than just the LLM model. And I have some sympathy for Yann LeCun who says, I think that LLMs are great, but actually that's not the way we've solved it in nature. If you look at the human brain, actually I suspect we have less layers of computation in the human brain than in many of the large language models which we have today. And I can tell you as an eye surgeon, the cortical computation for vision, for language, for cognition are often based on far more efficient structures than the energy-gobbling systems which we have today.

**17:43** · The point I'm making and where I'm agreeing with Yann LeCun is that in the end these are pattern recognition systems with attention, with memory, and out of what looks like simple fundamental abilities is emergent behavior which gives you conceptual understanding, which gives you language, which gives you the ability to do things. So my point is this is a field which is still exploding, and therefore approach this with humility. Approach this by just doing your best, improving the productivity of your daily job, but understand that actually we are perhaps one of the most privileged generations to be living through a revolution.

**18:37** · Tools matter more than models. And I think Gabriel will know — I've told him, by June I think it's June the 15th, I need NanoClaw to make all models first-class citizens. There are reasons for that which we can discuss later. And then finally, memory. It is a very human — and I think it is the great unsolved part of this frontier.

### Security and Policy Goals

**19:12** · Which on security, I'm not going to belabor this. Just as an aside, even if you hack my system, the most thing you'll get from it is my phone number. You will get summaries of foreign policy, but since it's foreign policy which I have espoused, and in any case I have curated the stuff I've put in — even if you take my system, I think it will generate the foreign policy of Singapore anyway. Now that's one way of addressing security: by making sure you only put what is already open source, what is already published, and you subject your systems to a level of transparency and scrutiny that can be withstood. But do not forget security remains paramount, and in fact the complication to the dissemination of AI is going to be commercial competition, national security, cyber security, and the superpower contestation. These are the political factors that are going to affect the availability, the speed, and the dissemination of AI of the future.

**20:45** · The goals: I'm a believer in deployment at the edge. I'm a surgeon. I believe in doing. I believe in fixing. I believe that's where lives are safe, value is created. Second, therefore the public policy goal is the democratization of these tools. And that's why you will see in the Economic Strategy Review Committee, DPM Gan said we are — Singapore is not likely to be at the frontier of model development, but we can be at the frontier of deployment at scale. So democratization, and therefore if that's what we believe, then it must be a decentralized, ground-up approach. And that's why I'm here today, because I found out this conference was organized less than 3 months ago by 65Labs. All the people you meet here, this is all not even their day job — it's a hack, right? But this is the way I believe the future is going to be created. So, thank you all for being here. Thank you for being part of this journey. Have a wonderful day, a wonderful future. Thank you very much.

**22:15** · [Audience member hands him a gift] You should have given this to me before. I would have won it. It wasn't — we weren't brief, but thank you so much. Thank you.

## Key Takeaways

1. **Personal understanding cannot be outsourced** — computation, memory, and knowledge dissemination can be delegated, but understanding and accountability cannot.
2. **Real value is created at ground level** — workflow by workflow, sector by sector, empowered individuals using existing tools — not in top-down model development.
3. **Barriers to entry have collapsed** — tool assembly (not coding) is sufficient. Dr. Balakrishnan built his agent without writing any glue code, running it on a Raspberry Pi with 8GB RAM.

## Tech Stack Mentioned

| Component | Tool |
|-----------|------|
| Agent platform | NanoClaw (containerized, short codebase) |
| Communication | WhatsApp via Bailey's |
| Memory system | Neoman (graph-based with entities, causality, temporal, semantic edges) |
| Embeddings | Ollama (local) |
| Speech-to-text | Whisper |
| Wiki generation | LLM-supervised wiki (Karpathy-style) |
| UI / Knowledge base | Obsidian + Apple iCloud |
| LLM | Claude |
| Hardware | Raspberry Pi (8GB RAM, 2-3 years old) |
