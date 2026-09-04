---
title: "Amazon ECS Managed Daemons now support non-critical daemons"
date: "2026-09-04"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/ecs-managed-daemons-non-critical/"
tags: ["RDS", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon ECS Managed Daemons now support non-critical daemons

**날짜:** 2026년 09월 04일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/ecs-managed-daemons-non-critical/

## 내용

Amazon Elastic Container Service (Amazon ECS) now support non-critical Managed Daemons for ECS Managed Instances. You can configure a daemon as non-critical so that your mission-critical application tasks continue running uninterrupted, even when a daemon fails, stops, or becomes unhealthy. 
Amazon ECS Managed Daemons lets you centrally deploy and manage software agents independently of application deployments to ensure consistent coverage and compliance across your container infrastructure. For some mission-critical applications, uninterrupted execution of application tasks may matter more than auxiliary daemon functionality like logging or metrics collection. With this launch, you can now configure a managed daemon as non-critical so that its failure does not cause your application tasks to churn. When a non-critical daemon task fails, stops, or becomes unhealthy, the container instance remains active, your existing application tasks continue running uninterrupted, ECS continues placing new application tasks on it, and instance registration is never blocked, so your tasks launch immediately even when the daemon fails to start. Amazon ECS emits an EventBridge event when a daemon task fails to start and records service action logs for both critical and non-critical daemons, giving you full observability into daemon health. 
To get started, you can use AWS Console, CLI, CloudFormation, or AWS SDKs to create a non-critical daemon by setting the critical parameter to false when creating or updating a daemon. Non-critical daemons are available in all AWS Regions where Amazon ECS Managed Daemons are supported. To learn more, refer to our documentation page.

## 핵심 요약

요약 미지원
