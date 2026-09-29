---
title: "Amazon DocumentDB (with MongoDB compatibility) now supports retryable writes"
date: "2026-09-29"
service: "DocumentDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-documentdb-retryable-writes/"
tags: ["DocumentDB", "2026", "new-region"]
nav_exclude: true
---

# Amazon DocumentDB (with MongoDB compatibility) now supports retryable writes

**날짜:** 2026년 09월 29일
**서비스:** DocumentDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-documentdb-retryable-writes/

## 내용

For developers building MongoDB-compatible applications, retryable writes improve application resilience during transient errors such as network interruptions or primary failovers. Amazon DocumentDB (with MongoDB compatibility) now supports retryable writes starting with engine version 8.0.2, eliminating the need for additional code changes when enabling this capability.
With retryable writes, the MongoDB driver automatically retries certain write operations one time if a transient error occurs. Most current MongoDB-compatible drivers enable retryable writes by default. With this release, applications connecting to Amazon DocumentDB 8.0.2 no longer need to set retryWrites=false in the connection string to avoid errors. Retryable writes are supported for all write commands except updateMany and deleteMany, as well as transaction commit and abort commands. On engine versions earlier than 8.0.2, retryable writes remain unsupported and must be disabled.
Retryable writes are available on Amazon DocumentDB 8.0.2 instance-based and serverless clusters in all regions where Amazon DocumentDB 8.0 is available. To get started with retryable writes, see the Amazon DocumentDB developer guide.

## 핵심 요약

요약 미지원
