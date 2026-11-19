---
title: "Amazon RDS now supports fast storage volume initialization"
date: "2026-11-19"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-fast-storage-volume-initialization/"
tags: ["S3", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon RDS now supports fast storage volume initialization

**날짜:** 2026년 11월 19일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-fast-storage-volume-initialization/

## 내용

Amazon RDS now initializes storage volumes faster when you perform a point-in-time restore (PITR), create a read replica, or convert a Single-AZ instance to Multi-AZ. Each of these operations creates storage volumes from a snapshot, and the data blocks are downloaded from Amazon S3 before you can access them. With fast storage volume initialization, you get a fully performant DB instance in a predictable amount of time. 
Previously, the initialization rate varied with your workload and with which blocks were accessed. As there was no dedicated bandwidth, so you could see increased I/O latency and had no way to tell when an instance would reach full performance. Now, each database instance is initialized at up to 4 TiB per hour, across every gp3 and io2 storage volume attached to the instance. If concurrent initialization across your account exceeds the available bandwidth, the remaining blocks initialize on a best-effort basis, so initialization is never slower than today. Your DB instance stays available and usable while initialization runs. 
Fast storage volume initialization is enabled by default and no action is required. To follow progress, use the StorageOperationStatus and StorageOperationPercentProgress fields in the Amazon RDS console, the DescribeDBInstances API, the AWS Command Line Interface (CLI), or AWS SDKs. 
This capability is available at no additional cost for RDS for MariaDB, RDS for MySQL, RDS for PostgreSQL, RDS for Db2, RDS for Microsoft SQL Server, and RDS for Oracle, in all commercial AWS Regions and the AWS GovCloud (US) Regions. To learn more, see Amazon RDS storage in the Amazon RDS User Guide.

## 핵심 요약

요약 미지원
