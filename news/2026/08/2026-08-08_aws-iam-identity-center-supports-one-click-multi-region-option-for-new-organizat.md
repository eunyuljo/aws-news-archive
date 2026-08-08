---
title: "AWS IAM Identity Center supports one-click multi-Region option for new organization instances"
date: "2026-08-08"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iam-identity-center-supports-one-click-multi-region-option-new-organization-instances"
tags: ["IAM", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center supports one-click multi-Region option for new organization instances

**날짜:** 2026년 08월 08일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iam-identity-center-supports-one-click-multi-region-option-new-organization-instances

## 내용

AWS IAM Identity Center now makes it easier to enable multi-Region support when creating a new organization instance. Previously, enabling multi-Region support required multiple steps including creating a customer managed KMS key, configuring key policies, and manually adding Regions. Now, customers creating a new IAM Identity Center instance in supported Regions can enable multi-Region in one click. 
When enabling a new organization instance, you can choose from three instance configuration options: single-Region instance, multi-Region instance, or custom instance. The multi-Region instance option automatically creates a customer managed multi-Region KMS key in your account and replicates your instance to an additional Region. This enables resilient AWS account and application access — your workforce can continue to access their AWS accounts even if IAM Identity Center experiences a disruption in the primary Region. The custom instance option lets you configure your Region settings individually, including the ability to use an existing customer managed KMS key from your account. 
Instance configuration options are available in 17 enabled-by-default commercial AWS Regions for organization instances of IAM Identity Center. Standard AWS KMS charges apply for the customer managed key created with the multi-Region instance option. IAM Identity Center is provided at no additional cost. 
To get started, see the IAM Identity Center User Guide. To learn more about multi-Region support, see Using IAM Identity Center across multiple AWS Regions. To learn more about IAM Identity Center, visit the product detail page.

## 핵심 요약

요약 미지원
