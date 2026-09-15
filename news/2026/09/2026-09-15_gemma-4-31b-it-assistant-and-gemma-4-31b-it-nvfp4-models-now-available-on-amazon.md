---
title: "Gemma-4-31B-it-assistant and Gemma-4-31B-IT-NVFP4 models now available on Amazon SageMaker JumpStart"
date: "2026-09-15"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/01/gemma-4-31b-it-assistant-gemma-4-31b-it-nvfp4-jumpstart/"
tags: ["SageMaker", "2026", "GA", "price-reduction", "performance", "ai-ml"]
nav_exclude: true
---

# Gemma-4-31B-it-assistant and Gemma-4-31B-IT-NVFP4 models now available on Amazon SageMaker JumpStart

**날짜:** 2026년 09월 15일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/01/gemma-4-31b-it-assistant-gemma-4-31b-it-nvfp4-jumpstart/

## 내용

Google DeepMind's Gemma-4-31B-it-assistant and NVIDIA's Gemma-4-31B-IT-NVFP4 models are now available on Amazon SageMaker JumpStart, expanding the portfolio of foundation models available to AWS customers. These two models bring the flagship Gemma 4 31B dense architecture to enterprise workloads in both full-precision and optimized quantized variants, enabling customers to deploy high-performance, scalable AI solutions on AWS infrastructure. 
These models address different enterprise AI challenges with specialized capabilities: 
Gemma-4-31B-it-assistant is built for multimodal reasoning, coding, and agentic workflows as the assistant-tuned variant of Google's flagship 31B dense model. It handles text and image inputs (including video as frame sequences) and generates text output, with a 256K-token context window and support for over 140 languages. Ranked #3 among open models on the Arena AI text leaderboard—outcompeting models 20x its size—it features a hybrid attention mechanism interleaving local sliding-window and full global attention with native function calling for building autonomous agents. 
Gemma-4-31B-IT-NVFP4 delivers the same Gemma 4 31B capabilities at a fraction of the memory footprint. Quantized with NVIDIA's ModelOpt framework to 4-bit FP4 precision, it reduces memory usage to ~18.5 GB (68% smaller than the base model) and achieves approximately 2.5x faster inference while retaining 97–99% of the original model's quality. Ideal for cost-efficient, high-throughput production deployments on NVIDIA RTX, DGX Spark, and data center GPUs. 
With SageMaker JumpStart, customers can deploy any of these models with just a few clicks to address their specific AI use cases. 
To get started with these models, navigate to the SageMaker JumpStart model catalog in the SageMaker console or use the SageMaker Python SDK to deploy the models to your AWS account. For more information about deploying and using foundation models in SageMaker JumpStart, see the Amazon SageMaker JumpStart documentation.

## 핵심 요약

요약 미지원
