---
title: "Amazon Bedrock expands API support and introduces Cross-Region Inferencing for OpenAI models in AWS GovCloud (US)"
date: "2026-10-31"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-openai-runtime-govcloud/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon Bedrock expands API support and introduces Cross-Region Inferencing for OpenAI models in AWS GovCloud (US)

**날짜:** 2026년 10월 31일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-openai-runtime-govcloud/

## 내용

Amazon Bedrock now supports the OpenAI GPT-5.6 models (Terra and Luna) on the bedrock-runtime endpoint, with support for the Responses, Converse, and Chat Completions APIs in AWS GovCloud (US). It also adds support for Cross-Region Inference, allowing customers to use Cross-Region Inference within AWS GovCloud (US) regions to access higher throughput and increased redundancy.&nbsp;&nbsp; 
Cross-Region Inference automatically routes inference requests across both AWS GovCloud (US) Regions to give you higher throughput, without you needing to manage capacity across multiple Regions. Cross-Region Inference within AWS GovCloud (US) routes requests across both regions so you can scale while maintaining US data sovereignty, giving you the broadest access to Bedrock capacity and the highest throughput during demand spikes. This launch also expands API support; you can use OpenAI GPT models with the Responses API, Chat Completions API, and the Converse API on the bedrock-runtime endpoint. Because these native OpenAI APIs now run on bedrock-runtime, the models work with the same account-level controls you already use for other models on Bedrock: usage appears in Bedrock model invocation logging (deliverable to Amazon S3 or Amazon CloudWatch Logs) and in Amazon CloudWatch metrics covering invocation counts, token counts, latency, throttles, and errors, and it is itemized in AWS Cost Explorer and the AWS Cost and Usage Report so you can attribute spend by model. 
Cross-Region Inference for OpenAI models is available in all AWS Regions where OpenAI models on Amazon Bedrock are offered. To get started, review the model cards for GPT-5.6 (Terra and Luna) in the Amazon Bedrock User Guide.

## 핵심 요약

요약 미지원
