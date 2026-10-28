---
title: "Amazon ECS now supports GPU sharing with NVIDIA Multi-Process Service (MPS)"
date: "2026-10-28"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ecs-gpu-sharing-nvidia-mps/"
tags: ["EC2", "2026", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon ECS now supports GPU sharing with NVIDIA Multi-Process Service (MPS)

**날짜:** 2026년 10월 28일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ecs-gpu-sharing-nvidia-mps/

## 내용

Amazon Elastic Container Service (Amazon ECS) now supports GPU sharing with NVIDIA Multi-Process Service (MPS), enabling you to run multiple Amazon ECS tasks concurrently on a single NVIDIA GPU. GPU sharing helps you increase GPU utilization and reduce infrastructure costs for workloads that use only part of a GPU's capacity, such as small-model inference, AV/ADAS simulations, embedding generation, and multi-model serving. 
With GPU sharing, you can pack more workloads onto each GPU instance without changing your application code. You define the GPU memory each container needs and can optionally set a maximum share of GPU compute, and Amazon ECS places tasks on GPUs with available capacity as your services scale and deploy. GPU sharing is supported on Amazon ECS Managed Instances and Amazon ECS on Amazon EC2. On Amazon ECS Managed Instances, Amazon ECS also monitors the MPS control daemon that enables sharing on each instance. If the daemon stops or becomes unhealthy, Amazon ECS automatically replaces the instance and moves your tasks to healthy capacity, so your GPU workloads keep running without manual intervention. 
To get started, use the AWS Management Console, AWS CLI, AWS SDKs, AWS CloudFormation, or other infrastructure-as-code tools to create a capacity provider with NVIDIA GPU instances, set the GPU sharing strategy and memory in the container definition of your task definition, and create a service on that capacity provider. This capability is available in all AWS commercial and AWS GovCloud (US) Regions. To learn more, visit the Amazon ECS GPU sharing documentation.

## 핵심 요약

요약 미지원
