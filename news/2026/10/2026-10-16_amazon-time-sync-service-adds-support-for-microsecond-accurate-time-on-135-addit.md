---
title: "Amazon Time Sync Service adds support for microsecond-accurate time on 135 additional EC2 instance types in all commercial regions"
date: "2026-10-16"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/time-sync-additional-instances-all-regions"
tags: ["EC2", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# Amazon Time Sync Service adds support for microsecond-accurate time on 135 additional EC2 instance types in all commercial regions

**날짜:** 2026년 10월 16일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/time-sync-additional-instances-all-regions

## 내용

Amazon Time Sync Service introduces support for microsecond-accurate time on 135 additional EC2 instance types—spanning 12 instance families—in all commercial regions. Built on Amazon's proven network infrastructure and the AWS Nitro System, microsecond-accurate time and nanosecond-precision hardware timestamps leverage the reference clocks running in the Nitro System directly, enabling customers to easily order application events, measure 1-way network latency, and increase distributed application transaction speed.
The newly supported families include eight Gen8 families (C8a, C8i, C8i-flex, C8id, M8i, M8i-flex, R8a, and X8i) and four Gen9 families (C9g, C9gd, M9g, and M9gd).
Starting today, customers can access microsecond-accurate time on these additional instance types by creating a Precision Time Placement Group (PTPG), a new placement strategy that allows customers to launch instances with Precision Time Protocol hardware clock (PHC) enabled. Customers that require both low network latency as well as precision time can associate a PTPG with their Cluster Placement Group (CPG), so that their low-latency workloads also benefit from microsecond-accurate time.
For more information, refer to the Amazon Time Sync Service documentation.

## 핵심 요약

요약 미지원
