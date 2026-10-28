---
title: "Amazon Aurora serverless now supports up to 384 ACUs"
date: "2026-10-28"
service: "Aurora"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-serverless-supports-384-acu/"
tags: ["Aurora", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Aurora serverless now supports up to 384 ACUs

**날짜:** 2026년 10월 28일
**서비스:** Aurora
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-serverless-supports-384-acu/

## 내용

Amazon Aurora serverless now supports database capacity of up to 384 Aurora Capacity Units (ACUs) for Aurora PostgreSQL-Compatible Edition, a 50% increase from the previous maximum of 256 ACUs. Each ACU provides approximately 2 gibibytes (GiB) of memory with corresponding CPU and networking, so a single Aurora serverless database can now scale up to 768 GiB of memory. When the workload completes, Aurora serverless automatically scales down to zero. This makes Aurora serverless especially well-suited for agentic AI applications, which typically have bursts of activity, long idle windows, and unpredictable traffic patterns. Aurora serverless handles all of it automatically, scaling capacity with your agents, so you only pay for what you use. 
With 384 ACU support, customers can now use Aurora serverless for even more demanding workloads while continuing to scale down to zero when not in use, paying only for the capacity consumed. For new clusters, select a supported Aurora PostgreSQL engine version and set your maximum capacity up to 384 ACUs. For existing clusters on Platform Version 4, simply modify the cluster to update the maximum capacity setting (and the engine version if needed). There will be no downtime if your database is already on Platform Version 4. For existing clusters on older platform versions, upgrade to Platform Version 4 through a pending maintenance action. 384 ACU support is available for Aurora PostgreSQL versions 18.4, 17.10, 16.14, 15.18, and 14.23, running on Platform Version 4. 
To learn more, see Aurora serverless capacity in the Amazon Aurora User Guide. For pricing details and Region availability, visit Amazon Aurora Pricing. &nbsp;To get started, create or modify an Aurora serverless database in the AWS Management Console.

## 핵심 요약

요약 미지원
