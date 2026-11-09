---
title: "Amazon EKS Auto Mode and Karpenter now support Dynamic Resource Allocation"
date: "2026-11-09"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-auto-mode-karpenter-dra/"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon EKS Auto Mode and Karpenter now support Dynamic Resource Allocation

**날짜:** 2026년 11월 09일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-auto-mode-karpenter-dra/

## 내용

Amazon Elastic Kubernetes Service (Amazon EKS) now supports Dynamic Resource Allocation (DRA) for NVIDIA GPUs and Elastic Fabric Adapter (EFA) network devices when using Amazon EKS Auto Mode and Karpenter. You can now define the device attributes your Kubernetes workloads need with DRA, share GPU devices across Pods, and allocate topology-aligned GPU and EFA devices while Amazon EKS Auto Mode and Karpenter dynamically scale Amazon EC2 instances based on workload demand. 
With DRA, you define ResourceClaim or ResourceClaimTemplate objects that describe what GPU or EFA devices can be allocated to workloads, by model, architecture, or other attributes. When running distributed training or inference, you can define PCIe-aligned GPU and EFA devices for optimal performance. Workloads then request those DRA objects in their configuration, and Karpenter automatically launches the lowest-cost instances that match. When using Amazon EKS Auto Mode, the NVIDIA DRA driver and EFA DRA driver (DRANET) are built-in, and you simply define your DRA objects and use them in your workloads. Amazon EKS Auto Mode automatically prevents workloads using DRA and workloads using device plugins for the same device type from running on the same nodes to mitigate the risk of silent device oversubscription during migrations. 
DRA support for Amazon EKS Auto Mode and Karpenter is available in all AWS Regions, except the AWS GovCloud (US) Regions and the China Regions. DRA support is available for all Kubernetes versions in Karpenter, and for Kubernetes versions 1.36 and newer in Amazon EKS Auto Mode. To learn more, see the DRA documentation in the Amazon EKS User Guide and Karpenter documentation.

## 핵심 요약

요약 미지원
