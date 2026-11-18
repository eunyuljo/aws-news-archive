---
title: "Amazon EKS Auto Mode now rightsizes Pods to reduce compute costs (Preview)"
date: "2026-11-18"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/eks-auto-mode-pod-rightsizing-preview/"
tags: ["EC2", "2026", "preview", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EKS Auto Mode now rightsizes Pods to reduce compute costs (Preview)

**날짜:** 2026년 11월 18일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/eks-auto-mode-pod-rightsizing-preview/

## 내용

Amazon Elastic Kubernetes Service (Amazon EKS) introduces resource optimization for EKS Auto Mode, a new capability that rightsizes the CPU and memory requests of running Pods based on their actual usage. CPU and memory requests are often set at deploy time and rarely revisited, and Auto Mode provisions EC2 instances to fit them. Rightsizing lets Auto Mode run the same Deployments and StatefulSets on fewer or smaller instances, without hand tuning and at no additional charge.
Turn on resource optimization by creating a ClusterResourceOptimizationPolicy in your EKS cluster, review its recommendations in the default Recommend mode, and switch to Apply mode when you're ready to resize running Pods in place, without recreating them. For example, a platform team running Java services under Argo CD can rightsize every application namespace without editing templates or creating GitOps drift, while resource optimization keeps memory above each Java heap and raises memory after an out-of-memory kill. It doesn't change the CPU or memory that a Horizontal Pod Autoscaler or KEDA scales on, and you can exclude workloads that the Vertical Pod Autoscaler already manages.
You can use resource optimization on EKS Auto Mode clusters running Kubernetes 1.36 or later in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Asia Pacific (Seoul), and Asia Pacific (Tokyo).
To learn more, see Rightsize workloads with resource optimization in the Amazon EKS User Guide and the EKS Auto Mode product page.

## 핵심 요약

요약 미지원
