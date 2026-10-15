---
title: "Amazon RDS Proxy now supports SQL Server 2022"
date: "2026-10-15"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/rds-proxy-supports-sqlserver-2022"
tags: ["RDS", "2026", "security"]
nav_exclude: true
---

# Amazon RDS Proxy now supports SQL Server 2022

**날짜:** 2026년 10월 15일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/rds-proxy-supports-sqlserver-2022

## 내용

Amazon RDS Proxy, a fully managed, highly available database proxy for Amazon Relational Database Service (RDS), now supports Amazon RDS for SQL Server&nbsp;instances running major version 2022.
 
 
 Amazon RDS Proxy sits between your application and the database to pool and share established database connections, improving database efficiency and application scalability. For Amazon RDS for SQL Server Multi-AZ databases, RDS Proxy automatically connects to the standby database instance during a failure, preserves application connections, and helps reduce failover times by up to 83%. RDS Proxy supports standard IAM authentication for SQL Server, where your applications authenticate to the proxy using AWS Identity and Access Management (IAM) and RDS Proxy manages database connections using credentials stored in AWS Secrets Manager.
 
 
 You can enable Amazon RDS Proxy for your SQL Server 2022 database in a few steps on the Amazon RDS console, then connect by pointing your application to the RDS Proxy endpoint. To get started, see our documentation.

## 핵심 요약

요약 미지원
