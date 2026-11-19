---
title: "Amazon CloudWatch simplifies network performance monitoring for your Amazon Virtual Private Cloud (VPC)"
date: "2026-11-19"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-network-path-monitoring/"
tags: ["EC2", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon CloudWatch simplifies network performance monitoring for your Amazon Virtual Private Cloud (VPC)

**날짜:** 2026년 11월 19일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-network-path-monitoring/

## 내용

Amazon CloudWatch Network Monitoring now allows you to monitor the health of the AWS network paths that your workloads take by using performance monitors. Performance monitors provide near real-time visibility into whether the AWS network is healthy for your workloads, without installing any software.
Performance monitors report per-path metrics such as latency, a network impact score that shows network health, and traffic volume across all flows in your VPCs. You simply select the VPCs you want to monitor, and metrics are available within minutes. Using telemetry AWS already collects, with no additional services to enable, performance monitors determine the paths your traffic takes, within and across Availability Zones, across AWS Regions, and to AWS services, for TCP, UDP, and ICMP traffic. They then score each path by comparing it with its own recent history and with all other paths AWS measures at the same time. For example, a path that suddenly degrades, or degrades with many other paths during an AWS network event, scores high. Metrics publish to Amazon CloudWatch for dashboards and alarms, and AWS Organizations integration lets you monitor VPCs across accounts and Regions.
Performance monitors complement flow monitors in CloudWatch Network Monitoring. When a checkout application slows down, a performance monitor shows whether the path from the web tier in one Availability Zone to the database in another is degraded. A high network impact score points to the AWS network, so your team can engage AWS Support instead of investigating your application. If the path is healthy, you can focus on your own stack, where flow monitors use software agents on Amazon EC2 and Amazon EKS to find affected connections, such as a payment pod retransmitting to the database.
For available AWS Regions, see the Regions list. To learn more, visit the Amazon CloudWatch Network Monitoring documentation.

## 핵심 요약

요약 미지원
