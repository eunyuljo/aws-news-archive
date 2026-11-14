---
title: "Amazon OpenSearch Serverless supports intelligent ingestion for time series collection"
date: "2026-11-14"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-serverless-nextgen-time-series-intelligent-ingestion"
tags: ["S3", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon OpenSearch Serverless supports intelligent ingestion for time series collection

**날짜:** 2026년 11월 14일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-serverless-nextgen-time-series-intelligent-ingestion

## 내용

The next generation of Amazon OpenSearch Serverless now supports intelligent ingestion for time series collections. You can bring logs and event data from Amazon S3 into a time series collection without operating an ingestion pipeline. With intelligent ingestion, you can now complete the setup and get data ingested with a few clicks in the AWS Management Console or with a single API call. 
Intelligent ingestion detects the data type, parses each record, and indexes it into your collection. It works with observability logs in JSON, NDJSON, and JSON arrays. Use an ingestion job for one-time loads, use an ingestion stream to keep the collection up to date as new objects arrive in S3, or backfill and then stream. Source buckets can be in the same AWS account as the collection or in a different one. Capacity scales with your workload up to the collection's configured limit, and you pay only for active processing. 
Once ingested, your data gets everything time series collections already provide. The collection absorbs ingest spikes automatically and keeps recent data in the hot tier for fast queries. Older data moves to the lower-cost warm tier based on the retention you set. Because tiering and retention are based on time, each document must include a valid timestamp field, and documents with a missing or invalid timestamp are rejected. Alerting and anomaly detection run directly on the ingested logs and events. Together, these make it simpler to put large S3 log archives to work for log analytics, application monitoring, and IoT telemetry. 
Intelligent ingestion for time series collections is available in seven regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland), Europe (Frankfurt) and Asia Pacific (Tokyo). To get started, open the Amazon OpenSearch Service console, choose your time series collection, and select the Ingestion tab. To learn more, see the intelligent ingestion documentation and the OpenSearch Serverless documentation. For pricing, see Amazon OpenSearch Service pricing. 
&nbsp;

## 핵심 요약

요약 미지원
