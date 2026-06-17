---
title: "PostgreSQL 19 Beta 1 is now available in Amazon RDS Database Preview Environment"
date: "2026-06-17"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/postgresql-19-beta-1-amazon-rds-database-preview-environment/"
tags: ["RDS", "2026", "GA", "preview", "price-reduction", "new-region"]
nav_exclude: true
---

# PostgreSQL 19 Beta 1 is now available in Amazon RDS Database Preview Environment

**날짜:** 2026년 06월 17일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/postgresql-19-beta-1-amazon-rds-database-preview-environment/

## 내용

Amazon RDS for PostgreSQL 19 Beta 1 is now available in the Amazon RDS Database Preview Environment, allowing you to evaluate the pre-release of PostgreSQL 19 on Amazon RDS for PostgreSQL. You can deploy PostgreSQL 19 Beta 1 in the Amazon RDS Database Preview Environment that has the benefits of a fully managed database.  PostgreSQL 19 adds native graph query support via SQL Property Graph Queries (SQL/PGQ), so you can express complex relationship traversals directly in standard SQL instead of building separate application logic or syncing data across two databases. It also introduces support for concurrent table repacking that rebuilds tables and reclaims unused storage, so production databases stay accessible during routine table maintenance. Logical replication now synchronizes sequence values to the replica automatically, eliminating manual sequence reconciliation after major version upgrade cutover. Logical replication can also be enabled dynamically without a server restart, reducing planned downtime. Please refer to PostgreSQL community announcement for more details.  Amazon RDS Database Preview Environment database instances are retained for a maximum period of 60 days and are automatically deleted after the retention period. Amazon RDS database snapshots that are created in the preview environment can only be used to create or restore database instances within the preview environment. You can use the PostgreSQL dump and load functionality to import or export your databases from the preview environment.  Amazon RDS Database Preview Environment database instances are priced as per the pricing in the US East (Ohio) Region.

## 핵심 요약

요약 미지원
