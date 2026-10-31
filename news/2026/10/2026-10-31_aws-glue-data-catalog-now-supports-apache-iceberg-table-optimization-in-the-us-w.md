---
title: "AWS Glue Data Catalog now supports Apache Iceberg table optimization in the US West (N. California) Region"
date: "2026-10-31"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/glue-data-catalog-optimizers-us-west-1/"
tags: ["CloudWatch", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS Glue Data Catalog now supports Apache Iceberg table optimization in the US West (N. California) Region

**날짜:** 2026년 10월 31일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/glue-data-catalog-optimizers-us-west-1/

## 내용

AWS Glue Data Catalog now supports automatic table optimization for Apache Iceberg tables in the US West (N. California) Region. Apache Iceberg is an open table format that delivers fast query performance over large tables in data lakes. With this launch, you can enable table optimization for individual tables or for all tables in your Data Catalog. 
Apache Iceberg tables accumulate small files, snapshots, and unreferenced files with every write, which slows queries and increases storage costs over time. Table optimization continuously monitors your tables to compact small files in the background, remove snapshots that are past your retention settings, and delete unreferenced files that are no longer needed. You can monitor each run from the AWS Glue console, Amazon CloudWatch metrics, and logs. 
You can enable table optimization using the AWS Glue console, AWS CLI, or AWS SDKs. For the full list of Regions where table optimization is available, see Supported Regions for table optimizers. To learn more, see Optimizing Iceberg tables in the AWS Glue Developer Guide. To get started, visit the AWS Glue product page.

## 핵심 요약

요약 미지원
