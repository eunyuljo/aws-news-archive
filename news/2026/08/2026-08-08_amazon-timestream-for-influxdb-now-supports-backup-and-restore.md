---
title: "Amazon Timestream for InfluxDB now supports backup and restore"
date: "2026-08-08"
service: "KMS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/timestream-influxdb-backup-restore/"
tags: ["KMS", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon Timestream for InfluxDB now supports backup and restore

**날짜:** 2026년 08월 08일
**서비스:** KMS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/timestream-influxdb-backup-restore/

## 내용

Amazon Timestream for InfluxDB now lets you create and manage your own backups and restore your data on demand. You can trigger one-time, on-demand backups, schedule automated recurring backups at the frequency and retention you choose, and restore a backup to a new resource or in place of an existing one. This capability is available for both the InfluxDB 2 and InfluxDB 3 engines through the AWS Management Console, the AWS CLI, and the Timestream for InfluxDB API.  With this capability, you control your data protection strategy. You can take an on-demand backup before a risky migration or configuration change. You can also define up to four automated backup configurations per resource using hourly, daily, weekly, monthly, or custom schedules, each with its own retention period. The first backup captures a full copy of your database, and subsequent backups are incremental, reducing the performance impact of ongoing backups. When you restore a backup, you can create a new resource that inherits the source configuration or replace an existing resource. If the source resource uses a Customer Managed key (KMS), its backups use the same key. 
Customer-driven backup and restore is available in all AWS Regions where Amazon Timestream for InfluxDB is available. To get started, open the Amazon Timestream console. For more information, see the Amazon Timestream for InfluxDB documentation and pricing page.

## 핵심 요약

요약 미지원
