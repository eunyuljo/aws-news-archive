---
title: "Amazon SageMaker AI announces training session APIs for serverless model customization"
date: "2026-10-23"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/training-session-apis-on-sagemaker-ai"
tags: ["SageMaker", "2026", "GA", "security", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI announces training session APIs for serverless model customization

**날짜:** 2026년 10월 23일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/training-session-apis-on-sagemaker-ai

## 내용

Amazon SageMaker AI serverless model customization now supports training session APIs, giving customers full control over their post-training algorithm without provisioning or managing GPU infrastructure. Managed techniques, including SFT, DPO, and other reinforcement learning methods, let customers pick a technique and a model and have SageMaker AI run the training. With training session APIs, teams get to write the training loop, whether that's reproducing SFT or DPO on their own terms or implementing a custom loss, a new RL reward signal, a data curriculum, or an algorithm straight from the latest research. Operations such as forward_backward(), optim_step(), and sample() become API calls against a live, stateful session, so customers compose whatever training procedure their technique requires while SageMaker AI handles GPU allocation, model and LoRA loading, distributed execution, fault recovery, checkpoint storage, and security.  Customers can call these operations directly from their own Python code to drive reinforcement learning, supervised fine-tuning, or custom training objectives against a live session, with checkpointing and resume built in. Billing is per token processed, so local computation like reward scoring isn't billed as GPU time. SageMaker AI is also releasing the SageMaker training sessions cookbook, a set of ready-to-run SFT and RL recipes customers can use as blueprints for their own training loops. 
Training session APIs are generally available today in US East (N. Virginia), US West (Oregon), and Asia Pacific (Mumbai). To get started, install the SageMaker Python SDK and clone the cookbook, or launch a notebook in SageMaker Studio and connect a coding agent. To learn more, visit the documentation&nbsp;and the Amazon SageMaker AI webpage.

## 핵심 요약

요약 미지원
