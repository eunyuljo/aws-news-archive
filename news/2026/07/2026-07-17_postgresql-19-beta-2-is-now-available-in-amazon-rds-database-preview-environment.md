---
title: "PostgreSQL 19 Beta 2 is now available in Amazon RDS Database Preview Environment"
date: "2026-07-17"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/postgresql-19-beta-2-amazon-rds-database-preview-environment/"
tags: ["RDS", "2026", "GA", "preview", "price-reduction", "new-region"]
nav_exclude: true
---

# PostgreSQL 19 Beta 2 is now available in Amazon RDS Database Preview Environment

**날짜:** 2026년 07월 17일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/postgresql-19-beta-2-amazon-rds-database-preview-environment/

## 내용

Amazon RDS for PostgreSQL 19 Beta 2 is now available in the Amazon RDS Database Preview Environment, allowing you to evaluate the pre-release of PostgreSQL 19 on Amazon RDS for PostgreSQL. You can deploy PostgreSQL 19 Beta 2 in the Amazon RDS Database Preview Environment that has the benefits of a fully managed database.  PostgreSQL 19 introduces parallel autovacuum with configurable worker limits, so routine maintenance no longer bottlenecks large databases. The new REPACK CONCURRENTLY command rebuilds tables and reclaims storage online, keeping production databases accessible without third-party extensions. Native SQL Property Graph Queries (SQL/PGQ) let you express relationship traversals directly in standard SQL, eliminating separate application logic. Logical replication now synchronizes sequence values automatically and can be enabled dynamically without a server restart, reducing planned downtime. Beta 2 adds bug fixes and stability improvements from the Beta 1 testing period, including refinements to parallel autovacuum worker coordination and REPACK CONCURRENTLY lock handling.&nbsp;Please refer to PostgreSQL community announcement for more details.  Amazon RDS Database Preview Environment database instances are retained for a maximum period of 60 days and are automatically deleted after the retention period. Amazon RDS database snapshots that are created in the preview environment can only be used to create or restore database instances within the preview environment. You can use the PostgreSQL dump and load functionality to import or export your databases from the preview environment.  Amazon RDS Database Preview Environment database instances are priced as per the pricing in the US East (Ohio) Region.

## 핵심 요약

요약 미지원
