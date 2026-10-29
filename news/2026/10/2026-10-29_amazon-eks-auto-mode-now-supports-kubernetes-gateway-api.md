---
title: "Amazon EKS Auto Mode now supports Kubernetes Gateway API"
date: "2026-10-29"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-auto-mode-kubernetes-gateway-api/"
tags: ["EKS", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon EKS Auto Mode now supports Kubernetes Gateway API

**날짜:** 2026년 10월 29일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-auto-mode-kubernetes-gateway-api/

## 내용

Amazon EKS Auto Mode now supports the Kubernetes Gateway API, giving customers a standard, portable way to define how traffic reaches their applications. Customers can configure application load balancing using Gateway and HTTPRoute resources, and EKS Auto Mode provisions and manages the underlying AWS infrastructure automatically. 
With this launch, EKS Auto Mode customers can adopt the next-generation Kubernetes traffic management standard without installing or configuring a separate controller. Capabilities include HTTP and gRPC routing, cross-namespace traffic routing for multi-team environments, weighted traffic splitting, header-based routing, and automatic TLS certificate discovery through AWS Certificate Manager. Existing workloads using Ingress resources continue to work alongside Gateway API resources. 
To get started, see the Amazon EKS documentation. Gateway API support is included as part of EKS Auto Mode and is available in all AWS Regions where EKS Auto Mode is supported. Standard charges apply for the AWS load balancing resources provisioned.

## 핵심 요약

요약 미지원
