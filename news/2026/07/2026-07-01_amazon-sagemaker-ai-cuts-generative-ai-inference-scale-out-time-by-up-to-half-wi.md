---
title: "Amazon SageMaker AI cuts generative AI inference scale-out time by up to half with automatic container image caching"
date: "2026-07-01"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/sagemakerai-inf-scale-out-time"
tags: ["SageMaker", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI cuts generative AI inference scale-out time by up to half with automatic container image caching

**날짜:** 2026년 07월 01일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/sagemakerai-inf-scale-out-time

## 내용

Amazon SageMaker Inference now supports container image caching, enabling up to 2x faster end-to-end scaling for generative AI models during scale-out events. When your endpoint scales out, the service pre-caches your container image so new instances can start serving traffic faster, without waiting for large container images to be pulled from Amazon ECR.  Generative AI workloads typically use large container images (10 GB or more) for deep learning frameworks and model serving. Previously, every new instance launched during scale-out had to pull the full image from ECR, adding several minutes of cold-start latency. Container image caching eliminates this bottleneck by pre-pulling the image so new instances launch with the container already available locally. Customers don't need to make any changes. The service automatically caches whatever image URI is specified in your endpoint or inference component configuration. This capability supports accelerator instance types, single-model endpoints, and inference component-based endpoints.  With this launch, SageMaker Inference now offers a comprehensive scaling optimization suite for generative AI: sub-minute concurrency metrics for up to 6x faster load detection, instance-store container caching for faster scaling on existing instances, and container image caching for up to 2x faster scaling on new instances.  Container image caching is available in all AWS commercial regions where SageMaker Inference is supported. To learn more, visit the launch blog.

## 핵심 요약

요약 미지원
