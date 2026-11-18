---
title: "Amazon EMR 8.2 is now available"
date: "2026-11-18"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-emr-8.2/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon EMR 8.2 is now available

**날짜:** 2026년 11월 18일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-emr-8.2/

## 내용

Amazon EMR 8.2 is now available with new features across Amazon EMR on EC2, Amazon EMR on EKS, and Amazon EMR Serverless. This release upgrades Apache Spark to 4.1.3, Apache Iceberg to 1.11.0, and Delta Lake to 4.2.0, and it is designated a Long Term Support (LTS) release. This release makes it easier to run secure, governed analytics at scale — you can now write to the same Delta Lake table on Amazon S3 from multiple clusters concurrently, refresh Iceberg materialized views incrementally, and propagate end-user identity from Spark jobs and interactive sessions all the way to AWS Lake Formation and Amazon S3 so access is authorized and audited as the original user. 
Amazon EMR 8.2 expands governance and performance across all three deployment options. New features include concurrent Delta Lake writes using Amazon S3 conditional writes (no DynamoDB log store required), and Lake Formation fine-grained access control (FGAC) now covers materialized views, governed user-defined functions, more Iceberg operations, and a broader set of Spark SQL features. The release also adds OpenLineage-based lineage capture to the AWS Glue Data Catalog and trusted identity propagation for steps and sessions. With EMR 8.2, data engineers can now precompute each pipeline stage as an Iceberg materialized view in SQL. Each materialized view refreshes only the changes instead of recomputing the entire source table across projections, inner joins, filters and SUM, COUNT aggregations. Specific to EMR on EC2, this release adds Spark Connect support on multi-primary clusters, along with Secret Agent improvements that cut user-provisioning latency by up to 97% under high concurrency. On EMR Serverless, new scaling profiles for Spark (performance-optimized, balanced, or cost-optimized) let you tune how quickly executors scale, and applications can now run Lake Formation-governed Glue UDFs. On EMR on EKS, the Spark Operator is upgraded to version 2 (based on open-source Spark Operator 2.5.0). 
Amazon EMR 8.2 is available in all AWS Regions where Amazon EMR is available. To learn more, see the Amazon EMR 8.2 Release Guide for EMR on EC2, the EMR Serverless release notes, and the EMR on EKS release notes, or get started by creating a cluster from the Amazon EMR console.

## 핵심 요약

요약 미지원
