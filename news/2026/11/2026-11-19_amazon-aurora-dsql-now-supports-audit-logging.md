---
title: "Amazon Aurora DSQL now supports audit logging"
date: "2026-11-19"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-aurora-dsql-audit-logging/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Aurora DSQL now supports audit logging

**날짜:** 2026년 11월 19일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-aurora-dsql-audit-logging/

## 내용

Amazon Aurora DSQL now supports database-internal audit logging, a fully managed capability that captures SQL statements executed on your cluster. Previously, AWS CloudTrail recorded who connected to a DSQL cluster, but not what they did once inside it. Now, financial institutions and regulated enterprises can meet production compliance requirements by capturing DDL, DML, DCL, and SELECT statements with full statement text, bind parameters, acting principal (both PostgreSQL role and AWS IAM identity), timestamp, table name, and transaction identifier. 
With audit logging, you can feed SIEM systems directly from Amazon S3, satisfy auditor requirements for change accountability, and reconstruct events after security incidents. Logs are delivered as structured JSON to your S3 bucket via CloudWatch Vended Logs. Configuration requires a single SQL setting—no extension to load and no log-shipping pipeline to build. 
Audit logging is available in all AWS Regions where Aurora DSQL is available. Audit logging will incur Aurora DSQL DPU charges, charges for log delivery through CloudWatch Logs, and charges for storing audit records in Amazon S3. For pricing information, see Aurora DSQL pricing. To learn more, see audit logging in the Aurora DSQL User Guide.

## 핵심 요약

요약 미지원
