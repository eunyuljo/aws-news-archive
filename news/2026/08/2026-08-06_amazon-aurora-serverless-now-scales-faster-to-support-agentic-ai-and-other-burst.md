---
title: "Amazon Aurora serverless now scales faster to support agentic AI and other bursty workloads"
date: "2026-08-06"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aurora-serverless-instant-12-acu-scaling"
tags: ["RDS", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon Aurora serverless now scales faster to support agentic AI and other bursty workloads

**날짜:** 2026년 08월 06일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aurora-serverless-instant-12-acu-scaling

## 내용

Amazon Aurora serverless now delivers higher initial capacity during scale-up events, reaching up to 12 ACUs within a second and continuing to scale up to 256 ACUs as your workload grows. When the workload finishes, Aurora serverless automatically scales down to zero. This makes it especially well-suited for agentic AI applications, which typically have bursts of activity, long idle windows, and unpredictable traffic patterns. Aurora serverless handles all of it automatically, scaling capacity with your agents, so you only pay for what you use.  This enhancement is enabled by default on all Aurora serverless clusters running on platform version 3 or 4, with no configuration changes required. Existing clusters on platform versions 1 and 2 can upgrade directly to the latest platform version 4 to benefit from these improvements. You can verify your cluster's platform version in the AWS Management Console under the instance configuration section, or via the RDS API's ServerlessV2PlatformVersion parameter.  For pricing details and Region availability, visit Amazon Aurora Pricing. To learn more, read the Aurora serverless scaling documentation, and get started by creating an Aurora serverless database in just a few steps in the AWS Management Console.

## 핵심 요약

요약 미지원
