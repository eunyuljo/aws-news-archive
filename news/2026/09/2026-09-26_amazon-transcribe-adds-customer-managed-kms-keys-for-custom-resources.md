---
title: "Amazon Transcribe adds customer-managed KMS keys for custom resources"
date: "2026-09-26"
service: "KMS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-transcribe/"
tags: ["KMS", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Transcribe adds customer-managed KMS keys for custom resources

**날짜:** 2026년 09월 26일
**서비스:** KMS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-transcribe/

## 내용

Amazon Transcribe now lets you encrypt your custom vocabularies, custom vocabulary filters, and custom language models at rest with a customer-managed AWS KMS key that you own and control.
Previously, these custom resources were always encrypted with an AWS owned key. Now you can supply your own symmetric AWS KMS key when you create or update these resources, so the artifacts Transcribe stores on your behalf are encrypted under a key in your account. If you do not provide a key, your resources continue to be encrypted with an AWS owned key—no action is required unless you opt in.
With a customer-managed key, you control key permissions and decide exactly which principals and services can encrypt and decrypt your custom resources. Every use of your key is logged in AWS CloudTrail, giving you a full audit trail for compliance and monitoring. You can also disable the key or transition resources to a different key to revoke access on your own schedule.
This feature is available in all AWS Regions where Amazon Transcribe is offered. To learn more, see Amazon Transcribe Developer Guide.

## 핵심 요약

요약 미지원
