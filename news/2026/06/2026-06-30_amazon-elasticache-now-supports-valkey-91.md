---
title: "Amazon ElastiCache now supports Valkey 9.1"
date: "2026-06-30"
service: "ElastiCache"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-elasticache-valkey-9-1/"
tags: ["ElastiCache", "2026", "GA", "performance"]
nav_exclude: true
---

# Amazon ElastiCache now supports Valkey 9.1

**날짜:** 2026년 06월 30일
**서비스:** ElastiCache
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-elasticache-valkey-9-1/

## 내용

Amazon ElastiCache now supports Valkey 9.1 for node-based clusters, delivering higher throughput, improved memory efficiency, and stronger access control for multi-tenant workloads. This release helps customers get more performance from existing infrastructure while simplifying common application patterns with new commands. 
Valkey 9.1 includes a redesigned I/O threading model that improves throughput by up to 17%, reduces memory usage for strings under 128 bytes by up to 20%, and introduces database-level access control lists that let administrators scope user permissions to specific numbered databases. New commands like HGETDEL for atomic hash field retrieval and deletion, MSETEX for setting multiple keys with a shared expiration, and CLUSTERSCAN for cluster-wide key iteration simplify workflows that previously required multi-step client logic. The release also adds new main-thread and I/O-thread usage metrics for better operational visibility.&nbsp; 
To get started, see Creating an ElastiCache cluster or upgrade an existing cluster. For more information about Valkey 9.1 features, see the Valkey 9.1 for ElastiCache launch blog. To learn more about the open source release, see the Valkey 9.1 community announcement.

## 핵심 요약

요약 미지원
