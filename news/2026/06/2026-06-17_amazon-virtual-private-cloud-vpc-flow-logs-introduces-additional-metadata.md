---
title: "Amazon Virtual Private Cloud (VPC) Flow Logs introduces additional metadata"
date: "2026-06-17"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-flow-logs-metadata"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# Amazon Virtual Private Cloud (VPC) Flow Logs introduces additional metadata

**날짜:** 2026년 06월 17일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-flow-logs-metadata

## 내용

Amazon Virtual Private Cloud (VPC) Flow Logs now supports EC2 resource tags and next-hop interface metadata, simplifying network monitoring and troubleshooting by eliminating the need to manually correlate flow log data with resource metadata. 
VPC Flow Logs enable you to capture and log information about your VPC network traffic to monitor and troubleshoot network traffic issues. With EC2 resource tag support, you can embed tag values from your network interfaces, EC2 instances, and auto scaling groups. This eliminates the need for you to join flow log data with separate tag metadata to correlate records with specific workloads. With next-hop metadata support, you can capture details about the next-hop network interface for each flow, including its interface ID, subnet, Availability Zone, VPC, and interface type. These fields help you understand how traffic traverses through network resources such as NAT Gateways, Network Load Balancers, and Transit Gateways without requiring manual correlation of multiple data sources.  VPC Flow Logs EC2 resource tag and next-hop metadata support is available in the following AWS Regions: US East (Ohio, N. Virginia), US West (Northern California, Oregon), Africa (Cape Town), Asia Pacific (Hong Kong, Hyderabad, Jakarta, Melbourne, Mumbai, Osaka, Seoul, Singapore, Sydney, Tokyo, Auckland, Taipei, Bangkok, Malaysia), Canada (Central), Canada West (Calgary), Europe (Frankfurt, Ireland, London, Milan, Paris, Spain, Stockholm, Zurich), Israel (Tel Aviv), South America (Sao Paulo), Mexico (Central), European Sovereign Cloud (Germany), and AWS GovCloud (US-East, US-West) Regions. To get started, see the VPC Flow Logs documentation.

## 핵심 요약

요약 미지원
