---
title: "Amazon CloudWatch Logs Insights adds 25 new query commands and functions"
date: "2026-07-17"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-cloudwatch-logs-insights-ql/"
tags: ["CloudWatch", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon CloudWatch Logs Insights adds 25 new query commands and functions

**날짜:** 2026년 07월 17일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-cloudwatch-logs-insights-ql/

## 내용

Amazon CloudWatch Logs Insights query language now supports 25 new commands and functions that expand your ability to query, transform, correlate, and analyze logs. Customers analyzing logs in CloudWatch Logs Insights often need to perform statistical aggregation, handle null values in time-series data, compare logs across time windows, detect outliers, and enrich events with lookup data.  With this launch, CloudWatch Logs Insights adds type conversion and encoding functions (hexToAscii, hexToDec, decToHex), date and time functions (parseDate, formatDate, queryStartTime, queryEndTime, queryTimeRange), string functions (messageSize), JSON inspection functions (jsonArraySize, jsonArrayContains), and a conditional validation function (isNumeric). It also introduces statistical commands (variance, topk, countFrequent), row-sequencing and null-handling commands (autoregress, accum, filldown, fillmissing), sessionization and time-comparison commands (sessionize, logcompare), a data analysis command (outlier), query-composition and join commands (where, appendcols), and a lookup enrichment command (cidrlookup).  These commands and functions are available today in all commercial AWS Regions. To learn more, see the Amazon CloudWatch Logs documentation.

## 핵심 요약

요약 미지원
