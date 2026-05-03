---
title: "Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor"
source: "https://www.youtube.com/watch?v=WE_Gnowy3uw"
author:
  - "[[AI Engineer]]"
published: 2026-04-30
created: 2026-05-03
description: "David Gomes shows how Cursor replaced a heavyweight WorkTrees feature with a lightweight layer built from skills, commands, and subagents. He walks through h..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=WE_Gnowy3uw)

## Transcript

### Introduction and the concept of markdown as code

**0:14** · Hi everyone. How you all doing? Thank you for uh coming today. Um I'm going to be talking about how markdown is basically the new code. Uh as TJA has already sort of previewed um we recently replaced a lot of code in the cursor application with just markdown just a skill and in today's talk I'm going to

**0:38** · share a bit of the journey of going from a fullblown feature with a lot of code a lot of dependencies a lot of complexity and tests into a much more lightweight streamdown version of the same feature effectively but just with a single skill.

**0:56** · Um, before I start though, I have to give you guys a little recap of git word trees and how they work in cursor. Now, if you haven't heard of word trees in git, they're effectively like um separate checkouts. And I'm sorry for the wide screen um but they're effectively like like separate checkouts of your repos that allow you to work in parallel. So different agents can be working on the same task at the same or on different tasks at the same time without um interfering with each other.

### Recap of Git work trees in Cursor

**1:29** · If you've never used this feature before in cursor, the way it works is that you can spin up an agent on an individual work tree. Um, and you will see, for example, the same file in two different work trees. And you can see that they look different because the agent is doing some work on on the work tree, but not on your primary checkout.

**1:50** · And anytime the agent runs commands or lints or anything it does will be isolated and scoped to that git word tree.

**1:59** · Um, with this feature, you can also um work even in parallel at the same time on the screen. you can have like these grids of agents working for you. Um, and if you say, "Hey, open a PR," the agent will open a pull request from that work tree with the changes that it produced inside that work tree. And one of the coolest things about this feature is that it allows you to give the same task even to different models at the same time and then compare what different models do on the same prompt.

**2:31** · So if you haven't heard of this, we call it best event and it's effectively a way for you to compete on on diff have have different models compete on the same task and then you can even preview the changes if it's a front-end um project you're working on. Uh you can um compare all the different visual implementations and then choose the one you prefer.

**2:55** · Now, if you have never heard about this all everything I'm talking about today, um I will also just say that it all came out in around October of last year alongside cursor 2.0.

### Complexity of the initial implementation

**3:10** · Um and when we initially shipped that, it came with a lot of complexity. Um we had to write all the code for creating word trees, managing these word trees, feeding them into the agent as context.

**3:23** · We also had to make sure that the agents were scoped and isolated and they could not escape the work tree they were working on. Uh we also have something called setup scripts which users can configure and run uh and and have cursor run them anytime an Asian starts operating on a given word stream. We also have the judging. So I didn't show you this before, but uh there's a little thumbs up icon on one of the models.

**3:46** · That's just a judge that we run um that tells you which implementation looks the best based on um different criteria. Uh and then we also had to make some changes to the harness uh and introduce some system reminders to help the agent stay on track in these word trees. And then finally, there's some cleanup complexity as well because people like to spin up hundreds of these word trees and then their disk sizes blow up and we have to help them by cleaning up the um the the word trees that stay behind.

**4:15** · Now, in our new implementation, the one that I'm going to be talking about today, we were able to get rid of most of these things. And in fact, I recently opened a PR uh removing this entire feature from cursor and it was a massive like deletion of of of code like I think it was around 15,000 lines of code deleted. The new implementation of the feature is almost as good as the previous one. um and it is much much more lightweight in terms of us to maintain it.

### Deleting 15,000 lines of code

**4:45** · Um and it even has some benefits compared to the previous implementation that I'll be talking about today. So how were we able to replace an entire feature with a skill?

### Implementing features with Skills and Sub-agents

**4:58** · We decided that there are two primitives that we could use to effectively allow cursor users to use word trees by simply leveraging two primitives. one is Asian skills and the other are sub Asians. So both of these are existing cursor features. You can learn more about them in our docs. Uh we have a page for skills and we have a page for sub Asians. And we realized that if we took these two things together, we could basically reimplement both the cursor work feature as well as the cursor best event feature with just markdown.

**5:30** · And this is a little video of how it works. So I can now as a user say slashwork tree and then I'll give it some task. I'll say fix a typo in the footer of the website and this agent will run in an isolated word tree and do its work there. So the way the skill is written is actually really simple. I can show you most of it.

### How the new Skills are structured

**5:53** · Uh it doesn't fit on the screen but it's basically a set of instructions telling the model um how to create word trees and um to run the setup scripts that the user might have configured. and then to stay on that checkout, right? We want to make sure that when the agent is operating on a word tree, it is staying in that checkout. Um the best event skill is very similar. It's actually even smaller. The entire skill fits on the screen here with with a small uh font.

**6:25** · Um, and what we're doing here is we're instructing the parent agent to go and create sub agents for each model and then spin up a word tree for each uh, so have each sub agent create its own work tree and work inside that work tree. Um, and then we also tell it to wait for all the subs and when they're done, please provide some commentary. Please let the user know um what um the different implementations by the different sub agents look like. Maybe you can grade them.

**6:57** · Maybe you can make some uh criticism of them and maybe you can help the user choose which one is the best.

**7:04** · Um and and please give that to the user in some nice table format or something.

**7:09** · But again, it's only around 40 lines of code and it's all marked down. Like it's not even code. And the previous version of this was maybe 4,000 lines of code.

**7:19** · Some of the considerations we have to have in this in the skill is that the skill must be crossplatform compatible like we have Windows specific instructions and we have Linux and Mac OS instructions as well. We also instruct the parent model to run the setup scripts for each word tree that the user might have configured. And then this is the hardest part. We'll spend a bit of time on this on the talk today.

**7:40** · We have to instruct the model to stay on that word tree, right? we have to really say, hey, do not ever work outside this and do not ever um escape, right? Um and we we do that with some aggressive prompting effectively.

### New Slash commands and workflow

**7:58** · So the new commands are slashword tree and then slashpass event to do the basic basically like um the to start agents in isolated work trees and to start multiple agents on the same task. And then we also have apply word tree and delete word tree to bring over changes from the side word tree into your primary checkout. And delete work tree just does uh what you would expect. Uh a little note is that these are not actually skills in cursor.

**8:27** · They're actually commands but the way these commands work in cursor is extremely similar to how skills work in that there the prompts only get loaded into the context if the user chooses to load them. Um, and the only reason we did it as commands and not as skills is so that the prompts for them can be controlled in our servers in our back end. This means I can iterate on these prompts um without you having to update your cursor version.

**8:55** · Um, if I do some improvements to these prompts, the next time you use them, you're going to have you're going to get the latest version of the prompts. But effectively, they work like skills. Um this is a demo of the best event um skill or command where I'm

**9:11** · giving the same task to Kimmy Grock composer GPT and opus and what you will see is that the parent agent starts by spinning up five sub agents on the five different models that I specified and each one is going to have its own work tree. Each each one has its own context and then opus takes a little longer as expected and then at the end the parent model as instructed will do that comparison ac across all the different subsations. It'll say um these two models did basically the same thing.

**9:45** · This one did something that none of the others did. And you can even talk to the parent agent and you can say oh I like this part that Opus did and I like this part that GPT did. Can you can you match them together? and the the parent agent will do that for you.

### Pros of the new implementation

**9:58** · Um, so let's talk about some of the pros of the new implementation and then I'll talk about some of the some of the the the cons, some of the things we lost um with this refactor. So the main pro of reimplementing this entire feature as a skill is that I have a lot less code to maintain. Uh selfishly, um I'm going to be spending a lot less time maintaining this feature. And this is an an advanced feature, right? We're not talking about a feature that is used by 90% of cursors users. Far from it. Work trees are kind of an advanced thing.

**10:30** · Um and so only the cursor power users that love paralyzing and having these grids of agents are using work trees. So it's not the kind of feature where we want to be spending a lot of time with maintenance.

**10:47** · Another advantage is that our users can now switch into a word tree halfway through a chat. It was not possible before. Um, we didn't want to pollute the prompt UI too much with all these like drop downs and settings. And so now that it's just a slash command, it's much easier for for users to switch to a word tree halfway through a chat. They can start talking about something and then if they decide they want to work on the site, they can do that with slashword tree. Another big advantage is that the previous implementation did not work if you were working on multiple repos at the same time.

**11:19** · So it's very common to have a multi-reo setup where maybe your front end and your back end are separate repos. In the past you could not do word trees in this kind of setup. It was just disabled. With the new slashword tree command everything works fine. the agent will make sure to create a word tree on each repo and then if you open a PR, it'll open two PRs, one for each repo. It works quite well.

**11:45** · Another advantage of the new skill implementation is that the judging experience at the end of knowing what model did which for best event is far superior. The parent now has a lot more context over what each of the sub aents did. And the user can even ask the agent to stitch together a little different piece pieces and bits from the different implementations which was not possible before. In the previous implementation, you had to choose one sub agent or one model and just stick with that.

**12:13** · Now let's talk about some of the cons.

### Cons and user feedback challenges

**12:15** · And if you're curious, um, we have a forums link here where we're actually getting some mixed feedback on the new implementation. Like some people were really accustomed to the old way of how the feature used to work. Um, and if you're curious, you can go and see that not everyone is happy with the change, at least for now. But we're we're tracking. What are the problems? Number one, it's very hard for the agent to stay on track. With our previous approach, um, the agent had to stay on track. Like it, we didn't let the model ever touch any files outside its work.

**12:48** · It was physically impossible for it to do so. Now we're trusting the model. So it's you could say it's a bit vibes based because we're basically saying hey operate on this directory and and and then like you know knock on wood please don't forget about this and especially over long sessions it's quite possible that the model will forget where it should be operating and sometimes these models especially the worst models will kind of hallucinate or they'll go a bit haywire and they'll start doing things they shouldn't but we're we're working on this.

**13:18** · Um, another con is that it feels slower because you're you're seeing the agent create the work tree and you're seeing that in your chat.

**13:29** · It's not actually slower, but it does feel like the agent is kind of like wasting time doing something that should be done for it in advance. Um, we're also looking at some improvements here.

**13:40** · And then finally, this is much harder to find the feature now, right? Like before whenever you opened cursor you had this dropdown that would show you do you want to run this task locally or do you want to run it in cloud or do you want to run it in a work tree now that entire dropdown is gone and so if you want to use work trees you have to know the feature exists so you can actually type /wart tree so the discoverability is a bit worse but as I mentioned before this is an advanced power user feature um

**14:07** · which we're personally okay we're we're okay with being less discoverable in general So, how can we make this skill better?

### Future improvements: Evals and RL training

**14:17** · Um, as I mentioned, the biggest problem right now is that the agent is not really always staying on track. Uh, there's two ways that we're going to improve this. One is with evals and then using those evals to improve the prompts and then the other one is through RL and training. So, at cursor, we train our own model called composer. And for composer 2, our the latest version of this model, we didn't have any RL tasks with these prompts.

**14:44** · We we didn't have any tasks in all of the many many thousands of tasks that we um use for RL actually operating in this type of environment. So we're working on adding a bunch of these tasks into our RL pipeline so that by the time we launch composer three or four or five u at least our own model will be much better at this. Obviously we cannot improve the models that the other companies develop but we've been sharing feedback with all the other labs and model providers on this kind of thing.

**15:14** · And for evals, uh I've been working on some evals for this feature and it was actually my first time or not my first time but one I'm I'm fairly um early in my u writing evals uh journey and I was actually very surprised if you use something like brain trust and shout out to brain trust they've been super helpful. Uh writing these kinds of eval is is actually super super easy. You don't have to know almost anything about evals and you can just prompt the agent. It'll do everything for you.

**15:45** · Um, effectively what I'm doing is I spin up the cursor CLI.

**15:50** · It's headless, so it's great for evals.

**15:53** · Um, and then I have two scorers. One that checks to see if the model did any work in its work tree as expected and then another one which is the reverse of that which is did the model do any work in the primary checkout where it shouldn't be doing any work. Uh, and so far the evals I've got are pretty simple. So I actually haven't been um able to simulate extremely long sessions, which is when the models start performing worse. But even so far, I've already understood that not all models are equally good at this.

**16:25** · So for example, haiku, which is a smaller, less intelligent model, will very often deviate and start working in the primary checkup. But the other models that I've been testing such as composer and grock um are doing much better. So I still have to improve these evals a lot more to make them more complicated. But the hope is that as soon as I can start to find patterns here, I can actually go and improve the prompts.

**16:51** · And then another thing we can do is have better system reminders to the models uh instructing them to stay on track and to not deviate from the word tree that they are supposed to be working in.

### What's next for Cursor 3.0 and native work trees

**17:05** · Okay. So, what's next? Um, the first thing is we're actually going to take a a small step back here and we're actually going to have a much more complete and native work trees implementation in the new cursor agent window. If you're uh if you've been following, we recently announced cursor 3.0.

**17:24** · Part of 3.0 0 is a more agentic interface for coding where you can still edit code and you can still see code but the UI and the UX are much more optimized around the agent and the chat interface. We believe this kind of interface is the right place for a proper word trees implementation. The kind of person who is more likely to be uh doing a bunch of local paralization is usually the same type of person that is more likely to use this type of UI.

**17:54** · So we're taking a small step back there and building a proper word trees uh implementation that is more native not so much agentic in the new UI. Also we're improving the skills um as I mentioned through this continued work on evals and then RL and other training work. And then finally we are actually looking into other parallelization primitives that are not git work trees.

**18:17** · So if you've used git work trees, you might know that uh they can be a bit slow to create. Um and also to uh they also use up a lot of disk space on your computer. Um and then finally uh they only work in git repos. So if you're using something other than git, there's really no local paralization primitive in cursor. Um in the near future we hope to uh share more about this but we're looking into some other solutions for local paralization that don't involve git and don't involve git work trees.

**18:49** · Um so yeah stay tuned for that. Um thank you all for coming to the talk today. Um I'm sure many of you have questions and I'm going to be around all day. Uh feel free to grab me anytime and uh um I'm happy to chat with anyone.

**19:04** · Thank you.