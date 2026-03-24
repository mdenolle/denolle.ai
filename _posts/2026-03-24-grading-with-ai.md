---
layout: default
title: "Grading by Hand, Verified by Machine"
series: agents-for-academic-practice
repo_url: "https://github.com/mdenolle/academic-practice-agents"
skills_url: "https://github.com/mdenolle/academic-practice-agents/tree/main/homework-grader"
discussion:
  url: ""
---

## Sixty-Four PDFs and No TA

It is the last week of the quarter. I have eight homework sets, eight students, and sixty-four handwritten PDFs of seismological derivations sitting in a folder — ungraded. The course had no teaching assistant this year. Like most US universities, mine has been trimming TA support while expecting better teaching in return. This quarter, I focused on content delivery and moved the grading to the end. Now there is no time.

I grade on a plane to a conference. I grade at 5 AM before my children wake up. I grade at 10 PM after they go to bed. The homework assignments are from Peter Shearer's *Introduction to Seismology* — exercises I genuinely admire for their ingenuity. They require students to derive canonical results by hand: wave equations, travel-time curves, moment tensor decompositions. The derivations are intentionally handwritten because I still want students to build reasoning through pen and paper, step by step, not by assembling code snippets.

But here is the dilemma. How do you grade handwritten mathematical derivations *fairly* when you are exhausted, scattered across time zones, and working in fragments between other obligations?

## The Grader's Dilemma

Grading is the least glamorous and most consequential role in academic life. It is where an instructor's fatigue most directly harms students. The eighth paper in a batch gets less attention than the first. A late-night session produces different judgments than a morning one. And I have to be honest about a pattern I have noticed in my own grading over the past ten years.

During the pandemic, I became — perhaps too American in this regard — deeply worried about student wellbeing. Worried that rigorous grading would discourage students from a field I wanted them to love. Worried about course evaluations. The result, looking back with clarity, is that my grades were inflated. Not dramatically, but consistently. Students who submitted plausible-looking work with correct final answers received high marks even when the reasoning was thin.

That instinct came from a good place. But it was not fair to the students who showed deep, careful reasoning as their rigor was not sufficiently distinguished from surface-level correctness.

Something has shifted in my teaching philosophy. Over the past three years, as AI tools have become capable of rapid implementation such as coding, computation, generating toy problems, I have come to value *depth of reasoning* more than ever. If an AI can produce a working script in seconds, what remains uniquely valuable in a student's education is the ability to derive, to reason through assumptions, to trace a physical argument from first principles. That is what handwritten homework tests.

But evaluating reasoning, not just checking final answers, is harder to grade. And harder to grade *fairly* when you are tired, traveling, or squeezing grading into the margins of an overfull schedule.

## The Machine That Reads Handwriting

The answer, it turned out, was a vision-language model. I had not expected this. I had forgotten how deep learning was fueled by handwritten datasets such as MINST, and was skeptical that any model could reliably parse the diversity of handwritten mathematical notation my students produce: neat cursive, rushed scrawl, iPad stylus, pencil on paper, equations that wander across margins. Even after this step, could a model then evaluate the *reasoning* behind those derivations against a rubric that prioritizes logical flow over correct endpoints.

I was wrong. 

Here is the pipeline I built, prompted entirely through Claude. The grading application and supporting scripts are publicly available in the [homework-grader](https://github.com/mdenolle/academic-practice-agents/tree/main/homework-grader) directory of the companion repository.

**Preparing the solutions.** Each homework set starts with three artifacts: the exercise instructions copied as text from Shearer's textbook, a screenshot of the publisher's solution key, and the student submissions as PDFs. The solution keys arrive as images — scanned pages of typeset mathematics. I uploaded these to Claude and asked it to parse each solution into structured markdown, question by question, with all mathematical notation preserved. I ran this parsing twice, comparing outputs, to catch transcription errors. The result: clean, machine-readable solution files for every question in the course.

**Building the grading application.** I prompted Claude to build a React application for structured grading. The app accepts the parsed solutions, a student roster, and a configurable rubric. For each homework set, I upload individual student PDFs — handwritten, varied in format, often with disorganized question headers that do not match the assignment numbering. The VLM reads each submission, maps student work to the correct questions despite formatting inconsistencies, and evaluates against the rubric.

**The rubric as specification.** This is where the context engineering matters most. The rubric is not a simple answer key. It encodes my pedagogical values: evaluate the reasoning, not just the final result. If a student arrives at the correct answer but shows no derivation, the score is capped at fifty percent. Partial credit flows from the logical structure of the argument — whether assumptions are stated, whether intermediate steps follow from prior ones, whether the physical interpretation accompanies the mathematics. The rubric is the agent's specification, and it carries the instructor's judgment into every evaluation.

**Review and analytics.** The app flags roughly five percent of grades for human review, cases where the model's confidence is low, where handwriting is ambiguous, or where a student's approach diverges significantly from the expected solution path. I review every flag. The app also provides per-question analytics: how each problem landed across all students, where the class struggled collectively, where individual students diverged from the group.

The entire pipeline — from solution preparation through grading eight homework sets for eight students — replaced what would have been twelve to twenty-four hours of manual grading.

## Where It Surprised Me

Two things surprised me.

First, the handwriting recognition was better than I expected. Across eight students with genuinely diverse handwriting styles — including one student who writes in extremely compressed notation and another whose iPad stylus produces thick, overlapping strokes — the VLM correctly parsed the mathematical content in the vast majority of cases. The five percent flag rate was not dominated by handwriting failures. It was dominated by cases where a student took a valid but unexpected derivation path that the model was not confident evaluating against the standard solution.

Second, the grading was stricter than mine. Not by a dramatic margin, but consistently. The model applied the rubric as written — reasoning required, partial credit for logical structure, no inflation for effort or good intentions. Looking at the results, I believe the stricter grading is correct. My prior leniency was the failure mode, not the model's consistency.

This is the part that is emotionally difficult, and I want to be honest about it. When you know a student worked hard, when you can see the effort in the handwriting, when the intention is clearly there but the reasoning is not — the human instinct is to round up. That instinct is real and it comes from care. But it is not fair to the students whose reasoning *is* there, whose rigor deserves to be distinguished. The model does not experience that emotional override. It applies the rubric. That consistency is a feature, not a limitation.

I still review every flagged case. I still set the rubric. I still decide what reasoning means in the context of each problem. The AI executes what I specify — consistently, at 5 AM and at 10 PM, on the first paper and the sixty-fourth.

## What This Enables

Here is the narrow claim I want to make.

**AI-assisted grading does not eliminate traditional pedagogy. It enables it.**

The widespread concern about AI in education is that it pushes everything toward automation — multiple-choice assessments, auto-graded coding assignments, the death of handwritten work. Many colleagues are considering returning to blue-book and oral exams precisely to prevent AI-assisted cheating. But blue-book exams without TA support mean even more grading load on instructors who are already stretched.

The VLM inverts this problem. Because a capable vision-language model can read handwritten mathematics and evaluate reasoning against a structured rubric, handwritten derivations *survive*. Instructors can assign rigorous, hand-derived problem sets — the kind that build the deep reasoning I now value most — without drowning in the grading load or sacrificing fairness to fatigue.

I am no longer scared of making students work by hand. I am no longer scared of my own tiredness corrupting the evaluation. I can provide constructive comments to every student, analyze which concepts landed and which did not, and use that analysis to adjust the course for next time. The grading became something I could learn from, not just something I had to survive.

## An Unresolved Question

Should students know their handwritten homework was evaluated by an AI?

If the rubric is mine, the solutions are mine, the flagged cases are reviewed by me, and the pedagogical values encoded in the grading specification reflect my judgment — is this different from training a teaching assistant and reviewing their work? The AI is more consistent than a tired TA. It is certainly more consistent than a tired me.

And if AI-assisted grading produces fairer, more rigorous, and more transparent evaluation than I would have produced alone at midnight on a Tuesday — does the student experience improve or degrade?

I have not resolved this. Transparency matters. But so does the recognition that the alternative was not some idealized version of careful, rested, fully attentive manual grading. The alternative was me, exhausted, grading on a plane, rounding up out of empathy. I am not sure that version was more fair.
