---
title: "Amazon SageMaker Feature Store now supports batch feature writes and record listing"
date: "2026-07-10"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amzn-sgm-feature-store-batch-write-list/"
tags: ["RDS", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker Feature Store now supports batch feature writes and record listing

**날짜:** 2026년 07월 10일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amzn-sgm-feature-store-batch-write-list/

## 내용

Amazon SageMaker Feature Store is a fully managed capability that makes it easy to compute, store, and retrieve features for training and deploying AI models. SageMaker Feature Store now supports new capabilities for high-throughput feature ingestion, record discovery, and offline store cataloging. Data scientists can now write multiple records across multiple feature groups in a single request with BatchWriteRecord, list the records stored in a feature group without knowing each record identifier in advance with ListRecords, and create tables and databases with custom names in the offline store.  Data scientists can use BatchWriteRecord to ingest feature data at scale with fewer API calls and lower latency than writing one record at a time. BatchWriteRecord targets the online store, the offline store, or both, returns individual record failures without failing the entire request, and supports time-to-live settings at the record, request, and feature group level. With ListRecords, data scientists can retrieve the record identifiers in a feature group, one page at a time, to browse and audit feature group contents, recover record identifiers, and manage the record lifecycle. When configuring an offline store, data scientists can also create Glue and Iceberg tables with custom names. These capabilities enable data scientists to ingest features at scale and manage the records stored in SageMaker Feature Store without building custom tooling. 
These capabilities are available in all AWS Regions where Amazon SageMaker Feature Store is available. For more information, see Amazon Feature Store Runtime and Offline Store Configuration documentation.

## 핵심 요약

요약 미지원
