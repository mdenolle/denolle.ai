---
layout: default
title: "Before the Prompt: What Actually Makes Academic Agents Work"
series: agents-for-academic-practice
repo_url: "https://github.com/mdenolle/academic-practice-agents"
skills_url: ""
discussion:
  url: ""
---

## What I Should Have Written First

I should have written this post before the one on teaching. After sharing that workflow, I realized the more fundamental question was hiding underneath: *what made the output go from generic to usable?*

The answer was not a better prompt. It was everything I had set up *before* the prompt.

For scientists, model output without deep context — without domain-specific knowledge or explicit structure — comes back bland at best and hallucinated at worst. I had been prompting ChatGPT with variations of "critique this project summary" for an interdisciplinary proposal combining environmental seismology, machine learning, and critical zone hydrology. The responses were polished and structurally hollow.

Then I reorganized. My OpenAI ChatGPT projects now carry rich context. I upload prior proposals and funder RFPs as part of the project's *sources* — its knowledge base. I write standing instructions specifying tone, audience, and what the model should not do. The project also accumulates *memory* from previous discussions, so each interaction builds on the last. Every time I prompt now, the output is grounded in my own framing, not the internet's average.

Even if base models do not improve, my *context engineering* changes the output from generic content to something actionable.

## Three Layers, Not One

What I have learned from this — and from building similar setups for teaching, reviewing, and communication — is that robust academic agents depend on three distinct layers, not just a clever prompt.

**The knowledge anchor.** This is the foundation: uploaded documents that give the model access to *my* domain knowledge rather than its generic training. For a proposal project, that means prior funded narratives, the specific RFP, reviewer feedback from past submissions, and relevant papers. For a course project, it means the textbook chapters, my syllabus, and the learning objectives. The model stops inventing grounding and starts drawing from mine. This is the single change that had the largest effect on output quality. Without it, every response defaults to the statistical mean of the internet — fluent, confident, and useless for specialized academic work.

**Standing instructions.** Each project carries a persistent instruction file that specifies the structure of the output, the tone, what the model should and should not do, and guardrails against known failure modes. These are not casual system prompts. They are closer to role specifications: who is the audience, what format should the deliverable take, what must be preserved exactly, what must never be fabricated. I iterate on these continuously — and increasingly, I use GPT and Claude themselves to rewrite the instructions, aligning them with emerging industry practices for agent design. The instructions are a living document, not a one-time setup.

**Prompt intent.** Each individual request is typically around 300 words, specifying the particular deliverable and the particular audience for *this* interaction. Academics shift audiences constantly — a funder expects a different register than a student, a journal reviewer expects different structure than a department committee. The prompt is where that intent gets declared. It sits on top of the knowledge anchor and the standing instructions, and it tells the model *what to do right now, for whom*.

A robust agent is not just an instruction. It is a specification that layers knowledge, standing rules, and situated intent. When any of these layers is missing, the output reverts to generic fluency.

## Where It Still Breaks

Even with all three layers in place, the system is not foolproof. Models still lack physical intuition. They can absorb my uploaded papers but cannot weigh the contested reliability of different published papers, whether it came from an AI-generated paper or from an established and trustworthy journal. They hallucinate rationale, not just citations — fabricating or predicting the *logic* for a methodological choice when the grounding is thin. That judgment remains mine, for now.

And the instructions themselves are an evolving experiment. I rewrite them regularly. I ask the models to critique and improve their own specifications. This raises a question I have not resolved: as the instructions become more sophisticated and are increasingly co-authored with AI, at what point does the specification itself need verification? Am I engineering guardrails, or am I pushing the hallucination risk one layer deeper?

I do not have the answer yet. But I have learned that the work that matters most happens before the prompt — in the knowledge you upload, the rules you write, and the intent you declare. The prompt is just the last mile.