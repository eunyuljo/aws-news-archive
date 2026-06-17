---
title: "AWS Lake Formation extends table permissions to access underlying data in Amazon S3"
date: "2026-06-17"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lake-formation-access-data-amazon-s3"
tags: ["S3", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Lake Formation extends table permissions to access underlying data in Amazon S3

**날짜:** 2026년 06월 17일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lake-formation-access-data-amazon-s3

## 내용

AWS Lake Formation now enables you to read and write the underlying data files in Amazon S3 for tables registered in the AWS Glue Data Catalog. This provides you with a single set of permissions for both SQL queries and direct file access using your existing Lake Formation table grants.  With this launch, Lake Formation provides temporary, scoped credentials for registered S3 locations based on your table permissions. SELECT permissions grant read access, and SUPER permissions grant read and write access to the data at that location. This capability comes built-in with Amazon EMR 7.13 or later. As a result, you can access data files directly from your Spark jobs for tasks that require file level access such as model training, feature engineering, or debugging data quality issues.  You can also integrate your Apache Spark or Trino applications using APIs or through an open source plugin provided by AWS. Additionally, all access is logged in AWS CloudTrail to provide a unified audit trail across SQL and file-based operations on your tables.  This feature is available at no additional charge in all AWS Regions where AWS Lake Formation is available. To learn more, see Lake Formation&nbsp;documentation, EMR documentation, API reference, and open source plug-in.

## 핵심 요약

요약 미지원
