---
title: "AWS Lambda adds support for GPU instances on Lambda Managed Instances"
date: "2026-11-19"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-gpu-managed-instances/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda adds support for GPU instances on Lambda Managed Instances

**날짜:** 2026년 11월 19일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-gpu-managed-instances/

## 내용

AWS Lambda now supports GPU-accelerated Event Functions on Lambda Managed Instances using EC2 G-series instances. You can now run GPU-accelerated workloads including AI&nbsp;inference, media processing, 3D rendering, scientific computing, and financial simulations on Lambda without managing&nbsp;GPU drivers, frameworks, or scaling. Lambda runs multiple invocations concurrently in each execution environment and scales responsively based on GPU utilization, CPU utilization, and concurrency to keep your GPUs busy&nbsp;and reduce costs. GPU-accelerated functions integrate with the same 200+ AWS event sources as other&nbsp;Event Functions, so you can add GPU compute as another step in your serverless application. 
Running GPU workloads today requires customers to provision hardware, manage&nbsp;driver and framework dependencies, and build custom scaling and capacity management. With this launch, you can go from code to a running GPU workload in minutes. Lambda provides GPU base images preconfigured with frameworks such as&nbsp;vLLM, SGLang, and PyTorch.&nbsp;You can run workloads with large artifacts using container images and NVMe ephemeral storage of up to 32 GB each. To reduce startup time, Lambda supports Seekable OCI (SOCI) lazy loading and streaming artifacts directly from Amazon S3.&nbsp;For resilience, you can select G-series instance types from multiple generations in the allowed instance types for your capacity provider. Lambda provisions instances from the newest generation that meets your function requirements and falls back to older generations when capacity is unavailable. 
GPU-accelerated Event Functions on Lambda Managed Instances is available in all AWS Commercial Regions where Lambda Managed Instances and EC2 G-series instances are available. You can configure GPU-accelerated functions using the AWS Console, AWS CLI, AWS SDKs,&nbsp;AWS CloudFormation, AWS CDK, or AWS SAM.&nbsp;You can also use this feature through&nbsp;coding assistants such as Kiro, Claude Code, or Codex by installing the Lambda Managed Instances skill&nbsp;from the Agent Toolkit for AWS. You pay the EC2 On-Demand price&nbsp;(Savings Plans and Reserved Instances apply)&nbsp;for your instance, plus a 9.75% Lambda management fee and $0.20 per million requests. To learn more, visit the AWS Lambda Developer Guide and AWS Lambda Pricing.

## 핵심 요약

요약 미지원
