---
title: "Amazon OpenSearch Service now supports index-level encryption"
date: "2026-10-12"
service: "OpenSearch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/opensearch-index-level-encryption"
tags: ["OpenSearch", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon OpenSearch Service now supports index-level encryption

**날짜:** 2026년 10월 12일
**서비스:** OpenSearch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/opensearch-index-level-encryption

## 내용

Amazon OpenSearch Service now supports index-level encryption, letting you encrypt each index at rest with its own AWS Key Management Service (AWS KMS) customer managed key.&nbsp;This helps you protect data with different ownership or sensitivity under separate keys on the same domain. For example, you can encrypt each tenant's data with its own key in a multi-tenant application.
Index-level encryption builds on the existing encryption at rest capability in Amazon OpenSearch Service. To enable it, set the encryption mode to Native and specify a customer managed AWS KMS key when you create a new domain using the AWS Management Console or the AWS CLI. You can then register additional keys with the domain and use them to encrypt individual indexes.
Index-level encryption is available for domains running OpenSearch version 3.3 or later in 14 AWS Regions: US East (N. Virginia, Ohio), US West (Oregon), Canada (Central), Asia Pacific (Mumbai, Seoul, Singapore, Sydney, Tokyo), Europe (Frankfurt, Ireland, London, Paris), and South America (São Paulo).&nbsp;There is no additional charge for the feature. Standard AWS KMS and OpenSearch Service charges apply.
To get started, see Index-level encryption in the Amazon OpenSearch Service Developer Guide.

## 핵심 요약

요약 미지원
