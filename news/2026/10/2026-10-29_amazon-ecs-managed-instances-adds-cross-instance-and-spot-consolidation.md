---
title: "Amazon ECS Managed Instances adds cross-instance and Spot consolidation"
date: "2026-10-29"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/ecs-managed-instances-consolidation/"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon ECS Managed Instances adds cross-instance and Spot consolidation

**날짜:** 2026년 10월 29일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/ecs-managed-instances-consolidation/

## 내용

Today, Amazon Elastic Container Service (Amazon ECS) Managed Instances introduces two infrastructure optimization updates: cross-instance and Spot consolidation. Cross-instance consolidation evaluates tasks running across multiple underutilized instances together, packing them onto fewer instances to raise utilization and lower costs. Spot consolidation extends this capability to Spot capacity, consolidating underutilized Spot Instances after first verifying replacement capacity is available.
Amazon ECS Managed Instances provisions, configures, and operates right-sized Amazon EC2 instances for your workloads, balancing availability and cost. Its infrastructure optimization continuously monitors your fleet, reclaiming idle capacity and consolidating underutilized instances with graceful start-before-stop task replacement. Until now, optimization evaluated each instance in isolation for replacement, which worked well when a capacity provider was configured with diverse instance types. However, when a capacity provider was configured with a narrow range of instance types, there were fewer opportunities to consolidate multiple underutilized instances, because no single replacement could yield savings. With cross-instance consolidation, ECS now evaluates and repacks tasks across multiple instances simultaneously. For example, in our testing with a capacity provider configured for c9g instances with a minimum size of 4xlarge, running 261 tasks (each 1 vCPU, 1.94 GiB), cross-instance consolidation reduced the fleet from 19 instances (seven 4xlarge, seven 8xlarge, four 12xlarge, and one 24xlarge) to 13 instances (eight 4xlarge and five 8xlarge), while raising CPU utilization from 42% to 91% and memory utilization from 41% to 88%. Spot consolidation applies the same approach to Spot capacity, first verifying replacement capacity is available. With these enhancements, ECS Managed Instances delivers deeper cost optimization for both your On-Demand and Spot workloads.
Cross-instance and Spot consolidation are now available at no additional cost in all AWS Regions, and apply automatically to all existing and new ECS Managed Instances capacity providers. To learn more, see our documentation.

## 핵심 요약

요약 미지원
