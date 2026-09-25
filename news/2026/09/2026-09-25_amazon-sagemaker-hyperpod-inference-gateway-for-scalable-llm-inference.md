---
title: "Amazon SageMaker HyperPod Inference Gateway for scalable LLM inference"
date: "2026-09-25"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-hyperpod-inference-gateway/"
tags: ["EKS", "2026", "GA", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker HyperPod Inference Gateway for scalable LLM inference

**날짜:** 2026년 09월 25일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-hyperpod-inference-gateway/

## 내용

Amazon SageMaker HyperPod Inference Gateway is a Kubernetes-native, GPU-aware routing system that deploys as a single EKS managed add-on on existing SageMaker HyperPod infrastructure with zero application changes. By replacing unintelligent round-robin load balancing with real-time inference-signal-driven routing, it reduces first-token latency by up to 82% and p99 TTFT reductions of 97–98% in mixed-hardware and burst traffic scenarios.
The Gateway is built around 3 core components. The Envoy Endpoint terminates HTTPS traffic and exposes a single private endpoint per cluster. The Body-Based Router reads the model name directly from each incoming request and routes it to the correct GPU pool - enabling one gateway to serve many models from a single endpoint URL with no client-side changes required. The Endpoint Picker continuously scores every model server pod in real time across 6 inference-level signals - KV cache utilization, queue depth, LoRA adapter residency, prefix cache hit rate, predicted latency and running requests - selecting the optimal pod for each individual request.
The gateway works with any OpenAI-compatible model server, including vLLM and SGLang, requiring no application code changes.
Per-cluster routing is available today in all AWS Regions where the SageMaker HyperPod inference add-on is supported. Coming soon - cross-cluster and cross-region routing with a centralized fleet gateway, global rate limiting, and cost-tier-aware traffic shaping.
To learn more, read the launch blog and explore the documentation

## 핵심 요약

요약 미지원
