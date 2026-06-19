---
title: "Amazon ECS announces faster service auto scaling"
date: "2026-06-19"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ecs-faster-autoscaling/"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon ECS announces faster service auto scaling

**날짜:** 2026년 06월 19일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ecs-faster-autoscaling/

## 내용

Amazon ECS service auto scaling now detects and responds to load changes faster with support for high resolution (20-second) metrics and metric publishing optimizations. In AWS benchmarking tests, time to trigger scale-out improved from 363 seconds to 86 seconds (76% faster, 4.2x), and total time to scale and provision new tasks improved from 386 seconds to 109 seconds (72% faster, 3.5x). Faster service auto scaling also enables you to reduce baseline capacity and lower compute costs while maintaining service reliability and performance as workload demand fluctuates.  Amazon ECS service auto scaling automatically adjusts task counts to meet workload demand with comprehensive scaling policies, including predictive scaling for recurring traffic patterns, scheduled scaling for planned events, and target tracking to scale dynamically on real-time metrics. With today's launch, target tracking policies for CPU and memory utilization now support 20-second metric resolution, in addition to the default 60-second resolution, for faster scaling signal detection. To get started, use the AWS Console, CLI, CloudFormation, or AWS SDKs to configure 20-second resolution for CPU or memory utilization metrics when creating or updating your ECS service, then configure a target tracking policy selecting the corresponding high-resolution predefined metric.  This feature is available in all AWS commercial and AWS GovCloud (US) Regions, across all ECS compute options: AWS Fargate, Amazon ECS Managed Instances, and Amazon EC2. High-resolution metrics are subject to standard CloudWatch charges; for a pricing example, see Amazon CloudWatch pricing. To learn more, see our documentation and the launch blog post.

## 핵심 요약

요약 미지원
