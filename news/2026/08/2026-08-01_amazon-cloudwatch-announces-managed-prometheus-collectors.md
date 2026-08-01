---
title: "Amazon CloudWatch announces managed Prometheus collectors"
date: "2026-08-01"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/cloudwatch-managed-collectors/"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch announces managed Prometheus collectors

**날짜:** 2026년 08월 01일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/cloudwatch-managed-collectors/

## 내용

Amazon CloudWatch now supports collecting Prometheus metrics from your AWS infrastructure using fully managed collectors — enabling you to monitor Amazon EKS, Amazon EC2, Amazon ECS, Amazon MSK, and Amazon OpenSearch Service workloads without deploying or managing any agents. 
Previously, getting Prometheus metrics into CloudWatch required deploying, scaling, and maintaining a self-managed OpenTelemetry Collector. Managed Prometheus collectors eliminate that overhead. You provide a scrape configuration and a connection to your resources, and CloudWatch handles provisioning, scaling, and collection automatically. Metrics are delivered in OpenTelemetry format and can be queried alongside your AWS vended metrics using PromQL — providing unified alarming, dashboarding, and cross-service correlation in a single view. 
Managed collectors support Kubernetes service discovery (EKS), DNS-based service discovery via AWS Cloud Map (ECS), direct instance scraping (EC2), and open monitoring endpoints (MSK, OpenSearch). Metrics for EKS, MSK and Open Search can be visualized in automatic dashboards, queried with PromQL and used in CloudWatch alarms. 
This feature is available in all AWS Regions where the CloudWatch OTLP endpoint is available, except Asia Pacific (New Zealand). Managed Prometheus collectors are charged by the hour and standard CloudWatch OpenTelemetry metric ingestion pricing applies. To get started, see the documentation.

## 핵심 요약

요약 미지원
