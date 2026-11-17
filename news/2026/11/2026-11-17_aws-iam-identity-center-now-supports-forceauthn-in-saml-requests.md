---
title: "AWS IAM Identity Center now supports ForceAuthn in SAML requests"
date: "2026-11-17"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/iam-identity-center-reauth/"
tags: ["IAM", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center now supports ForceAuthn in SAML requests

**날짜:** 2026년 11월 17일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/iam-identity-center-reauth/

## 내용

AWS IAM Identity Center now gives you the option to require workforce users to re-authenticate with your external identity provider (IdP) each time their user interactive session expires. By default, when a user's session expires, IAM Identity Center renews it through the user's existing IdP session, and the user isn't prompted to sign in again. For organizations with strict security or compliance requirements that mandate explicit user verification at regular intervals, this automatic renewal may not meet policy requirements. 
When you set user re-authentication to Required and a user's user interactive session expires, IAM Identity Center prompts the user to re-authenticate with your external IdP. This helps you enforce stronger sign-in controls for regulated workloads. IAM Identity Center implements this by adding the SAML 2.0 ForceAuthn attribute to the SAML request sent to your IdP. 
You can configure user re-authentication for any IAM Identity Center instance (organization or account) that's connected to an external IdP as its identity source. The setting applies only to service provider initiated sign-ins, where users sign in through your AWS access portal URL. Changes to the user re-authentication setting are logged in AWS CloudTrail, so you can audit when it was turned on or off. 
User re-authentication is available in all AWS Regions where IAM Identity Center is available at no additional cost. To learn more, see Require user re-authentication in the AWS IAM Identity Center User Guide.

## 핵심 요약

요약 미지원
