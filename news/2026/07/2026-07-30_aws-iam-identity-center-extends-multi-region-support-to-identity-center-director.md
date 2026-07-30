---
title: "AWS IAM Identity Center extends multi-Region support to Identity Center directory"
date: "2026-07-30"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-iam-identity-center-extends-multi-region-support-to-identity-center-directory"
tags: ["IAM", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center extends multi-Region support to Identity Center directory

**날짜:** 2026년 07월 30일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-iam-identity-center-extends-multi-region-support-to-identity-center-directory

## 내용

IAM Identity Center helps you configure the single sign-on experience of your workforce to AWS accounts and applications. You can now replicate IAM Identity Center from the primary AWS Region where you first enabled it to additional Regions of your choice when using Identity Center directory as your identity source. This extends the multi-Region support capability, previously available for Identity Center organization instances connected to external identity providers, to instances that use the Identity Center directory to manage and authenticate their workforce. This feature enhances resilience of user access to AWS accounts and helps you deploy AWS applications in the AWS Regions that best align with your business needs such as application data residency and proximity to users. 
When you enable this feature, IAM Identity Center automatically replicates your identities, entitlements, and other information from the primary Region to additional Regions. If IAM Identity Center is affected by a disruption in the primary Region, IAM Identity Center users continue to have access to their AWS accounts using the already provisioned entitlements in the additional Regions.&nbsp; 
AWS application administrators can use the standard application deployment workflow to deploy their application in an additional Region while you continue to administer IAM Identity Center in the primary Region. 
IAM Identity Center multi-Region support is currently available in the 17 enabled-by-default commercial AWS Regions for organization instances of IAM Identity Center. The IAM Identity Center organization instance must be configured with a multi-Region customer managed KMS key (CMK). To find out which AWS applications support deployment in additional Regions, visit AWS applications that you can use with IAM Identity Center. Standard AWS KMS charges apply for storing and using CMKs. IAM Identity Center is provided at no additional cost. To learn more about IAM Identity Center, visit the product detail page. To get started, see the IAM Identity Center User Guide.

## 핵심 요약

요약 미지원
