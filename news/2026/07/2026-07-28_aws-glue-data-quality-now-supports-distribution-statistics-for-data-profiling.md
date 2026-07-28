---
title: "AWS Glue Data Quality now supports distribution statistics for data profiling"
date: "2026-07-28"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-glue-data-quality-distribution-profiling"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# AWS Glue Data Quality now supports distribution statistics for data profiling

**날짜:** 2026년 07월 28일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-glue-data-quality-distribution-profiling

## 내용

AWS Glue Data Quality now supports a new Distribution Analyzer that generates frequency distribution profiles for your data. Using this new Distribution Analyzer in the Data Quality Definition Language (DQDL), you can generate histograms for numeric columns and value distributions for categorical, date, and boolean columns. With support for custom bin counts, you can explore the shape and patterns of your data at the granularity that matters most to your use case.  Understanding how data is distributed is foundational to building reliable data pipelines. Distribution statistics help you quickly identify skewness, outliers, and unexpected patterns across your datasets, without writing custom code. The capability integrates directly with your existing DQDL rulesets, so you can add distribution profiling alongside your current data quality checks in a single evaluation run. Distribution statistics are stored in Amazon S3 for future querying through services like Amazon Athena, and are also surfaced through APIs, making it easy to integrate distribution insights into monitoring workflows and visualization tools, including SageMaker Unified Studio.  AWS Glue Data Quality distribution statistics are available in all AWS commercial regions and AWS GovCloud (US) regions.  To learn more about Glue Data Quality, visit the AWS Glue Data Quality documentation. To get started with using Distribution Analyzer, visit the Analyzers documentation.

## 핵심 요약

요약 미지원
