---
title: "Amazon EKS now supports EFA and placement groups on Amazon EKS Auto Mode and Karpenter"
date: "2026-07-23"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-efa-placement-groups/"
tags: ["EC2", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon EKS now supports EFA and placement groups on Amazon EKS Auto Mode and Karpenter

**날짜:** 2026년 07월 23일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-efa-placement-groups/

## 내용

Amazon Elastic Kubernetes Service (EKS) now supports Amazon EC2 placement groups and Elastic Fabric Adapter (EFA) network device configuration for node pools on EKS Auto Mode and the open-source Karpenter project, enabling you to optimize EKS workloads for performance and availability. These capabilities allow you to control EFA network interface configuration and how EC2 instances are physically distributed across AWS infrastructure for distributed training and inference workloads.  With EKS Auto Mode and Karpenter’s EFA configuration, you can configure network interfaces as EFA-only or standard ENI on EFA-capable instances with both dynamic and static capacity node pools. EFA-only interfaces do not consume IP addresses, giving you fine-grained control over IP utilization in your VPC while achieving full interconnect bandwidth. With placement group support, you can launch EC2 instances using cluster, spread, or partition strategies directly from your EKS Auto Mode or Karpenter node pool configuration, giving you control over how instances are physically distributed without additional operational workarounds. Together, these capabilities let you optimize for the performance, availability, and fault isolation characteristics your workloads require, whether that's maximizing throughput for distributed training jobs or minimizing blast radius for critical production services.  These features are available in all AWS Regions where Amazon EKS is available. To get started and learn more, see the EKS Auto Mode User Guide and Karpenter documentation.

## 핵심 요약

요약 미지원
