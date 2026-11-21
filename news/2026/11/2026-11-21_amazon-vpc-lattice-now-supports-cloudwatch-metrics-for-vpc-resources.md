---
title: "Amazon VPC Lattice now supports CloudWatch metrics for VPC resources"
date: "2026-11-21"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/vpc-lattice-cloudwatch-metrics/"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# Amazon VPC Lattice now supports CloudWatch metrics for VPC resources

**날짜:** 2026년 11월 21일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/vpc-lattice-cloudwatch-metrics/

## 내용

Amazon VPC Lattice now publishes Amazon CloudWatch metrics for VPC resources. Resource owners — those who share resources via VPC Lattice — and resource consumers — those who access those shared resources — can now see TCP traffic to resources such as databases, clusters, and on-premises endpoints. Resource owners get metrics for resource gateways and resource configurations. Consumers get metrics for resource endpoints, service network endpoints, and service network VPC associations. Previously, resource access logs were the primary way to see this traffic, but they required additional processing and provided limited real-time visibility. Now you can monitor your layer-4 resources directly in CloudWatch. 
With these metrics, you can proactively catch connectivity issues and optimize resource capacity. Capacity planning metrics — including bytes processed, new flows, and active flows — let resource owners monitor traffic per resource gateway and per resource configuration to track load on shared resources. Reliability metrics, such as dropped packets, help you detect problems early. Resource gateways also report port allocation errors, which show when a resource gateway needs more IPv4 addresses per network interface. Consumers can monitor traffic per resource endpoint, service network endpoint, or service network VPC association. They can set CloudWatch alarms for when new flows drop to zero or dropped packets increase, catching an unreachable resource before their applications do. Both owners and consumers can break metrics down by Availability Zone to isolate zonal issues or verify connections after configuration changes. 
CloudWatch metrics for VPC resources are available in all AWS Regions where Amazon VPC Lattice is available. For the list of Regions, see the Amazon VPC Lattice FAQs. 
To learn more, see CloudWatch metrics for Amazon VPC Lattice in the Amazon VPC Lattice User Guide, or visit the Amazon VPC Lattice product page.

## 핵심 요약

요약 미지원
