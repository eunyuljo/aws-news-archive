---
title: "DeepSeek-V4-Pro, DeepSeek-V4-Flash, and DeepSeek-V4.1-Flash models now available on Amazon SageMaker JumpStart"
date: "2026-11-12"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/01/deepseek-v4-pro-v4-flash-v4.1-flash-on-sagemaker-jumpstart/"
tags: ["SageMaker", "2026", "GA", "price-reduction", "performance", "ai-ml"]
nav_exclude: true
---

# DeepSeek-V4-Pro, DeepSeek-V4-Flash, and DeepSeek-V4.1-Flash models now available on Amazon SageMaker JumpStart

**날짜:** 2026년 11월 12일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/01/deepseek-v4-pro-v4-flash-v4.1-flash-on-sagemaker-jumpstart/

## 내용

DeepSeek's DeepSeek-V4-Pro, DeepSeek-V4-Flash, and DeepSeek-V4.1-Flash models are now available on Amazon SageMaker JumpStart, expanding the portfolio of foundation models available to AWS customers. These three open-weight Mixture-of-Experts (MoE) language models, released under the MIT license, deliver frontier-class performance across reasoning, coding, and agentic workloads while activating only a fraction of their total parameters per token, enabling high efficiency at scale. 
These models address different AI challenges with specialized capabilities: 
DeepSeek-V4-Pro is designed for complex reasoning and high-quality text generation at flagship scale. This 1.6T-parameter MoE model activates 49B parameters per token and supports a 1M-token context window, making it well-suited for long-document analysis, multi-step reasoning, and demanding generation tasks that require maximum model capacity. 
DeepSeek-V4-Flash delivers strong performance at significantly lower compute cost as an efficient 284B-parameter MoE model activating 13B parameters per token. It supports the same 1M-token context window as V4-Pro, making it ideal for latency-sensitive and cost-conscious production deployments across a wide range of language tasks. 
DeepSeek-V4.1-Flash provides next-generation agentic efficiency with native multimodal support. Built on a novel Causal Encoder-Decoder (CED) architecture with a 552B-parameter backbone, it activates just 8B parameters during prefill and 16B during decode, supporting a 1M-token context window and 384K max output tokens. Its Compressed Sparse Attention 2 (CSA2) and FP4 KV caching reduce the global KV cache footprint to roughly 1/4 of V4-Flash, delivering substantially improved cost efficiency for agentic workloads, coding, and vision tasks. 
With SageMaker JumpStart, customers can deploy any of these models with just a few clicks to address their specific AI use cases. 
To get started with these models, navigate to the SageMaker JumpStart model catalog in the SageMaker console or use the SageMaker Python SDK to deploy the models to your AWS account. For more information about deploying and using foundation models in SageMaker JumpStart, see the Amazon SageMaker JumpStart documentation.

## 핵심 요약

요약 미지원
