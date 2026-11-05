---
title: "Amazon S3 Tables now provide a simple, cost-effective path for data lake modernization"
date: "2026-11-05"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-tables-managed-migration-hive-to-iceberg/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon S3 Tables now provide a simple, cost-effective path for data lake modernization

**날짜:** 2026년 11월 05일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-tables-managed-migration-hive-to-iceberg/

## 내용

Amazon S3 Tables now offer managed migration of your Apache Hive tables to Apache Iceberg. Iceberg adds ACID transactions, schema evolution, and time travel to your data lake, but moving off Hive usually means building a migration pipeline for each table, which can take weeks. You can now let S3 Tables manage your migration, resulting in query-ready Iceberg tables that stay optimized as data grows. 
S3 Tables validate, convert, and copy your data while production workloads keep running. To lower migration risk, you can review each step, sync destination tables with source changes as often as you need, or roll back to your source data. You pay only for the data that the job copies, with no charge for the Hive-to-Iceberg conversion, and source objects in S3 Intelligent-Tiering stay in their current access tier. If your tables use Snappy compression, S3 Tables recompress them to Zstandard (ZSTD) and compact them, which reduces storage and object count and improves query performance. 
To get started, visit the AWS Management Console or use the Amazon S3 Tables migration APIs. A migration skill is also available in the Agent Toolkit for AWS to help AI agents orchestrate the workflow autonomously.&nbsp;At launch, S3 Tables managed migration supports AWS Glue-registered Hive tables stored in Parquet format within the same AWS account and AWS Region. It is available in the following AWS Regions: US East (N. Virginia, Ohio), US West (Oregon), Asia Pacific (Mumbai, Singapore, Sydney, Tokyo), Europe (Frankfurt, Ireland, Stockholm). For pricing information visit Amazon S3 pricing. To learn more, see the Amazon S3 Tables overview page, documentation, and AWS News Blog.

## 핵심 요약

요약 미지원
