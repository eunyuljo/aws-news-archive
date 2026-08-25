---
title: "Amazon Redshift now supports concurrency scaling of streaming ingestion workloads from Amazon Kinesis data streams"
date: "2026-08-25"
service: "Kinesis"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/redshift-concurrencyscaling-for-kds-streams/"
tags: ["Kinesis", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon Redshift now supports concurrency scaling of streaming ingestion workloads from Amazon Kinesis data streams

**날짜:** 2026년 08월 25일
**서비스:** Kinesis
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/redshift-concurrencyscaling-for-kds-streams/

## 내용

Amazon Redshift, starting with patch P203, supports concurrency scaling for refreshes of Amazon Kinesis Data Streams (KDS)-connected streaming materialized views (MVs).  Amazon Web Services (AWS) Redshift Streaming Ingestion enables low-latency, high-speed data ingestion from Amazon KDS to Amazon Redshift data warehouses. The data lands in a Redshift streaming materialized view, providing fast access to external data, lowering data-access time, and reducing storage costs. Users can configure streaming ingestion for their Amazon Redshift cluster or Redshift Serverless workgroup using SQL commands. Once set up, each streaming materialized-view refresh can ingest hundreds of megabytes of data per second. If you have concurrency scaling enabled, your streaming workloads will now automatically scale by freeing-up your main Amazon Redshift cluster or workgroup to run other higher priority workloads.  You can start using this new capability immediately in all AWS regions where Amazon Redshift is available to scale your workload and build resilient analytics applications with predictable Service Level Agreements. To get started, refer to the Concurrency Scaling, Materialized Views and streaming ingestion sections of the Amazon Redshift documentation.

## 핵심 요약

요약 미지원
