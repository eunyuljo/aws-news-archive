---
title: "AWS Glue Data Catalog now supports table optimization, statistics, and crawlers for Apache Iceberg V3"
date: "2026-10-02"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-glue-iceberg-v3-optimization/"
tags: ["S3", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS Glue Data Catalog now supports table optimization, statistics, and crawlers for Apache Iceberg V3

**날짜:** 2026년 10월 02일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-glue-iceberg-v3-optimization/

## 내용

AWS Glue Data Catalog now supports table optimization, statistics, and crawlers for Apache Iceberg Version 3 (V3) tables. With these new capabilities, you can automatically maintain V3 tables, optimize them for query performance, and discover them in Amazon S3.
With table optimization, you can compact V3 tables using binpack, sort, or z-order strategies to improve query performance, and remove expired snapshots and orphan files to reduce storage costs. These optimizations support V3 data types, including variant, geospatial, and nanosecond-precision timestamps. You can also generate number of distinct values (NDV) statistics for V3 tables, which analytics engines use to plan queries efficiently. In addition, you can use Glue crawlers to discover V3 tables stored in Amazon S3 and register them in Glue Data Catalog, making them available to query with any V3-compatible engines.
These capabilities are available for Iceberg V3 tables in all AWS Regions where Glue Data Catalog table optimization, statistics, and crawlers are available. To learn more, see Glue Optimization, Glue Statistics, and Glue crawlers in the Glue Developer Guide.

## 핵심 요약

요약 미지원
