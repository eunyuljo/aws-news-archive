---
title: "AWS Elemental MediaConnect Router now supports configurable recovery latency modes"
date: "2026-08-21"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/mediaconnect-router-latency-modes/"
tags: ["CloudWatch", "2026", "new-region", "performance"]
nav_exclude: true
---

# AWS Elemental MediaConnect Router now supports configurable recovery latency modes

**날짜:** 2026년 08월 21일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/mediaconnect-router-latency-modes/

## 내용

AWS Elemental MediaConnect Router now enables customers to configure latency settings, providing control over the internal connection latency between inputs and outputs within the router. Previously, the protocol latency inside the router was set automatically by the service and could not be adjusted. 
MediaConnect Router now offers two latency configuration options on router outputs: balanced mode and low-latency mode. The balanced mode maintains the existing behavior for general use cases, while the low-latency mode optimizes the internal connection recovery time for latency-sensitive workflows. The appropriate mode is configured per router output, allowing the same input to feed multiple outputs with different latency requirements. A new CloudWatch metric, RouteFabricRecoveryLatency, provides visibility into the configured recovery latency for each route. 
Customers can configure and view the latency setting using the MediaConnect API or AWS Management Console and AWS CLI. 
Configurable recovery latency is available in all regions where MediaConnect Router is currently deployed. To learn more about latency modes, visit the AWS Elemental MediaConnect documentation.

## 핵심 요약

요약 미지원
