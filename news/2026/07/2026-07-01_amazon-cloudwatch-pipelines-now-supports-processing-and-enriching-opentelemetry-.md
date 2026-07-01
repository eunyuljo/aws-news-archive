---
title: "Amazon CloudWatch pipelines now supports processing and enriching OpenTelemetry metrics"
date: "2026-07-01"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/cloudwatch-pipelines-otel-metrics"
tags: ["CloudWatch", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch pipelines now supports processing and enriching OpenTelemetry metrics

**날짜:** 2026년 07월 01일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/cloudwatch-pipelines-otel-metrics

## 내용

Amazon CloudWatch pipelines now supports processing and enriching OpenTelemetry (OTel) metrics during ingestion. CloudWatch pipelines is a fully managed service that ingests, transforms, and routes telemetry data to CloudWatch without requiring you to manage infrastructure.  Until now, customers who needed to enrich or transform OTel metrics before storage had to build custom processing layers or modify application instrumentation at the source. With OTel metric processing in CloudWatch pipelines, you can apply metric transformations centrally as part of the ingestion path with no new infrastructure required. With CloudWatch pipelines, you can enrich metrics by adding business context such as team ownership, cost center, and environment tags to metrics from sources you cannot modify. You can strip high-cardinality labels from custom workloads to reduce storage costs, and rename metrics and attributes to enforce consistent naming conventions across your organization. Processing is applied transparently to matched metrics with no changes to application instrumentation required.  OTel metric processing for CloudWatch pipelines is available in all AWS Regions where CloudWatch pipelines and CloudWatch native OpenTelemetry metrics are supported. Processing of OTel metrics via pipelines is offered at no additional cost. Standard CloudWatch pricing for OTel metrics ingestion apply. For pricing details, see CloudWatch Pricing.  To get started, open the Amazon CloudWatch console, navigate to pipelines under Ingestion, and select CloudWatch Metrics (OTel) as the source. To learn more, see the CloudWatch pipelines documentation.

## 핵심 요약

요약 미지원
