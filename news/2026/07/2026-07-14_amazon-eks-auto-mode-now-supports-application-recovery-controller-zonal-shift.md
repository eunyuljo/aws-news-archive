---
title: "Amazon EKS Auto Mode now supports Application Recovery Controller zonal shift"
date: "2026-07-14"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/eks-auto-mode-arc-zonal-shift"
tags: ["EKS", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EKS Auto Mode now supports Application Recovery Controller zonal shift

**날짜:** 2026년 07월 14일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/eks-auto-mode-arc-zonal-shift

## 내용

Amazon Elastic Kubernetes Service (Amazon EKS) now supports Amazon Application Recovery Controller (ARC) zonal shift and autoshift for clusters using EKS Auto Mode. ARC helps you manage and coordinate recovery across AWS Regions and Availability Zones (AZs). With this launch, EKS Auto Mode automatically protects your compute during a zonal shift at no additional cost or configuration, helping you maintain Kubernetes application availability by shifting in-cluster network traffic away from an impaired AZ. 
Customers run highly available applications across multiple AZs in Amazon EKS to eliminate a single point of failure. Because EKS Auto Mode manages compute on your behalf, you get zonal shift support without setting flags, granting permissions, or managing Karpenter versions; simply enable ARC zonal shift on your cluster. When a zonal shift is activated, EKS Auto Mode stops provisioning new capacity in the impaired AZ and halts voluntary disruptions such as consolidation and drift for nodes in that zone. It also prevents voluntary disruptions in healthy zones if they depend on scheduling pods to the impaired zone. When the shift expires or is canceled, normal operations resume. You can start a shift manually, or authorize AWS to manage it using zonal autoshift, with practice runs to verify your cluster functions with one less AZ. 
ARC zonal shift support for EKS Auto Mode is available in all AWS Regions where EKS Auto Mode is offered. To learn more, visit the Amazon EKS product page, the ARC zonal shift documentation, and the Amazon EKS Auto Mode documentation.

## 핵심 요약

요약 미지원
