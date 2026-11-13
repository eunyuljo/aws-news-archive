---
title: "Amazon RDS for SQL Server now supports M8id and R8id instances"
date: "2026-11-13"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/rds-sqlserver-supports-m8id-r8id-instances"
tags: ["RDS", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon RDS for SQL Server now supports M8id and R8id instances

**날짜:** 2026년 11월 13일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/rds-sqlserver-supports-m8id-r8id-instances

## 내용

Amazon Relational Database Service (Amazon RDS) for SQL Server now supports M8id and R8id instances. These instances are powered by custom Intel Xeon 6 processors, available only on AWS, and include local NVMe SSD storage. They scale up to 384 vCPUs, 3 TiB of memory, and 22.8 TB of local NVMe SSD storage. That's 4x the vCPUs and memory and more than 6x the local storage of M5d and R5d instances. 
When you create or modify a DB instance to use M8id or R8id, RDS for SQL Server automatically places the tempdb data and log files on the local NVMe instance store. This gives tempdb lower read and write latency than Amazon EBS storage. Your database data and log files stay on Amazon EBS. Because snapshots don't include tempdb files on the instance store, your snapshots are smaller and use less of your free backup storage. To learn more, see Instance store support for the tempdb database on Amazon RDS for SQL Server. 
To use the new M8id and R8id instances, you can modify your existing RDS database instance or create a new RDS database instance from the RDS Management Console, or using the AWS SDK or CLI. M8id and R8id instances are available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Europe (Stockholm), Europe (Spain), Asia Pacific (Tokyo), Asia Pacific (Mumbai), Asia Pacific (Sydney), and Asia Pacific (Malaysia). For pricing details, see Amazon RDS for SQL Server Pricing.

## 핵심 요약

요약 미지원
