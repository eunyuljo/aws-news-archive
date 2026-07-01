---
title: "IAM Identity Center now enables programmatic AWS account access for customer managed applications"
date: "2026-07-01"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-iam-identity-center-account-access-customer-managed-apps/"
tags: ["IAM", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# IAM Identity Center now enables programmatic AWS account access for customer managed applications

**날짜:** 2026년 07월 01일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-iam-identity-center-account-access-customer-managed-apps/

## 내용

IAM Identity Center now enables customer managed applications to programmatically access AWS accounts on behalf of their users, including the ability to discover accounts and roles assigned to a user and retrieve temporary credentials required for AWS account access. 
If you have a customer managed application that authenticates users through an external identity provider (IdP), you can configure that IdP as a trusted token issuer (TTI) in IAM Identity Center. With this launch, you can now enable AWS account access for this application.&nbsp;Users who have already signed in through the IdP can access their assigned AWS accounts and obtain temporary security credentials for their authorized roles without a separate authentication flow.&nbsp;This eliminates redundant sign-in prompts that previously required users to re-authenticate even after signing in through their external identity provider. 
This feature is available for organization instances of IAM Identity Center. IAM Identity Center administrators must explicitly enable AWS account access for each customer managed application. Only management account administrators or delegated administrators can enable this capability, ensuring centralized governance over which applications can access account-level resources. 
This feature is available in all commercial AWS Regions, the AWS GovCloud (US) Regions, and the China Regions. To get started, navigate to the IAM Identity Center console, select your customer managed application, and enable AWS account access. For more information, see Enable AWS account access for customer managed applications in the IAM Identity Center User Guide.

## 핵심 요약

요약 미지원
