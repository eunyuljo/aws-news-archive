---
title: "Amazon CloudWatch EKS Container Insights now offers built-in monitoring for open source Kubernetes tools"
date: "2026-11-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-kubernetes-tools/"
tags: ["RDS", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon CloudWatch EKS Container Insights now offers built-in monitoring for open source Kubernetes tools

**날짜:** 2026년 11월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-kubernetes-tools/

## 내용

Today, Amazon CloudWatch announces built-in monitoring for open source tools running on your Amazon EKS clusters, including Karpenter, KEDA, vLLM, KServe, SGLang, Ray and Knative Serving. You get dashboards for the tools you already use without running Prometheus or Grafana yourself. 
Monitoring starts automatically when you enable OTel Container Insights. For your AI inference workloads, you can see queued requests, time to first token, and KV cache usage for each model server. For autoscaling, you can see which scalers are failing and how long your scale loop takes. CloudWatch tags every metric with its pod, workload, and node, so you can trace a slow model server to the node it runs on. 
These EKS solutions are available in version 8.0.0 and later of the add-on and Helm chart, in all AWS Regions where CloudWatch supports OpenTelemetry metrics. Metrics are charged at the Amazon EKS OpenTelemetry ingestion rate of $0.08 per GB. For details, see Amazon CloudWatch insights pricing.&nbsp; 
To get started, see Solutions in the Amazon CloudWatch User Guide.

## 핵심 요약

요약 미지원
