---
title: "Amazon Bedrock expands API support and introduces Cross Region Inferencing for OpenAI models"
date: "2026-08-18"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-cross-region-openai-v2/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon Bedrock expands API support and introduces Cross Region Inferencing for OpenAI models

**날짜:** 2026년 08월 18일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-cross-region-openai-v2/

## 내용

Amazon Bedrock now supports the OpenAI GPT-5.6 models (Sol, Terra, and Luna) on the bedrock-runtime endpoint, with support for the Responses, Converse, and Chat Completions APIs. It also adds support for cross-Region inference, allowing customers to use Global and Geo cross-Region inference to access higher throughput and lower inference costs.&nbsp;&nbsp; 
Cross-Region inference automatically routes inference requests across multiple AWS Regions to give you higher throughput, without you needing to manage capacity across multiple Regions. Geo cross region inference routes requests within a predefined geography—including new US Geo (US CRIS) support with this launch—so you can scale while keeping data processed within that geography, while Global cross region inference serve requests from any commercial AWS Region where the model is available, giving you the broadest access to Bedrock capacity and the highest throughput during demand spikes. With Global cross-Region inference you also get lower costs as Global inferencing is priced lower per token for OpenAI models than in-Region and Geo inferencing. This launch also expands API support—you can also use OpenAI GPT models with the Responses API, Chat Completions API, and the Converse API on the bedrock-runtime endpoint. Because these native OpenAI APIs now run on bedrock-runtime, the models work with the same account-level controls you already use for other models on Bedrock: usage appears in Bedrock model invocation logging (deliverable to Amazon S3 or Amazon CloudWatch Logs) and in Amazon CloudWatch metrics covering invocation counts, token counts, latency, throttles, and errors, and it is itemized in AWS Cost Explorer and the AWS Cost and Usage Report so you can attribute spend by model. 
Cross-Region inference for OpenAI models is available in all AWS Regions where OpenAI models on Amazon Bedrock are offered. To get started, review the model cards for GPT 5.6 (Sol, Tera and Luna) in the Amazon Bedrock User Guide.

## 핵심 요약

요약 미지원
