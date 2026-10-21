---
title: "Amazon Bedrock Advanced Prompt Optimization now supports prompt shortening"
date: "2026-10-21"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-prompt-optimization-shortening/"
tags: ["Lambda", "2026", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon Bedrock Advanced Prompt Optimization now supports prompt shortening

**날짜:** 2026년 10월 21일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-prompt-optimization-shortening/

## 내용

Amazon Bedrock Advanced Prompt Optimization now supports prompt shortening, an optional setting that reduces the length of your prompt while maintaining or improving your evaluation scores. Advanced Prompt Optimization optimizes prompts for any model on Amazon Bedrock against your own evaluation criteria. Until now, optimization focused on quality alone. Optimized prompts were often longer than the original. Longer prompts raise input token costs and can increase time to first token, which matters at scale and in latency-sensitive applications. 
When you turn on prompt shortening for a prompt template in your input dataset, the optimizer reduces the prompt's length. The optimized prompt is returned only when it is shorter than your original prompt and scores at least as high on your evaluation. Otherwise your original prompt is returned, so the setting never leaves you with a longer or lower-scoring prompt. Results include a compression ratio and the original and optimized token counts, in the output file and on the console results page. For example, a compression ratio of 0.7 means the optimized prompt uses 30% fewer tokens. Prompt shortening works with any evaluation method, including steering criteria, LLM-as-a-judge rubrics, and custom Lambda evaluators.&nbsp;&nbsp;&nbsp;&nbsp; 
Prompt shortening is available in all AWS Regions where Advanced Prompt Optimization is available. To get started, enable prompt shortening for a prompt template in your input dataset and create an optimization job as usual. To learn more, see Shorten prompts in the Amazon Bedrock User Guide, the Amazon Bedrock pricing page, and the Amazon Bedrock product page.

## 핵심 요약

요약 미지원
