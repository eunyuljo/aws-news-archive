---
title: "ECS Service Connect now supports Zone-Aware routing"
date: "2026-07-02"
service: "ECS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-service-connect-zone-aware/"
tags: ["ECS", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# ECS Service Connect now supports Zone-Aware routing

**날짜:** 2026년 07월 02일
**서비스:** ECS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-service-connect-zone-aware/

## 내용

Amazon Elastic Container Service&nbsp;(Amazon ECS) introduces zone-aware routing for ECS Service Connect, enabling customers to reduce cross Availability Zone (AZ) data transfer costs and latency by automatically prioritizing service-to-service traffic within the same AZ.  With this launch, ECS Service Connect preferentially routes requests to endpoints in the same AZ as the originating task while dynamically adjusting traffic weights as endpoints scale to maintain balanced load across target services. Previously, as customers distributed their applications across AZs for resiliency, service-to-service traffic led to significant cross-zone data transfer, requiring trade-offs between cost and resilience. Zone-aware routing eliminates this trade-off, and when local endpoints become unhealthy or fall below capacity thresholds, traffic automatically redistributes across healthy AZs to maintain availability without overloading any single zones.  Zone-aware routing is enabled by default for all new and existing services and requires no additional infrastructure or application code changes. Existing services require a one-time redeployment to enable the new routing behavior. You can use Amazon VPC Flow Logs with AZ metadata to monitor cross-AZ traffic patterns and validate routing effectiveness.&nbsp;This feature is available in all AWS commercial and AWS GovCloud (US) Regions,&nbsp;where ECS Service Connect is supported at no additional cost.&nbsp;For more details, refer to our documentation and launch blog post.

## 핵심 요약

요약 미지원
