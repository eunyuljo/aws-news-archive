---
title: "AWS Glue Data Catalog now supports  metadata exports to S3 Tables (Preview)"
date: "2026-08-07"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-glue-data-catalog-s3-tables/"
tags: ["S3", "2026", "preview", "new-region", "security"]
nav_exclude: true
---

# AWS Glue Data Catalog now supports  metadata exports to S3 Tables (Preview)

**날짜:** 2026년 08월 07일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-glue-data-catalog-s3-tables/

## 내용

AWS Glue Data Catalog is a centralized metadata repository that helps you discover and understand data, with semantic search and support for adding business context to datasets currently in preview. Today, we are adding two new capabilities to this preview: exporting catalog metadata exports to S3 Tables for metadata querying, and expanding the semantic search preview to catalogs encrypted with AWS Key Management Service (AWS KMS) customer managed keys. 
When you enable the Glue metadata export, your catalog's technical and business metadata, including glossary terms, custom metadata attachments, and asset descriptions, are written to tables in the managed aws-catalog S3 table bucket. Metadata is stored in Apache Iceberg format, enabling you to query, audit, and perform time travel queries for historical analysis using standard SQL in query engines that support Iceberg, such as AWS analytics services like Amazon Athena and Amazon QuickSight as well as third-party tools. This lets you join catalog metadata with other AWS service data for additional analysis, such as auditing glossary usage and metadata changes. Catalogs encrypted with customer managed keys now support the same business context enrichment and semantic search. 
You can use these capabilities in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), and Europe (Ireland). S3 Tables requests and storage are charged based on S3 pricing. To learn more, see the AWS Glue User Guide.

## 핵심 요약

요약 미지원
