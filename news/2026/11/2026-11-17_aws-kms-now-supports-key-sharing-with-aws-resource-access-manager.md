---
title: "AWS KMS now supports key sharing with AWS Resource Access Manager"
date: "2026-11-17"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/kms-key-sharing-resource-access-manager/"
tags: ["IAM", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# AWS KMS now supports key sharing with AWS Resource Access Manager

**날짜:** 2026년 11월 17일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/kms-key-sharing-resource-access-manager/

## 내용

AWS Key Management Service (KMS) now integrates with AWS Resource Access Manager (RAM), giving you a simpler and more consistent way to share KMS keys across your AWS accounts, within your organization in AWS Organizations, and with specific IAM roles and users. You can now let trusted parties define the access they need through reusable managed permissions in RAM, while keeping full control of your keys and key policies. To share a key, create a resource share by selecting the keys to share, choosing a managed permission, and specifying the principals. You can use AWS managed permissions for common scenarios, or customer managed permissions (CMPs) authored by you or by trusted parties such as SaaS providers and central security teams. 
Sharing KMS keys through RAM makes enabling cross-account access faster to set up and safer to maintain. The trusted parties who need access to your keys can publish the policy once as a CMP, without the need for you to modify the key policies by hand. You simply fill in the values that scope it to your environment and attach it to the resource share. Your existing key policy is untouched, so you are always in control of your key as your environment grows. When a new policy version is available via an updated CMP, you decide when to apply it to your resource shares. 
This enhancement is built on new AWS RAM capabilities that are available for every resource type RAM supports. CMPs now support multiple policy statements and additional IAM condition operators, including StringNotEquals, BoolIfExists, and ArnLike, along with the ForAnyValue and ForAllValues prefixes, so you can express precise, least-privilege access. The&nbsp;parameterized managed permissions lets you place a temporary placeholder in CMPs that allows each resource share owner to customize and scope down CMPs to their environment, enabling CMPs to be reused and serve many accounts. CMPs can now be published and shared across accounts, so the authors can maintain one permission, manage its versions centrally, and see every resource share that uses it, while other accounts can use it directly without keeping their own copy. 
KMS key sharing with RAM is available in all AWS Regions where both services are available, except the Middle East (UAE) and Middle East (Bahrain).&nbsp;For more information, see Sharing KMS keys with AWS RAM in the AWS KMS Developer Guide and Working with shared AWS resources in the AWS RAM Developer Guide.

## 핵심 요약

요약 미지원
