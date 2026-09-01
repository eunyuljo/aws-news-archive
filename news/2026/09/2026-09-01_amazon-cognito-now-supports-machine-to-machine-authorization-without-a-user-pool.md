---
title: "Amazon Cognito now supports machine-to-machine authorization without a user pool domain"
date: "2026-09-01"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cognito-get-client-token/"
tags: ["VPC", "2026", "new-region"]
nav_exclude: true
---

# Amazon Cognito now supports machine-to-machine authorization without a user pool domain

**날짜:** 2026년 09월 01일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cognito-get-client-token/

## 내용

Amazon Cognito now supports the GetClientToken API operation, enabling app clients to obtain access tokens for machine-to-machine (M2M) authorization directly through the AWS SDK, CLI, or API — without configuring a user pool domain. This gives you an additional path to authorize service-to-service communication for applications, microservices, and automated workloads. 
The new GetClientToken API operation lets your app client authenticate with its client ID and secret to receive an access token authorized for custom scopes on your resource servers. As a native AWS API operation, GetClientToken integrates seamlessly with AWS SDKs and supports AWS WAF and VPC interface endpoints (AWS PrivateLink). The existing domain-based OAuth 2.0 client-credentials flow remains available. 
This feature is available in all AWS Regions where Amazon Cognito user pools are available. To get started, configure an app client and call GetClientToken using the AWS Management Console, CLI, or SDKs. Standard Amazon Cognito M2M pricing applies. See Amazon Cognito Developer Guide and GetClientToken API Reference for details.

## 핵심 요약

요약 미지원
