---
title: "Amazon Aurora now supports PostgreSQL major version 18"
date: "2026-06-17"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-aurora-postgresql-major-version-18/"
tags: ["RDS", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon Aurora now supports PostgreSQL major version 18

**날짜:** 2026년 06월 17일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-aurora-postgresql-major-version-18/

## 내용

Amazon Aurora PostgreSQL-Compatible Edition now supports PostgreSQL major version 18, starting with version 18.3. This release brings community improvements to query performance and database management, and introduces support for pg_roaringbitmap, a new extension that performs fast, memory-efficient set operations on large collections of integers. This enables use cases such as audience segmentation, tag-based filtering, and permission checks directly in the database without application-layer processing.  PostgreSQL 18 introduces B-tree skip scans, which improve query performance, and reduce index storage and maintenance overhead. Major version upgrades now retain optimizer statistics, ensuring consistent query performance immediately after upgrading without waiting for statistics to be regenerated. Logical replication can now stream large transactions in parallel, reducing replication lag and keeping downstream systems more current. Please refer to the Amazon Aurora PostgreSQL release notes for details.  You can upgrade your database using several options including RDS Blue/Green deployments, upgrade in-place, or restoring a snapshot. Learn more about upgrading your database instances in the Amazon Aurora User Guide. Aurora PostgreSQL 18.3 is available in all commercial AWS Regions and AWS GovCloud (US) Regions.  Amazon Aurora is designed for unparalleled high performance and availability at global scale with full PostgreSQL and MySQL compatibility. It provides built-in security, continuous backups, serverless compute, up to 15 read replicas, automated multi-Region replication, and integrations with other AWS services. To get started with Amazon Aurora, take a look at our getting started page.

## 핵심 요약

요약 미지원
