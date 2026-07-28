---
title: "Amazon RDS for SQL Server now supports restoring TDE databases on Mult-AZ instances"
date: "2026-07-28"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/rds-sql-server-supports-tde-for-maz/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon RDS for SQL Server now supports restoring TDE databases on Mult-AZ instances

**날짜:** 2026년 07월 28일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/rds-sql-server-supports-tde-for-maz/

## 내용

Amazon Relational Database Service (Amazon RDS) for SQL Server now supports restoring Transparent Data Encryption (TDE)-enabled SQL Server databases on Multi-AZ instances and instances configured with a read replica in the same region, using native backup and restore. Previously, TDE-enabled database restore was available only for Single-AZ instances, requiring you to disable TDE or migrate to a Single-AZ configuration before restoring encrypted databases.  You can restore TDE-enabled database backups directly to Amazon RDS for SQL Server Multi-AZ instances and instances configured with a read replica in the same region. Back up your existing TDE certificate, store it in Amazon S3, and restore it to your Amazon RDS instance with the TDE option enabled.&nbsp;Then, restore your TDE-enabled database backup from Amazon S3 using Amazon RDS native backup and restore. This simplifies your migration and recovery workflows when you require both encryption at rest with TDE and the high availability of Multi-AZ deployments.  This feature is available in all AWS Regions where Amazon RDS for SQL Server is supported. To learn more, see the Amazon RDS for SQL Server User Guide.

## 핵심 요약

요약 미지원
