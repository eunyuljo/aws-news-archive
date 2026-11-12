---
title: "Amazon EKS Auto Mode now supports security groups for Pods"
date: "2026-11-12"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-auto-mode-security-groups-for-pods/"
tags: ["EC2", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon EKS Auto Mode now supports security groups for Pods

**날짜:** 2026년 11월 12일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-auto-mode-security-groups-for-pods/

## 내용

Amazon EKS Auto Mode now supports security groups for Pods, letting you apply dedicated Amazon EC2 security group rules to individual Pods. Different workloads on the same node can carry different security groups, giving your Pods network-level segmentation without creating separate node pools for each application. 
Security groups for Pods extends your existing AWS network controls to the Pod level, so your Pods can reach resources such as Amazon RDS and Amazon ElastiCache databases that authorize connections by security group under the same rules the rest of your VPC uses. You define which Pods receive which security groups with a SecurityGroupPolicy resource, and Pods not matched by a policy keep using their node’s security groups. 
Security groups for Pods is included as part of EKS Auto Mode at no additional charge and is available on clusters running Kubernetes version 1.36 or later, in all AWS Regions where EKS Auto Mode is supported. To learn more, see Security groups for Pods in the Amazon EKS User Guide and the Amazon EKS Auto Mode product page.

## 핵심 요약

요약 미지원
