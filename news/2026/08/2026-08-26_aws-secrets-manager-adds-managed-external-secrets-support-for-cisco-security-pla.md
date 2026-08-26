---
title: "AWS Secrets Manager adds managed external secrets support for Cisco Security Platform and Netskope"
date: "2026-08-26"
service: "SecretsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/secrets-manager-cisco-netskope/"
tags: ["SecretsManager", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Secrets Manager adds managed external secrets support for Cisco Security Platform and Netskope

**날짜:** 2026년 08월 26일
**서비스:** SecretsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/secrets-manager-cisco-netskope/

## 내용

AWS Secrets Manager now extends its managed external secrets capability to include Cisco Security Platform API keys and Netskope API tokens, enabling you to automatically rotate these third-party credentials directly from the AWS console without writing any custom rotation code. 
For Cisco Security Platform (Security Cloud Control), Secrets Manager rotates the API key's refresh token on your schedule, keeping the credential active and capturing the new refresh token Cisco periodically reissues. Following Cisco's standard OAuth pattern, your applications exchange the stored refresh token for short-lived access tokens on demand. For Netskope, Secrets Manager rotates RBACv3 service-account REST API tokens through Netskope's SCIM API and validates the newly generated token before completing rotation. Both integrations are self-authenticating — the stored credential authorizes its own rotation — so no separate administrator credential is required. 
These integrations join existing managed external secrets support for BigID, Confluent Cloud, Datadog, GitLab, Jenkins, MongoDB Atlas, Okta, Paddle, Salesforce, Snowflake, and SonarQube. 
Cisco Security Platform and Netskope managed external secrets are available in all AWS Regions where AWS Secrets Manager managed external secrets is supported. To learn more, visit the &nbsp;AWS Secrets Manager managed external secrets documentation&nbsp;.

## 핵심 요약

요약 미지원
