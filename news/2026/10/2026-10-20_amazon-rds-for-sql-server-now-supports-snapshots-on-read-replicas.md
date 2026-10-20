---
title: "Amazon RDS for SQL Server now supports snapshots on read replicas"
date: "2026-10-20"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/rds-sqlserver-supports-snapshots-on-read-replicas"
tags: ["RDS", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon RDS for SQL Server now supports snapshots on read replicas

**날짜:** 2026년 10월 20일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/rds-sqlserver-supports-snapshots-on-read-replicas

## 내용

Amazon Relational Database Service (Amazon RDS) for SQL Server now supports creating DB snapshots directly on read replica instances. Previously, you could create snapshots only on standalone and primary DB instances. You can now snapshot a read replica without promoting it first, giving you more flexibility in your backup and disaster recovery (DR) workflows.
Previously, enabling Multi-AZ on a promoted read replica meant waiting for an initial full snapshot to finish before the conversion could begin. On larger storage configurations—such as io2 volumes up to 64 TiB—that first snapshot could take a long time, making DR timelines hard to predict. Now, Amazon RDS for SQL Server maintains snapshot data on the read replica throughout its lifecycle, so the first snapshot after promotion completes faster. This shortens the time to enable Multi-AZ and helps you plan DR exercises with more predictable recovery timelines. You can take manual snapshots of a read replica, turn on automated backups by setting a backup retention period greater than zero, and retain automated backups when you delete the replica; however, point-in-time recovery (PITR) from a read replica isn't supported.
This feature works for both in-region and cross-region read replicas. It's available for SQL Server Enterprise Edition on all SQL Server versions that support read replicas, in all AWS Regions where Amazon RDS for SQL Server read replicas are available, including the AWS GovCloud (US) Regions.
To learn more, see Working with read replicas for Microsoft SQL Server. For pricing details, see Amazon RDS for SQL Server Pricing.

## 핵심 요약

요약 미지원
