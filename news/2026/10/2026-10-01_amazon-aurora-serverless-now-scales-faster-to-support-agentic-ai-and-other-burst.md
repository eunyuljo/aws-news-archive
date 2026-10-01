---
title: "Amazon Aurora serverless now scales faster to support agentic AI and other bursty workloads"
date: "2026-10-01"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aurora-serverless-instant-16-acu-scaling/"
tags: ["RDS", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon Aurora serverless now scales faster to support agentic AI and other bursty workloads

**날짜:** 2026년 10월 01일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aurora-serverless-instant-16-acu-scaling/

## 내용

Amazon Aurora serverless now scales in even larger steps, adding up to 16 ACUs to its current capacity within a second and continuing to scale up to 256 ACUs as your workload grows. With this launch, your workload will scale faster and reach capacity that it requires. When the workload finishes, Aurora serverless automatically scales down to zero, so you only pay for what you use. This makes it especially well-suited for agentic AI applications, which typically have bursts of activity, long idle windows, and unpredictable traffic patterns.
This enhancement is enabled by default on all Aurora serverless clusters running on platform version 3 or 4, with no configuration changes required. Existing clusters on platform versions 1 and 2 can upgrade directly to the latest platform version 4 to benefit from these improvements. You can verify your cluster's platform version in the AWS Management Console under the instance configuration section, or via the RDS API's ServerlessV2PlatformVersion parameter.
For pricing details and Region availability, visit Amazon Aurora Pricing. To learn more, read the Aurora serverless scaling documentation, and get started by creating an Aurora serverless database in just a few steps in the AWS Management Console.

## 핵심 요약

요약 미지원
