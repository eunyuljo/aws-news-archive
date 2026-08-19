---
title: "PostgreSQL 19 Beta 3 is now available in Amazon RDS Database Preview Environment"
date: "2026-08-19"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/postgresql-19-beta-3-amazon-rds-database-preview-environment/"
tags: ["RDS", "2026", "GA", "preview", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# PostgreSQL 19 Beta 3 is now available in Amazon RDS Database Preview Environment

**날짜:** 2026년 08월 19일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/postgresql-19-beta-3-amazon-rds-database-preview-environment/

## 내용

Starting today, Amazon RDS for PostgreSQL 19 Beta 3 is available in the Amazon RDS Database Preview Environment, allowing you to evaluate the pre-release of PostgreSQL 19 on Amazon RDS for PostgreSQL. 
PostgreSQL 19 Beta 3 adds new capabilities for query performance and autovacuum management. The new pg_stat_autovacuum_scores view helps you monitor and tune autovacuum prioritization. Parallel autovacuum can now use multiple workers to speed up maintenance on large tables. The new pg_plan_advice module lets you lock in efficient query plans to avoid unexpected slowdowns. Eager aggregation improves analytical queries by grouping data earlier, so queries process fewer rows and complete faster. Beta 3 also includes bug fixes and stability improvements from the Beta 2 testing period. Refer to the PostgreSQL community announcement for more details. 
Amazon RDS Database Preview Environment database instances are retained for a maximum period of 60 days and are automatically deleted after the retention period. Amazon RDS database snapshots that are created in the Preview Environment can only be used to create or restore database instances within the Preview Environment. You can use the PostgreSQL dump and load functionality to import or export your databases from the Preview Environment. Amazon RDS Database Preview Environment database instances are priced as per the pricing in the US East (Ohio) Region.

## 핵심 요약

요약 미지원
