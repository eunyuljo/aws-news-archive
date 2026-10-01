---
title: "Amazon S3 Tables now support all Apache Iceberg V3 data types"
date: "2026-10-01"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-tables-iceberg-v3-data-types"
tags: ["S3", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon S3 Tables now support all Apache Iceberg V3 data types

**날짜:** 2026년 10월 01일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-tables-iceberg-v3-data-types

## 내용

Amazon S3 Tables add support for geometry, geography, unknown, and nanosecond timestamp data types, along with column default values, as defined in the Apache Iceberg Version 3 (V3) specification. You can now store geospatial coordinates and nanosecond-precision event times natively instead of encoding them in strings or integers. This helps simplify data architecture while improving storage efficiency and performance. With this launch, S3 Tables support all data types introduced in V3, adding to existing support for the Variant data type, deletion vectors, and row lineage.
Geometry and geography columns store points, lines, and polygons natively, so fleet tracking and asset mapping workloads can filter on location at query time. Nanosecond timestamps let telemetry and financial workloads record event times at source precision. Column default values populate a newly added column for existing rows, with no backfill required. S3 Tables provide automatic table maintenance and compaction for Apache Iceberg tables, so tables using V3 data types stay performant and cost effective as data scales.
Support for these data types in S3 Tables is available in all AWS Regions where S3 Tables are available. To learn more, see Amazon S3 Tables,&nbsp;Apache Iceberg V3 on AWS, and the AWS Prescriptive Guidance&nbsp;for working with Iceberg table format specification version 3.

## 핵심 요약

요약 미지원
