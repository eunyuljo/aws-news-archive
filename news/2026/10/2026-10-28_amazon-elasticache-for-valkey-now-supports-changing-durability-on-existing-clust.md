---
title: "Amazon ElastiCache for Valkey now supports changing durability on existing clusters"
date: "2026-10-28"
service: "ElastiCache"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/elasticache-changing-durability/"
tags: ["ElastiCache", "2026", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon ElastiCache for Valkey now supports changing durability on existing clusters

**날짜:** 2026년 10월 28일
**서비스:** ElastiCache
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/elasticache-changing-durability/

## 내용

Amazon ElastiCache for Valkey now lets you enable or disable durability on your existing node-based clusters without creating a new cluster. Previously, you couldn't change the durability configuration of an existing cluster in place. This made it harder to move from caching to persistent data store use cases, or to adapt as your application requirements change. Now you can change durability at any point in your application's lifecycle. 
You can choose between two durability options: synchronous and asynchronous writes. Synchronous writes persist data across at least two AZs before responding to the client, designed for zero data loss at single-digit millisecond write latency. Asynchronous writes persist data after responding to the client, maintaining microsecond write latency at no additional cost. However, up to 10 seconds of uncommitted data could be lost in the rare event of a failure. Both options maintain microsecond read latency. You can now use ElastiCache for a broader set of use cases beyond caching where data loss is unacceptable such as AI agent long-term memory, AI agent workflow state, knowledge bases for RAG applications, payment tokenization, and real-time inventory management. 
This feature is available in all AWS Regions where ElastiCache for Valkey 9.0 and later is available. To get started, use the AWS Management Console, AWS SDK, or AWS CLI. For pricing, see the &nbsp;Amazon ElastiCache pricing page&nbsp;. To learn more, see &nbsp;Durability&nbsp; in the ElastiCache documentation.

## 핵심 요약

요약 미지원
