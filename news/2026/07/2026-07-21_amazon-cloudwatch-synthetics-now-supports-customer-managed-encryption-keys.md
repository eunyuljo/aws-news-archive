---
title: "Amazon CloudWatch Synthetics now supports customer managed encryption keys"
date: "2026-07-21"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/synthetics-customer-managed-keys/"
tags: ["CloudWatch", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon CloudWatch Synthetics now supports customer managed encryption keys

**날짜:** 2026년 07월 21일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/synthetics-customer-managed-keys/

## 내용

Amazon CloudWatch Synthetics now supports customer managed AWS Key Management Service (KMS) keys for encrypting canary environment variables, giving you full control over the encryption of sensitive configuration data such as API keys, credentials, and tokens. Previously, environment variables were encrypted at rest using only an AWS owned key. Now, in addition to the default AWS owned key, you can specify your own symmetric KMS key for encryption at rest, and you can also encrypt individual values client-side before they are stored. 
With encryption at rest, you specify a customer managed KMS key when creating or updating a canary, and CloudWatch Synthetics uses a grant on the key to handle encryption and decryption transparently. With client-side encryption, you encrypt values before storage, and your canary script decrypts them at runtime using the AWS KMS Decrypt API. This benefits teams in regulated industries that require organizational key management policies, auditability, or key rotation controls across all services. 
Amazon CloudWatch Synthetics customer managed key encryption is available in all commercial AWS Regions. Multi-location canaries can use a different KMS key per replica Region. 
To learn more, see Encrypting environment variables in the Amazon CloudWatch User Guide.

## 핵심 요약

요약 미지원
