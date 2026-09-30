---
title: "Amazon SageMaker Unified Studio now supports two new connection capabilities: Iceberg REST Catalog connections and IAM authentication for Amazon DocumentDB"
date: "2026-09-30"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-iceberg-rest-iam-documentdb/"
tags: ["S3", "2026", "preview", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon SageMaker Unified Studio now supports two new connection capabilities: Iceberg REST Catalog connections and IAM authentication for Amazon DocumentDB

**날짜:** 2026년 09월 30일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-iceberg-rest-iam-documentdb/

## 내용

Amazon SageMaker Unified Studio now supports two new connection capabilities: (1) Iceberg REST Catalog (IRC) connections for external Apache Iceberg catalogs, and (2) IAM authentication for Amazon DocumentDB. Together, they let data teams connect to a broader set of governed data sources and use credential-less authentication across projects.
Iceberg REST Catalog connections. SageMaker Unified Studio now supports Iceberg REST Catalog (IRC) connections, letting customers connect to external Apache Iceberg catalogs that follow the Iceberg REST specification. Supported catalog types include Snowflake Open Catalog (Polaris), Databricks Unity Catalog, and a Generic IRC type for any other spec-compliant catalog. Once connected, customers can browse the catalog in Data Explorer (list catalog/schema/table, view columns, sample data), read and write it in Visual ETL as a source or append/overwrite sink, and query it from data notebooks. Authentication uses OAuth2 or bearer token, and data access uses vended, short-lived Amazon S3 credentials. The connection lifecycle is fully supported - create, edit, delete, and test connection.
IAM authentication for Amazon DocumentDB. SageMaker Unified Studio now supports IAM authentication for Amazon DocumentDB connections, so customers can connect to DocumentDB without storing a database username or password in the connection or notebook. The connection authenticates using its own IAM role, which DocumentDB validates via AWS Security Token Service (AWS STS). This requires Amazon DocumentDB 5.0 or later instance-based clusters with TLS enabled. The connection can be used from data notebooks, Data Explorer, Test Connection, and Visual ETL data preview.
These connection capabilities are available today in all AWS Regions where Amazon SageMaker Unified Studio is available, at no additional cost.
To learn more about Amazon SageMaker Unified Studio, refer to the Amazon SageMaker Unified Studio User Guide.

## 핵심 요약

요약 미지원
