---
title: "Amazon Managed Service for Apache Flink introduces enhanced snapshots"
date: "2026-11-13"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/managed-flink-enhanced-snapshots/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Amazon Managed Service for Apache Flink introduces enhanced snapshots

**날짜:** 2026년 11월 13일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/managed-flink-enhanced-snapshots/

## 내용

Amazon Managed Service for Apache Flink now supports enhanced snapshots, a capability that lets you capture, export, and restore application state across Apache Flink applications and AWS Regions, so you can run blue/green deployments, easily migrate self-managed workloads to Amazon Managed Service for Apache Flink without losing state, and keep backup in a secondary Region for cross-Region recovery.
To deploy an application update without pausing processing for blue/green deployments, create an enhanced snapshot from an application and use it to start a second application. To migrate a self-managed workload, import its Apache Flink savepoint into Amazon Managed Service for Apache Flink as an enhanced snapshot. For cross-Region recovery, export an enhanced snapshot to an Amazon Simple Storage Service (Amazon S3) bucket, and replicate the exported state to a bucket in a secondary Region.
Enhanced snapshots are available today for applications on Apache Flink 1.20 and later in all AWS Regions where Amazon Managed Service for Apache Flink is available except European Sovereign Cloud (Germany). You pay for enhanced snapshot storage per GB-month as durable application backups. To learn more and get started, see enhanced snapshots in the Amazon Managed Service for Apache Flink Developer Guide. You can also use Agent Toolkit for AWS with Kiro, Claude Code, or Cursor for guidance on building and operating Flink applications with enhanced snapshots.

## 핵심 요약

요약 미지원
