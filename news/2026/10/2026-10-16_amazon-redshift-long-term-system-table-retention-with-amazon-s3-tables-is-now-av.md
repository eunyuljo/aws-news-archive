---
title: "Amazon Redshift long-term system table retention with Amazon S3 Tables is now available in additional AWS Regions"
date: "2026-10-16"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-long-term-system-table-retention-expansion/"
tags: ["S3", "2026", "GA", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon Redshift long-term system table retention with Amazon S3 Tables is now available in additional AWS Regions

**날짜:** 2026년 10월 16일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-long-term-system-table-retention-expansion/

## 내용

Amazon Redshift long-term retention for system table data through native integration with Amazon S3 Tables is now available in additional AWS Regions. With this feature, you can configure your Redshift system table data retention beyond the current 7-day limit to meet your compliance, auditing, and observability requirements. Once enabled, AWS automatically writes system table data to S3 Tables in Apache Iceberg format and manages partitioning, compaction, and retention.
Customers use Redshift system tables to monitor query performance, audit data warehouse activity, and meet compliance requirements. With this feature, system table data is replicated automatically, eliminating the need for custom extract transform load (ETL) pipelines and any resource contention with your production workloads. If you operate multiple data warehouses, you can consolidate their system table data into a single location for cross-warehouse observability and analysis. Because the data is stored in the open Apache Iceberg format, you can query it through Redshift, Amazon Athena, DuckDB, or any Iceberg-compatible engine, and build observability dashboards using AWS services or third-party tools without additional operations overhead. Additionally, the AWS Agent Toolkit provides skills for querying system table data to surface performance insights and optimization recommendations.
This feature is available for Amazon Redshift Provisioned RG and RA3 instances and Amazon Redshift Serverless in the following additional AWS Regions: Asia Pacific (New Zealand), Canada West (Calgary), AWS GovCloud (US-East), and AWS GovCloud (US-West). To learn more, visit our documentation or the blog.

## 핵심 요약

요약 미지원
