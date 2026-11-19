---
title: "Amazon Cognito now supports authentication level and method token claims"
date: "2026-11-19"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cognito-acr-amr-token/"
tags: ["Config", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Cognito now supports authentication level and method token claims

**날짜:** 2026년 11월 19일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cognito-acr-amr-token/

## 내용

Amazon Cognito now supports authentication context class reference (ACR) and authentication methods reference (AMR), by adding ACR and AMR claims to access, ID, and refresh tokens. Your application can use the authentication level (ACR) to make authorization decisions, such as requiring additional factors for sensitive operations. It can also use completed methods (AMR), such as time-based one-time password (TOTP), for auditing and compliance. 
Amazon Cognito defines four authentication levels based on the factors a user completes, from password-only (level 1) to a password with a TOTP (level 4). Each token reflects the level achieved during sign-in, so your application can make authorization decisions based on how a user authenticated. If your application requires a stronger level, you can request a target level in your application's sign-in flow or through managed login, and Amazon Cognito issues new tokens once the user completes the required factors. You can also customize ACR level URIs for your user pool. For federated users from an OpenID Connect (OIDC) provider, Amazon Cognito maps the provider's ACR and AMR values to your levels. 
ACR and AMR token claims are available in all AWS Regions where Amazon Cognito is offered. Every user pool includes ACR and AMR token claims, regardless of feature plan. Requesting a target authentication level and configuring custom ACR level URIs are available with the Essentials or Plus feature plan. To get started, configure ACR and AMR using the AWS Management Console, AWS CLI, or AWS SDKs. See developer guide for details.

## 핵심 요약

요약 미지원
