---
title: "AWS License Manager now supports AWS Managed Microsoft AD (Hybrid Edition)"
date: "2026-11-20"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/license-manager-hybrid-ad-support/"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS License Manager now supports AWS Managed Microsoft AD (Hybrid Edition)

**날짜:** 2026년 11월 20일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/license-manager-hybrid-ad-support/

## 내용

AWS License Manager now supports AWS Managed Microsoft AD (Hybrid Edition), so you can use your existing Microsoft Active Directory (AD) to manage user-based subscriptions for Microsoft Office, Visual Studio, and Remote Desktop Services Subscriber Access License (RDS SAL). Hybrid Edition, a feature of AWS Directory Service for Microsoft Active Directory, extends your existing directory into AWS. License Manager now works with that directory directly, so you no longer need to bear the cost of duplicating and maintaining the directory in AWS for licensing. 
Previously, onboarding Microsoft user-based subscriptions required a trust relationship between your directory and a second directory in AWS. If your security policies didn't allow that trust, you couldn't onboard without changing those policies. Now, license-included Microsoft Office and Visual Studio instances that you launch on Amazon Elastic Compute Cloud (Amazon EC2) join your existing directory and apply the same Group Policy settings, such as security baselines and audit policies, so you don't need to recreate them in a second directory. 
This feature is available in all AWS Regions where AWS License Manager user-based subscriptions and AWS Managed Microsoft AD (Hybrid Edition) are available. To learn more, see the AWS License Manager User Guide, or get started in the AWS License Manager console.

## 핵심 요약

요약 미지원
