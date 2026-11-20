---
title: "Amazon S3 Tables now support promoting replicas to writable tables"
date: "2026-11-20"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-tables-replication-writable-tables/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Amazon S3 Tables now support promoting replicas to writable tables

**날짜:** 2026년 11월 20일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-tables-replication-writable-tables/

## 내용

Amazon S3 Tables replication now lets you make a read-only replica of your Apache Iceberg table a standalone, writable table with a single API call. S3 Tables replication keeps read-only replica tables in sync with your source tables across table buckets, AWS Regions, and accounts. Instead of copying a replica into a new table, you can promote it in place to move writes to another Region. 
When you disassociate a replica from replication, the standalone table keeps its namespace and table name, so your queries and pipeline code carry over when you point your applications at it. The promoted table then works like an S3 table you created, and you can use it as a source for new replicas. 
This capability is available in all AWS Regions where S3 Tables replication is supported. You can use the AWS Management Console, AWS CLI, AWS SDKs, or S3 Tables API. For pricing details, visit the Amazon S3 pricing page. To learn more, see the S3 Tables overview page and documentation.

## 핵심 요약

요약 미지원
