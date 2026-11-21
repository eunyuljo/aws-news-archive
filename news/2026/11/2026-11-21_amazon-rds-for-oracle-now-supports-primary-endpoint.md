---
title: "Amazon RDS for Oracle now supports Primary Endpoint"
date: "2026-11-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-primary-endpoint-v2/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon RDS for Oracle now supports Primary Endpoint

**날짜:** 2026년 11월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-primary-endpoint-v2/

## 내용

Amazon Relational Database Service (Amazon RDS) for Oracle now provides a Primary Endpoint, a DNS name that always resolves to the current primary DB instance in a replica configuration. When you switch over to an Oracle replica, Amazon RDS points the Primary Endpoint to the new primary DB instance, so you don't need to change your application connection strings. Previously, after each switchover, you had to update connection strings or DNS records to point to the new primary DB instance, which often required change approvals and coordination across teams. 
With Primary Endpoint, you can run planned switchovers, such as disaster recovery drills, to replicas in the same AWS Region or to cross-Region replicas without changing your application configuration. If your applications connect through the Primary Endpoint, you don't need to update their connection strings after the switchover. 
Every RDS for Oracle Enterprise Edition DB instance has a Primary Endpoint at no additional charge, and you don't have to create it. The Primary Endpoint is provided in addition to the instance endpoint, so your existing applications aren't affected. 
Primary Endpoint is available in all commercial AWS Regions where Amazon RDS for Oracle is available. To learn more, see Using the Primary Endpoint for Amazon RDS for Oracle in the Amazon RDS User Guide.

## 핵심 요약

요약 미지원
