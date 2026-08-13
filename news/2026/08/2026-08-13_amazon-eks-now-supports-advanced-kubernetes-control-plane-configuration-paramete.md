---
title: "Amazon EKS now supports advanced Kubernetes control plane configuration parameters"
date: "2026-08-13"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-control-plane-configuration-parameters"
tags: ["EKS", "2026", "new-region"]
nav_exclude: true
---

# Amazon EKS now supports advanced Kubernetes control plane configuration parameters

**날짜:** 2026년 08월 13일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-control-plane-configuration-parameters

## 내용

Amazon Elastic Kubernetes Service (Amazon EKS) now supports configuring parameters for Kubernetes control plane components including the scheduler, controller manager, and API server. You can tune pod placement strategies to improve resource utilization, adjust how quickly horizontal pod autoscaling responds to changes in demand, set resource lifecycle parameters such as event retention duration, and more.  Cluster administrators now have more control over Kubernetes control plane parameters beyond the defaults. For example, you can set the scheduler's node resource fit strategy parameter to MostAllocated, which packs pods onto nodes that are already well utilized and helps you run the same workloads on fewer nodes. The default LeastAllocated strategy spreads pods across nodes, and you can keep it where headroom matters more than density.  You can configure Kubernetes control plane parameters in any AWS Region where Amazon EKS is available. For the full list of configurable parameters and to learn more, see Control plane configuration in the Amazon EKS User Guide.

## 핵심 요약

요약 미지원
