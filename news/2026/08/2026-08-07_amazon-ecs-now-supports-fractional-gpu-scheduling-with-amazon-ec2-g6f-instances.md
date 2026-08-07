---
title: "Amazon ECS now supports fractional GPU scheduling with Amazon EC2 G6f instances"
date: "2026-08-07"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecs-fractional-gpu/"
tags: ["EC2", "2026", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon ECS now supports fractional GPU scheduling with Amazon EC2 G6f instances

**날짜:** 2026년 08월 07일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecs-fractional-gpu/

## 내용

Amazon Elastic Container Service (Amazon ECS) now supports fractional GPU scheduling with Amazon EC2 G6f instances, enabling you to run your workloads on GPU partitions as small as one-eighth of an NVIDIA L4 Tensor Core GPU with 3 GB of GPU memory. Fractional GPUs give you the flexibility to right-size your containers for small-model AI inference, model experimentation, graphics rendering, and other workloads that do not require a full GPU, helping reduce infrastructure costs compared to provisioning a full GPU instance. 
You can request a fractional GPU by setting GPU=0.125, GPU=0.25, or GPU=0.5 in the container definition of your Amazon ECS task definition. Amazon ECS then places the task on a G6f instance that satisfies the request. Fractional GPU configuration is supported on both Amazon ECS Managed Instances and Amazon ECS on EC2. With ECS Managed Instances, you get a fully managed experience where ECS automatically handles instance provisioning, scaling, patching, and lifecycle management, so you can focus on your GPU workloads rather than infrastructure operations. ECS Managed Instances also include capabilities built specifically for accelerated workloads, such as GPU metrics through Amazon CloudWatch Container Insights, and automatic health monitoring that detects GPU hardware failures and replaces unhealthy instances to minimize workload disruption. 
This capability is available in all AWS Regions where Amazon EC2 G6f instances are available. To get started, use the AWS Management Console, AWS CLI, AWS SDKs, AWS CloudFormation, or other infrastructure-as-code tools to configure a capacity provider with G6f instances and specify a fractional GPU value in the container definition of your ECS task definition. To learn more, visit the Amazon ECS fractional GPU documentation and the Amazon EC2 G6 instance page.

## 핵심 요약

요약 미지원
