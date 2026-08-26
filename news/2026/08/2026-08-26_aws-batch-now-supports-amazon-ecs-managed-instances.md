---
title: "AWS Batch now supports Amazon ECS Managed Instances"
date: "2026-08-26"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-batch-on-ecs-managed-instances/"
tags: ["EC2", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Batch now supports Amazon ECS Managed Instances

**날짜:** 2026년 08월 26일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-batch-on-ecs-managed-instances/

## 내용

AWS Batch now supports Amazon ECS Managed Instances (ECS MI) as a new compute option, enabling you to run GPU-accelerated and compute-intensive batch workloads on AWS-managed infrastructure. With AWS Batch on ECS MI you can now access GPU-accelerated instances while AWS handles AMI updates, security patching,&nbsp;and instance lifecycle automatically, eliminating the operational overhead of customer-managed Amazon EC2 infrastructure.  To get started, create an AWS Batch on ECS MI compute environment using the AWS Batch CreateComputeEnvironment API or the AWS Batch Management Console. You can specify your allowed instance types and networking configuration in the managedInstancesProvider block, associate the compute environment with a job queue, and submit jobs using On-Demand, Spot, or reserved capacity.  AWS Batch on ECS Managed Instances is supported in all AWS Regions where AWS Batch is available. For more information, see the AWS Batch User Guide.

## 핵심 요약

요약 미지원
