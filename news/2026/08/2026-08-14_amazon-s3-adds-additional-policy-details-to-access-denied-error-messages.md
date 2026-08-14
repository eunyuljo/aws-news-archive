---
title: "Amazon S3 adds additional policy details to access denied error messages"
date: "2026-08-14"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/s3-additional-policy-details-access-denied-error-messages/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon S3 adds additional policy details to access denied error messages

**날짜:** 2026년 08월 14일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/s3-additional-policy-details-access-denied-error-messages/

## 내용

Amazon S3 now includes the specific AWS Identity and Access Management (IAM) and AWS Organizations policy Amazon Resource Name (ARN) in HTTP 403 Access Denied error messages for same-account and same-organization requests. This helps you quickly identify the exact policy responsible for a denied request and remediate the issue directly. 
Previously, S3 access denied error messages included the policy type and reason for denial, but when multiple policies of the same type existed, you still had to manually inspect each one to pinpoint the root cause. Now the error message includes the specific policy ARN for explicit deny cases, covering Service Control Policies (SCPs), Resource Control Policies (RCPs), identity-based policies, session policies, and permission boundaries. 
This capability is available in all AWS Regions, including the AWS GovCloud (US) Regions and the AWS China Regions. To learn more about how to troubleshoot access denied errors in Amazon S3, visit the S3 User Guide and the IAM troubleshooting documentation.

## 핵심 요약

요약 미지원
