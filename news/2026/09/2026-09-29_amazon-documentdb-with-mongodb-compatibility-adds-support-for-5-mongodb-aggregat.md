---
title: "Amazon DocumentDB (with MongoDB compatibility) adds support for 5 MongoDB aggregation stages and change stream capabilities in version 8.0.2"
date: "2026-09-29"
service: "DocumentDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-documentdb-8-0-2/"
tags: ["DocumentDB", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon DocumentDB (with MongoDB compatibility) adds support for 5 MongoDB aggregation stages and change stream capabilities in version 8.0.2

**날짜:** 2026년 09월 29일
**서비스:** DocumentDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-documentdb-8-0-2/

## 내용

Amazon DocumentDB (with MongoDB compatibility) now supports&nbsp;retryable writes, 5 new aggregation stages, and change stream enhancements starting from minor version 8.0.2. This release expands MongoDB API compatibility and improves query performance, making it easier to migrate MongoDB workloads to Amazon DocumentDB without application code changes.
Key new capabilities in version 8.0.2 include:
- Retryable Writes — insert, update, and delete operations automatically retry on transient network errors, improving application resilience during failovers.
 
 - New aggregation stages — $setWindowFields (with its full set of window operators), $bucketAuto, $facet, $graphLookup, and correlated $lookup, enabling advanced analytics, faceted search, and hierarchical queries.
 
 - Change stream enhancements — the $changeStreamSplitLargeEvent stage splits change events larger than the 16 MB limit into fragments, and change streams now emit events for createCollection and createIndex operations.
 
 - Query performance improvements — enhancements to the query planner add index-only scans for find and aggregation queries, index scans on $expr predicates, incremental sort, and faster count and countDocuments() operations.
 
 - Index management — support for the reIndex command on partial indexes.
These capabilities are available starting from Amazon DocumentDB 8.0.2 in all regions where Amazon DocumentDB is available. To learn more, see Supported MongoDB APIs, operations, and data types and Amazon DocumentDB release notes.

## 핵심 요약

요약 미지원
