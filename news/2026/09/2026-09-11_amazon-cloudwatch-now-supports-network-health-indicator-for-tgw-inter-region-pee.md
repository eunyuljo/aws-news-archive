---
title: "Amazon CloudWatch now supports network health indicator for TGW inter-Region peering using synthetic monitors"
date: "2026-09-11"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/cloudwatch-network-monitoring-tgw-support/"
tags: ["RDS", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon CloudWatch now supports network health indicator for TGW inter-Region peering using synthetic monitors

**날짜:** 2026년 09월 11일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/cloudwatch-network-monitoring-tgw-support/

## 내용

With synthetic monitors in Amazon CloudWatch Network Monitoring, you can now determine whether a network performance issue on a path that crosses an AWS Transit Gateway inter-Region peering connection is caused by the AWS network. This helps network operators and application developers cut the time spent isolating the source of degradation on these paths. 
Previously, for synthetic monitors, the network health indicator (NHI) covered only paths that connect through AWS Direct Connect. With this release, synthetic monitors extend it to paths that reach a destination in a peered Region over Transit Gateway inter-Region peering. For these paths, the indicator reflects the health of the AWS network path up to the Transit Gateway peering connection, and is published to your Amazon CloudWatch account so you can build dashboards and set alarms. 
For the full list of AWS Regions where Network Monitoring for AWS workloads is available, visit the Regions list. To learn more, visit the Amazon CloudWatch Network Monitoring documentation.

## 핵심 요약

요약 미지원
