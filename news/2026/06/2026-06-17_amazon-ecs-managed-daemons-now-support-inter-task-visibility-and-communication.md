---
title: "Amazon ECS Managed Daemons now support inter-task visibility and communication"
date: "2026-06-17"
service: "ECS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/ecs-managed-daemons-pid-ipc-modes/"
tags: ["ECS", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon ECS Managed Daemons now support inter-task visibility and communication

**날짜:** 2026년 06월 17일
**서비스:** ECS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/ecs-managed-daemons-pid-ipc-modes/

## 내용

Amazon ECS Managed Daemons now support inter-task visibility and communication, enabling customers to deploy tracing, profiling, and security agents that require access to application processes and shared IPC resources on ECS Managed Instances.  With this launch, you can configure two new settings in ECS daemon definitions: pidMode controls whether the daemon can see all processes on the instance, and ipcMode controls whether the daemon shares an IPC namespace with other containers on the instance. Setting either to "shared" grants the daemon access to the respective namespace; the default of "none" keeps daemons isolated from application containers and other tasks. These settings let you run process-aware and IPC-dependent agents as ECS daemons instead of embedding them as sidecars in application task definitions. ECS places exactly one daemon task per managed instance and starts daemons before application tasks, so platform teams can deploy and update agents independently with consistent coverage across all workloads.  To get started, register a daemon task definition specifying pidMode or ipcMode set to "shared" using the AWS Console, CLI, CloudFormation, or AWS SDKs, then create or update a daemon with associated ECS Managed Instances capacity providers in your clusters. This feature is now available in all AWS Regions at no additional cost. For more details, refer to our documentation.

## 핵심 요약

요약 미지원
