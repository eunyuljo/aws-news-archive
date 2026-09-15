---
title: "Qwen3.6-35B-A3B-NVFP4 and Wan2.1-T2V-1.3B-Diffusers models now available on Amazon SageMaker JumpStart"
date: "2026-09-15"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/01/qwen3.6-35b-a3b-nvfp4-wan2.1-t2v-1.3B-diffusers-jumpstart/"
tags: ["SageMaker", "2026", "GA", "performance", "ai-ml"]
nav_exclude: true
---

# Qwen3.6-35B-A3B-NVFP4 and Wan2.1-T2V-1.3B-Diffusers models now available on Amazon SageMaker JumpStart

**날짜:** 2026년 09월 15일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/01/qwen3.6-35b-a3b-nvfp4-wan2.1-t2v-1.3B-diffusers-jumpstart/

## 내용

NVIDIA's Qwen3.6-35B-A3B-NVFP4 and Alibaba's Wan2.1-T2V-1.3B-Diffusers models are now available on Amazon SageMaker JumpStart, expanding the portfolio of foundation models available to AWS customers. These two models bring specialized capabilities spanning agentic coding with long-context reasoning and lightweight text-to-video generation, enabling customers to deploy high-performance, scalable AI solutions on AWS infrastructure. 
These models address different enterprise AI challenges with specialized capabilities: 
Qwen3.6-35B-A3B-NVFP4 is optimized for agentic coding, multimodal reasoning, and long-context understanding as the NVIDIA-quantized variant of Alibaba's Qwen3.6-35B-A3B. This Mixture-of-Experts model contains 35B total parameters with only 3B activated per token (8 of 256 experts), supporting a 262K-token context window extendable to ~1M via YaRN scaling. Quantized to NVFP4 using NVIDIA's ModelOpt framework, it preserves thinking across conversation turns, multi-token prediction, and tool calling for multi-step agent pipelines—all at a significantly reduced memory footprint. 
Wan2.1-T2V-1.3B-Diffusers excels in text-to-video generation on consumer-grade hardware. Built on the diffusion transformer paradigm with a novel Video Variational Autoencoder (VAE), this 1.3B-parameter model generates high-quality, physics-consistent video clips from text prompts while requiring only 8.19 GB of VRAM. It can produce a 5-second 480p video on an RTX 4090 in approximately 4 minutes, making it one of the most accessible open-source video generation models available. 
With SageMaker JumpStart, customers can deploy any of these models with just a few clicks to address their specific AI use cases. 
To get started with these models, navigate to the SageMaker JumpStart model catalog in the SageMaker console or use the SageMaker Python SDK to deploy the models to your AWS account. For more information about deploying and using foundation models in SageMaker JumpStart, see the Amazon SageMaker JumpStart documentation.

## 핵심 요약

요약 미지원
