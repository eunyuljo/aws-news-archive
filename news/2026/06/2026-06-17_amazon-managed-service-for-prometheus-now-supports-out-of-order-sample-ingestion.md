---
title: "Amazon Managed Service for Prometheus now supports out of order sample ingestion"
date: "2026-06-17"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-managed-service-prometheus-outoforder-ingestion/"
tags: ["CloudWatch", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# Amazon Managed Service for Prometheus now supports out of order sample ingestion

**날짜:** 2026년 06월 17일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-managed-service-prometheus-outoforder-ingestion/

## 내용

Amazon Managed Service for Prometheus now supports out-of-order sample ingestion and a workspace-level rule query offset. All workspaces have a default out-of-order time window of 1 minute, allowing the workspace to accept metric samples arriving outside strict chronological order. You can adjust this window to match your ingestion patterns or set it to 0 to disable the feature and discard out-of-order samples. You can also configure a global rule query offset that introduces a delay before rule evaluation queries run, giving late-arriving samples time to be ingested before rules execute. 
Together, these features reduce data loss and improve alerting accuracy for workloads with distributed collectors, batched exports, or variable network latency. Out-of-order sample support ensures late-arriving data points are ingested rather than discarded, preserving metric completeness. The rule query offset compensates for the expected ingestion delay. Without it, rules evaluate instantly and may miss samples that haven't landed yet, producing results that differ from the same expression evaluated after all metrics arrive. Two new CloudWatch vended metrics, OutOfOrderIngestionRate and OutOfOrderSampleAge give you visibility into ingestion patterns, helping you tune both settings for your workload.&nbsp; 
Out-of-order sample ingestion and rule query offset are available in all AWS regions where Amazon Managed Service for Prometheus is generally available. To get started, configure the out-of-order time window and ruler query offset in your workspace settings via AWS console, API or CLI. For more information, see Amazon Managed Service for Prometheus user documentation.

## 핵심 요약

요약 미지원
