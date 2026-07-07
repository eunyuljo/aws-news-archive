---
title: "Amazon SageMaker HyperPod now supports disaggregated prefill and decode"
date: "2026-07-07"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-sagemaker-hyperpod-dpd/"
tags: ["EKS", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker HyperPod now supports disaggregated prefill and decode

**날짜:** 2026년 07월 07일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-sagemaker-hyperpod-dpd/

## 내용

Amazon SageMaker HyperPod now supports Disaggregated Prefill and Decode (DPD), an inference optimization that separates the two phases of large language model (LLM) inference — prefill and decode — onto dedicated GPU pools and transfers the key-value (KV) cache between them over Elastic Fabric Adapter (EFA) using GPU-Direct RDMA. Customers running LLMs in production for chat assistants, agentic pipelines, retrieval-augmented generation, and long-document analysis need consistent per-token latency and predictable throughput under mixed traffic, but when prefill and decode share the same GPU, a single long-context request can stall token generation for every concurrent request and force customers to over-provision one phase to protect the other.  With DPD, customers run compute-bound prefill on one set of GPUs and memory-bandwidth-bound decode on another, so the two phases no longer contend for the same resources. This delivers more consistent per-token latency under sustained concurrency, higher goodput at strict latency SLOs, and the ability to scale prefill and decode capacity independently to match the input and output distribution of the workload. An intelligent router automatically directs long-context requests through the disaggregated path and sends shorter prompts directly to the decoder, so customers get the benefit on the traffic that needs it without paying transfer overhead on short prompts. Customers enable DPD by adding a `pdSpec` section to the same `InferenceEndpointConfig` custom resource they already use for inference endpoints on the HyperPod Inference Operator, and DPD is composable with the existing KV cache offloading and intelligent routing features on HyperPod.  DPD is available for SageMaker HyperPod clusters using the EKS orchestrator on EFA-capable instance types in all AWS Regions where Amazon SageMaker HyperPod is available. To learn more, see Disaggregated Prefill and Decode for HyperPod inference&nbsp;in the Amazon SageMaker AI Developer Guide.

## 핵심 요약

요약 미지원
