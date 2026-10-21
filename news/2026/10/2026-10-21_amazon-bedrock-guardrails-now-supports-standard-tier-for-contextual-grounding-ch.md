---
title: "Amazon Bedrock Guardrails now supports Standard tier for contextual grounding checks"
date: "2026-10-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-guardrails-grounding-standard/"
tags: ["RDS", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Bedrock Guardrails now supports Standard tier for contextual grounding checks

**날짜:** 2026년 10월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-guardrails-grounding-standard/

## 내용

Amazon Bedrock Guardrails now offers a Standard tier for contextual grounding checks, which detect and filter hallucinations by checking whether a model response is grounded in your reference source and relevant to the user's query. The Standard tier is more robust than the Classic tier. It supports responses that include reasoning or conversational content, scores differently worded responses with the same meaning more consistently, and provides more comprehensive language support, matching the Standard tier for content filters and denied topics. Amazon Bedrock Guardrails provides configurable safeguards for generative AI applications on any foundation model through the ApplyGuardrail API.
Until now, contextual grounding checks applied strict grounding suited to summarization, paraphrasing, and question answering. With the Standard tier, you can also apply contextual grounding checks to conversational applications and to responses that reason over the source. You choose the tier for each guardrail in the Amazon Bedrock console or API. Existing guardrails keep the Classic tier until you change them. Pricing is the same for both tiers. To use the Standard tier, your guardrail must use cross-Region inference with a guardrail profile.
The Standard tier for contextual grounding checks is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), and Asia Pacific (Tokyo). To learn more, see the Amazon Bedrock Guardrails documentation on contextual grounding checks and safeguard tiers, or visit the Amazon Bedrock Guardrails product page.

## 핵심 요약

요약 미지원
