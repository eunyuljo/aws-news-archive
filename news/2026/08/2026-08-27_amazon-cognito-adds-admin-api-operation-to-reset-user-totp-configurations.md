---
title: "Amazon Cognito adds admin API operation to reset user TOTP configurations"
date: "2026-08-27"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cognito-totp-reset/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# Amazon Cognito adds admin API operation to reset user TOTP configurations

**날짜:** 2026년 08월 27일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cognito-totp-reset/

## 내용

Amazon Cognito now provides a new admin API operation to reset a user's time-based one-time Password (TOTP) multi-factor authentication (MFA) configuration. When users lose access to their TOTP device, administrators can remove the device association, allowing the user to enroll a new device on their next sign-in. 
This removes the need to recreate accounts to recover locked-out users if they lose access to their TOTP device. Customers can maintain MFA enforcement while providing a recovery path. 
This new capability is available in all AWS Regions where Amazon Cognito is available. To get started, access the AdminDeleteSoftwareToken API using the AWS CLI, SDKs, or APIs. See the developer guide for instructions.

## 핵심 요약

요약 미지원
