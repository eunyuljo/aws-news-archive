---
title: "Amazon CloudWatch Logs now automatically indexes frequently queried fields"
date: "2026-10-01"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/cloudwatch-logs-auto-indexes-fields/"
tags: ["CloudWatch", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon CloudWatch Logs now automatically indexes frequently queried fields

**날짜:** 2026년 10월 01일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/cloudwatch-logs-auto-indexes-fields/

## 내용

Amazon CloudWatch Logs now automatically indexes the fields you query frequently, speeding up CloudWatch Logs Insights queries without requiring any manual setup. Previously, you had to manually select the fields to index based on your query patterns and usage, requiring extra work for teams whose query patterns change over time.
CloudWatch Logs identifies the fields in your queries that you use for filtering with the = and IN operations and indexes them automatically, enabling queries to run faster and scan less data. Fields that are automatically indexed don't count toward your 20-field-per-log-group limit and are retained for 30 days. The list of automatically indexed fields is updated as your query patterns change. To keep a field indexed permanently, promote it to a field index policy using the console or API.
Auto-indexing is available in all AWS Regions where CloudWatch Logs field indexing is supported, at no additional cost. To learn more, see the Amazon CloudWatch Logs User Guide.

## 핵심 요약

요약 미지원
