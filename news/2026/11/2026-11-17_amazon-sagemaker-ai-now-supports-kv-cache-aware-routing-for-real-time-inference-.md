---
title: "Amazon SageMaker AI now supports KV cache-aware routing for real-time inference endpoints"
date: "2026-11-17"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-kv-cache-routing/"
tags: ["SageMaker", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI now supports KV cache-aware routing for real-time inference endpoints

**날짜:** 2026년 11월 17일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-kv-cache-routing/

## 내용

Amazon SageMaker AI now supports KV cache-aware routing for real-time inference endpoints, enabling you to reduce time to first token for LLM workloads with long or repeated prompts. Serving engines such as vLLM store the computed key-value (KV) cache for repeated prompt starts such as shared system prompts, documents, and conversation history, to skip repeated work. Across several instances, a request that lands where the cache is missing recomputes it. Under high load, instances also evict cached blocks to free GPU memory, including shared prompts and earlier conversation turns.
KV cache-aware routing sends each request to the instance that holds the longest matching part of its prompt in cache. The vLLM container reports the cache blocks it stores and evicts, and SageMaker routes with that live view. If the lookup is slow or finds no match, the endpoint falls back to load-aware routing, so the request is still served. Prefix-aware routing suits stable shared prompts, short prompts, or moderate load. KV cache-aware routing suits long prompts, high load, and limited GPU memory.
Customers can now enable this feature by setting `RoutingStrategy` to `KV_AWARE` on a production variant and adding one environment variable so the container reports cache events. Customer can invoke the endpoint with the same APIs and OpenAI-compatible payloads. It supports single-model endpoints and inference components, including LoRA adapters, on GPU instances. It requires the AWS vLLM Deep Learning Container version 0.33.0 or later with at least two instances or inference component copies. Detailed observability metrics show KV cache hit rate. There is no additional charge for KV cache-aware routing.
KV cache-aware routing is available today in all AWS Regions where Amazon SageMaker AI is available. To get started, update to the latest AWS SDK or CLI. To learn more, visit the Amazon SageMaker AI inference page and see the API documentation.

## 핵심 요약

요약 미지원
