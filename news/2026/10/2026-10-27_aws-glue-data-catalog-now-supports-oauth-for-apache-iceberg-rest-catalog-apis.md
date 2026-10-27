---
title: "AWS Glue Data Catalog now supports OAuth for Apache Iceberg REST Catalog APIs"
date: "2026-10-27"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/glue-catalog-oauth-iceberg-rest/"
tags: ["RDS", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Glue Data Catalog now supports OAuth for Apache Iceberg REST Catalog APIs

**날짜:** 2026년 10월 27일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/glue-catalog-oauth-iceberg-rest/

## 내용

AWS Glue Data Catalog now supports OAuth 2.0 bearer token authentication for Apache Iceberg REST Catalog (IRC) APIs using AWS Sign-In. The Apache Iceberg REST Catalog specification defines OAuth 2.0 as its standard authentication mechanism, and query engines such as Apache Spark, Trino, and Apache Flink implement it natively. These engines and external integration partners can now authenticate to the Glue Data Catalog Iceberg endpoint using standard OAuth 2.0 bearer tokens, in addition to AWS Signature Version 4 (SigV4). 
You can now grant partners federated access to your Iceberg tables without distributing AWS credentials. Using OAuth 2.0 Token Exchange (RFC 8693), you exchange an OpenID Connect (OIDC) identity token for a short-lived, Glue-scoped bearer token and include it in IRC requests following the same standards-based pattern used across the Iceberg ecosystem. Access remains governed by AWS IAM and AWS Lake Formation permissions. Common use cases include enabling third-party analytics and data cloud platforms to query tables in the Glue Data Catalog through a single, consistent authentication path. 
This capability is available in all AWS Regions where AWS Glue and Lake Formation are available. To learn more, see the AWS Glue User Guide and AWS Sign-In User Guide.

## 핵심 요약

요약 미지원
