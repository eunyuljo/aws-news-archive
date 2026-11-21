---
title: "Amazon CloudWatch Observability EKS add-on now supports custom OpenTelemetry and Prometheus telemetry"
date: "2026-11-21"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-addon-custom-telemetry/"
tags: ["EKS", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch Observability EKS add-on now supports custom OpenTelemetry and Prometheus telemetry

**날짜:** 2026년 11월 21일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-addon-custom-telemetry/

## 내용

Today, Amazon CloudWatch announces support for your own application telemetry in the CloudWatch Observability EKS add-on. The CloudWatch agent you already run now accepts metrics, traces, and logs from your applications, so you don't deploy and operate a separate collector to get them into CloudWatch. 
Applications instrumented with an OpenTelemetry SDK send to an OTLP endpoint that the agent serves on every node, on by default. Metrics arrive as CloudWatch metrics you query with PromQL, traces go to AWS X-Ray and Transaction Search, and logs go to CloudWatch Logs. 
For Prometheus metrics, the agent scrapes the targets described by standard ServiceMonitor and PodMonitor objects, with no Prometheus operator to run and no change to your scrape configuration. Each team defines its own targets alongside its application rather than in one central add-on configuration. Label selectors let you choose which monitors CloudWatch scrapes. 
Both sources carry the same Kubernetes, host, cloud, and service attributes the add-on applies to the pod they came from, so you can join application telemetry to your cluster metrics. 
Custom telemetry is available in version 8.0.0 and later of the EKS add-on and Helm chart, in all AWS Regions where CloudWatch supports OpenTelemetry metrics. Telemetry is charged at the Amazon EKS OpenTelemetry ingestion rate of $0.08 per GB. For details, see Amazon CloudWatch insights pricing. 
To get started, see Custom telemetry in the Amazon CloudWatch User Guide.

## 핵심 요약

요약 미지원
