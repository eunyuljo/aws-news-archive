---
title: "Muse-Glimmer-30B and Qwen 3.8-27B models now available on Amazon SageMaker JumpStart"
date: "2026-08-28"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/01/muse-glimmer-30b-qwen-3.8-27b-on-sagemaker-jumpstart/"
tags: ["SageMaker", "2026", "GA", "performance", "ai-ml"]
nav_exclude: true
---

# Muse-Glimmer-30B and Qwen 3.8-27B models now available on Amazon SageMaker JumpStart

**날짜:** 2026년 08월 28일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/01/muse-glimmer-30b-qwen-3.8-27b-on-sagemaker-jumpstart/

## 내용

Meta's Muse-Glimmer-30B and Alibaba's Qwen 3.8-27B models are now available on Amazon SageMaker JumpStart, expanding the portfolio of foundation models available to AWS customers. These two models bring specialized capabilities spanning autonomous local agentic workflows and multimodal long-horizon reasoning, enabling customers to deploy high-performance, scalable AI solutions on AWS infrastructure. 
These models address different enterprise AI challenges with specialized capabilities: 
Muse-Glimmer-30B is engineered for autonomous agentic tasks with multi-step reasoning, tool use, and failure recovery. This 30B-parameter dense model from Meta Superintelligence Lab combines a dedicated ~1.8B ViT-G/14 perception encoder with interleaved text and image inputs, a 131K+ context window, and selectable reasoning strength (low through extra-high). Released under Apache 2.0, it handles sequential tool calls, recovers from failures, and operates entirely without cloud infrastructure which is ideal for always-on enterprise agents. 
Qwen 3.8-27B excels in coding, multi-step agentic tasks, and multimodal understanding across text, images, and video. A dense 27B-parameter native vision-language model with a 262K context window (extendable to ~1M via YaRN scaling), it delivers substantial gains over its predecessor with adjustable reasoning effort levels. Scoring 61.7 on SWE-bench Pro and running at ~17GB quantized, it carries complex multi-step tasks through to completion with greater reliability. 
With SageMaker JumpStart, customers can deploy any of these models with just a few clicks to address their specific AI use cases. 
To get started with these models, navigate to the SageMaker JumpStart model catalog in the SageMaker console or use the SageMaker Python SDK to deploy the models to your AWS account. For more information about deploying and using foundation models in SageMaker JumpStart, see the Amazon SageMaker JumpStart documentation.

## 핵심 요약

요약 미지원
