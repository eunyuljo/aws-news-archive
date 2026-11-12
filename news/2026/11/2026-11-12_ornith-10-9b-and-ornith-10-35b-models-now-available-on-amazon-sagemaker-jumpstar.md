---
title: "Ornith-1.0-9B and Ornith-1.0-35B models now available on Amazon SageMaker JumpStart"
date: "2026-11-12"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/01/ornith-1-0-9b-ornith-1-0-35b-on-sagemaker-jumpstart/"
tags: ["SageMaker", "2026", "GA", "performance", "ai-ml"]
nav_exclude: true
---

# Ornith-1.0-9B and Ornith-1.0-35B models now available on Amazon SageMaker JumpStart

**날짜:** 2026년 11월 12일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/01/ornith-1-0-9b-ornith-1-0-35b-on-sagemaker-jumpstart/

## 내용

DeepReinforce AI's Ornith-1.0-9B and Ornith-1.0-35B models are now available on Amazon SageMaker JumpStart, expanding the portfolio of foundation models available to AWS customers. These two models are part of the Ornith 1.0 family of open-source, self-scaffolding agentic coding models released under the MIT license, achieving state-of-the-art performance among open-source models of comparable size on coding benchmarks such as Terminal-Bench 2.1, SWE-Bench, NL2Repo, and OpenClaw. 
These models address different agentic coding challenges with specialized capabilities: 
Ornith-1.0-9B is a lightweight 9B-parameter dense model post-trained on Qwen 3.5 9B, designed for efficient single-GPU deployment. With a 256K-token context window and 32 decoder layers, it is well-suited for individual developers and small teams running agentic coding workflows on a single GPU — including laptops with consumer-grade hardware. Its self-improving training framework uses reinforcement learning to jointly optimize scaffold generation and solution rollouts, enabling the model to discover better search trajectories and generate higher-quality code solutions. 
Ornith-1.0-35B is a 35B-parameter Mixture-of-Experts (MoE) model post-trained on Qwen 3.5, delivering stronger agentic coding performance while remaining deployable on a single 24GB consumer GPU. Like its smaller sibling, it employs reinforcement learning to jointly optimize the scaffolds that drive coding tasks and the resulting solution rollouts, discovering superior code trajectories. Its MoE architecture activates only a subset of parameters per token, providing a strong balance of quality and efficiency for production agentic coding workloads. 
With SageMaker JumpStart, customers can deploy any of these models with just a few clicks to address their specific AI use cases. 
To get started with these models, navigate to the SageMaker JumpStart model catalog in the SageMaker console or use the SageMaker Python SDK to deploy the models to your AWS account. For more information about deploying and using foundation models in SageMaker JumpStart, see the Amazon SageMaker JumpStart documentation.

## 핵심 요약

요약 미지원
