---
title: "AWS Secrets Manager now publishes secret update notifications to Amazon EventBridge"
date: "2026-07-23"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/secrets-manager-update-notifications"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS Secrets Manager now publishes secret update notifications to Amazon EventBridge

**날짜:** 2026년 07월 23일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/secrets-manager-update-notifications

## 내용

AWS Secrets Manager now automatically publishes events to Amazon EventBridge whenever your secret values change, enabling you to build event-driven workflows that respond in real time to secret updates.  Until now, you had to rely on AWS CloudTrail events parsed into EventBridge to know when a secret value changed — requiring you to match multiple API events such as rotation success, PutSecretValue, and UpdateSecretValue. With this launch, Secrets Manager publishes events directly into EventBridge whenever your secret value changes. You can use EventBridge rules to detect when the active secret value changes — such as during rotation — and route notifications to targets like AWS Lambda, Amazon SNS, Amazon SQS, or Amazon Step Functions. This enables you to proactively refresh cached credentials in your applications, restart dependent services, or update compliance reports for secret rotation.  Secret update notifications are published to your default event bus automatically with no additional configuration or opt-in required. This feature is available in all AWS Regions where AWS Secrets Manager is available at no additional cost. To get started, see secret event notifications&nbsp;in the AWS Secrets Manager User Guide.

## 핵심 요약

요약 미지원
