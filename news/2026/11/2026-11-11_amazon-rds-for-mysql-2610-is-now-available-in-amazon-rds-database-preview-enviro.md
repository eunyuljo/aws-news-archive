---
title: "Amazon RDS for MySQL 26.10 is now available in Amazon RDS Database Preview Environment"
date: "2026-11-11"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/rds-mysql-26-10-preview-environment/"
tags: ["RDS", "2026", "GA", "preview", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon RDS for MySQL 26.10 is now available in Amazon RDS Database Preview Environment

**날짜:** 2026년 11월 11일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/rds-mysql-26-10-preview-environment/

## 내용

Starting today, Amazon RDS for MySQL 26.10 is available in the Amazon RDS Database Preview Environment, allowing you to evaluate the pre-release of MySQL 26.10 on Amazon RDS for MySQL. 
MySQL 26.10 includes bug fixes, security patches, and some improvements to READ COMMITTED workload performance and purge lag warnings in the error log. On busy READ COMMITTED workloads, NUMA systems performance could be impacted as each read view that closed required a global mutex. Read-view objects can now be reused which eliminates the global mutex on closure. The error log now reports warnings when the history-list length (HLL) crosses innodb_max_purge_lag and when purge lag begins delaying DML, so you can detect purge backlogs before they affect performance. To learn more, please refer to the MySQL 26.10 release notes. 
Amazon RDS Database Preview Environment database instances are retained for a maximum period of 60 days and are automatically deleted after the retention period. Amazon RDS database snapshots that are created in the Preview Environment can only be used to create or restore database instances within the Preview Environment. Amazon RDS Database Preview Environment database instances are priced as per the pricing in the US East (Ohio) Region.

## 핵심 요약

요약 미지원
