---
title: "Amazon CloudWatch Logs Insights now lets you estimate bytes scanned before running a query"
date: "2026-10-01"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/cloudwatch-logs-estimate-bytes-scanned/"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch Logs Insights now lets you estimate bytes scanned before running a query

**날짜:** 2026년 10월 01일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/cloudwatch-logs-estimate-bytes-scanned/

## 내용

Amazon CloudWatch Logs Insights now lets you estimate the volume of log data, in bytes, that a query would scan over your selected log groups and time range - without running the query. This helps you adjust your log group selection, time range, and filters before running the query.
In the CloudWatch console, the estimate appears automatically in the query editor when you change the log group selection, time range, or query text. When using the AWS CLI or API, append the estimate command to your query to request it explicitly. Queries that use the estimate command incur no CloudWatch Logs Insights query charges.
The estimate command is available in all AWS commercial regions. To learn more, see the Amazon CloudWatch Logs documentation.

## 핵심 요약

요약 미지원
