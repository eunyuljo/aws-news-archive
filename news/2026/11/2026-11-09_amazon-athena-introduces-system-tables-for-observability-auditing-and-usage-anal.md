---
title: "Amazon Athena introduces system tables for observability, auditing, and usage analytics"
date: "2026-11-09"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/athena-system-tables/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon Athena introduces system tables for observability, auditing, and usage analytics

**날짜:** 2026년 11월 09일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/athena-system-tables/

## 내용

Amazon Athena now offers system tables which automatically capture your usage data and make it available for observability, usage analysis, and audit use cases. When you enable system tables, usage data is available within minutes of query completion across your workgroups and stored as service-managed, read-only Iceberg tables on Amazon S3 Tables with configurable retention. You can query it directly with Athena, while AWS manages the tables for you, including schema definition, partitioning, compaction, and snapshot maintenance, removing all operational burden. 
Athena provides usage data through APIs like GetQueryExecution, CloudWatch metrics, and CloudTrail logs. With this launch, usage data is also available as iceberg tables that you can search, filter, aggregate, and join directly without building or maintaining custom pipelines. Platform teams can query the query_executions table to build cost allocation dashboards that show data scanned by workgroup, by user, or by table using simple SQL statements, and without custom ETL. Additionally, the AWS Agent Toolkit provides skills for querying system tables to surface usage patterns and optimization recommendations. Because the data is stored in the open Apache Iceberg format, you can also query it with DuckDB, Amazon Redshift, Amazon EMR or any other Iceberg-compatible engine. 
Athena system tables are available in all AWS Regions where Athena and Amazon S3 Tables are available. To get started, enable system tables from the Athena console or API. To learn more, visit the Amazon Athena documentation or the &nbsp;blog.

## 핵심 요약

요약 미지원
