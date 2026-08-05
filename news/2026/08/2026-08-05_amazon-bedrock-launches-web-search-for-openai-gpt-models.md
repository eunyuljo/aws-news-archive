---
title: "Amazon Bedrock launches Web Search for OpenAI GPT models"
date: "2026-08-05"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-web/"
tags: ["Bedrock", "2026", "GA", "price-reduction", "performance", "security", "ai-ml"]
nav_exclude: true
---

# Amazon Bedrock launches Web Search for OpenAI GPT models

**날짜:** 2026년 08월 05일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-web/

## 내용

Today, we are announcing the general availability of Web Search on Amazon Bedrock, a built-in server side tool that performs web search entirely within AWS, enabling OpenAI models (GPT-5.4, GPT-5.5, and GPT-5.6 Sol/Terra/Luna) to ground responses with current web knowledge while maintaining data residency within your secured AWS environment with zero data egress. Previously, adding web grounding required onboarding a third-party search provider, managing separate API keys and billing, building custom orchestration, and conducting additional compliance reviews for each external vendor. Web Search removes this heavy lifting by enable grounding with a single parameter in an existing API call, with no vendor onboarding, no external APIs to orchestrate, and no additional vendor security reviews to conduct.  Web Search is built by Amazon, informed by years of experience across Alexa+, Amazon Quick and Kiro. It combines a web index operated by Amazon, spanning tens of billions of documents refreshed continually, with a built-in knowledge graph that provides verified facts. Rather than returning raw pages, Web Search performs semantic snippet extraction, delivering context-efficient results optimized for the model's context window with low latency. Web Search integrates through a standardized tool-use interface, compatible with the OpenAI Responses API. Simply add the web search tool to your API call, and Bedrock handles the entire search lifecycle server-side; a single API call returns a grounded response with citations.  Web Search on Amazon Bedrock is generally available today in US East (N. Virginia), US East (Ohio), and US West (Oregon). To get started, read our blog post Introducing Web Search on Amazon Bedrock for foundation model grounding, review the Web Search section in the Amazon Bedrock User Guide for technical documentation, and visit the Amazon Bedrock pricing page for cost details.

## 핵심 요약

요약 미지원
