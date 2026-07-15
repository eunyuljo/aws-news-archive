---
title: "AWS Elastic Disaster Recovery now supports Amazon EBS volume initialization rate"
date: "2026-07-15"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-hydration/"
tags: ["S3", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# AWS Elastic Disaster Recovery now supports Amazon EBS volume initialization rate

**날짜:** 2026년 07월 15일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-hydration/

## 내용

AWS Elastic Disaster Recovery (AWS DRS) now supports the Amazon EBS volume initialization rate, helping recovered volumes reach full performance faster during drills and recoveries. When DRS restores EBS volumes from snapshots, the data loads from Amazon S3 in the background, and I/O to blocks that haven't loaded yet can be slower until initialization finishes. With this launch, you can set a volume initialization rate on your DRS-managed EC2 launch template, and DRS applies it automatically when it creates volumes during recovery — bringing your applications to full storage performance on a predictable timeline. 
This is especially valuable for I/O-intensive workloads such as databases, where fast, consistent storage performance is critical to meeting your recovery time objectives. You set the rate once on the launch template, and DRS preserves it across the updates it makes for rightsizing or disk changes. If the rate cannot be applied for a given recovery, DRS completes recovery without it, so your recovery is never blocked. 
AWS DRS support for the EBS volume initialization rate is available in all AWS Regions and environments where the EBS volume initialization rate is offered. You are charged per GB based on the full snapshot size and the rate you specify; for details, see Amazon EBS pricing. To learn more, see the AWS Elastic Disaster Recovery User Guide.

## 핵심 요약

요약 미지원
