---
title: "Amazon RDS for Oracle now supports July 2026 Release Update"
date: "2026-08-26"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-rds-oracle-july-2026-release-update"
tags: ["RDS", "2026", "security"]
nav_exclude: true
---

# Amazon RDS for Oracle now supports July 2026 Release Update

**날짜:** 2026년 08월 26일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-rds-oracle-july-2026-release-update

## 내용

Amazon Relational Database Service (Amazon RDS) for Oracle now supports the Oracle July 2026 Release Update (RU) for Oracle Database versions 19c, 21c and 26ai. We recommend upgrading to the July 2026 RU as it includes security updates for Oracle database products. 
Starting with July 2026 releases, the naming format for an RU in Oracle Database 19c changes to &lt;version&gt;.ru-&lt;YYYY-MM&gt;.mrp-&lt;YYYY-MM&gt;.r&lt;N&gt;. For example, the RDS for Oracle July 2026 quarterly RU for Oracle Database 19c is named 19.0.0.0.ru-2026-07.mrp-2026-07.r1. When Oracle releases a monthly Critical Security Patch Update (CSPU) for Oracle Database 19c and 26ai, Amazon RDS will make it available as an MRP version that bundles the CSPU with additional Oracle-recommended fixes. Oracle Database 21c RUs retain their existing naming format. For details, see Release updates and monthly recommended patches.&nbsp; 
You can apply the July 2026 RU from the Amazon RDS Management Console, or by using the AWS SDK or CLI. To automatically apply updates to your database instance during your maintenance window, enable Automatic Minor Version Upgrade. 
You can also use AWS Organizations upgrade rollout policy to stagger automatic minor version upgrades for your Amazon RDS database instances. This feature allows you to automatically apply updates to non-production environments, validate the updates, and then automatically apply the same update to production environments. For additional details about using AWS Organizations upgrade rollout policy for automatic minor version upgrades, refer to Amazon RDS for Oracle documentation.&nbsp;

## 핵심 요약

요약 미지원
