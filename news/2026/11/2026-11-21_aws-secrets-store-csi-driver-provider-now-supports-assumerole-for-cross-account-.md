---
title: "AWS Secrets Store CSI Driver Provider now supports AssumeRole for cross-account secret access"
date: "2026-11-21"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-store-csi-driver-assumerole/"
tags: ["EKS", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Secrets Store CSI Driver Provider now supports AssumeRole for cross-account secret access

**날짜:** 2026년 11월 21일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-store-csi-driver-assumerole/

## 내용

The AWS Secrets Store CSI Driver Provider now supports AssumeRole (role-chaining), allowing Kubernetes pods to access secrets and parameters across AWS accounts by assuming an IAM role in the account where the secrets are stored. Previously, customers reading cross-account secrets needed to add a resource policy to each secret and use a customer-managed KMS key, as the AWS managed key (aws/secretsmanager) cannot be used for cross-account access. Now, teams can name a target role in the SecretProviderClass, and the provider assumes that role to fetch the secrets.
With AssumeRole support, customers managing hundreds of AWS accounts and thousands of services can simplify cross-account secret access. A single trust policy on one target role replaces resource policies on each secret. Secrets encrypted with the AWS managed key (aws/secretsmanager) and SSM parameters become readable across accounts. The target account sees workload-specific session names in CloudTrail events for better attribution. This feature works with both IAM Roles for Service Accounts (IRSA) and EKS Pod Identity on initial mount and rotation, and supports failover regions.
AssumeRole support is available in all AWS Regions where Amazon EKS and the AWS Secrets Store CSI Driver Provider are available.
To learn more, see the Assume an IAM role to retrieve secrets with the ASCP documentation.

## 핵심 요약

요약 미지원
