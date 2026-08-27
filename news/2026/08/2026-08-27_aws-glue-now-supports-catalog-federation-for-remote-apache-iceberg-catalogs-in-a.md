---
title: "AWS Glue now supports catalog federation for remote Apache Iceberg catalogs in AWS GovCloud (US) regions"
date: "2026-08-27"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-glue-catalog-federation-iceberg-govcloud/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# AWS Glue now supports catalog federation for remote Apache Iceberg catalogs in AWS GovCloud (US) regions

**날짜:** 2026년 08월 27일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-glue-catalog-federation-iceberg-govcloud/

## 내용

AWS Glue now supports catalog federation for remote Iceberg REST catalogs in AWS GovCloud (US) Regions. This capability provides direct and secure access to Iceberg tables, stored in Amazon S3 and cataloged in remote catalogs, using AWS analytics engines. 
With catalog federation, you can federate to Iceberg tables in remote catalogs using your preferred AWS analytics engines, without moving or copying tables. It synchronizes metadata real-time between AWS Glue Data Catalog and the remote catalog when data teams query Iceberg tables, which means that query results are always up-to-date with latest metadata. You can now choose the best price-performance for your workloads when analyzing remote Iceberg tables using your preferred AWS analytics engines, while maintaining consistent security controls when discovering or querying data. Catalog federation is supported by a wide variety of analytics engines, including Amazon Redshift, Amazon EMR, Amazon Athena, AWS Glue, and third-party engines like Apache Spark. 
Catalog federation uses AWS Lake Formation for access controls, allowing you to use fine-grained access controls, cross-account sharing, and trusted identity propagation when sharing remote catalog tables with other data consumers. Catalog federation integrates with catalog implementations that support the Iceberg REST specifications. 
Catalog federation is available in Lake Formation console and using AWS Glue and Lake Formation SDKs and APIs. This feature is generally available AWS GovCloud (US-East) and AWS GovCloud (US-West) regions. To learn more, visit the documentation.

## 핵심 요약

요약 미지원
