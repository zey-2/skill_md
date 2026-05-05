---
title: "Context Is the New Code — Patrick Debois, Tessl"
source: "https://www.youtube.com/watch?v=bSG9wUYaHWU&t=1100s"
author:
  - "[[AI Engineer]]"
published: 2026-05-03
created: 2026-05-04
description: "As AI coding agents become more capable, context is starting to matter as much as code. Yet while code has version control, review, testing, CI/CD, and production observability, the prompts, rules, an"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=bSG9wUYaHWU)

As AI coding agents become more capable, context is starting to matter as much as code. Yet while code has version control, review, testing, CI/CD, and production observability, the prompts, rules, and memory that drive agents are still often managed like ad hoc hacks.  
  
Patrick argues that context needs its own engineering discipline. He introduces the Context Development Lifecycle: Generate, Evaluate, Distribute, and Observe, along with the team practices that make context a shared, repeatable, and improvable part of software delivery. The session also explores the larger context flywheel, where better context leads to better agent output, which creates better observations, which in turn improves context again.  
  
Speaker info:  
\- https://x.com/patrickdebois  
\- https://www.linkedin.com/in/patrickdebois/  
  
Timestamps:  
0:00 - Introduction to the talk  
1:14 - Why context is the new code  
2:37 - Introducing the Context Development Lifecycle  
3:50 - Generate: Creating context for agents  
6:26 - Evaluate: Testing your context  
13:59 - Distribute: Sharing and packaging context  
17:49 - Observe: Monitoring and feedback loops  
22:33 - Conclusion and the context flywheel  
24:49 - Q&A session

## Transcript

### Introduction to the talk

**0:07** · \[music\] There's there's a few people who want to start earlier.

**0:17** · I know I'm going to take the opportunity to officially open kind of the architect track. There's no track host, so I do it myself. So, thank you for coming here. I hope you already had like a good conference. Um It's amazing that like so many people showed up. Um maybe before I start, um who's used any AI coding agent in this room? Raise your hand.

**0:40** · Like lower it. Who hasn't? Raise your hand.

**0:44** · Okay, my kind of people. Perfect. All right.

**0:48** · Um Okay. Context is a new code.

**0:54** · Or context development life cycle. Um I feel honored to be here. Every time I try to do a different talk at the AI engineering.

**1:01** · So, this is a little bit of um you know, thinking ahead. It's an unpolished thought. It's not like everything's there, but is there anything there in AI anyway? But So, let's start.

### Why context is the new code

**1:17** · I assume you all are now vibe coding with prompts. I barely touch anymore kind of the code. I just tell the AI to do something different.

**1:28** · So, I would say like context is the new code because it's being generated.

**1:35** · A little bit more advanced maybe is I see myself having a tendency is I had large pieces of code that I was using maybe some helpers and some other pieces.

**1:47** · And I just turned them into a skill.

**1:50** · We had that in our into our product. It was an onboarding from, you know, AI agents. Um People have Python, Node.js, all the various things. Then they have different tools for packaging and it is impossible to actually code that.

**2:06** · Like it will require a lot of coding.

**2:08** · But if I just say a skill says please first figure out what their package manager is, then figure out what their ecosystem is, and then do these steps together with the user.

**2:20** · You know, it's solved a lot more problems that we could ever code. So, that is another piece that I would say code is also transforming back into context as a skill as well, as a workflow that's reusable. And leave that with you.

### Introducing the Context Development Lifecycle

**2:37** · I like to think in parallels.

**2:39** · In 2009, I don't know if there is any DevOps people in the room. It was kind of me saying like what if ops looked more like dev? And then we got like, hey, collaboration, kind of our deployment, all that stuff. So, kind of, you know, last year I started thinking, what if context is the code?

**2:58** · How do we deal with this in a more consistent way?

**3:02** · And it's basically saying if we have a software development life cycle how does a context development life cycle look like? Because we're basically shifting somewhere else. It's context, it's not code. How does it look like?

**3:18** · I came up with this, you know, of course an infinity loop with some DevOps background. But the whole idea is that we generate a lot of context.

**3:26** · Then hopefully we test the context. We distribute context maybe to some colleagues, to some other parts of the organization. We observe whether it works, and if it doesn't work or works, we call like, you know, adapt and regenerate the context and then go from there. So, that's kind of the loop of the talk that I'll be going for with some examples.

**3:47** · So, step by step going through.

### Generate: Creating context for agents

**3:50** · Generate. It's probably the one that you're all most familiar with.

**3:55** · Because you're all prompting.

**3:57** · You're like the human context creation typing things, right? I was actually amazed that I just asked, tell me when my talk is at AI engineer, that it would fetch the website and it would just say, here's your talk. Like blew my mind. But hey, I I said like the context that I've given it, I'm Patrick, all that stuff, right? So, very simple context. It's what you do probably a lot in your setup.

**4:23** · If you get a little bit more advanced, you say that prompting is tedious. I want to have reusable prompts. So, you know, depending on the flavor of your coding agents, they call it instructions.

**4:33** · Luckily, there's a little bit of a standardization now happening where it's like an agent.md and some pieces like that. Boo Claude for still calling it Claude.md, but anyway, you get the picture. There's like reusable prompts, reusable pieces of context that we're doing.

**4:51** · We can also bring other context in.

**4:54** · If we have documentation of libraries that we use day to day we want to pull that in because the LLMs might not have the latest documentation.

**5:03** · And so it's hallucinating. Is it version two, version three? We don't know. So, we give it a context and say, please download the documentation. Hopefully then agent optimized. And then they will do a better job at generating the code for that version of the library.

**5:18** · Another piece of getting better context and creating context from libraries.

**5:24** · And of course, it wouldn't be complete if we would say pull context from wherever. MC Get it from your GitLab, GitHub, kind of Slack.

**5:35** · All context we're pulling in, we're creating. Even a ticket is creating context because we're pulling that in while we go there.

**5:45** · And then maybe the new kid on the block is, okay, what if we start like writing our prompts as specification spec-driven development which then gets broken down by the agent into a planning mode into step by step kind of prompts that it then kind of runs through. So, a lot creation happening in that field.

**6:06** · You know, simple. This is probably what you're closest to.

**6:10** · But when you're typing all that context and creating all that context you change two lines in your Claude.md.

**6:19** · Do you know the impact?

**6:21** · Is it like YOLO? Looks good to me. Let's do it. You have to think about how do we test things?

### Evaluate: Testing your context

**6:28** · It's not just about we have a piece of code and we have a piece of context now.

**6:34** · We need to write tests to see what is the impact. New coding agent? We don't know where the lines still work.

**6:42** · Now, it's not new in the world of AI engineering but it's not that common yet in the world of coding with AI that you start writing evals for which are tests for your kind of code context.

**6:59** · Uh a little bit hard to read, but you know, if you think in parallels we have different levels of testing in code, and the simple one could be linting. Your IDE is has the swiggly lines like, hey, this is not like, you know there's some incorrect syntax or you could do better like that.

**7:18** · Here's an example of a validation of a skill where we say, well, you need to have the description. It can only be so long. So, it's validating according to the spec of the format of the context in this case.

**7:32** · Simple analogy, simple linter that you can run.

**7:38** · And then you can do other things like and and I haven't found maybe the good coding equivalent, but think of this as a Grammarly.

**7:45** · Right? So, if you write context um is it actually can the agent understand what you're writing? If you write two words, it's not verbose enough for it to actually understand the context. So, what you can do is you can say ask is like, okay, you know, given this context, what do you think about Do you understand this? And then you can get feedback like, oh, it's not explicitly enough written or it's not complete. Like you're missing pieces.

**8:17** · So, that's kind of from tools as well. So, whenever you're writing now your context, you get a Grammarly saying, hey do this. That's why I like to voice code. For some reason, I'm way more elaborate voice coding than typing. I'm a bad typer, two fingers still after so many years. But when I talk, I was like, you know, I see the the sentences come on the screen, but it helps to get good context there.

**8:43** · All right, another kind of test.

**8:46** · So, imagine you put in your Claude.md or agent.md, I should say. Now, um every API point must use the prefix awesome.

**8:56** · Right? You have some convention in your company. Right? Which is great.

**9:00** · So, your prompter will be then, add me a new endpoint to save a user.

**9:05** · And you expect actually your coding agent to just say the code that's being generated has kind of {slash} awesome {slash} user.

**9:15** · That's great.

**9:16** · But the way we can test this is by asking then an LLM the code that was generated does it actually start with {slash} awesome? Now, you can do that with regex, I know. This is just for example purposes, but you can ask it to kind of judge your code based on your criteria and whether it did the right thing.

**9:40** · Right? So, imagine you would ask the same question without your context above.

**9:47** · No LLM is ever going to prefix your URL with awesome. So, that's kind of where your content or your company specific, your team specific things come in, and that's why you still write those tests to see if this still works. Now, maybe Gemini kind of reacts differently than Copilot or something, and in your company you need to make it more, you know, switchable of context. With this, you run the tests, and you can actually tell.

**10:14** · That's the difference.

**10:16** · And then you can make like whole suites, and I would compare that almost to unit tests. I have a bunch of these tests, and they tell me whether that's actually, you know, good code, the code is following the rules, and everything's fine. In this case, it's even kind of infrastructure as code. It doesn't need to be code only. It could be various things. Could be config files as well.

**10:35** · And I just have It's hard to read, but a bunch of kind of criteria that I just run every time to do that.

**10:44** · But, if you want to test, you know, whether an endpoint has {slash} awesome {slash} user, there's a real test that we want to run, which is I want to test the endpoint. I just don't want only to check the code. I want to have it running. So, when you give the judge a tool, and the judge becomes an agent, and it can do things in a sandbox and execute stuff.

**11:14** · It can actually do the do the curl. So, you can bind LLM as a judge with kind of some tooling, and then you can have multitude of tests actually, you know, in this case, it kind of ends up being an end-to-end test, right? Because it's not just looking at the file, it's actually running the piece with everything that it's supposed to do.

**11:36** · And then I can do this like given a certain commit in my repo, I want to run this scenario given this piece of context, did it make a difference? Yes or no? So, you're kind of like building this up while you're committing context also within your repo.

**11:55** · And because we now have tests, and it gives us feedback whether it's working yes or no, or what it's missing, we can optimize context. So, that's kind of the, you know, you we can put that in a code action or something that says like, "Okay, fix this context. Improve this context." With all the feedback the LLM has given us to improve that.

**12:17** · So, you know, again, coding uh improvements, but we start thinking more in testing that piece as well.

**12:26** · Now, one of the first reactions is once you have tests and optimizations, can we run this in a CI/CD system because that's perfect, right? That's where we run our all our tests and our test suites and do that.

**12:40** · Now, there's a little bit of a weird thing.

**12:43** · If you run evals, you run it once, you run it another time, it might not give the same result.

**12:50** · Remember, undeterministic things.

**12:54** · So, you cannot say, "Well, run it once, and then if it passes or not." You're going to be in for a treat because it's like, "Ah, I I can't debug that." So, think about this like you run it five times, and out of five, how many times does it succeed?

**13:12** · And, you know, maybe in several cases it hits 100% all the time, which is great.

**13:18** · But, in others not. And depending on how you change your context, it will influence which test actually work or not.

**13:26** · I find it personally helpful to think about this as error budgets.

**13:30** · I give a set of tests an error budget that I really care about, so it it's only allowed like, you know, to fail minimally, and other pieces are okay. So, that's how you have to think about testing context. You cannot do like exact testing all the time. It's a different way that this works.

**13:52** · All right. So, generate. Hopefully, you understand what the testing could do for you.

### Distribute: Sharing and packaging context

**13:59** · And distribute.

**14:00** · Maybe that's also something you already did.

**14:03** · If you maybe have checked context into your repo, right? Which is great, you know, all of a sudden it becomes available, your colleague checks it out.

**14:12** · Uh zero friction, I can push, I can share.

**14:15** · But, we have another mechanism for doing things. Think of this like Imagine you have a reusable context that you want to reuse across multiple projects, across multiple teams. We had the concept of a library.

**14:32** · So, what if we package kind of pieces of context, and then we are able to install pieces of context that we need for this project.

**14:43** · Guidelines, front end. It doesn't matter for that. And then if we take it that up a notch, how to discover what packages exists?

**14:53** · That's a registry.

**14:55** · Right?

**14:55** · Now, in that way, it's no surprise that you'll see things like skills and kind of the Tesla registry in the marketplace, where you can find a multitude of skills. Now, the reality is 99.9, and I mean that in a very sincere way, of the skills is crap.

**15:16** · But, it's good to learn from others to see what they're doing.

**15:21** · But, hardly of them, if you run kind of any set of evals on there, is actually up to a quality standard.

**15:29** · Now, that will likely improve. But, there's also a tendency is that a lot of the skills and pieces, people actually want to put that in their own registry.

**15:41** · So, I'll come to that later again. But, so you start seeing the gist, a skill not only contains context, it can contain scripts, it can contain documents, contain bunch of things. So, is this kind of the package format?

**15:58** · Probably, you know, plugins could now also contain MCP, but you see there's like a standard coming in.

**16:05** · Skills all of a sudden, when that came out, all the coding agents said, "We're supporting this as almost like a package format for people to distribute their context on."

**16:16** · And then when I have one piece of context, I have dependencies. And I'm sorry, but also with context we're going to have dependency hell.

**16:25** · Right? I I'm I'm I'm going to download this for front end, and maybe it's conflicting what is in the React context package. And so, you start having to deal with that as well. So, you start seeing also uh packages that's uh mirror your library versions, your code ver like your context versions, and kind of pull that in as well.

**16:48** · And of course, when we have packages and people are publishing things in registry, we need security.

**16:53** · Right? Open claw. Thank you for that.

**16:55** · Like everybody all of a sudden became aware that we need more secure things because we are able to run things on our laptop that are not and coming from strangers, right? So, Snyk has a way of scanning context, right? It's doing some credential handling. It's uh exposing some third-party pieces. So, you start seeing the scanners on the context as well.

**17:22** · And then when you think about security, who actually built the skill? How was it built? With what model was this built?

**17:30** · So, all kind of capturing what we learned in maybe with packaging, like the SBOM, is kind of the AI SBOM, like the packaged of context that we're putting in.

**17:42** · So, you've seen still on the path, right? You generate, evaluate, distribute.

**17:48** · Let's move into observe.

### Observe: Monitoring and feedback loops

**17:54** · When you are making libraries off skills and context for others, and I don't mean copy and paste this over Slack or something.

**18:03** · But, when you actually want to maintain this as something somebody else can use, similar to a library, um when they start using that, how do you get feedback whether that still works?

**18:15** · Now, a great place to get feedback is actually by looking at the agent logs.

**18:21** · So, imagine developer one coding on the project, and the agent is not doing what they want.

**18:33** · They could put this into their context, which is great, right? Okay, let let me do the TDD almost like, you know, I hit a problem. It's not TDD, but you get my gist.

**18:43** · Um or what if we at a team or an organization scale would look at the logs every time an agent said, "We're missing this piece."

**18:54** · And we surface that and say, "If everybody's missing this piece, we should create context for this."

**19:00** · And then we distribute the context to everybody, and all of a sudden the impact of improvement is for everybody.

**19:07** · Luckily, like the agent and D, there's now our standards becoming for logs. So, we can read from logs, and that's part of our feedback channel to see if the agent is actually using or missing some of the context.

**19:24** · Any feedback you get on a PR that's not complete, that's feedback on your context because that PR was created with certain pieces of context. If you say this is not correct, you can kind of keep arguing on the PR, or you can just say, "Let's improve the context." So, the next iteration actually improves, uh and you don't hit that same problem again.

**19:48** · What about running code in production that was generated from context.

**19:54** · And that's not correct because yes, we do our PR reviews and we say thumbs up, thumbs down and we give the feedback, but the actual feedback is also in production when it's running.

**20:04** · So, this is a tool that actually instruments your code, pushes it out, it's almost like a wrapper, it pushes it out to production.

**20:12** · When it fails, it says, "These pieces of code were changed and were failing.

**20:17** · Hey, in this case, input, output, it did something wrong.

**20:22** · Can we create a test case for this? So, the next time we don't hit this again in production?"

**20:29** · Feedback loop.

**20:31** · Now, these are all kind of pretty trivial like missing pieces of context or improvements.

**20:38** · But, if you run agents and the equivalent of scanning maybe, you know, in the CICD is you need to make sure when it's running in production, is it not doing strange things? So, we need kind of a way of looking at that.

**20:53** · Now, I've been toying myself with uh you know, sandboxing agents and it is a very resourceful at finding things.

**21:03** · I like, okay, you know, run this thing, try to figure out like anything useful to get break out of the system.

**21:11** · And okay, it uses my environment variables. Okay, stupid. Let's let me remove the secret. Let me look at your memory files. So, you have to really make make sure that like whatever it's doing, you can have a way of tracing this as well.

**21:28** · And uh apologize again for kind of the slide, but the gist is we can have a sandbox where the agent runs inside.

**21:39** · But, your code agent by default without any restrictions loads your agent.md, you load your skill.md.

**21:49** · Like, nothing is blocking that.

**21:52** · So, if you download this, immediately it's loaded.

**21:57** · So, you can't filter that with sandboxes. You need to have another way.

**22:02** · I call that a context filter. Think of this as a web application firewall that just filters out any patterns or prompt injections or stuff that is coming in directly in that piece.

**22:13** · And if you take that, there's a lot of talk here as well on harness engineering. Harness engineering itself also has this kind of full observability, looking at logs, looking at traces, looking at feedback.

**22:24** · So, it's kind of, you know, useful for training pieces, but as much useful for running your own pieces well.

### Conclusion and the context flywheel

**22:33** · Those were the pieces for me today.

**22:36** · I would say for a lot of people, there's like create context, test context. Think of this as your library authoring tool loop.

**22:47** · And then when you push this into the enterprise, there's an organizational loop. Hey, I made a library, somebody else is using it. I'm looking at whatever that's useful, whether that's still working, whether that's still working for all the other pieces. So, that's kind of like the kind of improvement almost like sonar CICD model for context. And then you're currently probably doing a lot at the individual solo model, you're improving, you're honing, crafting your own kind of markdown.

**23:17** · What if you start doing this more with your team? Make that a reflex. If it's missing, add some context. What if you put that out to a team of teams and you start having a flywheel, you know, if you fix it here, the other team can reuse it and and that's kind of like, you know, scaling things out into the organization as well.

**23:39** · And so, there's a lot of talk about LLMs and coding agents and I all love them, but the way that I see it is they're just the engine.

**23:48** · If you give the engine the wrong fuel, which is context, they're not going to perform. So, and you can't do anything on the LLMs, at least not me, right? I'm just using the coding agent, I'm using whatever they give me, but I can optimize my context uh and that's I think the message uh doing this more in an engineered way than just copy and pasting things and hoping for the best in there.

**24:13** · If you like this talk, connect on LinkedIn for the slides. Uh give me some feedback, good and bad.

**24:20** · If you want to try Tessel where we implement some of the pieces of this, uh have a go.

**24:26** · And if you're also interested in another conference, I know, you can never have enough conferences, uh visit uh AI DevCon, which I curate the content for uh here in London first and second of June.

**24:38** · And that's it. I can maybe take a few questions.

**24:42** · \[applause\] Any questions?

### Q&A session

**24:52** · Sure.

**24:54** · So, I was wondering if you have any thoughts about like more exotic forms of context like I don't know, the traditional ones. So, for example, one of the things I'm working on is automated system for uh scoping out architectural problems and like trying to create hard definitions for them so that you can feed that to the agent and, you know, create actual objectives uh tests.

**25:13** · Cool. Yeah.

**25:14** · Microphones.

**25:16** · Um and one of the things I've been testing out is like the ability to create consistency as a form of context or as a form of eval.

**25:23** · So, um given this rough like very loose definition of what the plan is, if can you put that if you try that agent system, turn that into a really crisp definition, and you just have that done in parallel, how often do you get the same crisp definition? And if they're all over the place, then the original definition was so poor, you need to like go back to base principles or to an architect. But, if they're all the same, then it's probably a pretty good definition and you can carry on with the downstream process.

**25:49** · So, I think it's like besides just code and typical evals, um any other sources of context for generating context that you think is useful?

**25:57** · Um I don't have maybe a a specific answer to your like exotic case, but uh I would say that maybe the piece that people are underestimating is that once you you know, you thought you were going to save time by writing actually your context uh instead of all your code, but if you take this rigorously, you're going to spend time on writing the right evals. Right. And that's kind of like, you know, a lot of work to kind of because now you don't only have one prompt that you're trying to get right.

**26:27** · It's like all the prompts of the evals and that like if people do almost like a like the more advanced people, they almost have their own process and they they build their own process on top of like for building the right evals on your business case as well. So, yeah.

**26:44** · Good question. Thank you. Any other questions?

**26:49** · If not, I'll be around. Um say hi. I'll also going to be at the Tessel booth. So, thank you very much and I'm going to make space for the next speaker. Thank you.

**27:03** · \[music\]