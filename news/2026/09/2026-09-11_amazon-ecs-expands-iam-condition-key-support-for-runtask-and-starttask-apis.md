---
title: "Amazon ECS expands IAM condition key support for RunTask and StartTask APIs"
date: "2026-09-11"
service: "ECS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-expands-condition-key-support/"
tags: ["ECS", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon ECS expands IAM condition key support for RunTask and StartTask APIs

**날짜:** 2026년 09월 11일
**서비스:** ECS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-expands-condition-key-support/

## 내용

Amazon Elastic Container Service (Amazon ECS) now supports the IAM condition keys for CPU and memory resources on the RunTask and StartTask APIs. Administrators can use these keys to enforce consistent CPU and memory limits across all methods of launching ECS tasks. This helps organizations prevent unexpected cost overruns and keep workloads aligned with their resource policies. Previously, the ecs:task-cpu and ecs:task-memory condition keys were available only on the RegisterTaskDefinition, CreateService, and UpdateService APIs. These condition keys are now extended on the RunTask and StartTask APIs. Now, IAM policies that reference these condition keys are evaluated when tasks are launched through RunTask and StartTask as well, giving administrators a single, unified mechanism to control resource allocation across their ECS environments. 
This enhancement is available in all AWS Regions where Amazon ECS is available, at no additional cost. To learn more about using condition keys with Amazon ECS, refer to our documentation.

## 핵심 요약

요약 미지원
