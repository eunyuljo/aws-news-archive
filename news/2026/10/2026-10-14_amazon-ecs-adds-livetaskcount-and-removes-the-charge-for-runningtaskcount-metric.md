---
title: "Amazon ECS adds LiveTaskCount and removes the charge for RunningTaskCount metric"
date: "2026-10-14"
service: "ECS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/ecs-service-metrics/"
tags: ["ECS", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon ECS adds LiveTaskCount and removes the charge for RunningTaskCount metric

**날짜:** 2026년 10월 14일
**서비스:** ECS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/ecs-service-metrics/

## 내용

Today, Amazon Elastic Container Service (Amazon ECS) announces LiveTaskCount, a new ECS service metric that reports how many tasks are actively running in your service, available to all customers at no additional charge. Additionally, the existing RunningTaskCount metric in Amazon CloudWatch Container Insights no longer incurs a charge.
LiveTaskCount reports the number of actively running ECS tasks across all desired states (ACTIVATING, RUNNING, and DEACTIVATING), including tasks still running while transitioning to a stopped state, for example, tasks undergoing connection draining during a scale-in event. This comprehensive state coverage makes LiveTaskCount well suited for autoscaling policies and capacity planning where a complete view of active, metric-generating tasks is required. It is available at no charge as part of ECS service utilization metrics and does not require opting in to CloudWatch Container Insights. The existing CloudWatch Container Insights RunningTaskCount metric tracks tasks where both the current and desired state are RUNNING, and continues to serve as a health and stability signal for customers who depend on it. With today's update, RunningTaskCount is now available at no additional charge for all CloudWatch Container Insights users.
These updates are available in all AWS Regions where Amazon ECS is available. No action is required, and the pricing change for RunningTaskCount takes effect beginning October 1, 2026, and applies automatically. To learn more, see ECS CloudWatch metrics and ECS Container Insights metrics. For a pricing example, see Amazon CloudWatch pricing.

## 핵심 요약

요약 미지원
