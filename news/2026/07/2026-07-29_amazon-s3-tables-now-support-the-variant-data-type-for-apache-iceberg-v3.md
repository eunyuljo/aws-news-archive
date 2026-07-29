---
title: "Amazon S3 Tables now support the Variant data type for Apache Iceberg V3"
date: "2026-07-29"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-s3-tables-variant-iceberg-v3/"
tags: ["S3", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon S3 Tables now support the Variant data type for Apache Iceberg V3

**날짜:** 2026년 07월 29일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-s3-tables-variant-iceberg-v3/

## 내용

Amazon S3 Tables now support the Variant data type as defined in the Apache Iceberg Version 3 (V3) specification. You can now write semi-structured data like JSON directly to S3 Tables without defining a fixed schema in advance, allowing you to land data faster while still getting efficient analytical query performance.  With the Variant data type, Apache Iceberg V3-compatible engines shred your semi-structured data into hidden columns as you write it, generating Parquet column statistics that query engines use for optimizations like file pruning, which reduces the data your analytical queries scan. S3 Tables also provide ongoing table maintenance, including compaction, for Variant columns, so you can consolidate data from small files into large files that Iceberg engines can read.  Variant support in S3 Tables is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and South America (São Paulo).  To learn more, see Amazon S3 Tables and the AWS Prescriptive Guidance for working with Iceberg table format specification version 3.

## 핵심 요약

요약 미지원
