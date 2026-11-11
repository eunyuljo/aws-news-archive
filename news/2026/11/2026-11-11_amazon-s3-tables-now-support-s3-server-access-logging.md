---
title: "Amazon S3 Tables now support S3 server access logging"
date: "2026-11-11"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-tables-server-access-logging/"
tags: ["S3", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon S3 Tables now support S3 server access logging

**날짜:** 2026년 11월 11일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-tables-server-access-logging/

## 내용

Amazon S3 Tables now support server access logging, providing you detailed records of the requests made to your table buckets. You can now track table operations, namespace management, and data access to support security audits, access analysis, and cost attribution. Log delivery is available at no additional cost, and you pay only for the storage of the log files. 
When you enable server access logging on a table bucket, S3 delivers logs for requests to all tables and namespaces in that bucket to a general purpose bucket in the same account and Region. Each record captures the requester, operation, table name, namespace, response status, and request timing, using the same space-delimited format as S3 server access logs for general purpose buckets. This lets you reuse your existing log analysis workflows to query S3 Table logs with any query engine of your choice such as Amazon Athena and DuckDB. 
Server access logging for S3 Tables is available in all AWS Regions where S3 Tables are available. You can enable it using the AWS Management Console, AWS CLI, AWS SDKs, or AWS CloudFormation. To learn more, visit the S3 Tables overview page and S3 Tables server access logging in the Amazon S3 User Guide.

## 핵심 요약

요약 미지원
