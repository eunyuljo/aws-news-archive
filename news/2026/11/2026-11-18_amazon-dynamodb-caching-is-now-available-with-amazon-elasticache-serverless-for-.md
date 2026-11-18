---
title: "Amazon DynamoDB caching is now available with Amazon ElastiCache Serverless for Valkey"
date: "2026-11-18"
service: "DynamoDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/dynamodb-caching-elasticache/"
tags: ["DynamoDB", "2026", "GA", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon DynamoDB caching is now available with Amazon ElastiCache Serverless for Valkey

**날짜:** 2026년 11월 18일
**서비스:** DynamoDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/dynamodb-caching-elasticache/

## 내용

Today, AWS announces the general availability of DynamoDB caching with Amazon ElastiCache Serverless for Valkey, a serverless alternative to Amazon DynamoDB Accelerator (DAX) that delivers sub-millisecond read latency for frequently accessed DynamoDB data. Previously, if you needed faster reads than the single-digit millisecond latency of DynamoDB, you had to provision and scale DAX nodes or run your own cache and keep it in sync with DynamoDB. Now you can access DynamoDB table data from a write-through cache that updates as data changes and scales automatically to meet changing workload demands, with no clusters or nodes to manage. 
DynamoDB caching requires no application logic changes and minimal configuration. You choose which DynamoDB tables and APIs to cache and how long to retain cached data. Your application's IAM credentials are used to access DynamoDB, so existing access control policies are automatically applied. 
DynamoDB caching is available in all commercial and AWS GovCloud (US) Regions. DynamoDB caching is offered at no additional cost, so you pay only for the ElastiCache Serverless and DynamoDB resources your applications use. To get started, see the ElastiCache Developer Guide.

## 핵심 요약

요약 미지원
