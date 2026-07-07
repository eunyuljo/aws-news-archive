---
title: "CloudWatch Application Signals now automatically captures errors, performance anomalies, and deployment events"
date: "2026-07-07"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/cloudwatch-service-events/"
tags: ["EKS", "2026", "new-region", "performance"]
nav_exclude: true
---

# CloudWatch Application Signals now automatically captures errors, performance anomalies, and deployment events

**날짜:** 2026년 07월 07일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/cloudwatch-service-events/

## 내용

Today, AWS announces Service Events for Amazon CloudWatch Application Signals, which automatically captures exception and latency event snapshots, function-level performance data, and deployment events from instrumented services without additional code changes. Customers can now quickly identify whether a deployment has introduced new exceptions by navigating to CloudWatch &gt; Application Signals &gt; [Service] &gt; Errors in the CloudWatch console. 
Service Events is available to any application with CloudWatch Application Signals enabled. Customers instrument their applications with the ADOT SDKs or the Amazon CloudWatch Observability EKS add-on. Once Application Signals is active, Service Events begins capturing exception and latency event snapshots and deployment events automatically. Optionally, customers can gain deeper performance visibility by turning on function-call metrics. 
Service Events is available in all commercial AWS Regions. Supported languages are Java, Python, and JavaScript. 
To get started, see Monitor service events in the Amazon CloudWatch User Guide. Service Events data is captured as logs. Function call metrics are captured as OpenTelemetry metrics. Standard CloudWatch pricing applies. For details, see CloudWatch pricing.

## 핵심 요약

요약 미지원
