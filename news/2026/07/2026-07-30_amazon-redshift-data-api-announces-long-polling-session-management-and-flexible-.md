---
title: "Amazon Redshift Data API announces long polling, session management, and flexible batch execution"
date: "2026-07-30"
service: "Redshift"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-data-api-longpolling-listsession-flexiblebatchexecute/"
tags: ["Redshift", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon Redshift Data API announces long polling, session management, and flexible batch execution

**날짜:** 2026년 07월 30일
**서비스:** Redshift
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-data-api-longpolling-listsession-flexiblebatchexecute/

## 내용

Amazon Redshift Data API introduces new capabilities that reduce the number of API calls to retrieve SQL statement metadata or results, provide visibility into sessions, and allow batch statements to execute on separate transactions.  Long polling: Long polling enables you to retrieve SQL statement metadata or results without polling repeatedly until the SQL statement reaches a terminal state, by delaying returning a synchronous response until the SQL statement finishes. To use this feature, specify the WaitTimeSeconds parameter on ExecuteStatement, BatchExecuteStatement, DescribeStatement, GetStatementResult, or GetStatementResultV2.  ListSessions: Applications that reuse sessions across multiple queries can now enumerate active sessions and filter by status, compute target, or database, eliminating the need to track session identifiers externally.  Flexible batch execution: BatchExecuteStatement now supports an ExecutionMode parameter with AUTO_COMMIT mode, allowing each SQL statement in a batch to execute independently so a single failure no longer rolls back the entire batch — useful for ETL pipelines and administrative scripts where partial completion is acceptable. In addition, BatchExecuteStatement now accepts an array of SqlParameter, enabling parameter reuse across all statements in a batch: define parameters once and reference them in any statement, eliminating the need to embed literal values in each query.  These features are generally available for Amazon Redshift Provisioned and Amazon Redshift Serverless in all AWS commercial and AWS GovCloud (US) Regions that support Amazon Redshift Data API. To get started, visit the Amazon Redshift Data API developer guide.

## 핵심 요약

요약 미지원
