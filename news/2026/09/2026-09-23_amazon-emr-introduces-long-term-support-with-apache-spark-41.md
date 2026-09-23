---
title: "Amazon EMR introduces Long Term Support with Apache Spark 4.1"
date: "2026-09-23"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-emr-long-term-support-spark-4-1/"
tags: ["S3", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon EMR introduces Long Term Support with Apache Spark 4.1

**날짜:** 2026년 09월 23일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-emr-long-term-support-spark-4-1/

## 내용

Amazon EMR introduces Long Term Support (LTS) releases, starting with emr-spark-8.1.0 and Apache Spark 4.1. With LTS, designated versions of the AWS runtime for Apache Spark receive 36 months of support. Amazon EMR provides LTS releases with fixes for critical and high severity security, bug, and data-corruption issues, subject to availability. LTS helps you run production Spark workloads on one release longer and upgrade on your own schedule, at no additional cost.
This release adds full support for Apache Iceberg v3, bringing new geospatial, high-precision timestamp, and schema-evolution capabilities to your tables. Spark SQL queries can reference catalogs by name, including cross-account and Amazon S3 Tables catalogs, and automatically detect Apache Iceberg, Delta Lake, and Apache Hudi table formats, without registering each catalog in your Spark configuration. Fine-grained access control now covers more Apache Iceberg operations and the Delta Lake VACUUM operation, so you can apply column-level and row-level permissions to a wider set of jobs. Amazon EMR on EKS clusters now support Spark Connect endpoints with token-based authentication.
emr-spark-8.1.0 is available in all AWS Regions where Amazon EMR is available, across Amazon EMR on EC2, Amazon EMR on EKS, and Amazon EMR Serverless.
To learn more, see the emr-spark-8.1.0 release notes and the Amazon EMR standard support policy. To get started, create an EMR cluster or application with emr-spark-8.1.0 from the AWS Management Console, or use the Apache Spark Upgrade Agent for Amazon EMR to move existing applications to the release.

## 핵심 요약

요약 미지원
