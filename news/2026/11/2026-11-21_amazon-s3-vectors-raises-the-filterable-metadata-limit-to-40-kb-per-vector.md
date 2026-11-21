---
title: "Amazon S3 Vectors raises the filterable metadata limit to 40 KB per vector"
date: "2026-11-21"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-vectors-raises-filterable-metadata-40kb-per-vector/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon S3 Vectors raises the filterable metadata limit to 40 KB per vector

**날짜:** 2026년 11월 21일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-vectors-raises-filterable-metadata-40kb-per-vector/

## 내용

Amazon S3 Vectors now supports up to 40 KB of filterable metadata per vector, up from 2 KB. You can attach and filter on more attributes per vector, such as category, permissions, timestamps, and descriptive tags, so your retrieval-augmented generation (RAG), agentic, and semantic-search applications can narrow results by more of the fields that matter to them. 
S3 Vectors provides native support to store and query vectors in Amazon S3, delivering purpose-built, cost-optimized vector storage and query at billion-vector scale. With this launch, indexes in new vector buckets support the higher limit by default, with no change to how you write vectors with PutVectors or run filtered queries with QueryVectors. To use the higher limit on an existing index, update it in place to enhanced index mode with the UpdateIndexMode API. 
The higher filterable metadata limit is available at no additional cost in all AWS Regions where Amazon S3 Vectors is available. To get started, use the AWS CLI, AWS SDKs, or the Amazon S3 console. To learn more, visit the Amazon S3 Vectors documentation.

## 핵심 요약

요약 미지원
