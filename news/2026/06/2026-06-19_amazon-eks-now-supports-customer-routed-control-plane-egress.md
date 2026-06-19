---
title: "Amazon EKS now supports customer-routed control plane egress"
date: "2026-06-19"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-customer-routed-control-plane-egress"
tags: ["EKS", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon EKS now supports customer-routed control plane egress

**날짜:** 2026년 06월 19일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-customer-routed-control-plane-egress

## 내용

Today, Amazon Elastic Kubernetes Service (Amazon EKS) introduces customer-routed control plane egress, a capability that lets you route outbound Kubernetes API server traffic through your own Amazon VPC. This includes admission webhook callbacks, OpenID Connect (OIDC) provider lookups, and aggregate API server requests. With customer-routed control plane egress, this traffic flows through your VPC, where you control the routing, security groups, and egress path.  Organizations with data perimeter requirements, compliance mandates, or private network infrastructure can use customer-routed control plane egress to reach private OIDC providers and webhook servers that are accessible only within their VPC, and control how that traffic routes through their network. To get started, set controlPlaneEgressMode to CUSTOMER_ROUTED when creating a new cluster or updating an existing cluster. To enforce this configuration organization-wide, use the eks:controlPlaneEgressMode IAM condition key with AWS Organizations Service Control Policies.  Customer-routed control plane egress is available at no additional cost in all AWS Regions where Amazon EKS is available. To learn more, see Configure control plane egress routing in the Amazon EKS User Guide.

## 핵심 요약

요약 미지원
