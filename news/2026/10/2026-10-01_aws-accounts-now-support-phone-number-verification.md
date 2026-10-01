---
title: "AWS accounts now support phone number verification"
date: "2026-10-01"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-accounts-phone-number-verification/"
tags: ["General", "2026", "new-region"]
nav_exclude: true
---

# AWS accounts now support phone number verification

**날짜:** 2026년 10월 01일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-accounts-phone-number-verification/

## 내용

AWS Accounts now support phone number verification for primary contact phone numbers. Previously, phone numbers in AWS account contact information were validated for format but never verified through an out-of-band mechanism. Now, customers can verify their phone numbers via SMS one-time passcode (OTP).
To verify a phone number, customers initiate verification through the AWS Management Console or programmatically via the new SendPhoneNumberVerification API, which sends a 6-digit OTP. After entering the code, the VerifyPhoneNumber API validates and persists the verified status. When a phone number is changed through the PutContactInformation API, customers will be prompted to complete verification again. The GetContactInformation API now exposes verification status, enabling customers to confirm which phone numbers have been verified.
For AWS Organizations customers, phone number verification supports inheritance from the management account. When a verified phone number is applied to member accounts from the management account, those member accounts inherit the verified status if the number matches the management account, eliminating the need to verify the same number across thousands of accounts. Member accounts that independently change their own phone numbers will need to complete verification separately.
This feature is available in all AWS commercial regions. To learn more about phone number verification, visit the AWS Account Management documentation.

## 핵심 요약

요약 미지원
