---
title: "Amazon ECS Action Logs now cover tasks, container instances, and capacity providers"
date: "2026-11-21"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ecs-action-logs-expanded-troubleshooting"
tags: ["S3", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon ECS Action Logs now cover tasks, container instances, and capacity providers

**날짜:** 2026년 11월 21일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ecs-action-logs-expanded-troubleshooting

## 내용

Amazon Elastic Container Service (Amazon ECS) now extends Action Logs to include tasks, container instances, clusters, and capacity providers, so you can see why your tasks failed or why your clusters didn't scale as desired. Action Logs provide detailed, timestamped records of the actions Amazon ECS performs on your behalf, and until now covered service deployments and managed daemon updates. With the expanded coverage, you can diagnose task failures and scaling issues yourself, and resolve them faster than before, without contacting AWS support. If you use Action Logs already, you receive the new events automatically with no configuration changes. 
When a task fails to start, Action Logs show the reason. Examples include image pull failures, missing permissions for Amazon EBS volumes, or lack of available IP addresses in the subnet. When a running task stops, you can see the container exit code and the health check that triggered the stop. For cluster infrastructure, Action Logs record container instance registration and draining, Amazon EC2 instances that fail to register with a cluster, capacity provider changes, and managed scaling actions, including when an Amazon EC2 Auto Scaling group reaches its maximum size. Each log entry includes the event name, log level (INFO, WARN, or ERROR), relevant resource ARNs, and a status reason. 
Action Logs is available in AWS Regions, including the AWS GovCloud (US) Regions.&nbsp;You can opt in at the cluster level through the Amazon ECS console or the Amazon CloudWatch vended logs APIs, and deliver logs to Amazon CloudWatch Logs, Amazon S3, or Amazon Data Firehose. Standard pricing for each destination applies. To learn more, see Monitor Amazon ECS operations with Action Logs in the Amazon ECS Developer Guide.

## 핵심 요약

요약 미지원
