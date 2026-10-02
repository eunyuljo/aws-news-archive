---
title: "Apache Iceberg materialized views now support system-managed write protection"
date: "2026-10-02"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/system-managed-iceberg-materialized-views"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Apache Iceberg materialized views now support system-managed write protection

**날짜:** 2026년 10월 02일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/system-managed-iceberg-materialized-views

## 내용

Today, AWS announces system-managed materialized views for Apache Iceberg. Materialized views let you precompute an expensive query once and reuse the result across engines. Because this result is an open Iceberg table in your data lake, anyone with write access can change it, either through the catalog or by writing to the files in Amazon S3. System-managed materialized views close this gap by only allowing AWS Glue to write the materialized view's data and definition, so the result stays exactly as computed regardless of who has write access to the table or the underlying S3 files.
To get started, write the SQL that defines the materialized view and, optionally, a refresh schedule. AWS Glue then computes the results, stores them as a standard Apache Iceberg table in your Amazon S3 Tables bucket, and keeps them current on your schedule. Because the result is an ordinary Iceberg table in the AWS Glue Data Catalog, any Iceberg-compatible engine can read it directly, while the service guarantees no other writer can alter it. You get a governed, always-consistent dataset that you can confidently share. You can still refresh, reschedule, or drop the view whenever you need to.
System-managed Apache Iceberg materialized views are available in all regions where Apache Iceberg materialized views are supported. To learn more, see System-managed materialized views&nbsp;in the AWS Glue Developer Guide.

## 핵심 요약

요약 미지원
