---
title: "Aurora PostgreSQL with express configuration now supports Amazon VPC"
date: "2026-11-20"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-postgresql-express-vpc/"
tags: ["RDS", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Aurora PostgreSQL with express configuration now supports Amazon VPC

**날짜:** 2026년 11월 20일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-postgresql-express-vpc/

## 내용

Aurora PostgreSQL databases created with express configuration can now move into an Amazon Virtual Private Cloud (VPC) with a single API call or a modify action in the Amazon RDS console. This helps you take AI-built prototypes and other applications to production without migrating data, while meeting your security and compliance requirements. You can also create a new database cluster inside a VPC using express configuration. 
With express configuration, Aurora PostgreSQL lets you create and query a serverless database in seconds. Connectivity runs through an internet access gateway, which makes this a good fit for rapid prototyping and AI agent-driven development. When your application is ready for production, a single ModifyDBCluster API call moves the cluster into a VPC and turns off the internet access gateway. That gives you security groups, private subnets, and features such as Aurora Global Database, Amazon RDS Blue/Green Deployments, and Amazon RDS Proxy. The move requires no data migration, keeps your cluster endpoint the same, and interrupts connectivity only briefly. You can also reverse it with the same API call. 
This feature is available in all AWS Regions where Aurora PostgreSQL with express configuration is available. To get started, use the Amazon RDS console, AWS CLI, or AWS SDKs. To learn more, see the Aurora User Guide.

## 핵심 요약

요약 미지원
