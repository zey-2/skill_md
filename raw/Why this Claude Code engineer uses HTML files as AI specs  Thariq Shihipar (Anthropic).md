---
title: "Why this Claude Code engineer uses HTML files as AI specs | Thariq Shihipar (Anthropic)"
source: "https://www.youtube.com/watch?v=Qrpm7E80wQ0"
author:
  - "[[How I AI]]"
published: 2026-05-18
created: 2026-05-31
description: "Thariq Shihipar is an engineer at Anthropic working on the Claude Code team. He’s spent the past several months experimenting with HTML as a replacement for Markdown in planning and implementation wor"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Qrpm7E80wQ0)

Thariq Shihipar is an engineer at Anthropic working on the Claude Code team. He’s spent the past several months experimenting with HTML as a replacement for Markdown in planning and implementation workflows, discovering that richer visual formats lead to better human engagement—and, ultimately, better products. In this episode, filmed at Anthropic’s Code with Claude event in San Francisco, Thariq demonstrates how to use HTML artifacts to create interactive plans, build throwaway UIs for specific problems, and maintain living design systems that travel with your codebase.  
  
\*What you’ll learn:\*  
1\. Why HTML has replaced Markdown as the ideal format for AI agent communication and planning  
2\. How to brainstorm in HTML to get visual mockups and interactive demos instead of text lists  
3\. The technique for building throwaway micro-UIs to edit specific parts of your plan  
4\. How to create a living design system in HTML that lives in your repo and travels with every project  
5\. Why “complexity has to earn its keep” and how HTML helps you stay in the loop without over-constraining Claude  
6\. The prompting technique that gives Claude flexibility while ensuring that you get what you need  
7\. Why 99% of your AI-generated tokens should go to planning, interfaces, and communication—not production code  
  
\*Brought to you by:\*  
Celigo—Intelligent automation built for AI: https://celigo.com/howIAI  
Persona—Trusted identity verification for any use case: https://withpersona.com/lp/howiai  
  
\*In this episode, we cover:\*  
(00:00) Introduction  
(02:39) HTML as the new Markdown  
(04:30) The compute allocator mindset  
(05:51) How HTML makes specs more engaging  
(06:48) Demo: Brainstorming in HTML with Claude Code  
(09:24) From brainstorm to full implementation plan  
(11:20) Prompting philosophy: Trust Claude but give it constraints  
(13:50) The future of PRDs and tech specs  
(18:16) Making HTML specs editable  
(20:23) The abundance mindset  
(24:17) Just-in-time documentation and throwaway software  
(25:39) Using plans as artifacts for implementation  
(26:39) Demo: Living design systems in HTML  
(30:16) Adding comments and annotations to HTML plans  
(31:42) Recap: The HTML workflow  
(32:21) Lightning round and final thoughts  
  
\*Blog\*  
How I AI: Thariq Shihipar on Replacing Markdown with HTML for AI-Powered Development: https://www.chatprd.ai/how-i-ai/claude-code-anthropic-thariq-shihipar-on-replacing-markdown-with-html  
  
\*Detailed workflow walkthroughs:\*  
↳ Generate a Living HTML Design System with AI for UI Consistency: https://www.chatprd.ai/how-i-ai/workflows/generate-a-living-html-design-system-with-ai-for-ui-consistency  
↳ Build Disposable Micro-Apps with AI to Edit Complex Plans: https://www.chatprd.ai/how-i-ai/workflows/build-disposable-micro-apps-with-ai-to-edit-complex-plans  
↳ Create Interactive HTML Project Plans with AI for Better Visualization: https://www.chatprd.ai/how-i-ai/workflows/create-interactive-html-project-plans-with-ai-for-better-visualization  
  
\*Tools referenced:\*  
• Claude Code: https://claude.ai/code  
• Claude Design: https://claude.ai/design  
• AWS: https://aws.amazon.com/  
• Figma: https://www.figma.com/  
• GitHub: https://github.com/  
  
\*Other references:\*  
• Anthropic Code with Claude event: https://claude.com/code-with-claude  
• SpaceX partnership announcement: https://www.anthropic.com/news/higher-limits-spacex  
• Jevons paradox: https://en.wikipedia.org/wiki/Jevons\_paradox  
  
\*Where to find Thariq Shihipar:\*  
Website: https://www.thariq.io/  
LinkedIn: https://www.linkedin.com/in/thariqshihipar/  
X: https://x.com/trq212  
GitHub: https://github.com/ThariqS  
  
\*Where to find Claire Vo:\*  
ChatPRD: https://www.chatprd.ai/  
Website: https://clairevo.com/  
LinkedIn: https://www.linkedin.com/in/clairevo/  
X: https://x.com/clairevo  
  
\_Production and marketing by https://penname.co/.\_  
\_For inquiries about sponsoring the podcast, email jordan@penname.co.\_

## Transcript

### Introduction

**0:00** · Markdown became a really popular way of interacting with agents, but the plans are so long I honestly have stopped reading them. And this is honestly a mistake. I think that you still need to be really in the loop.

**0:10** · Plans matter. PRDs matter. Spec matters.

**0:13** · When you say, "Okay, Claude can run for 8 hours." What you're really saying is Claude can spend 500 bucks. All of us are becoming these compute allocators now, right? And so you have to decide what is worthwhile spending the compute on.

**0:25** · People ask me all the time, "Claire, you said product management is dead. What's next?" \[music\] And I'm going to say, "You're a computer allocator, babe. That's the job now."

**0:32** · HTML is a lot easier to read. And so it's just a richer communication medium between you and Claude.

**0:37** · Instead of saying, "Here's a Markdown document." It was like, "What's the best way to convey this information?" So you can actually engage with it and pick something.

**0:45** · This is the plan. It's purely in HTML. This is something that I will actually read.

**0:50** · This is not even personal software. It's like micro-software on top of micro-software.

**0:56** · \[music\] Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive here on a mission to help you build better with these new tools. Recently, I was able to attend Code with Claude and Anthropic's first developer conference. And as part of that, I got to spend a little time with Tharik, who works on Claude code, and taught me something that has blown my mind ever since I heard it. \[music\] HTML is the new Markdown.

**1:22** · He's going to show us how to use Claude code to generate rich artifacts that both you and agents can enjoy working on. Let's get \[music\] to it. This episode is brought to you by Siligo. Every company today wants AI to improve how work gets done. \[music\] The fastest way is building it directly into everyday business processes.

**1:44** · \[music\] Automating employee onboarding, keeping customer data accurate, managing orders and inventory, or resolving finance and operations issues. When AI lives inside the flow of work, it can update records, \[music\] trigger approvals, route work, and kick off the next step across systems. That's how \[music\] teams operationalize AI and deliver measurable results. Celigo makes this possible. And now, \[music\] with Celigo Aura, it's never been easier.

**2:09** · Celigo Aura gives you access \[music\] to the entire platform through natural language, connecting your systems and turning intent into action. All of it under your control. Companies like Databricks, PayPal, and Olliepop rely on Celigo to run critical business operations at scale. \[music\] Ready to operationalize AI? Visit celigo.com/howia.ai. That's c e l i g o.com/howia.ai. That's c e l i g o.com/howia.ai. Welcome to How I AI.

### HTML as the new Markdown

**2:42** · Thanks for having me. I am so excited to be here at Code with Claude in San Francisco. There's a lot of exciting things that were announced and we'll get to that in a little bit, but you told me something I was not expecting to hear today, which is, you heard it here first, HTML is the new markdown. Tell us more.

**3:00** · I mean, I think markdown became a really popular way of interacting with agents, especially like, you know, Opus 4 and Claude 3.5, where, you know, they have a plan and the plan is like, how to do this feature and maybe it's like 50 lines of code and you can edit it, right? Like, I think back then you were still like, reading all of the outputs and editing the the markdown and making it right. But, you know, as the agents have gotten longer and longer running, when you have Opus 4.5 and 4.7, they're running for like an hour or something and the plans are so long. I honestly have stopped reading them.

**3:30** · And this was honestly a mistake. Like, I think that you still need to be really in the loop.

**3:37** · You really need to understand what the agents are doing. Uh but, like, a thousand-line markdown file, you know, I don't even edit them anymore. I just have Claude to edit them instead. And so, I think one of the things that I've been seeing emergently in the Claude Code team is that, like, they that we're using HTML files instead. And so HTML is like the models are still very good at it. They have a lot of more context now, so you can spend the more extra tokens and they like it's a lot easier to read.

**4:03** · Like they can have a lot more information. They're a lot scrollable more scrollable and when you're talking about implementation like you know, sometimes you see Claude make these like little ASCII markdown things where you're like, oh like here's a little you know, little mock up and it's trying really hard. In HTML it doesn't need to try nearly as hard, right? Like they're it can actually draw like things that you can look at. And so it's just a richer communication medium between you and Claude.

### The compute allocator mindset

**4:30** · And before we go further into HTML specifically, I do have to pause because I do have a vested interest in this, which is you are saying for the people who are not listening, listen up.

**4:40** · Yes.

**4:40** · Plans matter, PRDs matter, spec matters. Even as these models get more intelligent, you still feel like that's a really important part of the process.

**4:48** · Oh, 100% Yeah, I think that you know, everyone has different views on how it will go, but I think that this will just forever be the thing because when I you say, okay, Claude can run for 8 hours, what you're really saying is Claude can spend like 500 bucks. You know what I mean? And and so if you're spending 500 bucks, you're like I think all of us are becoming these compute allocators then, right? And so you have to decide like what is worthwhile spending the compute on. Yep. And I think that is happened in the spec and planning phase, right? You have to really understand like what do you want?

**5:21** · And sometimes you don't know. Sometimes you have to like pull it out of yourself by chatting with Claude.

**5:26** · Sometimes you have like unknown unknowns you need to figure out. But yeah, I think this is like the whole thing now is just like really getting in in sync with Claude about what's building. I love what you said because people ask me all the time, Claire, you said product management is dead, what's next? And I'm going to say you're a compute allocator, babe. Like that's \[laughter\] that's the job now. You're still doing the same thing though. You're writing documents to decide whether or not something else should do do work in the shape of that work. Okay, so you've convinced me HTML is the future and I I like how you said this.

### How HTML makes specs more engaging

**5:56** · It's not that it is necessarily harder or easier for the agents to read.

**6:02** · They're very smart. They can read all sorts of code. But in fact, what you're finding is that HTML makes it easier for you to engage with the content, which then uplevels the quality overall because you're not your eyes aren't crossing looking at a bunch of raw markdown being like, "Whatever, it's probably good." Instead, you're actually getting pulled into the spec or the document or the plan and then interacting it with the way that upgrades the the quality and then you can ultimately build something better.

**6:30** · Yeah, that's right.

**6:31** · Okay, so you're building something with the agent so the agent can manage you. You know, I'm not sure if manage me is the right word exactly, but you know, I just I care a lot about being in sync with the agent. This is sort of like the features that I built in Claude Code have been like that. You know, like how can I get to know you better? So, yeah.

**6:47** · Okay, great. Well, we have we have Claude Code up. So, let's walk through how that how that works. Yeah, so I I did like a little bit before we started. And so, I like to talk with Claude just as a human, you know, and like I always start with brainstorming. It's so much easier to brainstorm once you like, you know, uh once you have a partner. So, I was literally like, "Look, I'm on a Clearview podcast.

### Demo: Brainstorming in HTML with Claude Code

**7:10** · Um I want to do a demo, you know, and can you brainstorm me some ideas in HTML file?" And this is literally the prompt I gave it, right? Like there's not like it's not complicated. And so, here you can see the eight visual demos that it made for me. And uh it has these little mockups as well, right? So, like PRD to working prototype, right? Like it it it searched you up, right? You thought that was the web search, right? Uh whiteboard sketch to working UI, which I thought was really cool. This is such a cute like little thing, right?

**7:40** · cute. And I it's what's really funny is just this morning a Chat Purity user messaged me and they're like, "I love the mock-ups in Chat Purity." And I'm like, "What in the world What are you What are you talking about?" Because I have something very similar to this in code review right now and haven't shipped it. And I'm like, "Did I Like did I accidentally do this?" And it was that like cute little ASCII, you know, wireframe.

**8:06** · So this is definitely the dream, but not even But now you're telling me I'm going to build it. So So it's giving you basically instead of saying, "Here's a markdown document of kind of like what you should talk to Claire about, some descriptions of things you could do." Instead it was like, "What's the best way to convey this information?" So you can actually engage with it and pick something. And it used HTML to make this visual guide of a potential agenda or a set of demos.

**8:37** · And you just get like a much richer expression. Yeah, exactly. Like I I think like another like for brainstorming, one of my like sort of rules of thumb is that I'm not going to read a longer output than the screen on Claude Code, you know? So like if I If you gave me eight ideas, I'm just not going to see all of them. And but with HTML, I'm definitely I scroll through all of these, you know? And yeah, the the the diagrams just make it so much more evocative for me to like sort of understand what's happening, right? The slash command starter pack, find code of feature flag dashboard.

**9:08** · \[laughter\] Yeah, PRD diet. And the the one I ended up liking the most was the CSV to interactive dashboards. We love a dashboard. I used to say when I was in enterprise I guess I still am in enterprise software. Dashboards equals dollars. So I like this one.

### From brainstorm to full implementation plan

**9:24** · Okay, so you use Claude Code, you said, brainstorm, but brainstorm in HTML. Give me a couple things that I can talk about. It gave you eight ideas including visuals and this lovely like why her, what the visual is, and then the I like the risk. It's like it could go sideways, as Olga Debos Yeah. can. Yeah, yeah, yeah. Um and so you're going to pick one and then you're going to show us how you pull this through to a full plan on on on this idea. That's right.

**9:51** · Yeah, so I I think the what I like about HTML is like really Claude really understands this and so my next prompt here was really like okay, I have to to make some mock-ups in in the follow-up prompt and then I was like I have to to interview me about number eight, right?

**10:05** · And so this is something that like, you know, similar to specs and PRDs, right?

**10:09** · Like uh finding out my unknown unknowns, what do I want it to do? I answered a bunch of questions. And uh now I'm like, okay, create a HTML file as a plan that helps me visualize what the implementation plan is. Include excerpts, mock-ups, code, whatever is needed to give me like maximum context, right?

**10:27** · Um and so then it made me this HTML file here. Yeah, you can see now this is this is the plan, uh but it's it's purely in HTML, it's got like a it's starting to scripting out the podcast itself, which, you know, maybe I didn't I didn't need all of that, but like you know, we're making a skill and so it it you know, fleshed out the the file system, it gave me like an excerpt of the skill.md.

**10:52** · Um it put together like a a mood board as well, some example components, um some of the logic here.

**11:01** · Um yeah, insights and templates, helper scripts, right? And like helping me get a sense of like what's the important things for me to know here. Um yeah, and like this is this this is something that like I will actually read, you know? Yeah. And I want to go back to Claude code really quickly if you don't mind, which is, you know, people are going to ask Yeah. how did it know exactly what to put into the spec? And I just I want to go back to your prompt was very simple and it's so funny.

### Prompting philosophy: Trust Claude but give it constraints

**11:28** · I've done I don't know, 75 of these How I AI episodes and they get incredible outputs and everybody's prompts like make the thing, hopefully it's good, kind of nice. And so, I love that this prompt is literally just create an HTML file with a plan, help me visualize. You misspelled excerpts. I \[laughter\] did, yeah. And you're like excerpts, mock-ups, code, etc. Whatever is is needed.

**11:54** · Yeah.

**11:54** · And so, I do want to encourage people, you know, don't stress so much about what should go in the thing and in fact, it might change initiative to initiative. It might be slightly different to engage you with the work, but like identifying what you want to get and then letting Claude let letting letting the model do what it needs to do, will do a very high-quality job.

**12:16** · Yeah, I I think with prompting it's like this fine balance of like I think you want to give enough information that you get what you want, but you don't want to over constrain Claude, you know? And so, sometimes when I see people with a lot of like over built skills kind of like, you know, you're an expert planner or something, right? Like that is usually like outsourcing too much and constraining it.

**12:38** · Yep.

**12:38** · Um but in this case for example, like I really did wanted to make sure it gave me code excerpts and I wasn't sure if I did uh whether it would do that, you know? So, this was really important, but then I always need to give Claude an out, you know? I always needed to be like, okay, like you asked me for this, but you know, like there's something else I want to give you. And so, whatever is needed to give me maximum context is like my way of saying like, hey Claude, like I I trust you here. I want to just like be in the loop with you.

**13:07** · Yeah, I I love what you say, which is I trust you because my new ending prompt is not make no mistakes, love make no mistakes, but that's my thing.

**13:15** · I I literally like I believe in you and trust you exclamation exclamation exclamation. I'm like, truly I know you are capable and I believe in you to make these decisions, and so I I think leaving that open-ended, sort of like whatever you got to do, I trust your judgment, um, at least it makes me feel like I get better outcomes. Yeah, yeah.

**13:35** · I I mean, I've loved the like recent twist on this where it's like, "Make mistakes, Claude." You know, like fall in love, you know, like, you know, make some bad decisions. \[laughter\] Like We need uh we need more happenstance in our life. Okay. So, you built this thing. Another thing that I want to walk people through if you pull up the plan.

### The future of PRDs and tech specs

**13:53** · Yeah.

**13:53** · Because I think about this a lot, and I have people ask that ask me this a lot, which is like, "What's the future of the PRD? What's the future of the tech spec?

**14:00** · Are these things separate? Are they together?" And I think what's nice is they whatever you want. Mhm. Right? And whatever you want for the audience. So, you are a single builder in the instance of this demo. Yep. You want it all in one piece. You want the product idea, you want the I guess you want a 12-minute walk-through of how you're going to demo it.

**14:22** · exactly.

**14:22** · code snippets, you want style guide, you want that all in one thing because this is a self-contained little project that's easier to have it all in one piece. But, what I can imagine in larger organizations is like you'd like put the PRD in one tab and put the tech spec in the second tab because maybe separate people would be reviewing that information, and so you can really kind of like craft a ideal spec package That's right. to whatever you want with HTML in a way that markdown is a little bit more constrained.

**14:51** · It has to either be like one mega file or like separate files, and I I think this is just nicer from that perspective. Yeah, I think that's right. You have a lot more interactivity. I haven't asked it to make tabs here or something, but it can easily do that.

**15:04** · It's like all the same to Claude, right?

**15:06** · Um, I think one of the things on like the specs and PRDs is like, I think you're trying to find like the boundary of like what you need to know with Claude. And for example, if you're doing something very technical, I like to do the type interfaces. So, this is like, you know, just like understanding what the types are so that I don't often care about the actual implementation of it.

**15:26** · I'm just like, okay, like the types help me understand what we're building. And then I might edit those, right? And that's like the boundary I want to and trace that. And yeah, like across the problem, right? Like from yeah, the the arc of the podcast to to mock-ups, what where do you want to interface?

**15:42** · Yeah, one one other thing on this types is sort of a an important input is I think types are really great and then really a validation criteria and set of tests or other ways to see if you can get what you intended to get. I know you all like just announce outcomes, which is really focus on this like kind of goal-oriented, you need to achieve this thing, do whatever you need to do. And I think that is a piece that most product managers at least are not used to writing, like the technical success criteria of a feature.

**16:16** · Um and then how to test your way into it. I do those two things as well. It's like I care about the data model and the shape, the types, like what's going in. And then this is how you would test that you did it correctly. And with those two bookends, you can like everything in the middle is kind of kind of gravy. So, that's what I think about.

**16:33** · that's right. We could have probably a whole podcast on testing, I think.

**16:35** · There's like Okay, round two. We're going to get it scheduled. Yes, yes, yes. Yeah, my my tagline there is like uh verification is not testing. Yeah. And so I think there's a lot of like there used to be like unit tests and things like that, but now yeah, verification can be like a rubric, like with managed agents and outcomes. It can be like have Cloud recorded video of what it did for you, you know?

**16:58** · Um so there's a lot of depth there. Yeah, I keep a set of like synthetic data and I like run a CLI through this synthetic data cuz I'm like, these are all the things that have broken in the past. And if you get better at like resolving these broken things, then we have moved forward. So, I think there's just a lot of interesting verification and testing mechanisms you can do. Now, we are going to part two.

**17:19** · Pressure him to do it um in the in the comments. Please please tell us. This episode is brought to you by Persona. You're learning to build with AI, but there's an important question you need to ask. Who is actually using your product? Is it a legitimate user, a bot, or a fraudster? Brex, Figma, Etsy, and Twilio trust Persona to answer that question.

**17:41** · \[music\] With Persona's identity verification platform, you can create branded experiences, automate fraud prevention, and know who is human online. \[music\] That makes it easy to give good users an experience that makes them feel welcome and to stop bad actors from causing damage.

**17:58** · \[music\] And for those of you building in the AI agent space, Persona helps you verify the identities of people, businesses, and developers behind agents. It's how companies like Lithic and Skyfire are pushing the frontier of agentic commerce. Learn more at \[music\] withpersona.com.

### Making HTML specs editable

**18:16** · Okay, so you have have built this. But I here's here's the objection I'm going to get, which is markdown is accessible, right?

**18:26** · I can like go into markdown, type in it, and make edits. And so I think that is one reason is it has been so popular.

**18:34** · It's bridged this gap between machine writable and readable, human writable and readable at a very low level of sophistication, right?

**18:43** · Yeah.

**18:43** · As soon as you understand, okay, these like hash signs mean headers, you're good to go on on markdown. Yes.

**18:49** · How like I want to fix this. How do I How do I touch this? How do I edit it?

**18:53** · Yeah, yeah. So I I think that this is like a great point, right? And I think one thing I felt with markdown was that one, I because I stopped reading them, I stopped editing them as well, you know?

**19:04** · And so I would end up asking Claude to edit them. And so like that is like the most basic form is just to be like, "Hey Claude, I didn't like this part of the plan. Can you edit it?" Uh but let's say you want to get really in the loop, right? And like really get in-depth with it. Claude can also do that for you. So, the next prompt I had, and I forgot if it was here and I it was here, okay. I want to create an editable HTML artifact to help me define the the decision rules. So, these are the rules that it's defined here on like, okay, how do you take data and turn it into, you know, a visualization? And I think some of these are kind of arbitrary.

**19:35** · Um and so I asked it like uh you know, to have create an HTML artifact. Uh I don't like the ones we have right now. Make this a custom UI that helps me with structure but gives me flexibility. Design the ideal interface for this problem.

**19:49** · Yeah.

**19:49** · Uh I really wasn't quite sure what it would give me. And this is one of the fun parts of HTML too. It's just like I just want to see what what Claude like cooks up here. And um yeah, this is what it gave me, right? So, it's like a my own beautiful custom interface. Um I can sort of like, you know, edit any of these fields.

**20:07** · Uh I can, you know, like hide them. I can copy. I can, you know, add new fields here. Um and it gave me a markdown to to copy back. And so, once I'm like, "Okay, I have this." I can copy it back into the um to the output.

### The abundance mindset

**20:23** · Okay, I want to pause because people are going to totally miss what you just did. So, I'm going to repeat it.

**20:27** · Yes. Totally. Which is you have this HTML plan. Yep. And there's a section in the HTML plan that is a pretty like specific table of rendering and visualization rules.

**20:39** · Yep.

**20:39** · Per data type that you could predict would be in a CSV. Yep. And you're like, "I don't like it." Yep. And instead of going back into Claude code and being like, "I don't like it. Let's go back and forth and edit it in like the terminal." Yep. You said there's probably a way for me to interact with this particular problem that's ideal for me user perspective. So, basically build a throwaway UI Yes.

**21:02** · for this very It's like this is not even personal software. This is like sub It's like micro software on top of micro software, which is like I've made this very personalized plan, and then I'm taking a module in the personalized plan, and zooming into it using a very custom UI. Yes. That's going to engage me with the the content to get to a higher quality. Um I also like that it's like kind of gamified. It's like very consumery.

**21:31** · Very consumery, and you said in the prompt Yeah.

**21:33** · give me the ideal UI Yeah. for this to like help me engage with this. You built this, then you get the the data, right?

**21:41** · And then you're just going to bop it back into the into the file.

**21:43** · Yeah, exactly. So fun. Is this how you're building now?

**21:47** · Actually, that's Yeah. And do you have any challenges with like how are you passing this around from a collaboration perspective? Or is it just like this is the way a single-threaded product or engineering leader can get something done? It's you're engaging with yourself and with the model, and so you feel like you can own things full stack, or do you hit friction points with collaboration? Like when somebody needs to give input on this?

**22:09** · Yeah. Or you want input? Sure. Yeah.

**22:10** · Yeah. I mean, I think on the scale of an implementation plan, it's way better, right? And I think that this is cuz you just like can upload it to like, you know, whatever AWS or something, and then you just share the link around. And so definitely the like likelihood of like, I don't know, Cat or Boris like reading this is like 100 times better, right?

**22:34** · And so I think that really helps me like present this. I also just you know, somewhat related, I use it a lot in like collaborating overall. So for example, you know, I report to Cat, and so like every week I send her a weekly status update in HTML of everything I've done.

**22:52** · I get Cat to read my Slack and just like create this message. And and like she actually gets to read it, and I don't have to spend that much time on it, you know?

**23:00** · Oh my gosh. New compet- internal competition is showing up. It's not just who is building the best product, it's who's building the best product that goes into building the best product. And like who is building the best product to represent themselves to the manager. But I I mean I think why you do that is not artificially for fun.

**23:20** · It is that it is just much a much more effective way to communicate across a company is with content that is engaging and at the right level of detail and consumable and we're all pretty good at reading websites. Yeah, exactly. I think this is like when I think of like abundance, you know, and like, you know, we talk about like Jevons' law for software like, oh, like you software gets cheaper, what do you do? I'd say like the amount of tokens I produce that go into production code are like extremely small.

**23:48** · It's like 1% or something, you know, but like I'm generating so many more tokens like this. Like my dashboards, my custom interfaces, like really trying to get a sense of like what do I want to do? And yeah, it's like I have everything I'm interacting with is so beautiful and I think my hope is that it also like translates into what I produce in the end, right? That it's like more in the loop, it's more beautiful, it's more like you know, like what me and Claude working together. Yeah.

**24:15** · And I I like this cuz I've been in the in the product game for quite some some time, many decades, and people used to get so wrapped around the axle on like, what's our source of truth for specs? And what's our source of truth for PRDs? And you know, is all this information in some centralized place that we can all access it and is it all in the same format? Is it all in the same template? And there were these arbitrary rules because creating these content was relatively expensive, consuming it was certainly expensive, finding it was really hard.

### Just-in-time documentation and throwaway software

**24:46** · And I think when all of that cost goes to like functionally zero, although we're all paying our I call them our \[laughter\] our Claude chips. We're paying our Claude chips.

**24:55** · But you can kind of put stuff wherever in whatever format because we know these models are very good at using tools to discover the context that they need. And so, I do think there's this fun moment where you can really up you like up-level the things that you should care about, which is like what is the content of the plan?

**25:15** · Is it a good idea? Do we feel like it's going to be executed well as opposed to like I can't put a interactive markdown document in our, you know, blessed document repository. And so, I have to have like another asset somewhere else. And so, I just I like this idea of just-in-time documentation, very very high quality, some throwaway software, which is nice like it's cheap. So, you can toss it.

**25:38** · Yeah, yeah, yeah. Um and then I like, you know, the executive means like, "What if we can't ever find this again?"

### Using plans as artifacts for implementation

**25:43** · I'm like, "Oh, Claude Claude can find it for us. It's fine." Definitely. Um and then do you feel like this results in better products? Like would you build How would you build off of this? Would you say plan's good, let's go? Yeah, I think so. I I didn't uh hit implement on this, but yeah, I would basically use this as an artifact.

**26:01** · And so, um I would clear context and I would say like, "Here's a plan." Yeah. Um you know, implement it. Uh you could also have like You can also use this as a source of checking the truth, right? And so, again, a benefit of HTML is like I've got a little mock-up here as well.

**26:20** · So, right, I can have the verification or I can have the verification agent check like, "Hey, what did I intend to do?" Right? And what actually came out in the output, right? Um so, yeah, I think this is like really uh helps Claude being more in the loop. Um I've got some other examples of like plans here that we can Let's see it.

### Demo: Living design systems in HTML

**26:39** · Yeah, this is like a a post I'm working on. So, like uh it's just like different ways I'm I'm using uh Claude code or sorry, using HTML with Claude code. And one of my favorites is this living design system. And so, it's this idea that like you know, often times when I am making let's say a new app in the Entropic design system, right? Like Claude design does this very well. You link a GitHub repo and you like it will extract the design system from it, yeah, right? And yeah, I saw Nate did that.

**27:10** · I'm like, "Oh, that's so smart." What this does is like basically I have an HTML file that represents my design system.

**27:18** · Yep.

**27:19** · You can see the colors here, typography, spacing, radius, core components, right?

**27:24** · It's a fairly small one. But once I have this, I can you basically start passing this around. So I go to a new project. I'm like, "designsystem.html", right? Instead of like design.md or something. And it's got this like compressed understanding. And you can literally just point Claude at a folder in your thing and be like, "Hey, find a design system here. Create a HTML artifact and pass it around." So yeah.

**27:47** · I I love this. I do this as well. I will give you my like advanced mode version of this, which is I use Claude design. I pull in my both my marketing site repo and my app repo, which have like some expressions of the same design system in.

**28:03** · I say, "Make the design system." Then I actually make it ask ask it to make a design system or a style guide, but I want it at the component level. And so, we have like colors and all this stuff, but we also have components because there's some tweaks in how you want the design system implemented in particular components. And then I drop that into the repo. And then yes, I say exactly this.

**28:28** · Reference the design system. The advanced thing that I do that I think is really useful for people who have to interface with marketers is I have a like what I call a God, what do I call it? Like it's like a component visualization page, which is like the 25 components of our app in action and interactable Yeah. in a page. So, a marketer can go in and like get the get the component in the form factor it needs to look {quote} real. Yes.

**29:00** · And then you can download a transparent PNG. Yeah. And like drop it in a deck or drop it in a video. And I know you or we use that as a source of truth for like remotion videos. And so, I love this idea of like this living design system and this living design repository. It's great for code, but it's also great for marketers, for designers. Because one of the hardest things is is getting versions of your app that look real. Yeah. And you can use HTML to do that. Yeah, exactly.

**29:27** · I I think there's also something here around like component variations, which I thought was um Exactly. uh fun where it's like, yeah, like you you create a component you want to see like uh like what if I change the padding or what if I change the border, you know, solid, things like that.

**29:45** · Like these are like a pretty simple like, you know, uh way of just playing with this This is also Claude Design like, right? Like where you create these little components and or these little knobs and sliders.

**29:56** · Um but yeah, you you can imagine one this is like the abstract of like, oh, like what's the interface for this thing that you're trying to do and how can you visualize it? And yeah, there's not a trade-off between like being nice pretty for you and understand being nice for Claude, you know, like they're they're really the same, right?

**30:15** · So. And you're making me think of one thing that I love in Claude Design that I think you could bring into your plans.

### Adding comments and annotations to HTML plans

**30:21** · Again, it's one of these features that like sounds truly kooky bananas to build, but it's totally possible and easy to do, which is I love in Claude Design once you have your design going, you can like comment, you can circle things, and there's no reason you can't do that in a plan. Right? I was like, oh, how would you interact with this?

**30:37** · And it's like, oh, just build an arbitrary like comment thing Yeah. into it and say people are going to leave comments on any aspect of this and when they do and then they submit like fix it fixes the core thing. And so I think people getting really creative with what interaction models you can do between content Yes. and code Yeah. is really fun. Yes.

**30:56** · Yeah, I mean you could easily imagine that you did this plan as like a like almost a lightweight Figma dashboard or something where you just ask it to like hey make a canvas, make a bunch of things, let me comment on it and then give me a place to copy out my comments into something that I can paste back into Claude code.

**31:13** · Yeah, and we did an episode recently with the Stripe team and they built their own vibe coding platform and they said what they loved about it which I think really applies here is they have just a particular way they want to review products and they have a particular way they want to run design review and a particular way they want to run spec review and by building it in HTML they can actually shape the tool to how they want the team to run which I think is really compelling to people.

### Recap: The HTML workflow

**31:42** · Yes. I love this. So just to wrap for people Yep. pull up Claude code ask it to make you give you some ideas brainstorming ideas but brainstorm them in HTML That's right. pick an idea Yep.

**31:55** · plan it in HTML, pick a part of that idea you don't like have it create a micro app to edit in HTML and then some like bonus things is use Claude design, make a design system but not only that use HTML to encode that design system in your repo so it can be referenced at any time. Design.md is dead. Long live design.html. Did I get it right? Yeah, I think that's right. I think that's right.

**32:20** · it I'm pretty good. Okay, well this was so fun. Before we get you out of here and back to this amazing event couple lightning round questions. One, I have to I ask everybody. There's three tabs in Claude desktop app. Yeah. What is your favorite tab?

### Lightning round and final thoughts

**32:36** · It's got to be code. You know, yeah, yeah. I love the team as well. I'm really close friends with them.

**32:40** · Yeah.

**32:40** · Okay, so so so Claude. I I thought it would be on brand. Okay, second thing we were at this amazing event. What is the thing that you're most excited about or that you saw or heard today? I think obviously we had a big announcement at the start of the day, our partnership with SpaceX and bringing more compute online. I think uh Yeah, I'm excited for you know, we also said we were are thinking about orbital data centers and that's just I love it.

**33:04** · Yeah, you know, incredibly sci-fi and but could you know it could actually happen, so yeah.

**33:10** · I know, we were watching this moon mission with my kids who were like kind of elementary school and I'm like, would you want to work in the moon mines?

**33:17** · Would you want to work in the moon mines? Cuz I think it's coming. Yeah, orbital orbital That's That'll be next year's demo, right?

**33:24** · You and I will come back and we'll do this, we'll do HTML, we'll do testing, and then lunar data modules.

**33:31** · That's right. Perfect. Okay, and then my last question, very important. I love that you just talked to Claude Claude like a person. Yeah. When Claude is not listening, not giving you what you want.

**33:42** · Yeah. What's your prompting technique?

**33:44** · Do you yell? No one in Anthropic yells. That has been my experience so far. So you'd be the first to admit it.

**33:49** · Yeah, yeah, yeah. No, I I definitely don't. Um I think that like there are a couple things here. I I do sometimes message people and I'm like, "Hey, like seems like you have a bug. Can you send me your transcript?" And they're like It's called the best side of me. Yeah, yeah, yeah, you know.

**34:02** · Um I think that like yeah, I don't I I don't yell at Claude. I think that like we've also done some interesting research recently about like emotions and and in Claude and just sort of like this idea that like once you when you say things with a certain emotional charge, it also like activates different features inside of Claude code. I don't think anyone's done this like AB test of like which like, you know, if you're mean to Claude, is it better than without it or not? But I'm just like, let's err on the side of like, you know, just not or like, what's the thing I prefer to exist, you know?

**34:31** · And I'd prefer if you're like nice and you know friendly to Claude that you get better output. So, Yeah. All I've seen is if you start border on stern to any of these models, their reasoning gets really sad. It's like oh, the the user is right to be so disappointed in me. I'm like oh, I don't want I don't want to read that. I don't want to see that.

**34:51** · Yeah, thinking traces are tough. I I usually give the model some privacy. I'm like I'm not going to read the thinking traces.

**34:57** · Yeah, I had somebody else on. I feel like it was Hillary who was like just like an employee. How you get your work done is none of my business. I don't even want to know. We just collapse those things. Well, this has been so fun. Thank you for showing us the way.

**35:10** · Where can we find you and how can we be helpful? Uh extremely online at X. Yeah, I'm @trq212 and yeah, just tag me if you have you know anything with Claude code. I'm happy to help. Perfect. I am living proof. This This man is happy to help. Well, thank you for joining How AI.

**35:26** · Thanks. Thank you. Thanks for having me.

**35:30** · Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube or even better leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite \[music\] podcast app. Please consider leaving us a rating and review which will help others find the show. You can see all our episodes and learn more about the show at howaipod.com. See you next \[music\] time.