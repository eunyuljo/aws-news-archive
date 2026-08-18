---
title: "Amazon EC2 Auto Scaling now supports batch instance termination"
date: "2026-08-18"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-auto-scaling-batch-termination"
tags: ["EC2", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EC2 Auto Scaling now supports batch instance termination

**날짜:** 2026년 08월 18일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-auto-scaling-batch-termination

## 내용

Amazon EC2 Auto Scaling now supports batch instance termination in a single API call. You can now pass up to 100 instance IDs to the TerminateInstanceInAutoScalingGroup API to terminate them as a batch, reducing the number of API calls needed to scale down your Auto Scaling groups. 
Batch termination is designed for workloads that need to rapidly scale down, such as AI/ML training jobs, container orchestrators, or event-driven architectures that spin up large fleets temporarily. All instances in a batch are validated atomically before termination begins, and existing Auto Scaling behaviors such as lifecycle hooks and load balancer connection draining are preserved for each instance in the batch. 
This feature is available in all AWS Regions at no additional cost. 
To learn more, visit Amazon EC2 Auto Scaling User Guide and Amazon EC2 Auto Scaling API Reference Guide.

## 핵심 요약

요약 미지원
