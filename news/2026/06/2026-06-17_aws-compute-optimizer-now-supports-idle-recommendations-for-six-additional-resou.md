---
title: "AWS Compute Optimizer now supports idle recommendations for six additional resource types"
date: "2026-06-17"
service: "DynamoDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-compute-optimizer-six-new-idle"
tags: ["DynamoDB", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Compute Optimizer now supports idle recommendations for six additional resource types

**날짜:** 2026년 06월 17일
**서비스:** DynamoDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-compute-optimizer-six-new-idle

## 내용

AWS Compute Optimizer now identifies idle resources for Amazon DynamoDB provisioned tables, Amazon ElastiCache (Redis and Valkey), Amazon MemoryDB, Amazon DocumentDB (provisioned and serverless), Amazon WorkSpaces, and Amazon SageMaker endpoints. This expansion enables you to detect unused resources across more of your AWS environment and identify potential cost savings. 
Compute Optimizer analyzes utilization metrics to determine whether a resource is idle. Customers can set this lookback period based on the nature of their workloads. For each resource type, Compute Optimizer evaluates service-specific signals such as consumed capacity, cache hits, active connections, and CPU utilization. When Compute Optimizer identifies potential idle resources, it surfaces these recommendations, along with detailed utilization metrics and estimated savings in the console, enabling you to evaluate recommendations before acting. You can also view idle resource recommendations across all AWS accounts in your organization through the Cost Optimization Hub, with de-duplicated estimated savings with other recommendations on the same resources. 
For more information about the AWS Regions where Compute Optimizer is available, see the AWS Region table. For more information about AWS Compute Optimizer, visit our product page and documentation. You can start using AWS Compute Optimizer through the AWS Management Console, AWS CLI, and AWS SDK.

## 핵심 요약

요약 미지원
