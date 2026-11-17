---
title: "IAM Identity Center now supports VPC endpoints and network access controls"
date: "2026-11-17"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/iam-identity-center-vpc-endpoints/"
tags: ["IAM", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# IAM Identity Center now supports VPC endpoints and network access controls

**날짜:** 2026년 11월 17일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/iam-identity-center-vpc-endpoints/

## 내용

AWS IAM Identity Center now supports interface VPC endpoints powered by AWS PrivateLink and network access controls, enabling you to keep IAM Identity Center traffic private and restrict which networks can reach your&nbsp;IAM Identity Center services. 
Previously, IAM Identity Center rejected traffic arriving through VPC endpoints, requiring all sign-in and API traffic to use public endpoints. With this launch, you can create interface VPC endpoints for&nbsp;AWS access portal and service APIs to route traffic over the AWS private network. IAM Identity Center sign-in traffic flows through the AWS Sign-in VPC endpoint. You can attach VPC endpoint policies to each endpoint to scope which AWS organizations, accounts and resources are reachable through your private connection. 
Network access controls add a second layer of enforcement at the IAM Identity Center instance level. When enabled, you can require that all access arrive through a VPC endpoint, allow specific IP address ranges or VPCs as trusted sources, and exclude individual applications from enforcement to accommodate services that connect from outside your VPC. SCIM provisioning traffic from your external identity provider can be independently restricted to known IP address ranges. Network access controls are configured through the IAM Identity Center API and are disabled by default. 
This capability is available in all commercial AWS Regions and the AWS GovCloud (US) Regions at no additional cost. To learn more, see Interface VPC endpoints in the IAM Identity Center User Guide.&nbsp;For more information, visit the IAM Identity Center product page.

## 핵심 요약

요약 미지원
