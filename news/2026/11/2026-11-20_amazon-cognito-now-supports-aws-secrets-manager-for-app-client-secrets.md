---
title: "Amazon Cognito now supports AWS Secrets Manager for app client secrets"
date: "2026-11-20"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-secrets-manager-integration/"
tags: ["IAM", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon Cognito now supports AWS Secrets Manager for app client secrets

**날짜:** 2026년 11월 20일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-secrets-manager-integration/

## 내용

Amazon Cognito now integrates with AWS Secrets Manager, so you can store and manage your user pool app client secrets in Secrets Manager. Amazon Cognito helps you implement secure sign-in and access control for users, AI agents, and microservices in minutes. An app client secret authenticates your application to Cognito. Previously, you had to manage and rotate these secrets in Cognito directly.
With this integration, you can leverage Secrets Manager for capabilities including rotation, access control with AWS Identity and Access Management (IAM) policies, and encryption with an AWS managed key or your own AWS Key Management Service (AWS KMS) customer managed key. This can help with periodic credential rotation or compliance requirements; this also helps with keeping secrets out of the console. You can enable this integration for either a new or an existing app client, and disable it at any time.
This integration is available in all AWS Regions where Amazon Cognito and AWS Secrets Manager are available, except AWS European Sovereign Cloud (Germany). Standard AWS Secrets Manager charges apply. To learn more, see the Amazon Cognito Developer Guide for instructions.

## 핵심 요약

요약 미지원
