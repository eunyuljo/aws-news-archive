---
title: "Amazon ECS advanced deployment strategies now available in AWS European Sovereign Cloud"
date: "2026-07-22"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-adv-deployments-eu-sovereign-cloud/"
tags: ["Lambda", "2026", "GA", "performance"]
nav_exclude: true
---

# Amazon ECS advanced deployment strategies now available in AWS European Sovereign Cloud

**날짜:** 2026년 07월 22일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-adv-deployments-eu-sovereign-cloud/

## 내용

Amazon Elastic Container Service (Amazon ECS) now supports built-in blue/green, linear, and canary deployment strategies in the AWS European Sovereign Cloud, making software updates for containerized applications safer and allowing you to release new application versions faster with greater confidence. Built directly into Amazon ECS, these capabilities eliminate the need for custom deployment tooling while providing production-ready controls including deployment lifecycle hooks, bake time, and quick rollback. 
With these strategies, Amazon ECS provisions a new application version alongside the existing version and allows you to validate it before shifting production traffic. Blue/green deployments shift traffic in a single step, linear deployments shift traffic in equal increments over a specified period, and canary deployments shift a small percentage initially before shifting the remainder. You can use deployment lifecycle hooks, including Lambda hooks and pause hooks, to run custom validation logic and approval workflows at specific deployment stages. You can also configure bake time to evaluate the new version after traffic has shifted, and roll back without downtime if regressions are identified. To automatically detect failures, configure Amazon CloudWatch alarms or Amazon ECS deployment circuit breaker, or initiate a rollback directly using the StopServiceDeployment API. 
These capabilities are available for Amazon ECS services using Application Load Balancers (ALB), Network Load Balancers (NLB), and Amazon ECS Service Connect. You can configure deployments using the AWS Management Console, AWS CLI, AWS SDKs, or infrastructure-as-code tools on new or existing Amazon ECS services. To learn more, see our documentation for Amazon ECS blue/green, linear, and canary deployments, and deployment lifecycle hooks.

## 핵심 요약

요약 미지원
