---
title: "AWS IAM now provides role manager to set up IAM roles automatically"
date: "2026-08-13"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iam-role-manager"
tags: ["Lambda", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS IAM now provides role manager to set up IAM roles automatically

**날짜:** 2026년 08월 13일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iam-role-manager

## 내용

Today, AWS announces the general availability of role manager, a capability in AWS Identity and Access Management (IAM) that automatically sets up the IAM roles your AWS services need. When you set up a supported service in the console, role manager creates a default role on your behalf, or reuses one that already exists in your account if it already matches the required permissions. You can enable or disable role manager at any time, as well as inspect the AWS-managed templates that role manager deploys on your behalf. 
Role manager supports 6 AWS service consoles at launch, including AWS Lambda and Amazon EventBridge. For example, when you create an AWS Lambda function, role manager applies the AWS-managed template for that workflow. Roles created via role manager appear in the IAM console as standard IAM roles that you fully control, and you can identify the ones role manager created. When you are ready to tighten permissions, you can disable role manager and use IAM Access Analyzer to refine each role to only the permissions it needs. 
Role manager is available in all AWS Regions, except the AWS GovCloud (US) Regions and the China Regions. 
To learn more, see How AWS IAM role manager rethinks the starting point for IAM roles on the AWS Security Blog, or Create roles automatically with role manager in the IAM User Guide.

## 핵심 요약

요약 미지원
