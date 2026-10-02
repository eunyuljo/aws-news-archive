---
title: "AWS IAM Identity Center extends multi-Region support to more AWS Regions"
date: "2026-10-02"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-iam-identity-center-extends-multi-region-support-to-more-aws-regions"
tags: ["IAM", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center extends multi-Region support to more AWS Regions

**날짜:** 2026년 10월 02일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-iam-identity-center-extends-multi-region-support-to-more-aws-regions

## 내용

IAM Identity Center helps you connect your workforce identities to AWS once and streamline access management to AWS accounts and applications. You can now replicate IAM Identity Center to opt-in AWS Regions, and between Regions within the AWS GovCloud (US) and AWS China Regions. Previously, multi-Region support was available in the enabled-by-default commercial AWS Regions. This helps you improve the resilience of user access to AWS accounts and deploy AWS applications in the AWS Regions that best align with your business needs.
When you enable multi-Region support, IAM Identity Center automatically replicates your identities, entitlements, and other information from the primary Region to additional Regions. If IAM Identity Center is affected by a disruption in the primary Region, users continue to have access to their AWS accounts using already provisioned entitlements in the additional Regions. AWS application administrators can use the standard application deployment workflow to deploy their application in an additional Region while you continue to administer IAM Identity Center in the primary Region.
Multi-Region support is available for organization instances that use an external identity provider or the IAM Identity Center directory as the identity source, and requires a multi-Region customer managed KMS key (CMK). When you create a new instance, you can enable multi-Region support with a single click, which also creates the CMK. For existing instances, create a multi-Region CMK in AWS KMS, then configure it in IAM Identity Center. Standard&nbsp;AWS KMS charges apply for storing and using CMKs. IAM Identity Center is provided at no additional cost.
 
 
 For the full list of AWS Regions where multi-Region support is available, see AWS Capabilities by Region.&nbsp;To learn more about multi-Region support, see Using IAM Identity Center across multiple AWS Regions. To find out which AWS applications support deployment in additional Regions, visit AWS applications that you can use with IAM Identity Center.

## 핵심 요약

요약 미지원
