---
title: "Amazon RDS for SQL Server supports additional SQL trace flags"
date: "2026-09-03"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/rds-sqlserver-supports-additional-trace-flags/"
tags: ["RDS", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon RDS for SQL Server supports additional SQL trace flags

**날짜:** 2026년 09월 03일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/rds-sqlserver-supports-additional-trace-flags/

## 내용

Amazon RDS for SQL Server&nbsp;supports 18 additional SQL trace flags that you can enable through database parameter groups. Trace flags are configuration switches that modify SQL Server engine behavior — such as query optimizer cardinality estimation, lock escalation, statistics management, and memory handling — to allow database administrators to fine-tune performance and address workload-specific challenges. With this expansion, you have greater flexibility to optimize and stabilize your SQL Server workloads directly within your managed RDS environment. 
The newly supported trace flags include: 647, 652, 1448, 3654, 4138, 4139, 7745, 8285, 8780, 9432, 9481, 9492, 9592, 11024, 11042, 12502, 12618, and 12656. These trace flags address scenarios such as query plan optimization, DDL performance improvements, availability group replication, Query Store behavior, automatic plan correction, and known engine bug mitigations. Because trace flags modify core SQL Server engine behavior, you should test them in a non-production environment before applying them to production instances. Some trace flags can impact system performance, increase memory usage, or change query execution plans in unexpected ways. 
Trace flags are available in all AWS Regions where Amazon RDS for SQL Server is supported. To get started, update your RDS parameter group to enable the desired trace flags and apply it to your DB instance.&nbsp;To learn more, see Amazon RDS for SQL Server User Guide.

## 핵심 요약

요약 미지원
