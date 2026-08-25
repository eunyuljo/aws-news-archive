---
title: "Amazon EKS now supports multiple external OIDC identity providers per cluster"
date: "2026-08-25"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-multiple-oidc-providers"
tags: ["EKS", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon EKS now supports multiple external OIDC identity providers per cluster

**날짜:** 2026년 08월 25일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-multiple-oidc-providers

## 내용

Amazon Elastic Kubernetes Service (Amazon EKS) now supports multiple external OpenID Connect (OIDC) identity providers per cluster. You can associate up to 10 OIDC identity providers with a single cluster, giving you more flexibility in how you authenticate users and workloads to your Kubernetes clusters.  Many organizations use different identity providers for different user populations, such as employees, contractors, and CI/CD systems. You can now associate each of these providers directly with your cluster, without consolidating users into a single provider or running an intermediary identity broker. Each provider is configured and managed independently, so each population authenticates through its own provider and identity mapping. Your existing IAM authentication continues to work alongside every configured provider. You add each provider the same way as before, using the AWS Management Console or the AssociateIdentityProviderConfig API through the AWS CLI and AWS SDKs.  This capability is available at no additional cost in all AWS Regions where Amazon EKS is available. To learn more, see Grant users access to Kubernetes with an external OIDC provider in the Amazon EKS User Guide.

## 핵심 요약

요약 미지원
