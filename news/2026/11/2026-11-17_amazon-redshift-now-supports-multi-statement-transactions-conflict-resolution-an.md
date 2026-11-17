---
title: "Amazon Redshift now supports multi-statement transactions, conflict resolution, and time travel for Apache Iceberg"
date: "2026-11-17"
service: "Redshift"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/redshift-time-travel-multi-statement"
tags: ["Redshift", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Redshift now supports multi-statement transactions, conflict resolution, and time travel for Apache Iceberg

**날짜:** 2026년 11월 17일
**서비스:** Redshift
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/redshift-time-travel-multi-statement

## 내용

Amazon Redshift now supports multi-statement transactions, automatic write-conflict resolution, and time travel for Apache Iceberg tables. You can run multi-step, concurrent transformation pipelines directly on Iceberg tables and audit the results, with the transaction semantics you expect from a data warehouse. This helps anyone writing to Iceberg tables at production scale. Batch jobs get all-or-nothing commits across multiple steps. Streaming and scheduled jobs can write to the same tables at the same time. Analysts, auditors, and AI agents can query a table as it existed at any point in time. 
With multi-statement transactions, you group several statements in a single BEGIN…COMMIT statement and publish them as one atomic Iceberg snapshot. This means a multi-step load such as a MERGE followed by a DELETE, can be commited together as one atomic operation, are never queryable in a half-applied state, and roll back cleanly if there's a failure. Automatic conflict resolution lets concurrent writes, such as streaming inserts alongside scheduled deletes, write to the same table and commit together when their changes don't overlap, instead of failing and retrying. Time travel lets you query a table as it existed at a past point in time with AS OF TIMESTAMP. You can use it to reproduce reports, audit changes, or recover from a bad write without keeping extra copies. These capabilities are available in all AWS commercial Regions for Amazon Redshift’s provisioned RG or serverless clusters that are writing to or querying Iceberg tables.. To get started, see the following list of resources: 
1/ Resolving concurrent writes for Apache Iceberg tables using Amazon Redshift 
2/ Multi-statement transactions for Apache Iceberg tables in Amazon Redshift 
3/ Time travel support for Apache Iceberg&nbsp;

## 핵심 요약

요약 미지원
