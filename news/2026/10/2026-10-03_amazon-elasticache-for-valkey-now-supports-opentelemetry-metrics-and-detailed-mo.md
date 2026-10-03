---
title: "Amazon ElastiCache for Valkey now supports OpenTelemetry metrics and detailed monitoring"
date: "2026-10-03"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-elasticache-valkey-opentelemetry-metrics-detailed-monitoring"
tags: ["CloudWatch", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon ElastiCache for Valkey now supports OpenTelemetry metrics and detailed monitoring

**날짜:** 2026년 10월 03일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-elasticache-valkey-opentelemetry-metrics-detailed-monitoring

## 내용

Amazon ElastiCache for Valkey now publishes OpenTelemetry metrics to Amazon CloudWatch for your node-based clusters, and each metric carries attributes you can filter and aggregate on with Prometheus Query Language (PromQL) expressions. ElastiCache now offers two monitoring modes. Standard monitoring, the existing experience, continues to publish CloudWatch Metrics (Classic) every 60 seconds and now also publishes a core set of OpenTelemetry metrics at the same interval at no additional charge. Detailed monitoring, the new mode, lets you select from the full set of OpenTelemetry metrics and publish them every 15 seconds.
With OpenTelemetry metrics, you can detect any node in a cluster nearing its connection limit, break errors down by type during an incident, or forecast if a node will run out of memory. You can run these queries in CloudWatch and Grafana, keeping PromQL skills your team already has. With detailed monitoring, you can balance diagnostic depth and cost, with 15-second metrics enabling detection of short-lived events like latency spikes. The core set of OpenTelemetry metrics also powers ElastiCache Insights, a pre-built dashboard in Amazon CloudWatch.
To get started, open the Metrics tab for a cluster in the Amazon ElastiCache console, select Detailed, and choose Configure detailed metrics.
OpenTelemetry metrics and detailed monitoring are available for node-based Valkey clusters in all AWS Regions where Amazon CloudWatch supports OpenTelemetry metrics. There is no additional charge from ElastiCache for detailed monitoring. CloudWatch pricing for OpenTelemetry metrics applies to the detailed monitoring metrics you select, alarms you create, and PromQL API queries you run.
To learn more, see Monitoring ElastiCache with OpenTelemetry metrics in the Amazon ElastiCache User Guide.

## 핵심 요약

요약 미지원
