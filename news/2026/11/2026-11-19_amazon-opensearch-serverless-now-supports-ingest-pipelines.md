---
title: "Amazon OpenSearch Serverless now supports ingest pipelines"
date: "2026-11-19"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/opensearch-serverless-support-ingest-pipelines"
tags: ["Lambda", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon OpenSearch Serverless now supports ingest pipelines

**날짜:** 2026년 11월 19일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/opensearch-serverless-support-ingest-pipelines

## 내용

Amazon OpenSearch Serverless now supports ingest pipelines, so you can clean, enrich, and vectorize documents inside your collection as they are indexed, without running separate preprocessing infrastructure. Teams building search, log analytics, and generative AI applications can replace data-prep code in Lambda functions or ETL jobs with transformations that apply consistently to every document, regardless of how it is ingested. 
You can use ingest pipelines to normalize and clean data with processors such as copy, date, dot_expander, join, lowercase, uppercase, remove, rename, set, and trim. For semantic and AI search, you can chunk long text with text_chunking and generate embeddings at ingest time with text_embedding, text_image_embedding, and sparse_encoding. The ml_inference processor calls any model you have connected and lets you map its input and output fields yourself. You create and manage pipelines with the familiar OpenSearch _ingest/pipeline APIs. You can test a pipeline against sample documents with the _simulate API before sending it live traffic, then apply it as an index's default pipeline or on individual indexing and bulk requests. 
Pipeline processing uses your collection's indexing OpenSearch Compute Units (OCUs) and is billed the same way as other indexing activity. If you use a remote model with an ML processor, the model provider bills inference separately. Ingest pipelines are available in all AWS Regions where Amazon OpenSearch Serverless is available. 
To get started, see Ingest pipelines in Amazon OpenSearch Serverless in the Amazon OpenSearch Service Developer Guide. To learn more about OpenSearch Serverless, visit the Amazon OpenSearch Serverless product page. 
&nbsp;

## 핵심 요약

요약 미지원
