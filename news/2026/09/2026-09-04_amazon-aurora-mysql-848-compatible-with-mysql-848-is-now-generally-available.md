---
title: "Amazon Aurora MySQL 8.4.8 (compatible with MySQL 8.4.8) is now generally available"
date: "2026-09-04"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-aurora-mysql-848-available/"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon Aurora MySQL 8.4.8 (compatible with MySQL 8.4.8) is now generally available

**날짜:** 2026년 09월 04일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-aurora-mysql-848-available/

## 내용

Starting today, Amazon Aurora MySQL-Compatible Edition 8.4 will support MySQL 8.4.8. In addition to several security enhancements and bug fixes, Aurora MySQL 8.4.8 includes several improvements, such as support for post-quantum TLS (PQ-TLS) key exchange, transaction timeout, multi-source replication, and delayed replication. PQ-TLS provides you with post-quantum cryptography options for encrypting your data in-transit. Transaction timeout helps prevent performance issues caused by long-running transactions blocking innoDB purge. 
Multi-source replication allows consolidation of data from multiple sources into a single replica to enable critical use-cases, such as merging shards, reporting, and backups. Delayed replication lets you set a configurable replication lag to protect against accidental data loss. To learn more about these replication features, please refer to the launch announcement. For more details, refer to the Aurora MySQL 8.4 and MySQL 8.4.8 release notes. 
You can upgrade your databases during scheduled maintenance windows using automatic minor version upgrades. To simplify operations at scale, enable automatic minor version upgrades and use the AWS Organizations Upgrade Rollout Policy to orchestrate upgrades across your clusters in phases. You can perform minor version upgrades in-place or via snapshot restore. This release is supported in all AWS Regions where Aurora MySQL is available. 
Amazon Aurora is designed for high performance and availability at global scale with full MySQL compatibility. It provides scale-to-zero serverless compute, Aurora Global Database for multi-Region resilience, Aurora I/O-Optimized for improved price performance on I/O-intensive workloads, and built-in security and continuous backups. To get started, take a look at Aurora’s getting started page.

## 핵심 요약

요약 미지원
