---
title: "Amazon EC2 Auto Scaling now supports reservations then balanced Availability Zone distribution"
date: "2026-07-01"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/ec2-auto-scaling-res-then-balanced/"
tags: ["EC2", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon EC2 Auto Scaling now supports reservations then balanced Availability Zone distribution

**날짜:** 2026년 07월 01일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/ec2-auto-scaling-res-then-balanced/

## 내용

Amazon EC2 Auto Scaling now offers reservations-then-balanced, a new Availability Zone (AZ) distribution strategy that prioritizes launching instances into your capacity reservations before distributing remaining capacity evenly across Availability Zones. This enables you to maximize utilization of pre-purchased capacity such as On-Demand Capacity Reservations (ODCRs), Capacity Blocks, and Interruptible Capacity Reservations, while retaining the operational simplicity and resilience of Auto Scaling.  Starting today, you can configure reservations-then-balanced by setting the capacity distribution strategy in the AvailabilityZoneDistribution configuration of your Auto Scaling group and targeting reservations by Capacity Reservation Group ARN or by individual Capacity Reservation IDs. There is no additional charge to use reservations-then-balanced; you continue to pay standard EC2 pricing for your reservations and any On-Demand or Spot instances launched by the group. 
Reservations-then-balanced is available today in all AWS commercial Regions. To learn more, visit the Amazon EC2 Auto Scaling User Guide.

## 핵심 요약

요약 미지원
