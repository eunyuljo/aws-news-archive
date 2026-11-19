---
title: "Amazon S3 Replication adds exclusions and Multi-Region key resolution"
date: "2026-11-19"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-replication-exclusions-multi-region-key-resolution/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon S3 Replication adds exclusions and Multi-Region key resolution

**날짜:** 2026년 11월 19일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-replication-exclusions-multi-region-key-resolution/

## 내용

You can now replicate data in Amazon S3 buckets with fewer replication rules using two new S3 Replication capabilities, exclusions and Multi-Region key resolution. Buckets that many tenants or applications share often need many rules to skip certain data or to match encryption keys in each AWS Region. With these capabilities, customers who manage multi-tenant and shared buckets can replace many replication rules with a single rule. 
With exclusions, you can replicate an entire bucket while skipping specific prefixes or tagged objects, such as logs or experimental data. With Multi-Region key resolution, S3 Replication encrypts each replica with the matching AWS Key Management Service (AWS KMS) Multi-Region key in the destination Region, so replicas meet the same encryption requirements as their source objects. For example, a bucket that stores data for hundreds of tenants, each with its own Multi-Region key, can replicate with a single rule, including tenants you add later. 
Exclusions and Multi-Region key resolution are optional and available at no additional charge in all AWS Regions. To get started, use the AWS SDKs, AWS CLI, S3 API, or S3 console. To learn more, visit the S3 Replication product page and Replicating objects within and across Regions in the S3 User Guide.

## 핵심 요약

요약 미지원
