---
title: "Amazon RDS for Db2 now supports object-level audit policies"
date: "2026-11-21"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-db2-supports-object-level-audit-policies"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Amazon RDS for Db2 now supports object-level audit policies

**날짜:** 2026년 11월 21일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-db2-supports-object-level-audit-policies

## 내용

Amazon RDS for Db2 now supports object-level audit policies, giving you fine-grained control over which database objects are audited. You can create custom audit policies and attach them to specific tables, users, groups, roles, and authorities in your RDS for Db2 databases. 
With object-level audit policies, you can focus on auditing the objects that matter most — for example, a single table that contains sensitive data or a specific user — without generating audit records for your entire database. Object-level audit policies complement the existing database-level audit logging in Amazon RDS for Db2. You can use both at the same time, and they operate independently.&nbsp; 
Amazon RDS provides stored procedures to create, modify, attach, detach, and drop object-level audit policies. Audit records are uploaded to the same Amazon S3 bucket that you configured for Db2 audit logging. 
Object-level audit policies for Amazon RDS for Db2 are available in all AWS Regions where Amazon RDS for Db2 is available. To get started see the Amazon RDS User Guide.&nbsp;

## 핵심 요약

요약 미지원
