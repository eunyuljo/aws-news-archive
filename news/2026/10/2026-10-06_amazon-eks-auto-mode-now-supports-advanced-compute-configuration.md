---
title: "Amazon EKS Auto Mode now supports advanced compute configuration"
date: "2026-10-06"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/eks-auto-mode-advanced-compute-config/"
tags: ["EC2", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# Amazon EKS Auto Mode now supports advanced compute configuration

**날짜:** 2026년 10월 06일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/eks-auto-mode-advanced-compute-config/

## 내용

Amazon Elastic Kubernetes Service (EKS) Auto Mode now lets you tune kubelet settings, Linux kernel sysctls, and hugepages directly in the NodeClass Kubernetes resource. You can now run workloads that require specific node tuning on EKS Auto Mode, which automates node provisioning, scaling, patching, and upgrades for you.
With the new advancedCompute field in NodeClass, you can configure user namespaces for rootless container builds in CI/CD pipelines, tune eviction thresholds and container log rotation to protect nodes from disk and memory pressure, raise network and ARP cache limits for large clusters, and pre-allocate 2Mi or 1Gi hugepages for HPC, database, and latency-sensitive workloads. You apply these settings declaratively using the Kubernetes API. EKS Auto Mode validates them, applies them at node boot, and preserves them through scaling and upgrade events, so your workloads get the tuning they need while EKS Auto Mode continues to manage the underlying infrastructure, with no EC2 launch templates, custom AMIs, or privileged DaemonSets to maintain.
Amazon EKS Auto Mode advanced compute configuration is available in all AWS Regions where EKS Auto Mode is available.
To get started, see the Amazon EKS Auto Mode product page, and see Create a Node Class for Amazon EKS in the Amazon EKS documentation.

## 핵심 요약

요약 미지원
