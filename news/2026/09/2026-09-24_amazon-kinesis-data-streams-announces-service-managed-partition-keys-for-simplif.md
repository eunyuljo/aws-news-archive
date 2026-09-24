---
title: "Amazon Kinesis Data Streams announces Service-Managed Partition Keys for simplified data ingestion"
date: "2026-09-24"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/kinesis/service-managed-partition-keys"
tags: ["RDS", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon Kinesis Data Streams announces Service-Managed Partition Keys for simplified data ingestion

**날짜:** 2026년 09월 24일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/kinesis/service-managed-partition-keys

## 내용

Amazon Kinesis Data Streams now supports service-managed partition keys for On-Demand Standard and On-Demand Advantage streams, automatically distributing records across shards without requiring customers to specify partition keys to publish data. This capability simplifies data ingestion for workloads where record ordering is not required, eliminating hot partition keys and reducing time to production for streaming workloads.
Amazon Kinesis Data Streams is a serverless streaming data service that makes it easy to capture, process, and store data streams at any scale. Many streaming use cases such as log aggregation, metrics collection, and IoT telemetry do not require ordering guarantees and benefit from prewarmed capacity for instant scaling. Previously, customers generated random partition keys (such as UUIDs) to distribute data, but random partitioning can still produce uneven throughput across shards, causing throttling for some partition keys even when the stream has sufficient aggregate capacity. By opting into service-managed partition keys, customers no longer need to specify partition keys when publishing data to streams in on-demand mode. The service automatically distributes records based on available warm capacity, allowing customers to scale to gigabytes per second without maintaining any distribution logic. Customers who want to send records without specifying a partition key can simply upgrade to the latest AWS SDK or Kinesis Producer Library (KPL) version to benefit from this capability.
Service-managed partition keys for Amazon Kinesis Data Streams is available today in all AWS commercial regions at no additional cost. To get started, visit the Amazon Kinesis Data Streams documentation (https://aws.amazon.com/kinesis).

## 핵심 요약

요약 미지원
