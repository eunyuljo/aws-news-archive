---
title: "AWS Cost and Usage Report 2.0 now supports table configurations update"
date: "2026-06-17"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cost-usage-report/"
tags: ["Config", "2026", "GA", "price-reduction"]
nav_exclude: true
---

# AWS Cost and Usage Report 2.0 now supports table configurations update

**날짜:** 2026년 06월 17일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cost-usage-report/

## 내용

AWS today announces that AWS Cost and Usage Report 2.0 (CUR 2.0) now supports updates to data table configurations via the AWS Management Console and SDK/CLI. This capability allows customers to modify their existing exports to take advantage of new CUR 2.0 features without having to delete and recreate their exports.  Previously, customers configured CUR 2.0 exports with specific table settings — including export content, time granularity, column selection, export format, and destination settings. When AWS introduces new features, such as additional columns and finer row-level granularity, existing export settings intentionally remained unchanged to protect ETL jobs that depended on a stable schema. However, customers who wanted to adopt these new capabilities and were ready for the new schema couldn't simply update their preference in existing export. They had to delete their existing export and create a new one with the new preference. With this launch, customers can update their table configuration directly through the AWS Management Console or SDK/CLI and begin receiving exports with their updated preferences starting from the next scheduled export delivery.  To learn more about this feature, see AWS Data Exports and AWS Billing and Cost Management in the AWS Cost Management User Guide.

## 핵심 요약

요약 미지원
