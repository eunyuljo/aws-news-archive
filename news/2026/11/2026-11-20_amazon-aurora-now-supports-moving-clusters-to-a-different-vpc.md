---
title: "Amazon Aurora now supports moving clusters to a different VPC"
date: "2026-11-20"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-move-clusters-to-different-vpc/"
tags: ["RDS", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Aurora now supports moving clusters to a different VPC

**날짜:** 2026년 11월 20일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-move-clusters-to-different-vpc/

## 내용

Aurora PostgreSQL and Aurora MySQL clusters can now move from one Amazon Virtual Private Cloud (VPC) to another without data migration. You can move a cluster with a single API call or a modify action in the Amazon RDS console. This lets you move a cluster to a VPC with more IP address space or a non-overlapping CIDR range, consolidate your network architecture, or meet changing security and compliance requirements. 
Previously, moving an Aurora cluster to a different VPC meant creating a new cluster in the target VPC, migrating your data, and updating your applications with new connection strings. Now, a single ModifyDBCluster API call moves your existing cluster to the new VPC. Your data stays in place, your cluster endpoint stays the same, and connectivity is interrupted only briefly during the move. Before you start, turn off features that are tied to the cluster's current VPC, such as Aurora Global Database, Amazon RDS Proxy, and Amazon RDS Blue/Green Deployments. You can set them up again in the new VPC after the move. 
This feature is available for Aurora PostgreSQL and Aurora MySQL in all AWS Regions where Aurora PostgreSQL with express configuration is available. To get started, use the Amazon RDS console, AWS CLI, or AWS SDKs. To learn more, see the Aurora User Guide.

## 핵심 요약

요약 미지원
