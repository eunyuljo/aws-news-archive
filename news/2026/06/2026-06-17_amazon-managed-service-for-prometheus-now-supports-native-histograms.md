---
title: "Amazon Managed Service for Prometheus now supports Native Histograms"
date: "2026-06-17"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-managed-service-prometheus-native-histograms/"
tags: ["General", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon Managed Service for Prometheus now supports Native Histograms

**날짜:** 2026년 06월 17일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-managed-service-prometheus-native-histograms/

## 내용

Amazon Managed Service for Prometheus now supports ingestion, storage, and querying of Prometheus native histograms, enabling customers to capture high-resolution metric distributions with greater precision and lower cardinality than classic histograms. DevOps engineers, site reliability engineers, and platform teams monitoring latency, request durations, and other distributions can now get more accurate percentile calculations without pre-defining bucket boundaries or managing high-cardinality time series. 
Native histograms use exponential bucketing to automatically adapt resolution to your data, storing an entire distribution in a single time series rather than requiring one series per bucket boundary. This reduces active series count, as a classic histogram with 20 buckets that previously required 22 time series now requires only one, while delivering more precise tail-latency insights from functions like histogram_quantile(). You can adopt native histograms incrementally alongside existing classic histograms, migrating workloads at your own pace without disrupting current monitoring. Amazon Managed Service for Prometheus meters and charges native histograms based only on populated buckets that contain actual observations, so you don't pay for empty buckets in sparse distributions.&nbsp; 
This capability is available in all AWS Regions where Amazon Managed Service for Prometheus is offered. To get started, see Amazon Managed Service for Prometheus documentation.&nbsp;To learn about Native Histograms pricing, visit the Amazon Managed Service for Prometheus pricing page.

## 핵심 요약

요약 미지원
