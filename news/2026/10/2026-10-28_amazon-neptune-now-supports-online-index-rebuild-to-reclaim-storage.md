---
title: "Amazon Neptune now supports online index rebuild to reclaim storage"
date: "2026-10-28"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/neptune-online-index-rebuild/"
tags: ["Config", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon Neptune now supports online index rebuild to reclaim storage

**날짜:** 2026년 10월 28일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/neptune-online-index-rebuild/

## 내용

Amazon Neptune Database now supports online index rebuild, a new capability that helps database administrators and application teams defragment Neptune indexes and reclaim unused storage space without taking their database offline. Over time, insert, update, and delete operations create gaps of unused space within data pages, keeping the VolumeBytesUsed metric artificially elevated even after data is deleted. This fragmentation increases I/O costs and degrades query performance for teams running Gremlin, openCypher, or SPARQL workloads at scale.
With online index rebuild, read and write queries continue uninterrupted on both the writer instance and read replicas throughout the entire rebuild process. You can target all indexes, only quad indexes, or only dictionary indexes, making this feature well-suited for post-deletion cleanup, periodic maintenance, storage limit management, and performance tuning on heavily fragmented databases. Tunable concurrency and write buffer size settings let you balance rebuild speed against workload impact, while built-in storage safety mechanisms protect against storage exhaustion during the operation.
Online index rebuild is available starting with Amazon Neptune engine release 1.5.0.0 on provisioned writer instances, in all regions where Amazon Neptune Database is supported. To learn more about configuring and running online index rebuild, including API references and tuning guidance, visit the Amazon Neptune documentation.

## 핵심 요약

요약 미지원
