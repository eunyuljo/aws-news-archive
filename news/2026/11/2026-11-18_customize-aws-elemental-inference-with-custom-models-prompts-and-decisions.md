---
title: "Customize AWS Elemental Inference with custom models, prompts, and decisions"
date: "2026-11-18"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/elemental-inference-functions-decisions/"
tags: ["Bedrock", "2026", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# Customize AWS Elemental Inference with custom models, prompts, and decisions

**날짜:** 2026년 11월 18일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/elemental-inference-functions-decisions/

## 내용

AWS Elemental Inference now lets you customize how it analyzes your live video in two ways. You can create functions that ask custom questions of the video using multi-modal foundational models in Amazon Bedrock, or add contextual metadata decisions using labels and questions you define. Both run on the same pipeline as built-in features such as vertical video creation and smart subtitles, and return results through the GetMetadata API, with no separate pipeline to build. 
Use contextual metadata decisions when the answer you need fits labels and yes/no questions. You define yes/no questions, such as whether a scene is a weather report, or "pick-one" categories, such as genre. For each scene, contextual metadata returns a decision and a confidence score for every label and question, alongside the standard Interactive Advertising Bureau (IAB), Global Alliance for Responsible Media (GARM), and mood fields, so your workflows can act when confidence meets a threshold you set. No model selection or prompt writing is required. 
Use functions for open-ended answers, custom response formats, or analysis contextual metadata doesn't cover, such as sponsor logo exposure. A function specifies an Amazon Bedrock model and JSONata expressions that shape the request and response. You attach it to a feed and choose how frequently it runs. 
Contextual-metadata decisions configuration is included in the contextual metadata price. Functions are available at no additional charge on feeds with at least one feature active; Amazon Bedrock usage is billed separately. Both are available in all AWS Regions where AWS Elemental Inference is available. 
To learn more, see the AWS Elemental Inference user guide.

## 핵심 요약

요약 미지원
