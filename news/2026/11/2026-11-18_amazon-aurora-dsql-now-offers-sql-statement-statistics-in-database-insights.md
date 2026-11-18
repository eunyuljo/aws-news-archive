---
title: "Amazon Aurora DSQL now offers SQL statement statistics in Database Insights"
date: "2026-11-18"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-dsql-statement-statistics/"
tags: ["RDS", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon Aurora DSQL now offers SQL statement statistics in Database Insights

**날짜:** 2026년 11월 18일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-dsql-statement-statistics/

## 내용

Amazon Aurora DSQL now records statistics for each SQL statement your cluster runs and publishes them as Amazon CloudWatch OpenTelemetry (OTel) metrics. You can view them in Amazon CloudWatch Database Insights. For each statement, you see how often it runs, how long it takes, the rows it scans, returns, or changes, and the DPUs it uses. 
Statement statistics measure every successful statement rather than sampling activity. Use them to find the statements that take the most time, run most often, or cost the most. In Database Insights, choose a statement under Top SQL to see its normalized SQL text and per-call charts. You can also query the metrics with PromQL in CloudWatch. Turn on statement statistics for each cluster in the Aurora DSQL console or the API when you create or update the cluster. 
Statement statistics are available in all AWS Regions where Aurora DSQL is available. Standard CloudWatch metrics and Logs charges apply, with no additional Aurora DSQL charge. To learn more, see monitoring SQL statements with statement statistics in the Aurora DSQL User Guide and CloudWatch pricing.

## 핵심 요약

요약 미지원
