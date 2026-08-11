---
title: "FLUX.2-small-decoder and gemma-4-12B-it models now available on Amazon SageMaker JumpStart"
date: "2026-08-11"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/01/flux.2-small-decoder-gemma-4-12B-it-on-sagemaker-jumpstart/"
tags: ["SageMaker", "2026", "GA", "performance", "ai-ml"]
nav_exclude: true
---

# FLUX.2-small-decoder and gemma-4-12B-it models now available on Amazon SageMaker JumpStart

**날짜:** 2026년 08월 11일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/01/flux.2-small-decoder-gemma-4-12B-it-on-sagemaker-jumpstart/

## 내용

Black Forest Labs' FLUX.2-small-decoder and Google's gemma-4-12B-it models are now available on Amazon SageMaker JumpStart, expanding the portfolio of foundation models available to AWS customers. These two models bring specialized capabilities spanning efficient image generation decoding and unified multimodal understanding, enabling customers to deploy high-performance, scalable AI solutions on AWS infrastructure. 
FLUX.2-small-decoder is optimized for faster image decoding with lower VRAM usage in FLUX.2 image generation pipelines. It is a distilled VAE decoder that serves as a drop-in replacement for the standard FLUX.2 decoder, delivering approximately 1.4× faster decoding speed at 1.4× lower VRAM consumption with minimal to zero quality loss. Benefits increase at higher resolutions where the decoder processes more pixels, making it ideal for production-grade image generation workloads at scale. 
gemma-4-12B-it excels in unified multimodal understanding across text, image, and audio inputs with native support for function calling and agentic workflows. It features an encoder-free architecture where all modalities flow directly into a single decoder-only transformer, delivering performance nearing Google's larger 26B MoE model at less than half the memory footprint. Compact enough to run on 16GB of RAM, it enables powerful multimodal and agentic experiences for enterprise deployments. 
With SageMaker JumpStart, customers can deploy any of these models with just a few clicks to address their specific AI use cases. 
To get started with these models, navigate to the SageMaker JumpStart model catalog in the SageMaker console or use the SageMaker Python SDK to deploy the models to your AWS account. For more information about deploying and using foundation models in SageMaker JumpStart, see the Amazon SageMaker JumpStart documentation.

## 핵심 요약

요약 미지원
