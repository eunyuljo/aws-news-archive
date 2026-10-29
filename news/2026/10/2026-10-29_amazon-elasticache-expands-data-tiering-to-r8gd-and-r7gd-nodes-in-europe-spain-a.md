---
title: "Amazon ElastiCache expands data tiering to R8gd and R7gd nodes in Europe (Spain) and Asia Pacific (Hyderabad)"
date: "2026-10-29"
service: "ElastiCache"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/elasticache-data-tiering-spain/"
tags: ["ElastiCache", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon ElastiCache expands data tiering to R8gd and R7gd nodes in Europe (Spain) and Asia Pacific (Hyderabad)

**날짜:** 2026년 10월 29일
**서비스:** ElastiCache
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/elasticache-data-tiering-spain/

## 내용

Amazon ElastiCache for Valkey data tiering is now available on Graviton4-based R8gd nodes in the AWS Europe (Spain) Region, and on Graviton3-based R7gd nodes in the Europe (Spain) and Asia Pacific (Hyderabad) Regions. Data tiering is a lower-cost way to scale your Valkey clusters to hundreds of terabytes of capacity. It uses solid state drives (SSDs) on each node alongside memory. When memory fills up, ElastiCache automatically moves the least recently used items to SSD. When your application reads an item stored on SSD, ElastiCache moves it back into memory before serving the request. Data tiering is a good fit for workloads that regularly access up to 20% of their dataset, and for applications that can tolerate some extra latency when they read data from SSD. 
R8gd nodes are powered by AWS Graviton4 processors. They deliver up to 47% higher throughput, up to 43% lower P99 latency, and up to 31% better price-performance than Graviton3-based nodes of the same size. R7gd nodes are powered by AWS Graviton3 processors. They deliver up to 28% more throughput (read and write operations per second), up to 21% better P99 latency, and up to 25% more network bandwidth than Graviton2-based nodes. Actual performance varies by node size and workload. 
You can use data tiering on R8gd and R7gd nodes with Valkey 7.2 and later. To get started, create a new cluster or upgrade an existing one with the AWS Management Console, the AWS CLI, or the AWS SDKs. For pricing, see the &nbsp;Amazon ElastiCache pricing page&nbsp;. To learn more, see &nbsp;Data tiering&nbsp; and &nbsp;Supported node types&nbsp; in the ElastiCache documentation.

## 핵심 요약

요약 미지원
