---
title: "Amazon Aurora MySQL now supports multi-source replication and delayed replication"
date: "2026-09-04"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-aurora-mysql-multisourcerep-delayedrep/"
tags: ["RDS", "2026", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon Aurora MySQL now supports multi-source replication and delayed replication

**날짜:** 2026년 09월 04일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-aurora-mysql-multisourcerep-delayedrep/

## 내용

Starting today, Amazon Aurora MySQL supports two new replication capabilities: multi-source replication and delayed replication. Multi-source replication lets a single Aurora MySQL cluster replicate from multiple source databases at the same time, making it easier to consolidate data from separate MySQL databases. This enables critical use-cases, such as merging shards or aggregating data from separate databases (e.g. regional or departmental instances) into a central location for operational workflows, such as reporting and backups. To learn more, please refer to the MySQL multi-source replication documentation.  Delayed replication lets you configure a binlog replica to intentionally lag behind its source by a set period of time, giving you a simple safeguard against human error and logical data corruption. If a harmful change is made on the source, you can recover quickly by stopping replication to the replica before the change is applied and promoting it, without performing a full database restore. A delayed replica also provides a convenient fallback during upgrades and a way to inspect an earlier state of your data. To learn more, please refer to the MySQL delayed replication documentation.  Together, these capabilities give you greater flexibility and stronger data protection when replicating into Aurora MySQL. Multi-source replication and Delayed replication are supported on Aurora MySQL version 8.4.8 and higher, in all AWS Regions where Aurora MySQL is available. For additional information on Aurora MySQL disaster recovery, see the guidance from our solutions library. To learn more, please refer to Aurora MySQL 8.4 release notes.  Amazon Aurora is designed for high performance and availability at global scale with full MySQL compatibility. It provides scale-to-zero serverless compute, Aurora Global Database for multi-Region resilience, Aurora I/O-Optimized for improved price performance on I/O-intensive workloads, and built-in security and continuous backups. To get started, take a look at Aurora’s getting started page.&nbsp;

## 핵심 요약

요약 미지원
