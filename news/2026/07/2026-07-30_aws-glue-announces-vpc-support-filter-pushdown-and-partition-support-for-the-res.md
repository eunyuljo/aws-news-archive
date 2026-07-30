---
title: "AWS Glue announces VPC support, filter pushdown, and partition support for the REST API connector"
date: "2026-07-30"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-glue-rest-connector-filtering-partitioning-vpc"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS Glue announces VPC support, filter pushdown, and partition support for the REST API connector

**날짜:** 2026년 07월 30일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-glue-rest-connector-filtering-partitioning-vpc

## 내용

AWS Glue now supports VPC connections, filter pushdown, and partition support for the REST API connector. The REST API connector enables you to ingest data from any source that exposes a REST-based API, including proprietary systems and emerging platforms without native AWS Glue connectors. With this launch, you can operate your ETL pipelines from data sources with REST API endpoints by securely connecting to private endpoints, transfering only the data they need, and parallelizing reads for faster ingestion, all without writing custom code  With VPC support, you can use the REST API connector to access data sources hosted in private subnets or connected through VPNs or AWS PrivateLink, without exposing traffic to the public internet. Filter pushdown translates your query predicates into API-native parameters, so only matching records leave the source, reducing data transfer costs and improving job performance. Partition support splits large datasets across multiple Spark workers using field-based or record-count strategies, providing parallel reads that reduce ingestion time for high-volume, paginated APIs.  These capabilities are available in all AWS commercial regions where AWS Glue is available.  To get started, visit the AWS Glue REST API connector documentation.

## 핵심 요약

요약 미지원
