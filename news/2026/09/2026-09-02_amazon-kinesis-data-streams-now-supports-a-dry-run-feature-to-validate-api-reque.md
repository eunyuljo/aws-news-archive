---
title: "Amazon Kinesis Data Streams now supports a dry run feature to validate API requests"
date: "2026-09-02"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-kinesis-data-streams-api/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon Kinesis Data Streams now supports a dry run feature to validate API requests

**날짜:** 2026년 09월 02일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-kinesis-data-streams-api/

## 내용

Amazon Kinesis Data Streams now supports a dry run feature to check whether an API request would succeed without executing the operation. Customers can now set the new optional parameter ‘DryRun’ to true in their API requests to validate permissions before interacting with a stream in production. 
Previously, customers had no safe way to test whether their application had the correct permissions to access a stream. They would often send a request engineered to fail after checking permissions, such as a PutRecord request with a payload deliberately larger than the maximum supported size. This approach was fragile as it depended on current service limits, and if those limits ever changed, the request could unexpectedly succeed, writing unintended records into the production stream and into any downstream consumers. Now, customers can simply set the parameter ‘DryRun’ to true to indicate they only want to validate the API request. If all checks complete successfully, the API returns a ‘DryRunOperationException’, confirming the request would have succeeded without the ‘DryRun’ parameter. 
The dry run feature is available for five APIs (PutRecord, PutRecords, GetRecords, GetShardIterator, and SubscribeToShard) in all AWS Regions where Amazon Kinesis Data Streams is available. For more information about dry run, see Test your permissions and request inputs with dry run in the Amazon Kinesis Data Streams Developer Guide. To get started with dry run, see the Amazon Kinesis Data Streams API Reference.

## 핵심 요약

요약 미지원
