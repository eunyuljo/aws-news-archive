---
title: "Amazon EKS now supports AWS PrivateLink for the cluster OIDC endpoint"
date: "2026-07-29"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-oidc-endpoint-privatelink"
tags: ["EKS", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon EKS now supports AWS PrivateLink for the cluster OIDC endpoint

**날짜:** 2026년 07월 29일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-oidc-endpoint-privatelink

## 내용

Amazon Elastic Kubernetes Service (Amazon EKS) now supports AWS PrivateLink for the cluster OIDC discovery and JWKS endpoint. You can now reach the endpoint used by IAM roles for service accounts (IRSA) privately from your VPC without requiring internet egress.  Each EKS cluster publishes public signing keys at its OIDC endpoint for IRSA. With AWS PrivateLink for the cluster OIDC endpoint, tools running inside your VPC, such as eksctl, Terraform, or custom token validators, can now reach the OIDC discovery document and JWKS privately by creating an interface VPC endpoint for the com.amazonaws.&lt;region&gt;.oidc-eks service. This enables IRSA setup and token validation in VPCs without internet egress and ensures correct DNS resolution when the EKS management VPC endpoint is enabled with private DNS.  AWS PrivateLink for the cluster OIDC endpoint is available at no additional cost beyond standard AWS PrivateLink pricing in all AWS Regions where Amazon EKS is available. To get started, see Access the cluster OIDC endpoint using AWS PrivateLink in the Amazon EKS User Guide.

## 핵심 요약

요약 미지원
