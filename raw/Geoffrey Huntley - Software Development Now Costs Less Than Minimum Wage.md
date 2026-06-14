---
title: "Geoffrey Huntley - Software Development Now Costs Less Than Minimum Wage"
source: "https://www.youtube.com/watch?v=6zQTQ4iVaKg"
author:
  - "[[PyCon Lithuania]]"
published: 2026-04-24
created: 2026-06-07
description: "Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=6zQTQ4iVaKg)

## Transcript

**0:03** · Give me a moment to get this all set up.

**0:05** · Um this is my first time to the Baltics.

**0:09** · Um and it's actually quite lovely.

**0:12** · Um I've never been to this side of Europe before.

**0:16** · So when the opportunity came across to uh share some things that's happening around the world, um the opportunity I was like, yeah, okay, I'm just going to come. Community conference, do the talk.

**0:27** · I am currently 35 days on 95 days of travel around the world giving this talk.

**0:35** · And one of the thing that is for sure is different societies and different cultures evolve at different paces.

**0:43** · And while something may be true or could be true in one market and one culture, doesn't mean it's going to be true here.

**0:52** · And to back up uh uh previous speakers, as confident I may seem, I don't bloody know.

**1:01** · I don't think anyone knows where this is going.

**1:05** · I'm old, a little bit crusty, and I'm able to pattern match.

**1:10** · And the same time I've uh I've burned a lot of tokens.

**1:14** · In the last 12 months, I think I've burned close to $800,000 US in tokens.

**1:20** · Um and that's allowed me to see some things.

**1:23** · Um and burning those tokens has allowed me to uh create some things. So this talk is called software development now costs less than minimum wage.

**1:36** · I'm going to be using the word software development here.

**1:39** · It's a little bit provocative, right? Software development is essentially coding.

**1:45** · There's always has been a difference between coding and software engineering.

**1:50** · Always has. But things have changed.

**1:55** · So this is me at Atlassian 2 months ago at a cursor meetup.

**2:05** · And I was just uh giving a talk very similar to this talk and explaining how the unit economics of software has forever changed.

**2:14** · It turns out if you run Claude or any of the frontier models in a loop, software development now costs $10.42 an hour.

**2:27** · You can autonomously build software in your sleep.

**2:31** · If you don't think that's possible, go to YouTube.

**2:35** · Search for all the people who are not software developers using the Ralph Wiggum loop, and they're building things. They're going to sleep, they're waking up, and they're going, "Yo, check out Ralph loop. It's it built me this Discord bot."

**2:48** · It's kind of weird, and it's left me kind of like sick and worried that software is kind of forever changed.

**2:54** · Um Ralph, if you're not familiar, it's uh if you're using Claude code now, cursor co-pilot, it's built in.

**3:03** · It's a technique for managing memory.

**3:06** · It's a technique for managing memory.

**3:11** · And um I'm wearing this a nice little hat because it's kind of a counter talk.

**3:17** · This one is going to be a little bit gloomy, I'm afraid. So I need something \[snorts\] that keep me a little bit happy.

**3:24** · You see, my kind of oh \[ \_\_ \] moment in time, sorry language, I am Australian, started about 2 and 1/2 years ago.

**3:36** · Um I ran um I started playing around with memory management with these LLMs.

**3:43** · And these these LLMs used to be how would I describe it? They were like wild horses.

**3:50** · And it required a great deal of skill to actually tame these models and get good out outcomes from them.

**3:58** · But since doing these talks and where we are now in in the time that's gone by, these models are like they come factory de- they come with factory defaults and they just work. You don't need to tame the horses anymore.

**4:16** · They just work.

**4:18** · And the skill floor is completely just dropped. Um So let's get into it. So this is my 6-month recap. If you're not familiar with my writing, um this is where I was similarly going around the world and asking people to invest in themselves, please pay attention. Things are changing.

**4:37** · \[snorts\] When I first discovered Ralph, I actually didn't publish it immediately. I sat on it for 6 months, and I went around giving talks and asking people, "Build your agent. Have you built an agent? This is how you build an agent. This is now a fundamental skill for software development."

**4:56** · And um the rest is history. Um I ended up in Silicon Valley, showed uh the memory management technique to some folks in Silicon Valley, and next thing you know, we've got entire batches of Y Combinator startups all using Ralph. And it went explosively viral in January this year. You see, the unit economics of business have forever changed.

**5:22** · What does it mean when software development costs $10.42 an hour?

**5:26** · And keep in mind this was the pricing for Sonnet 4 5. We did this calculation over 8 months ago. If you take the same techniques and run it on a like an alley model or something from ZAI, it's cents an hour. Right? This is we're entering in really interesting territory here, folks.

**5:50** · So what does it mean when \[sighs\] if your identity function is to be a software developer, and anyone can now be a software developer?

**6:01** · Like a few people have introduced themselves as Python developers. They've been doing this for X years. It's part of their identity function. It's like a job title. It's part of like the psychological who they are. And AI has essentially just erased all that. And it's enabled people who are not software developers to write software. Here I am at the same cursor meetup.

**6:29** · There was speakers after speakers after speakers. These were designers, product managers, everyone. They're they're just talking about how they're writing software. And they're having the time of their lives because they haven't they don't have the psychological wound. They never actually had something loss. They don't have a loss function. They just got, "Hell yeah, this is cool. I can build stuff."

**6:55** · And uh 2 weeks ago when I was in New Zealand giving this talk, just before that, I did a little tour to Lord of the Rings Hobbiton.

**7:06** · And uh the tour guide operator, it was like, "Hey Jeff, what do you do?

**7:10** · What's your name? What do you do?" And I was like, "Oh, I do AI." Next thing you know, he's yakking his head off talking about cursor and all the things that he can he's building with it as well. He's not a software developer. He's a tour guide for Lord of the Rings.

**7:23** · \[sighs\] Oof.

**7:25** · You see, now everyone is a software developer. Everyone is now a software developer because cursor co-pilot, any one of the the coding harnesses out there, even lovable, right? It's enabled everyone to become a software developer, which means the unit economics of business have changed. But it's more fundamental than that because societies have been structured on a scarcity of knowledge. We charge money because knowledge was scarce.

**8:02** · The more scarce the knowledge is, the more money that we could charge. Right? And this is how we structured our societies. This isn't uh this is knowledge work.

**8:13** · \[snorts\] And we've gone from a knowledge scarcity economy to now a knowledge abundance economy. AI stands for amplified intelligence. It like amplifies what you already know. So anyone in the room who is a software engineer will get a better outcome than the tour guide from Hobbiton because they know what to prompt. It amplifies what you already know.

**8:40** · My question is, how long does that advantage last before someone encapsulates that you should use property-based testing, you should use Python types, all the rest, up as a skills file?

**8:52** · As soon as it's a skills file, next thing you know, that that tour guide operator is going to be using that and getting similar outcomes. But it's not just software development. This is essentially all white-collar work. The same thing if you apply it to the legal profession. And all these different knowledge professions that have been based on the idea of scarcity, it's now abundance.

**9:16** · Ouch.

**9:17** · \[snorts\] Now you might have seen this.

**9:21** · It's about 2 months ago. Block lays off nearly half of its staff because AI. Its CEO said most would do the same.

**9:31** · Now, it's tough.

**9:36** · I remember being at Atlassian talking about how if uh their customers start doing layoffs similar to how Block is doing layoffs, then it makes their unit economics with business unstable. Because if you make money on SaaS, on charging per customer, and they start doing layoffs, then that that that creates a cascading domino effect for the stability of your business. Now, my personal take here is Jack is right. Well, with some nuance.

**10:09** · I don't think AI is factored in yet. I think what we're seeing right now with the current headlines is classic they've over-hired and they're making corrections. And the stock market is rewarding cutting. I don't think the true implications of AI of like layoffs due to AI have started yet. That's my honest take. You see, for the last 2 months, been traveling around, catching up with venture capitalists in New Zealand, Australia, San Francisco, and Korea.

**10:48** · And I've been pitching this idea.

**10:51** · Why does someone need to raise seed capital venture capital anymore?

**10:58** · If it's just a five-man show now. You see, venture capitalists don't even know if software is still investable. If you think you've been disrupted downstream here in like doing software development, understand upstream in the funding department, they're not even sure their business model is still viable. This is the This is the topic the talk of town right now.

**11:26** · Is trying to figure out this thing. Is software still investable?

**11:32** · Ouch. So, there's this disruption at our level and there's a disrupt a disruption at the finance level up above as well. So, every story needs a frame. So, for absolutely no particular reason at all, I'm going to pick SAP Concur. Um I've been forced to use it once in my life and I did not enjoy the product experience. Expense management is never good or easy or fun, but their software is not great at all.

**12:08** · I was just surprised to learn that they have a fixed overhead a payroll of 6,800 people building payroll software.

**12:18** · What?

**12:20** · How many people does it take to change a light bulb?

**12:24** · So, we think about it. Business has been designed like this since the 1970s or even before. What we do is we get a whole bunch of builders and then we have a a management layer. Also known as the coordination layer. And I think that era is at least in the SaaS space has come to an end.

**12:55** · This is going to be the year where we figure out whether it actually is happening and what the implications of AI is going to be. Again, I don't know where this is going. This is how people are thinking. A question for the room.

**13:12** · How long does it take to transform 6,800 employees with literacy of AI?

**13:20** · You see, the way I look at AI, AI is kind of like a guitar. You get good at a guitar through deliberate intentional practice. But everyone is kind of like forcing guitars down on the employees right now.

**13:36** · Um and some of the thinking now is like, well, how long does it take to transform all this staff?

**13:45** · Like 3, 4 years? More?

**13:49** · Is that enough time?

**13:51** · The other side of this thinking is, why would you?

**13:55** · Why would you transform your staff?

**13:59** · Right? So, this is what we've got right now. We've got um the guitar has been forced down onto all employees around the world and it's like, pick up the guitar and play. Literally right now, all employee corporations just trying to do pulse checks whether you're curious.

**14:19** · Will you pick up the guitar and play and get good at it or not?

**14:24** · And that's the first binary decision whether you make a cut or not if they decide to make cuts.

**14:30** · Have you been practicing? Have you been learning? Have you been curious?

**14:36** · Cuz they're thinking like, why would I transform 6,800 people?

**14:41** · AI means I need less. Because we know small teams get better outcomes. If anyone's organized a party before in their life, they they know the complications of growing a friendship group or inviting too many people at to a party that don't know each other at once. It just doesn't work. The more people, the more connections, the more complexity, the more drama. The same is true in organizations. You see, smart founder founders understand this.

**15:14** · Here's a tale from a founder in New Zealand. They started making adjustments back in 2023. You see, adjustments with workforce that you might be hearing in the news now, they're they're like the they're not exactly the laggards, but like it's not new. Like smart founders have been making these adjustments years ahead of this cuz they've been tuned in and paying attention what's going on.

**15:42** · \[snorts\] We're smaller, but effectively we're smaller, but we effectively cut 2/3 of our uh our staff by telling our board that we wouldn't backfill in May 2023. It was the best decision as I got rid of all the people who are sick of hearing about AI. Get rid of the detractors. Right? Get rid of the negative energy within the company. So, they've reduced from 60 people down to 20 people.

**16:13** · And they're getting 30 times the output what they did with 60 people. Now, I know this founder and it's true. You see, one of the hardest things about AI is it's kind of been rammed into the world non-consensually. It's just you have no choice in it, really. Um if you want a choice whether AI gets used or not, uh it really comes down to find a employer that speaks with your values or start your own company.

**16:51** · But keep in mind, there's never been a market for artisanal high-quality software ever. So, it's really important that you put your chin up.

**17:05** · Get through it.

**17:07** · Get through your loss function. Go through your five stages of grief because artisanal hand typing of code is over, folks. We now have the Miter saw. We've got the CNC machine. There is still a place for typing code in an IDE. That place is at home. Not in the workplace.

**17:30** · You see, this is going to be really tough for some people. You see, for some people, they've spent years doing game of friends activities within their organization to get where they are now. The middle management coordination layer. It's all going to be for nothing. It's all going to be for nothing if this year we see what how it pans out in the current trajectory and it's all going to be for nothing.

**18:00** · You see, in the org chart above, consider what is the value?

**18:06** · What is What is What is the coordination layer do here in the organization?

**18:11** · What value do they provide to the business?

**18:14** · If the value that you provide to your organization is a task, well, guess what?

**18:22** · AI does tasks really well. If it's summarizing information and coordinating and disseminating information, AI does that really well. So, for the middle management layer, I'll have to say, if I'm not sure how the European market will develop, but at least in the Silicon Valley market right now, if you're a middle manager, you are screwed. You are utterly screwed. Get back on the tools. Get back on the tools. You're first in the firing line.

**18:51** · We're starting to see ratios of 50 engineers to one manager now.

**18:57** · Okay?

**18:59** · That's kind of sucks. Can you imagine like how much time these people have spent doing Dilbert activities to get where they are?

**19:08** · And uh if you were a founder and this was your own company, coming out of your own payroll, why wouldn't you cut them?

**19:17** · Right? Why wouldn't you?

**19:19** · If you can do less with more and it's your own personal paycheck in your own wallet, your own funding, why wouldn't you cut them?

**19:27** · AI enables a path towards this reality. We're starting to see this transpire. You see, there's a new class of company that's kind of come into existence over the last 6 months. I call them a model first company. A model first company is a company that to use an analogy of woodworking again. In woodworking there's a there's a saying that you should work with the grain of the wood, not against the grain.

**20:02** · At a model first company, they just like hey, the frontier labs are using rust, so we should use rust cuz they're dogfooding it. So we're just going to use rust, which means it's going to be good.

**20:14** · They're also using Python, so good thing Python here. They're dogfooding Python, so Python's on the on the track. But if you're a corporate or not a model first company, you might be using Java or Kotlin or what else have you?

**20:28** · Or .NET. The frontier labs aren't dogfooding that. So all of a sudden, they're not actually experiencing what they're shipping, and you're just a anomaly on the benchmark, so you're kind of fighting against the grain of the wood, where the grain of the wood is what the models want to do. And you're going to extend this a little bit even more further.

**20:48** · You see, a model first company focuses and has designed around shipping and leaning into the latent capabilities and space of what the model wants to do.

**21:02** · Whereas a corporate will spend all their time trying to context engineer and make the LLM do all the fancy stuff that the corporate needs to do, but all the corporate stuff, if you look at it from the right lens, is \[ \_\_ \] Right?

**21:16** · So, I think we're going to get two classes of companies, a model first company and a corporate. I'll expand a little bit later. I want you to consider how long it take to transform a organization 6,800 employees 3 4 years to transform. And like think about the staff and morale and all these things if they do do layoffs. Like it it it's brutal to the culture of a company.

**21:47** · Um a verse a model first company. And this is what we're starting to look at as a prototype, the idea of a model first company. The idea is you just have builders.

**22:00** · Just builders.

**22:02** · You have a really good designer, a really good product manager, a really good engineer, and you focus on automating your job function. That's your job. It's not writing code, it's automating your job function. And that's what an AI manager is. Instead of programming the code, you're programming the agentic agentic loops that automate your job function. They're working with leverage. This is how companies have been built for the last 6 months in the valley.

**22:34** · You see, if we rewind time to Christmas 2 years ago, it was pretty clear to me where things were going. Back in 2024, the models were already good enough to cause societal disruption. But they were like wild stallions. It quite it required a lot of skill to tame to tame them to get good outcomes. But fast forward now and the Christmas um we had we had a another oh \[ \_\_ \] Um there's a couple of things.

**23:13** · I think we can actually time these moments in society based on holidays. Like there was nothing too special about December. The models had been getting better, but what happened was people actually had the time to sit down and play and realize that oh crap, everything's changing.

**23:37** · So, regardless of the technological rollouts and advancements, I think we're going to see every holiday break, Christmas, Easter, all the rest, is we're going to get a rollout event of oh crap moments in time for folks.

**23:55** · \[snorts\] You see, to stress this point, the people who are getting the most out of AI for the last 2 years have been putting in deliberate intentional practice. This morning, I had a Zoom call at 4:00 a.m. to San Fran. There's a community of uh hyper engineers. To join this community of hyper engineers, you need to be spending $20,000 a month on the tokens.

**24:26** · And it is vetted before you join. There are people out there building with leverage like you would not believe. And it they're doing absolutely absurd things. And they're able to do that because they've put in deliberate intentional practice. They they learn the patterns and tricks. They've developed an intuition on how the models work. It's not like you can just drop a guitar on people and expect them to make discoveries.

**24:53** · Like it it requires a deliberate intentional practice and a curiosity. Again, musos don't just pick up a guitar and experience failure and go, "Well, it sucked." And the guitar will always suck.

**25:11** · No, they they they deliberately practice. They go, "Is this a banjo? Is this a ukulele?

**25:17** · What is this?"

**25:19** · And you can think of a banjo or ukulele or different type of guitar would be a different model from a different provider. What is the what is the differences between all the different models?

**25:30** · These people last 2 and 1/2 years have been developing a taste and opinion. They know which models do what, when they're good for what scenario, etc. And for the people who haven't been paying attention, this is bad. So, I think the uh world is now divided in a pretty brutal K-shaped economy, where we got the model first companies up there on the top left and the corporates who are saying AI is not real.

**26:04** · In Australia, there's still companies that have outright banned AI within the organization. That is wild. I guess there's going to be some similar here as well. It's kind of like banning like GCP or AWS. Uh there are valid reasons for it, but this does create problems for uh retainment of employees. You see, you see, a model first company is kind of like a apex predator that can work on margins.

**26:49** · The idea that you could have a five-person or 10-person company able to do leverage of 100 people.

**26:57** · What happens when that person or that company enters into the market and directly competes with an incumbent that has 1,000 people on the payroll?

**27:07** · So, I don't think that the layoffs are going to be like companies want to do layoffs. I think it's going to be a natural like we've got these really lean companies working with leverage using AI. They're going to attack the the moats of the corporate companies, and the net net result of that is they're going to have to do the inevitable. See, it's cuz it starts slow.

**27:31** · It starts slow.

**27:32** · This is kind of the the exception right now. The idea of a model first company 6 months in. But the model first companies are the building with the with the grain of the wood. They're focusing on the workflows. As soon as the models get better, their workflows get better automatically. They're building with latent space. They've got less people. They can be more nimble to classical startup type things.

**28:02** · And I think as the models get better, what we get is slope on slope acceleration, where instead of this being like a 10-year horizon, time is compressed. If you're a traditional company, you wouldn't normally worry about startups because startups take a long time to get to market to attack you.

**28:22** · Um here as the models get better and the workplaces get better and practices get better, and as they run leaner, I think the timeline gets accelerated. It's compressed. It's not like 10 years. It's a couple years type things. If you look at the revenue that's coming in for these model first companies right now, it's it's parabolic. It's crazy. It's absolutely crazy.

**28:48** · Now, one thing I've also been thinking about is if you understand what's going on and you work at a company that's banned AI, and you and you care about providing a job for your family and like income for your family, why would you stay at that company?

**29:10** · Why would you stay at that company?

**29:14** · So, what I think it happens is a couple of the best employees leave the company and they go and they form their own business. They come back and they attack their previous employer and operate on leaner margins. And over time, this becomes the norm. Now, the real question is, unfortunately, for the people who do get displaced by AI.

**29:41** · Notice I'm saying do. If from my from my point of view, it's inevitable that there will be displacement by AI. But it hasn't started yet. Where do they get jobs? They needed employment. So, let's take the engineers at Block who are great engineers, didn't make the cut. They're going to need a job. Well, there's a resume pedigree there. You worked at Block. So, they're going to go to the next employer.

**30:12** · And then they're like, "Okay, that employer is going to ask him to do what?"

**30:16** · They're going to ask him to implement AI and automate the job function.

**30:20** · What happens to the people who don't make the cut at that company?

**30:23** · This is where I'm concerned where it could get recursively feral really fast.

**30:30** · Really, really fast.

**30:34** · I don't know.

**30:36** · This is what concerns me. You see, when you understand how real AI really is and you really start playing with it and actually start building your own agent and then you build an agent on an agent type topics and you start automating job functions.

**30:59** · It it kind of changes you. It kind of changes you. I I'm I can walk through a conference and see a vendor and go, "Are you dead or alive?" just by asking the business unit metrics type topics. It really changes you. It's really weird. Um what I can say to uh folks is there is a difference between an employer self-harming themselves and an a employee self-harming themselves.

**31:31** · I'll expand.

**31:33** · All right. If an employer has banned AI, they're kind of self-harming themselves in the end in my point of view. Maybe some industries are regulated and they shouldn't be. That's fine. If you're in SaaS and you banned AI, you uh really cocking up. Really, really cocking up. Now, if you're not investing in yourself and you haven't built your agent and really getting good with these topics, you actually self-harming your employability.

**32:05** · I I I can't be any more straight up and down than that. You see, as I've been stressing in my writing for for the last year and a half now, employers trade employees trade time and skill for money.

**32:24** · All right.

**32:26** · If a company is having issues with AI, that's a company issue. It's not an employee issue. Right? If a company is having problems adopting AWS, that's a company issue.

**32:41** · You see, there was there was there's times and tails. I guess there's people in the room here who've moved on from an employer because they were using uh they were using ESX and they wanted to get cloud knowledge. They seen the industry had moved and they want to remain relevant so they continue to trade time and skill for money. The same thing's happening here, but the the pace is accelerated and compressed in my point of view.

**33:11** · And I'm really deeply concerned that if people do not invest in themselves and learn some of these fundamentals and a failure to upskill with AI or play with the guitar, then they're basically self-harming. I don't want I don't want to see that at all.

**33:35** · \[snorts\] Closing ponderous.

**33:38** · Closing ponderous.

**33:43** · Folks, this is my own personal journey with AI back when I was a tech lead at Canberra.

**33:51** · With 2,000 engineers, I went through my personal oh crap moment and I enumerate for the organization and I asked people, "Hey, have you seen what I'm seeing?"

**34:01** · And it roughly maps out like this. And I guess you could probably see yourself here or somewhere here on these people development stages. I wrote this uh a year and a half ago. It really starts with uh "It's not good enough. Prove it to me it's not hype."

**34:17** · That was me.

**34:20** · I was that I was that person up there 2 and 1/2 years ago because a junior was playing with uh with these tools and they're just going, "Wow, it's amazing." I just dis- dismissed it as hype. I tried it in GPT-3 days and it was not crap. I wasn't paying attention.

**34:38** · Wasn't paying attention.

**34:39** · So, please pay attention. So, you start playing with it a little bit more and you're experimenting with it.

**34:45** · And the more you experiment with it, the more you get closer to the middle. I was like, "Oh crap. Will I have a job in the future?"

**34:52** · Now, the problem is at most employers around the world right now, there is no bridge. They just push the guitar onto the organization and everyone's having this collective oh crap moment back in December. A lot of fear, uncertainty, and doubt. And there's no bridge being made for people. So, if you understand what's going on, be that bridge.

**35:17** · Right?

**35:19** · Now, you might notice a line here. You might notice the line here. This is kind of brutal. I don't hire on the left side of the line anymore. There's a pool of software engineers for the last 2 and 1/2 years who've been curious, who are building agents, who are absolutely token maxing right now, and are exceptionally good at what they're doing. It's not just engineers, it's product managers, there's sales people, etc.

**35:46** · Like, I saw the matter hands that went up who built \[snorts\] an agent. Congratulations. For the people who haven't built an agent, please go home and build an agent tonight because you just got mugged by a 13-year-old who just built an agent. Farage, as you just saw, built himself a coding agent. You see, there is there's two categories of software engineers now. You got this brand new computer.

**36:11** · You got the consumers who are using the the tools every day and they're switching between all the tools every day. They're fashion fashion chasing because they don't understand the inner mechanics of an engine.

**36:24** · Right?

**36:25** · An engine being AI or a coding agent. The only reason you'll understand how an engine works is if you disassemble one, you assemble one.

**36:36** · Farage did that.

**36:39** · And this is what we're finding is juniors don't have this loss function. They don't have this identity crisis. They have no loss. So, they just go forward and mug. So, I'm not that too concerned about juniors and their place of like raising juniors and the continuation of our profession.

**36:58** · I'm really concerned about people who are stuck in the in that middle phase of oh crap, what will I need to do?

**37:05** · There's still time. Different markets work at different paces. But, there's really two uh personas now.

**37:13** · There's the uh I'm using a a cursor and these all these coding agents and the other one is "Yeah, I built an agent. I built many agents. I know the limitations. I've got taste. I know which models work. I know what what you got to do to a model to get it to work. They know how to juice it. They don't know what a temperature is. They know what the right temperature is for the right type of thing. They built this intuition on how it works."

**37:37** · And they've rebuilt an engine, they know the components of engine, and they can automate their business function. The folks on the top right are absolutely banking right now.

**37:50** · Absolute bank.

**37:53** · Whereas uh the people who are just consuming, um AI also stands for something else as well. It stands for actually India. And I don't mean that in a a racial tense. I mean that in the classical software off-source uh outsourcing sense. We're starting to see this happen with Silicon Valley.

**38:15** · If you're pulling in 500 grand a year US and you're just sitting there scrolling TikTok while like Claude Code does its thing, what's your value?

**38:25** · What's your value?

**38:27** · You can pay some person in Bangalore 100 a year US to get the exact same result. So, it's really important to go up the power domain, not to be a consumer, to actually rebuild an agent, folks. Because uh software outsourcing is back in fashion again. You see, if I was ask you what a primary key is, you should know what a primary key is.

**38:52** · But, if I was to ask you, "What is an agent?"

**38:57** · If I was to pull you up on up on stage and like, "Hey, could you teach someone in the room how the state machine works within an agent? How does the state machine work for a sequence diagram from the client to the server? How does that all work? How deep can you get? What happens when you turn a computer on?"

**39:17** · Unfortunately, not enough people know how to do this. Folks, that website there, ghuntley.com/agent, it goes to a free workshop. It's three under lines of code is the highest ROI you can do to improve yourself and give you surety of what your next steps are. If you're stuck in fear and paralysis about AI, just build your damn agent. And then once you got your agent, here's the trick. Use the agent to self-improve itself.

**39:50** · It's a little chat app. You want a web app? Use the chat app to recursively convert the chat app into a web app. And then all of a sudden you got a web-based coding agent.

**40:01** · Simple.

**40:02** · Get a taste of building with recursive latent space. And it's all really silly, folks, because like the big scary boogeyman that everyone's scared about with AI is just literally a for loop. It's like a while true for loop that continually allocates to an array, and that array gets sent sent off by a HTTP API. And there's no memory on the on that API, so that's why the array continually expands.

**40:32** · And that's the big scary boogeyman that everyone is scared about. It is really that simple. Just learn the loop. Learn where it's not great, where it is good, develop a taste. You know what I mean? Like if someone is a brewmaster of beer and they've never drank alcohol in their life, I'm not drinking their beer. Like consume a little bit, like and develop a taste, folks.

**41:00** · Okay, closing ponderous. Um code is no longer an input. For a long time we've had our identity function as we're monkeys at typewriters, we're typing things. Hell, we even make glorified uh glorified interfaces for our typewriters, IDEs. Like I don't know, and the people around me, we we we haven't opened up an IDE in a very long time, folks.

**41:27** · Um it's just terminal agents all building abstractions on top that automatically ship software. Like the idea of software factories is a thing. Now one of the things I'm starting to think about is software is now really clay on a pottery wheel. Previously we've focused on engineering perfection or making sure it's right, making sure it's right, making sure it's right, because the old bugs take a long time to resolve if they get past the QA type thing.

**42:03** · Do they really now?

**42:04** · Think about it.

**42:06** · If you instrument your code base well with OTEL, you Sentry, or any one of these things well can't you just connect an agent to that Sentry alert to automatically raise a pull request to automatically resolve and fix that problem?

**42:21** · So a lot of these old things and how we're running our business and now invalidated. So software to me is becoming more like clay on the pottery wheel.

**42:31** · Get it done.

**42:34** · Get it right.

**42:37** · And make it better. We're still engineers, but like and we're applying engineer principles, but we're no longer front-loading all this time on making sure the code is perfect. We're focusing on business value and shipping for the business. We're thinking like business owners.

**42:56** · Now \[cough\] I've talked about this but there's some very unstable moats in business right now. If you're a SaaS company and you charge per employee like at Last Seen, etc. If their customers start doing layoffs then that it hurts your fundamentals and then etc. It's a very unstable metric. Anything that charges per human it's a very dangerous business metric right now. Very bad dangerous business metric. Instead, you should be thinking about changing some of the fundamentals.

**43:31** · This is hard. If you currently charge per human in established SaaS business, change your different unit economic is really really hard thing to do. It's a really hard transition to do. So a stable business moat would be anything like AWS AWS or cloud compute costs, \[snorts\] like utility meterage-based pricing. You see, for the future what we're seeing is like the cell now the majority of visitors to the Vercel website aren't humans anymore. It's agents.

**44:06** · So we're starting to see websites aren't really designed for humans anymore, they're designed for the agentic experience. They're doing SEO for agents. Um and you want to be designing in a way that agents can actually buy from your business. An agent isn't a human, so we need new financial metrics on how to operate businesses.

**44:27** · Oof.

**44:29** · Now there was an old saying that ideas were worthless.

**44:35** · Execution is everything.

**44:37** · This is flipped, folks. Ideas are now execution. You can literally just rip a fart into code code and get that outcome. So that's changed, folks. Anyone who is an idea person is now uh is now you can now ship something. The question is whether it has taste. Now that anything can be built, one of the hardest things to decide is whether it should be built or how it should be built.

**45:13** · I must say as much of a booster of AI that I might seem to be a lot of companies these days won't be able to adopt AI because of their entire workflow the workflow in their business hasn't been modernized enough to be able to adopt AI in the first place. There's still companies sending around uh links backwards and forward instead of links backwards and forwards, they're sending file attachments in it in Outlook.

**45:41** · Final.psd, final final.psd, final final final.psd. Like none of this stuff that's if they're heavy email-based culture agents are not really good for that type of stuff. So removing waste from your systems and processes is perhaps a bigger acceleration than AI itself. It's a precursor before a company can adopt AI.

**46:04** · For example, a form of waste, like what's the point of Agile anymore?

**46:09** · Folks? Why do we do daily stand-ups? Do we Do we do estimations? Planning poker?

**46:15** · That's always been like I never liked it, but it's definitely waste now. Like get rid of it, junk it.

**46:23** · What about um what about any form of management layer between the engineers and the customer?

**46:33** · Right? I'm not saying that you should get rid of the PM layer.

**46:36** · Right?

**46:38** · But maybe the engineers should become PMs and work directly with the customers. Cuz we used to be like that in the in the late '90s, engineers used to work directly with the customers. And we used to refine the needs of the customers to determine what's built and we had ultimate accountability for what was built and how it was built.

**47:00** · So removing a lot of waste in organizations is going to be a bigger accelerator than AI itself, I think. Again, it's going to be really hard, folks, because uh I like to say that AI is a eraser device of identity functions. Someone goes, "Hey, I'm a .NET developer." I don't care. You're a Python developer. I don't care.

**47:27** · You go, "Hi, my name is Jeff." And they go, "Hi, yeah, I'm I'm I'm like Bernard." And I'm like, "Hey, Bernard." He's like, "Oh yeah, I work at this company this many years and all this." They lead with their identity function. Hey, we we even have identity functions of like, do you use Emacs?

**47:44** · Vim?

**47:45** · JetBrains?

**47:47** · Right? We've got these subculture identity functions that like who we identify as. Doesn't matter anymore. It's been erased. It's gone. But it's not just editors, it's programming languages. You should be able to hire a good software engineer, test them on the fundamentals and go, "Sweet, you're now a Rust developer." And they they go, "I don't know Rust." You go, "Well 48 hours you will be." Like AI is the ultimate learning tool as well.

**48:13** · Uh AI is the ultimate learning tool. If someone says, "Oh, I don't know this, I'm not going to learn this." they're self-harming their employability. Like literally now if software engineers are fungible in the sense of like between the identity functions but the quality of the software engineer is not. But that's always been true. There's a wider pool for companies to pick from. It's no longer this software engineer with his X years of Python anymore.

**48:41** · It's this caliber of software engineer across all the languages and now you're doing Python. Folks, I want you to um kind of put your own life jacket on before attempting to assist others. And that is really simply build your damn agent, folks, please. Build your damn agent. And then once you have built your own damn agent, teach someone else how to build their own agent.

**49:10** · It's really that simple. We're going to get the mentoring mentorship going again. If you work at a company that has banned AI you should leave that company.

**49:23** · Flat out.

**49:25** · If they ban AI, you should leave that company right now. It's \[snorts\] going to be really interesting to see how this all pans out, folks. It's going to be a really interesting year. You see for a lot of people they haven't realized that AI is at the door knocking at the door because AI is tunneling under their house. If you for you coming here today means you know about AI.

**50:00** · You know about how real it is. You know you can see and taste the fear of disruption and what's going to mean for yourself. Go on the street, have a conversation with people about AI. They don't even know what's going on. So all I can ask is you tap someone on the shoulder and stress that they should play with this. They should invest in themselves and pay attention.

**50:23** · Because the worst thing I would like to happen is for essentially wake up and it's like job losses and they didn't they didn't even know about the disruptive effects of AI. With that, thank you.