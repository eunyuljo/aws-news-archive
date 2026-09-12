---
title: "Amazon SageMaker HyperPod now supports model caching for faster inference autoscaling and reduced cold starts"
date: "2026-09-12"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/sgm-hyperpod-model-caching-inf/"
tags: ["S3", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker HyperPod now supports model caching for faster inference autoscaling and reduced cold starts

**날짜:** 2026년 09월 12일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/sgm-hyperpod-model-caching-inf/

## 내용

Amazon SageMaker HyperPod now supports model caching, an inference optimization that pre-loads model weights and container images onto cluster nodes so pods start in seconds instead of minutes. 
When running LLM inference at scale for workloads like chat assistants, agentic pipelines, RAG, and document analysis, cold start is a real bottleneck. Deployments and scale-out events spend most of their time downloading container images and model weights. As model size increases, this gets worse, with large models taking tens of minutes before they can serve traffic. 
Model caching solves this with two independent capabilities. The weights cache stores model weights on local NVMe so pods read from fast local storage instead of pulling from S3 or FSx over the network. The image cache pre-pulls the container image so pods skip the ECR download entirely. If a pod lands on a node without a warm cache, it falls back to pulling from the original source automatically, so there is no risk of pods getting stuck or failing. 
Benchmarks across models from 57 GB to 145 GB show around 60% faster scale-out, and the image cache cuts over two minutes of image-pull time (97% reduction). The benefit grows with model size while retaining the reliability of the original source path. 
Customers enable model caching through the HyperPod Inference Operator by adding a modelCacheConfig section to their InferenceEndpointConfig or JumpStartModel resource. The operator handles the full lifecycle with no manual setup or cleanup. 
Model caching is now generally available in all regions where SageMaker HyperPod is available. To get started, see the SageMaker HyperPod documentation. 
&nbsp;

## 핵심 요약

요약 미지원
