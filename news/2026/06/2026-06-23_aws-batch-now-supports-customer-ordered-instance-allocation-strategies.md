---
title: "AWS Batch now supports customer-ordered instance allocation strategies"
date: "2026-06-23"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/batch-ordered-allocation-strategies/"
tags: ["EC2", "2026", "new-region", "performance"]
nav_exclude: true
---

# AWS Batch now supports customer-ordered instance allocation strategies

**날짜:** 2026년 06월 23일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/batch-ordered-allocation-strategies/

## 내용

AWS Batch now offers the Best Fit Progressive Ordered (BFPO) and Spot Capacity Optimized Prioritized (SCOP) allocation strategies, giving you more control over instance type prioritization in your compute environments. BFPO and SCOP enable you to manually define instance type ordering based on your workload-specific performance characteristics.  To use these features in AWS Batch, specify BEST_FIT_PROGRESSIVE_ORDERED allocation strategy for your on-demand compute environments or SPOT_CAPACITY_OPTIMIZED_PRIORITIZED for your Amazon EC2 Spot compute environments and provide an ordered list of instance types or families. These features are available via the AWS Batch API (CreateComputeEnvironment or UpdateComputeEnvironment) or the AWS Batch Management Console.  BFPO and SCOP allocation strategies are supported today in all AWS Regions where AWS Batch is available. For more information, see the AWS Batch User Guide.

## 핵심 요약

요약 미지원
