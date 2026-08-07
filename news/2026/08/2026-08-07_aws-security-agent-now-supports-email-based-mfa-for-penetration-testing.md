---
title: "AWS Security Agent now supports email-based MFA for penetration testing"
date: "2026-08-07"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-security-agent-mfa/"
tags: ["General", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Security Agent now supports email-based MFA for penetration testing

**날짜:** 2026년 08월 07일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-security-agent-mfa/

## 내용

AWS Security Agent (now part of AWS Continuum) now enables penetration testing of applications that use email-based multi-factor authentication (MFA) as part of their login flow. Previously, applications requiring one-time codes or verification links sent by email were out of scope for automated pentesting because the agent had no mechanism to intercept those messages. This launch expands coverage for penetration testing customers whose target applications rely on email-based authentication. 
To use this feature, AWS Security Agent generates a unique forwarding address per credential, allowing you to route your application's MFA emails directly to the agent using a forwarding rule in your existing email provider. During a pentest, the agent automatically reads the forwarded message and submits the code or link to complete authentication — no email account credentials are stored, preserving a strong privacy posture. This capability complements existing TOTP support, giving customers a unified solution for testing applications across multiple MFA methods. 
This feature is available in all AWS Regions where AWS Security Agent is supported. 
To learn more, visit the AWS Security Agent product page and the AWS Security Agent User Guide.&nbsp;

## 핵심 요약

요약 미지원
