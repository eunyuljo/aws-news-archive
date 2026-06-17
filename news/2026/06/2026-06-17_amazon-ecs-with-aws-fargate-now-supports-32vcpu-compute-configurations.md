---
title: "Amazon ECS with AWS Fargate now supports 32vCPU compute configurations"
date: "2026-06-17"
service: "ECS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ecs-fargate-32vcpu"
tags: ["ECS", "2026", "new-region", "performance", "security", "ai-ml"]
nav_exclude: true
---

# Amazon ECS with AWS Fargate now supports 32vCPU compute configurations

**날짜:** 2026년 06월 17일
**서비스:** ECS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ecs-fargate-32vcpu

## 내용

Amazon Elastic Container Service (Amazon ECS) with AWS Fargate now supports 32vCPU compute configurations, enabling customers to run more demanding applications with greater flexibility and performance. AWS Fargate offers 32vCPU tasks with the following memory configurations: 60 GiB, 120 GiB, or 244 GiB, for both x86-based and ARM-based workloads on Linux. These new task sizes extend Amazon ECS’s capability to support high-performance computing use-cases, large-scale data processing, AI inference, and other compute-intensive workloads. With 32vCPUs and up to 244 GiB of memory, Amazon ECS customers can now deploy larger containers and scale applications beyond previous limits, all while leveraging the reliability, security, and scalability of AWS Fargate.  To use the new 32vCPU task sizes, simply configure your task definitions to specify 32 as the vCPU value and select one of the new memory options (60, 120, or 244 GiB), then deploy your Amazon ECS services or tasks as usual via the AWS Management Console, CLI, or your infrastructure-as-code of choice. The new vCPU and memory configurations are available on both Fargate and Fargate Spot capacity providers, and existing Compute Savings Plans apply automatically. For pricing details, refer to AWS Fargate pricing page.  The 32vCPU tasks are available with Amazon ECS and AWS Fargate in all AWS commercial and AWS GovCloud (US) Regions. To learn more, refer to the Amazon ECS documentation.

## 핵심 요약

요약 미지원
