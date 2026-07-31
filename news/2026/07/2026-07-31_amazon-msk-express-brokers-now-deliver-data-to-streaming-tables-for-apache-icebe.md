---
title: "Amazon MSK Express brokers now deliver data to streaming tables for Apache Iceberg"
date: "2026-07-31"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-msk-streaming-tables-for-apache-iceberg"
tags: ["S3", "2026", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon MSK Express brokers now deliver data to streaming tables for Apache Iceberg

**날짜:** 2026년 07월 31일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-msk-streaming-tables-for-apache-iceberg

## 내용

Amazon MSK Express brokers now deliver data to streaming tables for Apache Iceberg, a new capability that continuously materializes Apache Kafka topics as Apache Iceberg tables on Amazon S3 Tables. Amazon MSK data delivery to streaming tables can reduce the cost of ingesting and delivering Apache Kafka data into Amazon S3 Tables by up to 60% versus self-managed deployments and reduces downstream query costs by up to 30% versus self-managed Apache Kafka deployments. 
Customers rely on Apache Kafka to ingest real-time data for use cases like fraud detection and personalization and increasingly want to unify that data with Apache Iceberg tables for near real-time analytics but integrating the two forces them to operate complex custom pipelines, manage format conversions, and contend with the small-file problem, where high-volume ingestion creates many small parquet files that slow downstream queries and increase costs. With this capability, intelligent inline compaction eliminates the performance impact of small files and keeps query performance predictable without sacrificing data freshness, while built-in coordination resolves concurrent writer conflicts across high-throughput consumers. Amazon MSK supports throughput of up to 10 GB/s for delivery to Apache Iceberg on Amazon S3 Tables, and because this native capability adds no broker egress throughput, customers avoid the incremental infrastructure costs of scaling connector pipelines and match capacity to actual demand rather than peak. Customers deliver data to streaming tables and query or transform the data with any engine of their choice, including Apache Spark, Trino, or Apache Flink.&nbsp; 
To get started, customers open the Amazon MSK console, select the Express cluster, and enable the capability in a few clicks, or use the MSK APIs or MCP server. Amazon MSK data delivery to streaming tables is available today in every AWS Region where Amazon MSK Express brokers are offered. For pricing information, visit the pricing page. To learn more, visit the Amazon MSK Developer Guide&nbsp;and Amazon MSK AI skills.

## 핵심 요약

요약 미지원
