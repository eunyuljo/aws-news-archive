---
title: "Amazon CloudWatch Synthetics now supports multilocation canaries"
date: "2026-06-20"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-synthetics-multilocation/"
tags: ["CloudWatch", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon CloudWatch Synthetics now supports multilocation canaries

**날짜:** 2026년 06월 20일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-synthetics-multilocation/

## 내용

Today, Amazon CloudWatch Synthetics announces support for multilocation canaries, allowing developers and site reliability engineers to run the same canary across multiple AWS Regions simultaneously from a single point of management. Previously, monitoring application availability from multiple geographic locations required creating and managing separate canaries in each Region, adding operational overhead and increasing the risk of configuration drift. With multilocation canaries, you create and manage a canary in one primary Region, and CloudWatch Synthetics automatically replicates it to the additional Regions you choose, consolidating all run data, metrics, and artifacts in the primary Region. 
Multilocation canaries help you ensure consistent user experience worldwide, identify region-specific performance bottlenecks, and validate that third-party dependencies like CDNs and payment processors work across all locations. Replica canaries run independently, giving you resilient monitoring coverage across geographic locations. You can also configure alarms that activate only when issues are detected from multiple locations, increasing alert confidence and helping your team focus on real customer-impacting problems. Amazon CloudWatch Synthetics multilocation canaries are available in all AWS commercial Regions that support CloudWatch Synthetics. You can upgrade existing single-region canaries to multilocation by adding replica Regions without recreating them. For more information about regional availability, see the AWS Region table. 
To learn more about CloudWatch Synthetics, see Using synthetic monitoring in the Amazon CloudWatch User Guide. To get started, visit the Amazon CloudWatch product page.

## 핵심 요약

요약 미지원
