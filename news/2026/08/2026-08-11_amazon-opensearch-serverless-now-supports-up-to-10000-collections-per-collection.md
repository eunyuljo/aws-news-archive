---
title: "Amazon OpenSearch Serverless now supports up to 10,000 collections per collection group"
date: "2026-08-11"
service: "OpenSearch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-opensearch-serverless-supports-10000-collections-per-collection-group/"
tags: ["OpenSearch", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon OpenSearch Serverless now supports up to 10,000 collections per collection group

**날짜:** 2026년 08월 11일
**서비스:** OpenSearch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-opensearch-serverless-supports-10000-collections-per-collection-group/

## 내용

The next generation of Amazon OpenSearch Serverless now supports up to 10,000 collections within a single collection group, increased from the previous limit of 1,500. Collection groups organize multiple collections and enable them to share OpenSearch Compute Units (OCUs), even when the collections are encrypted with different AWS KMS keys. With this higher limit, you can consolidate significantly more collections into a single collection group and manage them under a shared set of capacity limits. 
Customers use collection groups to reduce costs by sharing compute across many collections rather than provisioning separate OCUs for each KMS key, while still maintaining collection-level security and access controls. As customer workloads have grown, particularly for multi-tenant applications that provision a collection per tenant, the previous limit of 1,500 collections per group constrained how many tenants could benefit from a shared compute pool. Raising the limit to 10,000 collections on the next generation of Amazon OpenSearch Serverless lets you scale these workloads further, improve compute utilization, and lower per-collection cost, without creating and operating additional collection groups. The higher limit applies automatically to new and existing nextgen collection groups. 
The increased limit is available on the next generation of Amazon OpenSearch Serverless in all AWS Regions where it is available. To learn more, see Amazon OpenSearch Serverless&nbsp;technical documentation and quotas. 
&nbsp;

## 핵심 요약

요약 미지원
