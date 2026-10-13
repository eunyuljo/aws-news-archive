---
title: "Amazon EMR now supports native data quality checks in Apache Spark jobs"
date: "2026-10-13"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-emr-data-quality-spark/"
tags: ["EC2", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EMR now supports native data quality checks in Apache Spark jobs

**날짜:** 2026년 10월 13일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-emr-data-quality-spark/

## 내용

Amazon EMR now validates data quality natively within Apache Spark jobs. Data engineering teams can catch quality issues inline before bad data reaches downstream systems, without building or maintaining separate validation infrastructure. Amazon EMR Data Quality, powered by AWS Glue, is available at no additional cost and uses the same declarative rules language (Data Quality Definition Language) and APIs as AWS Glue for a consistent experience across both engines, and works with Apache Iceberg, Apache Hudi, and Delta Lake across EC2, EKS, and Serverless deployment modes.
With this feature, you can author validation rules in your Spark scripts or reference rules stored in the AWS Glue Data Catalog, and then apply them at any stage of your pipeline i.e., after reading data, during transformation, or after processing. With 30+ rule types, including dynamic rules that compare against historical runs and ML-based anomaly detection for tracking drift over time without specifying fixed thresholds, Amazon EMR Data Quality provides the flexibility of choosing the validation framework that fits your needs. You can take actions like failing a pipeline, filtering invalid records, or routing them to quarantine based on the quality evaluation results. Results are produced at the dataset, rule, and row level, so that you can easily identify which records or rules are driving the quality failures.
Amazon EMR Data Quality is available on AWS runtime for Apache Spark (emr-spark-8.1.0) in all AWS Commercial, AWS GovCloud (US), and AWS China Regions.
To get started, visit Amazon EMR Data Quality documentation and add DQDL rules for data quality validation to the Spark scripts of your EMR workloads.

## 핵심 요약

요약 미지원
