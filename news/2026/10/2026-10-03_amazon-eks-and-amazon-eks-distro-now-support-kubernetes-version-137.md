---
title: "Amazon EKS and Amazon EKS Distro now support Kubernetes version 1.37"
date: "2026-10-03"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-distro-kubernetes-version-1-37"
tags: ["EKS", "2026", "new-region"]
nav_exclude: true
---

# Amazon EKS and Amazon EKS Distro now support Kubernetes version 1.37

**날짜:** 2026년 10월 03일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-distro-kubernetes-version-1-37

## 내용

Kubernetes version 1.37 introduced several new features and bug fixes, and AWS is excited to announce that you can now use Amazon Elastic Kubernetes Service (EKS) and Amazon EKS Distro to run Kubernetes version 1.37. Starting today, you can create new EKS clusters using version 1.37 and upgrade existing clusters to version 1.37 using the EKS console, the eksctl command line interface, or through an infrastructure-as-code tool.
Kubernetes version 1.37 introduces several key improvements, promoting the Metrics API to general availability as metrics.k8s.io/v1. This API provides Pod and node CPU and memory usage for the Horizontal Pod Autoscaler and kubectl top. Dynamic Resource Allocation (DRA) device taints and tolerations also graduate to general availability, letting DRA drivers and administrators taint devices such as GPUs so the scheduler avoids them unless tolerated. Horizontal Pod Autoscaler scale-to-zero graduates to beta and is enabled by default, allowing autoscalers with minReplicas: 0 that use object or external metrics to scale workloads to zero Pods when idle and back up when demand returns. To learn more about Kubernetes version 1.37, see our documentation and the Kubernetes project release notes.
EKS now supports Kubernetes version 1.37 in all the AWS Regions where EKS is available, including the AWS GovCloud (US) Regions.
You can learn more about the Kubernetes versions available on EKS and instructions to update your cluster to version 1.37 by visiting EKS documentation. You can use EKS cluster insights to check if there are any issues that can impact your Kubernetes cluster upgrades. EKS Distro builds of Kubernetes version 1.37 are available through ECR Public Gallery and GitHub. Learn more about the EKS version lifecycle policies in the documentation.

## 핵심 요약

요약 미지원
