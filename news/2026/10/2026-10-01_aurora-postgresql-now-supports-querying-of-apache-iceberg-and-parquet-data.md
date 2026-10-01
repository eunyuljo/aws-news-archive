---
title: "Aurora PostgreSQL now supports querying of Apache Iceberg and Parquet data"
date: "2026-10-01"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aurora-postgresql-query-apache-iceberg-and-parquet/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Aurora PostgreSQL now supports querying of Apache Iceberg and Parquet data

**날짜:** 2026년 10월 01일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aurora-postgresql-query-apache-iceberg-and-parquet/

## 내용

Starting today, you can directly query operational data together with data stored in data lakes in Apache Iceberg and Parquet formats using your existing PostgreSQL applications and tools, without extract, transform, and load (ETL) pipelines or data duplication.
Applications increasingly need access to data from data lakes, often stored in Apache Iceberg and Parquet formats, to make more informed decisions and automate business processes. Accessing it has typically required pipelines that copy data from your data lake into Aurora, driving up costs and engineering work as schemas evolve. With this launch, you can create PostgreSQL foreign tables that reference your Iceberg or Parquet data in Amazon S3, Amazon S3 Tables, or AWS Glue Data Catalog. When customers query these foreign tables, Aurora uses DuckDB’s high-performance query engine, embedded in PostgreSQL, to execute the query against the underlying Iceberg and Parquet data. Your existing applications and BI tools continue to use the same PostgreSQL interface.
You can also query tables from external Iceberg REST Catalog (IRC)-compatible catalogs federated through AWS Glue Data Catalog, without moving or duplicating data. For latency-sensitive workloads, you can materialize Iceberg or Parquet data into native Aurora PostgreSQL tables using standard SQL statements, without an ETL pipeline.
The capability is generally available on Aurora PostgreSQL starting 17.11, 18.6 and higher in all AWS commercial and GovCloud (US) Regions, at no additional charge. To get started, use the Amazon RDS console or any PostgreSQL client. To learn more, see the blog post or&nbsp;documentation.

## 핵심 요약

요약 미지원
