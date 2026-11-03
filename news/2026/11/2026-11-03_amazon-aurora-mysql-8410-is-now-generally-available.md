---
title: "Amazon Aurora MySQL 8.4.10 is now generally available"
date: "2026-11-03"
service: "Aurora"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-aurora-mysql-8410-available/"
tags: ["Aurora", "2026", "GA", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon Aurora MySQL 8.4.10 is now generally available

**날짜:** 2026년 11월 03일
**서비스:** Aurora
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-aurora-mysql-8410-available/

## 내용

Starting today, Amazon Aurora MySQL-Compatible Edition 8.4 supports MySQL 8.4.10. We recommend upgrading to the newer minor versions to accept fixes for Common Vulnerabilities and Exposures (CVEs) in prior versions of MySQL and to benefit from bug fixes, performance improvements, and new functionality added by the MySQL community. For more details, refer to the Aurora MySQL 8.4 and MySQL 8.4.10 release notes. 
Aurora MySQL 8.4.10 adds support for global transaction identifiers (GTID) tags, which lets you assign a user-defined tag to&nbsp;GTIDs&nbsp;to help you&nbsp;identify and group related transactions in binary log replication. This release also adds&nbsp;support for a maximum of 50,000 simultaneous connections per DB instance, which allows connection-intensive applications to scale without adding a connection pooling layer. Learn more about maximum connections best practices in the Amazon Aurora MySQL User Guide. &nbsp; 
You can upgrade your databases during scheduled maintenance windows using automatic minor version upgrades. To simplify operations at scale, enable automatic minor version upgrades and use the AWS Organizations Upgrade Rollout Policy to orchestrate upgrades across your clusters in phases, validating on lower-priority environments before upgrading your most critical ones. You can perform minor version upgrades in-place or via snapshot restore. Learn more about performing version upgrades in the Amazon Aurora User Guide. This release is supported in all AWS Regions where Aurora MySQL is available. 
Amazon Aurora is designed for high performance and availability at global scale with full MySQL compatibility. It provides scale-to-zero serverless compute, Aurora Global Database for multi-Region resilience, Aurora I/O-Optimized for improved price performance on I/O-intensive workloads, and built-in security and continuous backups. To get started, take a look at Aurora's getting started page.

## 핵심 요약

요약 미지원
