---
title: "Amazon CloudWatch Logs Insights adds 23 new query commands and functions"
date: "2026-06-17"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-logs-insights-new/"
tags: ["CloudWatch", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch Logs Insights adds 23 new query commands and functions

**날짜:** 2026년 06월 17일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-logs-insights-new/

## 내용

Amazon CloudWatch Logs Insights query language now supports 23 new commands and functions that give you new ways to query, parse, transform, and analyze your logs. Customers analyzing logs in CloudWatch Logs Insights often need to do conditional processing, string conversions, process IP addresses, parse different file formats, and execute complex stats commands.  With this launch, CloudWatch Logs Insights provides new hash functions (md5, sha256), string functions (strcontains supporting case-insensitive search, split), conditional logic (if statement), and conversion functions (toNumber, toInt, toLong, toDouble). It also adds IP functions (ipv4ToNumber, isPrivateIP, isPublicIP, isReservedIP), analytics functions (rate, count_over_time, sum_over_time, offset, histogram), and parse functions (parse CSV, parse XML, parse multi, values, addtotals). Additionally, queries now support “limit any N” to fetch the first N results, and can use up to 10 stats commands.  These commands and functions are available today in all commercial AWS Regions. To learn more, see the Amazon CloudWatch Logs documentation.

## 핵심 요약

요약 미지원
