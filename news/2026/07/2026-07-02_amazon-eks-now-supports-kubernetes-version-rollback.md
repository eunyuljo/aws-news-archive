---
title: "Amazon EKS now supports Kubernetes version rollback"
date: "2026-07-02"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-version-rollback"
tags: ["EKS", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EKS now supports Kubernetes version rollback

**날짜:** 2026년 07월 02일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-version-rollback

## 내용

Amazon Elastic Kubernetes Service (Amazon EKS) now supports Kubernetes version rollback, enabling you to revert to the previous Kubernetes minor version within 7 days if any issues arise after an upgrade. This provides an additional safety net for your upgrade workflow, allowing you to validate the new version under real production conditions and rollback if needed.  You can initiate a rollback using the Amazon EKS console, AWS CLI, or AWS SDKs. Before proceeding, Amazon EKS evaluates your cluster rollback readiness insights that include automated checks covering API compatibility, version skew, add-on compatibility, cluster health, and more. For clusters running EKS Auto Mode, EKS automatically manages the rollback of worker nodes before reverting the control plane, honoring your configured disruption controls.  Amazon EKS version rollback is available at no additional cost in all AWS Regions where Amazon EKS is available. To get started, see version rollback in the Amazon EKS User Guide.

## 핵심 요약

요약 미지원
