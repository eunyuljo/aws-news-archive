---
title: "Amazon SageMaker HyperPod Inference now supports NVIDIA Dynamo for disaggregated and multi-node inference"
date: "2026-11-19"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-nvidia-dynamo/"
tags: ["SageMaker", "2026", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker HyperPod Inference now supports NVIDIA Dynamo for disaggregated and multi-node inference

**날짜:** 2026년 11월 19일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-nvidia-dynamo/

## 내용

Amazon SageMaker HyperPod Inference now supports NVIDIA Dynamo. You can now serve models that are too large for a single instance, and keep token generation fast when prompts are long. You don't have to build or operate distributed serving infrastructure yourself. HyperPod manages Dynamo for you through the Inference Operator add-on.
As models grow, two problems limit inference. A large model can need more GPU memory than one instance has. Long prompts also slow token generation, because the prefill and decode stages compete for the same GPUs. Until now, customers had to build and run their own distributed serving stack to work around both.
With Dynamo on HyperPod, you can run a single model across multiple nodes. You can also split prefill and decode into separate GPU pools that scale independently, so a long prompt no longer stalls token generation for other requests. KV-aware routing sends each request to a worker that already holds the relevant cached context. This cuts recomputation and raises throughput. HyperPod runs the underlying infrastructure: EFA networking, GPU capacity management, node replacement, endpoint registration, autoscaling, and observability. Your team can spend its time on the models instead.
To get started, bring your existing Dynamo manifests if you want full control. You can also use a simplified configuration that HyperPod translates into the underlying infrastructure.
Amazon SageMaker HyperPod Inference with NVIDIA Dynamo support is available in US East (N. Virginia, Ohio), US West (N. California, Oregon), Europe (Frankfurt, Stockholm, Ireland, London, Spain), Asia Pacific (Mumbai, Hyderabad, Singapore, Sydney, Jakarta, Melbourne, Tokyo), and South America (São Paulo). To learn more, see the Amazon SageMaker HyperPod documentation.

## 핵심 요약

요약 미지원
