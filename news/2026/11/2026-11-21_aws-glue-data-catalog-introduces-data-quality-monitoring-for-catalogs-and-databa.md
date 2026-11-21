---
title: "AWS Glue Data Catalog introduces data quality monitoring for catalogs and databases"
date: "2026-11-21"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/glue-catalog-data-quality-monitoring/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# AWS Glue Data Catalog introduces data quality monitoring for catalogs and databases

**날짜:** 2026년 11월 21일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/glue-catalog-data-quality-monitoring/

## 내용

AWS Glue Data Catalog introduces data quality monitoring for catalogs and databases, powered by AWS Glue Data Quality, which profiles and evaluates your tables at catalog scale from a single configuration. You define data quality checks once for a catalog, a database, or a single table, and AWS Glue Data Quality evaluates every table in scope, including tables added later, on the cadence you choose. Quality issues surface as data changes, without per-table setup or manual runs, which helps keep bad data from reaching downstream consumers. 
You can use built-in profiling options that AWS Glue provides for common baseline statistics or provide your own Data Quality Definition Language (DQDL) ruleset with analyzers, rules, or both to hold every table in a database to the same quality standards. You have the flexibility to run evaluations once when you create the configuration or set up triggers, so evaluations run on a schedule or whenever table metadata changes, including every Apache Iceberg commit. After three runs on a table, AWS Glue Data Quality flags anomalous statistics that drift outside expected bounds, surfacing changes that no rule covers. Results are accessible through the existing AWS Glue Data Quality APIs, or you can opt-in to write them to Apache Iceberg tables in the AWS Glue Data Catalog or to Amazon S3. 
Data quality monitoring for catalogs and databases in AWS Glue Data Catalog is available in all AWS Commercial, AWS GovCloud (US), and AWS China regions. 
To get started, create a data quality configuration by using the AWS CLI, API, or SDKs, which support built-in profiling and custom DQDL rulesets at the catalog, database, or table level. In Amazon SageMaker Unified Studio, you can turn on profiling for a catalog or database from the catalog page. To learn more, visit the AWS Glue Data Quality documentation and the Amazon SageMaker Unified Studio documentation.

## 핵심 요약

요약 미지원
