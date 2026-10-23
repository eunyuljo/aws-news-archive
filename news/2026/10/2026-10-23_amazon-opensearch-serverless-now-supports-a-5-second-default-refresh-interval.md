---
title: "Amazon OpenSearch Serverless now supports a 5-second default refresh interval"
date: "2026-10-23"
service: "OpenSearch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-opensearch-serverless-supports-5-second-refresh-interval/"
tags: ["OpenSearch", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon OpenSearch Serverless now supports a 5-second default refresh interval

**날짜:** 2026년 10월 23일
**서비스:** OpenSearch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-opensearch-serverless-supports-5-second-refresh-interval/

## 내용

Starting today, Amazon OpenSearch Serverless reduces the default refresh interval to 5 seconds for both search and vector collections. The refresh interval controls how quickly newly ingested documents become available for search. By lowering the default from 10 seconds to 5 seconds, newly written data becomes searchable faster, giving applications quicker read-after-write visibility automatically, with no configuration changes and no action required on your part. 
This improvement applies to the next generation of Amazon OpenSearch Serverless and takes effect by default on both search and vector collections. Faster refresh is valuable for workloads that continuously ingest data and need near real-time retrieval, including full-text search over frequently updated content as well as vector use cases such as retrieval-augmented generation (RAG), semantic search, and recommendation and personalization systems. This means applications and AI agents can retrieve and act on the most recently ingested data sooner, improving the relevance and accuracy of search results and RAG responses for datasets that change frequently. 
The 5-second default refresh interval is available in all&nbsp;24 regions&nbsp;where Amazon OpenSearch Serverless is available today. To learn more, see the Amazon OpenSearch Serverless documentation.

## 핵심 요약

요약 미지원
