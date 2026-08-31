---
title: "Amazon OpenSearch Service adds new Cluster Insights for faster diagnosis of cluster status"
date: "2026-08-31"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/opensearch-cluster-status-insight/"
tags: ["RDS", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon OpenSearch Service adds new Cluster Insights for faster diagnosis of cluster status

**날짜:** 2026년 08월 31일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/opensearch-cluster-status-insight/

## 내용

Amazon OpenSearch Service has expanded Cluster Insights with 17 new insights that identify the root causes behind Red and Yellow cluster status and provide actionable recommendations to resolve them. These insights cover resource exhaustion scenarios including JVM out-of-memory, sustained CPU saturation, as well as configuration issues such as zone imbalance, and misconfigured replica counts. 
Previously, when a cluster entered Red or Yellow status due to unassigned shards, diagnosing the underlying cause required manually correlating multiple metrics across nodes and availability zones. With these new insights, OpenSearch Service automatically identifies the specific resource constraint or misconfiguration responsible and provides tailored recommendations — such as scaling up instance types, increasing disk capacity, or correcting shard allocation settings — so you can restore cluster stability faster. 
Six new Critical-severity insights detect conditions causing primary shards to become unassigned (Red status), while eleven insights ranging from Medium to Critical severity surface issues preventing replica shard allocation (Yellow status). Each insight identifies affected nodes and provides specific remediation recommendations to help you take targeted corrective action. 
These insights are available at no additional cost for Amazon OpenSearch Service domains running OpenSearch 1.0 and later, and Elasticsearch 6.8 and later, across 11 Regions globally: US East (N. Virginia, Ohio), US West (Oregon), Canada (Central), Asia Pacific (Sydney, Tokyo), and Europe (Frankfurt, Ireland, London, Paris, Stockholm). To learn more, visit the Cluster Insights documentation or view the complete catalog of available insights.

## 핵심 요약

요약 미지원
