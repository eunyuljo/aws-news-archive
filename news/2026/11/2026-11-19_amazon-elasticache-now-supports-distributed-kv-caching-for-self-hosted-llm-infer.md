---
title: "Amazon ElastiCache now supports distributed KV caching for self-hosted LLM inference"
date: "2026-11-19"
service: "ElastiCache"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/announcing-distributed-kv-caching-for-self-hosted-llms-with-amazon-elasticache/"
tags: ["ElastiCache", "2026", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon ElastiCache now supports distributed KV caching for self-hosted LLM inference

**날짜:** 2026년 11월 19일
**서비스:** ElastiCache
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/announcing-distributed-kv-caching-for-self-hosted-llms-with-amazon-elasticache/

## 내용

Amazon ElastiCache for Valkey now offers fully managed distributed KV caching, a new capability that reduces self-hosted large language model (LLM) inference costs by up to 40% and time to first token (TTFT) by up to 80%. Customers who self-host LLMs pay for redundant GPU work because small, isolated caches on each server can't hold or share the growing context AI agents and chat applications resend. Distributed KV caching extends GPU-local caches with a shared tier so any server can reuse KV state for days across sessions, routing shifts, and server failures. GPUs can fetch cached KV state in milliseconds to serve more requests and respond faster. 
Distributed KV caching runs on cache.i8ge.48xlarge nodes in the same Availability Zone as the GPU fleet and connects to GPUs through Remote Direct Memory Access (RDMA) over Elastic Fabric Adapter (EFA).&nbsp;Distributed KV caching works with open-weight, fine-tuned, and custom models, whether they use full, sparse, hybrid, or other attention designs. You can add distributed KV caching to the inference engines you already use, including vLLM, SGLang, and TensorRT-LLM, through the LMCache connector with a configuration change. You can also use the open-source KVTrace tool to estimate the cost and latency reductions on your own application traffic before deploying anything, at no charge. 
Distributed KV caching is available today on ElastiCache for Valkey in 13 AWS Regions across the US, Europe, and Asia Pacific. To get started, create a cluster with cache.i8ge.48xlarge nodes using the AWS CLI&nbsp;in the same AZ as your GPU fleet and adding the endpoint to your inference engine. To learn more, read the AWS blog for a technical deep dive and performance results, or visit the Amazon ElastiCache documentation. For pricing, see the Amazon ElastiCache pricing page.

## 핵심 요약

요약 미지원
