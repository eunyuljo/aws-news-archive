---
title: "Amazon CloudWatch Observability EKS add-on now supports telemetry filtering"
date: "2026-11-21"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-otel-addon-filtering/"
tags: ["EKS", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch Observability EKS add-on now supports telemetry filtering

**날짜:** 2026년 11월 21일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-otel-addon-filtering/

## 내용

Today, Amazon CloudWatch announces telemetry filtering for the CloudWatch Observability EKS add-on, so you can stop paying to ingest telemetry you don't use. 
You can now set cluster-wide include and exclude lists for namespaces, metric names, and pod and node labels. Exclude the non-production namespaces you don't monitor, drop high-cardinality metrics by name, and keep only the labels you group by rather than every label on every resource. Because ingestion is billed per GB, collecting less lowers what you pay, and you can adjust filters with a single add-on configuration update as your clusters change. 
Telemetry filtering is available in version 8.0.0 and later of the EKS add-on and Helm chart, in all AWS Regions where CloudWatch supports OpenTelemetry metrics. Telemetry sent through the add-on is charged at the Amazon EKS OpenTelemetry ingestion rate of $0.08 per GB. For details, see Amazon CloudWatch insights pricing. 
To get started, see Amazon CloudWatch Observability EKS add-on in the Amazon CloudWatch User Guide.

## 핵심 요약

요약 미지원
