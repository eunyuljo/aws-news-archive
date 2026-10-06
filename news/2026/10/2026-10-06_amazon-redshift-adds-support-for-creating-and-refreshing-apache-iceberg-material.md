---
title: "Amazon Redshift adds support for creating and refreshing Apache Iceberg materialized views"
date: "2026-10-06"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-iceberg-materialized-views"
tags: ["S3", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon Redshift adds support for creating and refreshing Apache Iceberg materialized views

**날짜:** 2026년 10월 06일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-iceberg-materialized-views

## 내용

Amazon Redshift now supports the creation and refresh of Apache Iceberg materialized views. Materialized views pre-compute expensive joins and aggregations once and store the results in an Apache Iceberg table in Amazon S3 or Amazon S3 table buckets, registered in the AWS Glue Data Catalog. Materialized views are created using familiar SQL — CREATE MATERIALIZED VIEW ... USING ICEBERG and the results are instantly queryable by any Iceberg-compatible engine, including Amazon Athena, Apache Spark on Amazon EMR and AWS Glue, and third-party engines such as Trino, or Snowflake. Redshift keeps them current by recomputing only what has changed with manual incremental refresh, and because the results are Iceberg tables in the Glue Data Catalog, they are governed and discovered like any other catalog table.
Data teams often build analytics in stages, stitching together different engines to clean and transform raw data before serving it. This adds pipeline orchestration overhead and can introduce semantic differences between engines. Iceberg materialized views deliver value in two ways. First, instead of hundreds of users and teams re-running the same expensive joins and aggregations, and re-scanning source tables on every query, you compute the result once and everyone reads the precomputed table. Second, you can run an end-to-end pipeline using a single engine like Apache Spark and now Amazon Redshift, and every downstream consumer shares the same open result without the overhead of orchestrating multiple engines. Either way, the output is an open Iceberg table that any engine can read without copies or conversion. You can still load these tables into Redshift Managed Storage (RMS) as native RMS materialized views for your most performance-sensitive dashboards.
You can create Iceberg Materialized Views in any region where Redshift Serverless and provisioned Graviton instances are supported. To learn more, see Materialized views stored as Apache Iceberg tables in the Amazon Redshift Database Developer Guide, the CREATE MATERIALIZED VIEW command reference, and the Materialize once, query anywhere blog post.

## 핵심 요약

요약 미지원
