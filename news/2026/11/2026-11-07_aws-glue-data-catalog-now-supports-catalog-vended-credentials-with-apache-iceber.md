---
title: "AWS Glue Data Catalog now supports catalog-vended credentials with Apache Iceberg REST catalog federation"
date: "2026-11-07"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/glue-catalog-vended-credentials-iceberg/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Glue Data Catalog now supports catalog-vended credentials with Apache Iceberg REST catalog federation

**날짜:** 2026년 11월 07일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/glue-catalog-vended-credentials-iceberg/

## 내용

AWS Glue Data Catalog now supports external catalog's vended credentials in Apache Iceberg REST catalog federation. You can now read external Iceberg tables from Amazon Athena, Amazon EMR, Amazon Redshift, and AWS Glue using coarse-grained table grants in your external Iceberg catalog. 
Glue Data Catalog already federates to external Iceberg REST catalogs through an AWS IAM role that you configure with access to your Amazon S3 buckets. This enhancement in Glue Data Catalog provides another way to connect to an external Iceberg catalog and read only the tables that the external catalog authorizes. It uses temporary security credentials that are scoped to the Amazon S3 storage prefix and vended by your external Iceberg catalog. AWS Lake Formation manages access control when you query an external table using any AWS analytics engine, letting you restrict access further down to specific rows and columns and share external Iceberg tables across AWS accounts. 
This feature is available through the AWS Lake Formation Management Console, AWS CLI, and the AWS Glue and Lake Formation SDKs. This feature is available in all commercial AWS Regions where Glue and Lake Formation are supported. To learn more, visit the documentation.

## 핵심 요약

요약 미지원
