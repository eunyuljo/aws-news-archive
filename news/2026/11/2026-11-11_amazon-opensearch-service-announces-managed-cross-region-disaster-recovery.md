---
title: "Amazon OpenSearch Service announces managed cross-Region disaster recovery"
date: "2026-11-11"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-service-managed-cross-region-disaster-recovery/"
tags: ["CloudWatch", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon OpenSearch Service announces managed cross-Region disaster recovery

**날짜:** 2026년 11월 11일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-service-managed-cross-region-disaster-recovery/

## 내용

Amazon OpenSearch Service now offers managed cross-Region disaster recovery, so you can meet strict availability and business continuity requirements for mission-critical search, AI, and analytics workloads without building or maintaining replication yourself. After you create domains in two Regions, you can pair them with a single API call or a few steps in the AWS Management Console. 
Managed disaster recovery delivers a recovery point objective (RPO) of under one minute and a recovery time objective (RTO) of under 20 minutes. The secondary domain stays continuously in sync with the primary. For planned events such as maintenance or Region rotation, a switchover swaps the two domains' roles with zero data loss. If your primary domain becomes unavailable, a failover promotes the secondary, with data loss limited to the replication lag. After a failover, you restore protection by pairing the new primary with a secondary domain. You can monitor replication health and lag with Amazon CloudWatch metrics. 
Managed disaster recovery requires OpenSearch 3.7 or later and supports domains in the same AWS account, including domains encrypted with customer managed AWS Key Management Service (AWS KMS) keys. Domains that use UltraWarm storage or OpenSearch Optimized instances (OR1 or OR2) aren't supported. If you're on an earlier version, clone-based upgrades let you test OpenSearch 3.7 against your workload, cut over when you're ready, and roll back if needed. 
There's no additional charge for managed disaster recovery. You pay standard rates for the secondary domain and cross-Region data transfer. For details, see Amazon OpenSearch Service pricing. 
Managed disaster recovery is available today in all commercial AWS Regions where Amazon OpenSearch Service is available (Region list). To get started, see the disaster recovery documentation.

## 핵심 요약

요약 미지원
