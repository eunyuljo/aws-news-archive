---
title: "AWS IAM Identity Center makes management of AWS account access optional for new organization instances"
date: "2026-08-06"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-identity-center-accounts-optional/"
tags: ["IAM", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center makes management of AWS account access optional for new organization instances

**날짜:** 2026년 08월 06일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-identity-center-accounts-optional/

## 내용

AWS IAM Identity Center now lets you decide whether to enable management of AWS account access when you create a new organization instance. This allows you to use IAM Identity Center to manage access to AWS applications only, without the need to manage access to AWS accounts. This feature is available at the time of initial configuration of an IAM Identity Center instance and does not affect existing IAM Identity Center instances. 
IAM Identity Center enables you to connect your workforce identities to AWS once and offer AWS application owners across your organization streamlined access management. Application end users benefit from single sign-on, user awareness, and consistent authentication experience across AWS applications. Previously, this meant you also needed to manage access to AWS accounts. With this release, account management is now optional. When you choose not to enable management of AWS accounts, IAM Identity Center does not provision its service-linked role into your member accounts, which reduces the access surface in your environment. You can enable account management permissions later through instance settings or the UpdateInstance API.&nbsp; 
This capability is available in all AWS Regions where IAM Identity Center is available. To get started, see Configure instance settings in the IAM Identity Center User Guide.

## 핵심 요약

요약 미지원
