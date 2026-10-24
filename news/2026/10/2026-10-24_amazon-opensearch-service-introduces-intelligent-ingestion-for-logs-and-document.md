---
title: "Amazon OpenSearch Service introduces intelligent ingestion for logs and documents in Amazon S3"
date: "2026-10-24"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-opensearch-intelligent-ingestion-logs-documents-s3"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Amazon OpenSearch Service introduces intelligent ingestion for logs and documents in Amazon S3

**날짜:** 2026년 10월 24일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-opensearch-intelligent-ingestion-logs-documents-s3

## 내용

Amazon OpenSearch Serverless now offers intelligent ingestion, a fully managed feature that turns logs and documents stored in Amazon S3 into searchable content in Amazon OpenSearch Serverless (NextGen) collections . With intelligent ingestion, you can set up ingestion with a few clicks in the AWS Management Console or a single API call, with no ingestion infrastructure to manage. Intelligent ingestion supports observability logs and structured data in JSON, NDJSON, and JSON array formats, and unstructured files in PDF, Word, plain text, and Markdown formats. 
You choose an S3 source and a collection index, and intelligent ingestion handles the rest. It automatically detects data types, parses documents, describes images, chunks text, generates vector embeddings, and indexes the results. You don't need to manage ingestion or document-processing infrastructure, or size capacity in advance. Use ingestion jobs for one-time loads such as migrations and backfills, or ingestion streams to keep an index in sync as new objects arrive in your bucket. Capacity scales with your workload up to the collection's configured limit, and you pay only for active processing. Source S3 buckets can be in the same AWS account as the collection or in a different account. 
For logs and structured data, intelligent ingestion applies transformations and optionally adds embeddings, with no pipeline code. For unstructured data, it parses PDF, Word, plain text, and Markdown files while keeping headings, reading order, and tables intact, so the content lands in an index ready for semantic and hybrid search. When documents contain charts, diagrams, screenshots, or photos, a vision-language model generates text descriptions that are indexed with the surrounding content, making visual information searchable too. 
Intelligent ingestion is available today for Amazon OpenSearch Serverless (NextGen) collections, with Amazon S3 as the source, in seven AWS Regions. To get started, open the Amazon OpenSearch Service console, choose your collection, and select the Ingestion tab. To learn more, see Intelligent ingestion in the Amazon OpenSearch Service Developer Guide. For pricing, see Amazon OpenSearch Service pricing.

## 핵심 요약

요약 미지원
