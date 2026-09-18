---
title: "Amazon ECS deployment observability for Amazon ECS Managed Daemons in AWS Management Console"
date: "2026-09-18"
service: "ECS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-daemon-deployment-console/"
tags: ["ECS", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon ECS deployment observability for Amazon ECS Managed Daemons in AWS Management Console

**날짜:** 2026년 09월 18일
**서비스:** ECS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-daemon-deployment-console/

## 내용

Amazon Elastic Container Service (Amazon ECS) now provides a consolidated deployment view for Amazon ECS Managed Daemons, giving you a single place to see how far a deployment has progressed, what is failing, and what could stop it. This helps you monitor Managed Daemon deployments at a glance and resolve issues faster, whether a rollout is in progress or you are reviewing what happened after it completed, eliminating the need to piece together deployment status from multiple sources.  The deployment view presents a lifecycle timeline with timestamps at each step and the total deployment duration, including the rollback path if a deployment is interrupted. Progress bars for each capacity provider track instances completed, in progress, and remaining, as well as instances draining and being replaced when a capacity provider is removed. A monitoring panel shows deployment circuit breaker, deployment alarm, and container health check state, each with live Amazon CloudWatch alarm detail and whether it can stop the deployment. If a daemon task fails, the affected capacity provider shows the stop reason with links to the task, its logs, and the matching troubleshooting guide, including the failure that caused a rollback. The view also displays target and source revisions with instance counts, drain percentage, and bake time.  This enhancement is available as a console-only view in all AWS Commercial Regions at no additional cost. To get started with Amazon ECS Managed Daemons, refer to our documentation.

## 핵심 요약

요약 미지원
