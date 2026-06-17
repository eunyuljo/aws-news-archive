---
title: "Amazon S3 Vectors now supports up to 10,000 similarity search results per query"
date: "2026-06-17"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/s3-vectors-supports-10000-search-results-per-query"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Amazon S3 Vectors now supports up to 10,000 similarity search results per query

**날짜:** 2026년 06월 17일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/s3-vectors-supports-10000-search-results-per-query

## 내용

Amazon S3 Vectors can now return up to 10,000 similarity search results per query, a 100x increase from the previous limit.&nbsp;The higher result limit helps you retrieve a larger, more comprehensive set of candidates during similarity queries. This is especially valuable for applications with multi-stage retrieval pipelines that need to apply additional processing such as reranking, aggregations, or deduplication to produce a more relevant final result set. 
To get started with the higher limit, use the latest AWS SDK and update your application code to specify up to 10,000 relevant results (topK nearest neighbors) when making a QueryVectors API request. Query results are now returned across multiple pages, and you can start processing the first page immediately while retrieving additional pages as needed. For queries that return larger result sets, you pay a small data-returned fee based on the total size of results returned. The first 512 KB of data returned per query is free. For full pricing details, visit the S3 pricing page. 
S3 Vectors supports retrieving up to 10,000 results per query in all AWS Regions where it is available. To learn more about S3 Vectors, visit the product page and S3 User Guide.

## 핵심 요약

요약 미지원
