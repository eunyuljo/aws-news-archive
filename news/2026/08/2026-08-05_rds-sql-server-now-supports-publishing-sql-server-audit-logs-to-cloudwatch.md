---
title: "RDS SQL Server now supports publishing SQL Server Audit logs to CloudWatch"
date: "2026-08-05"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/rds-sqlserver-publish-sql-audit-to-cw/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# RDS SQL Server now supports publishing SQL Server Audit logs to CloudWatch

**날짜:** 2026년 08월 05일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/rds-sqlserver-publish-sql-audit-to-cw/

## 내용

Amazon Relational Database Service (Amazon RDS) for SQL Server now supports publishing SQL Server Audit logs to CloudWatch.&nbsp;SQL Server Audit is a native SQL Server feature that allows tracking and logging events that occur on the Database Engine. On Amazon RDS, you can create audits and audit specifications in the same way that you create them for on-premises SQL Server database servers. 
Now you can publish the audit logs to S3, CloudWatch, or both. If you enable both S3 and CloudWatch options, the audit log publication will be marked as "completed" only after the audit log files are uploaded to both S3 and CloudWatch. Once the audit logs are in CloudWatch, you can perform real-time analysis of the log data. If you enable retention, RDS keeps your audit logs on your DB instance for the configured period of time. 
For more information, see SQL Server Audit (database engine) in the SQL Server documentation. For detailed configuration instructions, see the Amazon RDS for SQL Server User Guide. This feature is available in all AWS Commercial and AWS GovCloud (US) Regions where Amazon RDS for SQL Server is available.

## 핵심 요약

요약 미지원
