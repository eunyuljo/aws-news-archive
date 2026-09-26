---
title: "AWS IAM outbound identity federation now supports interface VPC endpoints for OIDC discovery"
date: "2026-09-26"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts-vpc-oidc/"
tags: ["IAM", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS IAM outbound identity federation now supports interface VPC endpoints for OIDC discovery

**날짜:** 2026년 09월 26일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts-vpc-oidc/

## 내용

AWS Identity and Access Management (IAM) outbound identity federation now supports Amazon Virtual Private Cloud (VPC) endpoints for the OpenID Connect (OIDC) discovery APIs. You can now access the OIDC discovery metadata and JSON Web Key Set (JWKS) verification key endpoints from within your VPC using AWS PrivateLink, without requiring traffic to traverse the public internet.
IAM outbound identity federation eliminates the need to use long-lived credentials when your AWS workloads access external services. Instead, your workloads request short-lived JSON Web Tokens (JWTs) from AWS Security Token Service (AWS STS). External services verify these tokens using public verification keys and metadata available at OIDC discovery endpoints. Previously, the OIDC discovery endpoints were only reachable over the public internet, so a verifying workload running in a VPC without internet access could not retrieve them. With this launch, you can create an interface VPC endpoint to reach these endpoints privately, keeping the verification key retrieval traffic within the AWS network. This capability helps you meet network security requirements for workloads that operate in VPCs with restricted internet access, while still enabling external services to verify JWTs.
This feature is available in all commercial AWS Regions, the AWS GovCloud (US) Regions, and China Regions. There is no additional charge for this feature beyond standard AWS PrivateLink pricing. To learn more, see the IAM User Guide.

## 핵심 요약

요약 미지원
