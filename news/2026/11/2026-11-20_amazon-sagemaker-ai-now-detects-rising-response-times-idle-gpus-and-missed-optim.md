---
title: "Amazon SageMaker AI now detects rising response times, idle GPUs, and missed optimizations on your generative AI inference endpoints"
date: "2026-11-20"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-monitors-endpoints/"
tags: ["SageMaker", "2026", "GA", "price-reduction", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI now detects rising response times, idle GPUs, and missed optimizations on your generative AI inference endpoints

**날짜:** 2026년 11월 20일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-monitors-endpoints/

## 내용

Amazon SageMaker AI now monitors the response time and GPU use of generative AI inference endpoints by default and notifies customers when responses slow down, GPUs sit mostly idle, or a configuration falls behind. Customers run GenAI Inference Recommendations to test configurations designed to restore response time or lower cost on their recent traffic, and they see measured results before anything changes in production. 
The best configuration for generative AI inference endpoints changes after deployment, as traffic shifts and new serving techniques become available. An endpoint whose latency rises or whose GPUs sit idle keeps running until users complain or the bill arrives. 
With this launch, SageMaker AI tracks response time and GPU capacity use and checks each endpoint's configuration. It does not read customer requests or responses. Findings include slower response times, unused GPU capacity, and configuration gaps such as an older serving container, missing speculative decoding, or missing GPU kernel tuning. When a change holds across the past week or a configuration gap is found, customers receive one AWS Health notification per endpoint in the AWS Management Console. 
Each notification links to the SageMaker AI Agentic Experience in SageMaker Studio with the endpoint and recent traffic already filled in. Customers run Generative AI Inference Recommendations, which compares the current configuration and options on response time, traffic handled, and cost per million tokens. Tests leave the production endpoint untouched, and nothing changes until the customer applies a result. Customers can turn off monitoring anytime. 
This capability is available in US East (N. Virginia, Ohio), US West (Oregon), Europe (Ireland, Frankfurt), Asia Pacific (Singapore, Tokyo) with no additional charge for monitoring. Standard compute costs apply for recommendation jobs. To learn more, visit the blog post or the documentation.

## 핵심 요약

요약 미지원
