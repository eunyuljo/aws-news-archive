---
title: "Amazon S3 Vectors metadata pre-filtering is now available in AWS GovCloud (US) Regions"
date: "2026-10-10"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/s3-vectors-metadata-pre-filtering-in-govcloud-regions/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon S3 Vectors metadata pre-filtering is now available in AWS GovCloud (US) Regions

**날짜:** 2026년 10월 10일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/s3-vectors-metadata-pre-filtering-in-govcloud-regions/

## 내용

Amazon S3 Vectors metadata pre-filtering is now available in the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions. Pre-filtering evaluates metadata filters before running similarity search, returning up to 5x more of the matching vectors when your filter is selective. S3 Vectors also adds a prefix match operator ($startsWith) for filtering on values like paths and URLs. Together, these improvements give your retrieval-augmented generation (RAG), agentic, and semantic-search applications more complete results when you filter, so your applications return more relevant answers.
S3 Vectors provides native support to store and query vectors in Amazon S3, delivering purpose-built, cost-optimized vector storage and query at billion-vector scale. With this launch, indexes in new vector buckets in the AWS GovCloud (US) Regions use metadata pre-filtering by default, with no change to how you write vectors with PutVectors or run filtered queries with QueryVectors. To use pre-filtering on an existing index, update it in place with the UpdateIndexMode API. You can also compare pre-filtering against your current filtering on the same index, using a per-query parameter on QueryVectors, before you update.
Metadata pre-filtering is available at no additional cost in all commercial AWS Regions where Amazon S3 Vectors is available, and in the AWS China Regions. We are in the process of deploying this change and plan to complete the deployment in the coming days. To get started, use the AWS CLI, AWS SDKs, or the Amazon S3 console. To learn more, visit the Amazon S3 Vectors documentation and the AWS News blog.
&nbsp;

## 핵심 요약

요약 미지원
