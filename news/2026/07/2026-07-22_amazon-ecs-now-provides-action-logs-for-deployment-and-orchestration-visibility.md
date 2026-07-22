---
title: "Amazon ECS now provides Action Logs for deployment and orchestration visibility"
date: "2026-07-22"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-action-logs/"
tags: ["S3", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon ECS now provides Action Logs for deployment and orchestration visibility

**날짜:** 2026년 07월 22일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-action-logs/

## 내용

Today, Amazon Elastic Container Service (Amazon ECS) introduces Action Logs, a new observability feature that delivers detailed, timestamped records of the actions Amazon ECS performs on behalf of customers during service deployments and ECS Managed Daemon updates. By surfacing service-side operations that were previously invisible, Action Logs help you monitor and troubleshoot your workloads directly, without contacting AWS Support or manually correlating data from multiple sources. 
With Action Logs, you gain visibility into key deployment state transitions of service deployments, Managed Daemon updates. Each log entry includes the event name, log level(INFO, WARN, OR ERROR), relevant resource ARNs, and a status reason, helping you reduce mean time to resolution when issues arise. You can opt in at the cluster level through the Amazon ECS console or by using Amazon CloudWatch vended logs APIs, and choose to deliver logs to Amazon CloudWatch Logs, Amazon S3, or Amazon Kinesis Data Firehose depending on your operational needs. At launch, Amazon Q in the Amazon ECS console integrates with Action Logs to automatically detect deployment issues such as circuit breaker rollbacks and unstable service revisions, providing customers with root cause analysis, resource-level comparisons, and step-by-step remediation guidance without leaving the console. Standard CloudWatch Logs, Amazon S3, or Amazon Data Firehose pricing applies for log ingestion and storage. For pricing details, see Amazon CloudWatch Pricing. 
Amazon ECS Action Logs are available in all AWS Regions, including the AWS GovCloud (US) Regions. To learn more, refer Monitor Amazon ECS operations with Action Logs in Amazon ECS Developer Guide.

## 핵심 요약

요약 미지원
