---
title: "Amazon DynamoDB Streams now supports timestamp-based stream processing"
date: "2026-10-16"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-dynamodb-streams-timestamp-processing"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon DynamoDB Streams now supports timestamp-based stream processing

**날짜:** 2026년 10월 16일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-dynamodb-streams-timestamp-processing

## 내용

Amazon DynamoDB Streams now supports timestamp-based stream processing, enabling you to begin reading stream records from a specific point in time. Previously, you could only start from the oldest retained record (up to 24 hours old) or from new records written after you start consuming the stream. Now, you can supply a timestamp and begin processing at the first record written at or after that time using the AT_TIMESTAMP shard iterator type.
Timestamp-based stream processing can be used with the Amazon Kinesis Client Library (KCL) through the DynamoDB Streams Kinesis adapter. It helps you avoid reprocessing entire retained streams or missing records when resuming stream consumption, supporting common use cases such as recovery after an interruption, data replay for debugging and auditing by reading from a specific point in the past, skipping a backlog by resuming from a recent timestamp near the latest records, and synchronizing after a restore by beginning at the export timestamp following a point-in-time recovery (PITR) export.
Timestamp-based stream processing is available in all commercial AWS Regions, the AWS GovCloud (US) Regions, and the China Regions. There is no additional charge for this feature beyond standard GetRecords API request charges. To get started, see Amazon DynamoDB Streams timestamp documentation in the DynamoDB developer guide.

## 핵심 요약

요약 미지원
