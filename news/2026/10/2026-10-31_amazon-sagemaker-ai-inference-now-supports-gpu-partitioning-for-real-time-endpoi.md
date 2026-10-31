---
title: "Amazon SageMaker AI inference now supports GPU partitioning for real-time endpoints"
date: "2026-10-31"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-gpu-partitioning/"
tags: ["SageMaker", "2026", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI inference now supports GPU partitioning for real-time endpoints

**날짜:** 2026년 10월 31일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-gpu-partitioning/

## 내용

Amazon SageMaker AI inference now supports GPU partitioning, enabling you to run several models on a single GPU instead of dedicating a whole accelerator to each one. Using NVIDIA Multi-Instance GPU (MIG) technology, SageMaker AI divides a GPU into as many as seven isolated partitions, each with its own memory and compute. Customers serving small and mid-size models, such as fine-tuned variants, embedding models, rerankers, and classifiers, previously had to give every model an entire accelerator, so an instance hosted no more models than it had GPUs and paid for GPU capacity those models could never use.
With GPU partitioning, you choose how to divide the GPUs behind your endpoint and place each model on a partition sized to fit it. Several models then share one accelerator with hardware-enforced isolation, so a busy model cannot take memory or throughput from the models beside it. Right-sizing an accelerator to a workload also opens up newer instance generations that would otherwise be more capacity than a single model needs. You configure GPU partitioning when you create an endpoint that hosts inference components, and you continue to invoke each model by name, so your application code doesn't change.
GPU partitioning is available on P4d, P5, G7, and G7e instances in US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (Ireland). To learn more, visit the Amazon SageMaker AI deployment page and see the Amazon SageMaker AI Developer Guide.

## 핵심 요약

요약 미지원
