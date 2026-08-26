---
title: "AWS Lambda functions now support full IAM resource-based policies"
date: "2026-08-26"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-lambda-full-iam-resource-based-policies/"
tags: ["Lambda", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Lambda functions now support full IAM resource-based policies

**날짜:** 2026년 08월 26일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-lambda-full-iam-resource-based-policies/

## 내용

AWS Lambda functions now support full Identity and Access Management (IAM) resource-based policies, enabling platform admins and security teams to define granular access permissions using the full capabilities of AWS IAM. With full IAM resource-based policies, you can define permissions for multiple principals and actions in a single policy document and leverage the full range of IAM condition keys.  Previously, Lambda functions&nbsp;required customers to add permissions individually per principal. This provided limited flexibility for&nbsp;platform admins and security teams&nbsp;who want to manage permissions at scale.&nbsp;Now, Lambda functions support full IAM resource-based policies, including the full range of IAM condition keys. This provides a broader range of policy capabilities and streamlines policy management for teams operating multi-account architectures or managing multiple resources. For example, you can now use IAM condition keys to restrict access based on source IP or principal tag, and platform teams can now allow multiple&nbsp;services to invoke a function by using a single policy, rather than maintaining multiple statements to add permissions.  You can update resource-based policies in one step using the JSON editor in the AWS Lambda console, AWS CLI, AWS SDK, or infrastructure as code tools such as AWS CloudFormation and AWS SAM. To learn more, explore the Lambda resource-based policy examples&nbsp;in the AWS Lambda Developer Guide.&nbsp;  Full IAM resource-based policies are available in all AWS commerical Regions at no additional charge.

## 핵심 요약

요약 미지원
