---
title: "Amazon ECS now supports configurable deployment circuit breaker settings"
date: "2026-07-02"
service: "ECS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-circuit-breaker-settings/"
tags: ["ECS", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# Amazon ECS now supports configurable deployment circuit breaker settings

**날짜:** 2026년 07월 02일
**서비스:** ECS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-circuit-breaker-settings/

## 내용

Amazon Elastic Container Service (Amazon ECS) now gives you more control over when a service deployment is considered failed and automatically rolled back. You can now customize deployment circuit breaker settings to match your application's startup behavior, deployment needs, and tolerance for task failures, so rollback works the way you need across different applications and environments.  The ECS deployment circuit breaker automatically detects failed deployments and rolls them back to the last successful deployment once a failure threshold is reached. With this launch, you can set the deployment circuit breaker threshold using either a fixed task failure count or a percentage of your service's desired task count, and choose how failures are counted using either a consecutive model, where the counter resets when a healthy task starts, or a cumulative model, where failures keep adding up throughout the deployment. For example, you can set lower thresholds for faster rollbacks in development and test environments, or allow more tolerance for applications that experience expected startup failures before stabilizing.  This feature is available in all AWS Regions where Amazon ECS is available. You can configure deployment circuit breaker settings for new and existing ECS services using the AWS Management Console, AWS CLI, AWS SDKs, AWS CloudFormation, AWS CDK, and Terraform. To learn more, see the ECS deployment circuit breaker documentation.

## 핵심 요약

요약 미지원
