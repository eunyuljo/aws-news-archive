---
title: "AWS Glue zero-ETL adds target table property ownership and conflict detection"
date: "2026-09-15"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/glue-zero-etl-ownership-conflicts/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# AWS Glue zero-ETL adds target table property ownership and conflict detection

**날짜:** 2026년 09월 15일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/glue-zero-etl-ownership-conflicts/

## 내용

AWS Glue zero-ETL integrations now detect table property conflicts and track integration ownership. When you configure a source table and target catalog, Glue associates the resulting table properties with the owning integration, so two integrations can no longer be pointed at the same target table without your knowledge. This works across Amazon S3 Tables and SageMaker Lakehouse catalogs. 
Data teams running multiple zero-ETL integrations gain predictable control over where each source table lands. If you attempt to create or modify an integration whose table properties are owned by another integration, Glue identifies the owning integration and guides you to choose a different target or update the existing one, so your pipelines stay isolated and your data lands exactly where you intend. 
This feature is available in all AWS Commercial and AWS GovCloud (US) Regions where AWS Glue zero-ETL integrations are supported. 
To learn more, refer to the AWS Glue Developer Guide and get started in the AWS Glue console.

## 핵심 요약

요약 미지원
