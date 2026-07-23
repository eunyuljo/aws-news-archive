---
title: "AWS Lambda durable functions now supports customer managed key encryption"
date: "2026-07-23"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/durablefunctions-cmk/"
tags: ["Lambda", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Lambda durable functions now supports customer managed key encryption

**날짜:** 2026년 07월 23일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/durablefunctions-cmk/

## 내용

AWS Lambda durable functions now supports encryption of durable execution data with an AWS Key Management Service (AWS KMS) customer managed key. Lambda durable functions&nbsp;lets you build long-running, reliable workflows directly in your Lambda function code with automatic state management. Lambda encrypts execution state at rest by default with an AWS owned key.&nbsp;Now with support for AWS KMS, you can choose and manage the encryption key yourself. 
If you operate in regulated industries such as financial services or healthcare, your data governance policies may require customer-owned encryption keys. You can now configure a customer managed key for durable execution data, giving you control over key rotation and who can access execution history and state. The durable execution key operates independently of the function-level key that protects environment variables and SnapStart snapshots, so you can manage access to execution data separately from function configuration. 
This feature is available in all AWS Regions where Lambda durable functions is available. Standard AWS KMS charges apply for customer managed keys. There are no additional Lambda charges for this feature. 
To learn more, see Encrypting Lambda durable execution data in the AWS Lambda Developer Guide.&nbsp;

## 핵심 요약

요약 미지원
