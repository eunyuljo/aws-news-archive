---
title: "Amazon SageMaker Unified Studio now supports data profiling and anomaly detection"
date: "2026-08-19"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/05/smus-data-profiling"
tags: ["RDS", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon SageMaker Unified Studio now supports data profiling and anomaly detection

**날짜:** 2026년 08월 19일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/05/smus-data-profiling

## 내용

Amazon SageMaker Unified Studio now supports data profiling and anomaly detection, powered by AWS Glue Data Quality. Data stewards, engineers and analysts can generate statistical profiles of their data to understand its shape and completeness, and track how these statistics change over time. Anomaly detection helps identify when data points drift from historical patterns without requiring predefined thresholds or custom rules. These capabilities are available for both data at rest in catalog tables and data in transit within Visual ETL jobs. 
With this launch, a dedicated Data profile tab on catalog tables provides on-demand and scheduled profiling that computes dataset-level and column-level statistics. As profile history accumulates, anomaly detection builds a baseline of expected behavior and flags data points that fall outside the predicted range. This is particularly useful when you may not be aware of specific thresholds, or when expected values change over time and fixed rules could become stale. For data in transit, the same profiling statistics and anomaly detection are available on the results page of any Visual ETL job with an Evaluate Data Quality transform. 
This feature is available in all AWS Regions where Amazon SageMaker Unified Studio is available. To learn more, visit the Amazon SageMaker Unified Studio documentation.

## 핵심 요약

요약 미지원
