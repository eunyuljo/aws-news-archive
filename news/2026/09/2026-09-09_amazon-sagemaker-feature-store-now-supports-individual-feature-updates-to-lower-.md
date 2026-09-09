---
title: "Amazon SageMaker Feature Store now supports individual feature updates to lower write latency"
date: "2026-09-09"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/sgm-feature-store-update-record/"
tags: ["SageMaker", "2026", "GA", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker Feature Store now supports individual feature updates to lower write latency

**날짜:** 2026년 09월 09일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/sgm-feature-store-update-record/

## 내용

Amazon SageMaker Feature Store is a fully managed capability that makes it easy to compute, store, and retrieve features for training and deploying AI models. SageMaker Feature Store now supports feature-level writes, a new capability for updating individual features in a record. Data scientists can now update one or more feature values in a single request, without rewriting the entire record. 
Data scientists can use a single update call to replace the read-modify-write pattern their pipelines run today. Each write updates only the features in the request and leaves every other feature in the record unchanged, which lowers write latency and cost. When multiple pipelines write to the same feature group, each pipeline updates only the features it computes, so a streaming job and a nightly batch job can update the same record independently. This capability enables data scientists to update a single feature at high processing volumes, without building merge logic in their data ingestion pipelines. 
This capability is now available in all AWS Regions where Amazon SageMaker Feature Store is available. For more information, see Amazon Feature Store Runtime, Standard V2 documentation and launch blog.

## 핵심 요약

요약 미지원
