---
title: "AWS Glue Data Quality now supports anomaly detection and writing results to the AWS Glue Data Catalog"
date: "2026-07-28"
service: "Glue"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-glue-data-quality-catalog-anomaly-detection-write-results"
tags: ["Glue", "2026", "new-region"]
nav_exclude: true
---

# AWS Glue Data Quality now supports anomaly detection and writing results to the AWS Glue Data Catalog

**날짜:** 2026년 07월 28일
**서비스:** Glue
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-glue-data-quality-catalog-anomaly-detection-write-results

## 내용

AWS Glue Data Quality now supports anomaly detection for Catalog-based data quality evaluations and the ability to write evaluation results to AWS Glue Data Catalog (GDC) tables. These capabilities work across both ETL jobs and Catalog evaluations, giving you a consistent data quality experience regardless of workflow type.  With anomaly detection support for GDC, you can identify unexpected changes in data statistics such as sudden drops in distinct values or row count spikes in your GDC tables using ML-powered time-series forecasting, without writing rules with explicit thresholds. This is especially valuable for data engineers monitoring hundreds of tables in the GDC who need to surface issues automatically.  With results storage in GDC, Data Quality rule outcomes, profiling metrics, and anomaly predictions (with confidence bounds) are written back to GDC tables, creating a queryable record of all quality evaluations. Whether the evaluation runs in an ETL job or directly on a Catalog table, results can be queried at any time using standard SQL.  AWS Glue Data Quality anomaly detection and Catalog results storage are available in all AWS commercial regions and AWS GovCloud (US) regions.  To get started, visit the AWS Glue Data Quality documentation.

## 핵심 요약

요약 미지원
