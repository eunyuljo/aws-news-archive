---
title: "Amazon RDS for PostgreSQL now supports PostgreSQL 19 Beta 4 in the Amazon RDS Database Preview Environment"
date: "2026-09-25"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/postgresql-19-beta-4-amazon-rds-database-preview-environment/"
tags: ["RDS", "2026", "preview", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon RDS for PostgreSQL now supports PostgreSQL 19 Beta 4 in the Amazon RDS Database Preview Environment

**날짜:** 2026년 09월 25일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/postgresql-19-beta-4-amazon-rds-database-preview-environment/

## 내용

Starting today, Amazon RDS for PostgreSQL 19 Beta 4 is available in the Amazon RDS Database Preview Environment, allowing you to evaluate the pre-release of PostgreSQL 19 on Amazon RDS for PostgreSQL.
PostgreSQL 19 Beta 4 refines the query performance and autovacuum management capabilities introduced in earlier releases and includes bug fixes and stability improvements since Beta 3. Fixes include pg_stat_autovacuum_scores view reporting for TOAST tables and corrected freeze-score scaling so you can tune autovaccum prioritization effectively. Parallel autovacuum now shares a rebalanced cost limit across its workers to keep maintenance on large tables within your configured limits. Refer to the PostgreSQL community announcement for more details.
Amazon RDS Database Preview Environment database instances are retained for a maximum period of 60 days and are automatically deleted after the retention period. Amazon RDS database snapshots that are created in the Preview Environment can only be used to create or restore database instances within the Preview Environment. You can use the PostgreSQL dump and load functionality to import or export your databases from the Preview Environment. Amazon RDS Database Preview Environment database instances are priced as per the pricing in the US East (Ohio) Region.

## 핵심 요약

요약 미지원
