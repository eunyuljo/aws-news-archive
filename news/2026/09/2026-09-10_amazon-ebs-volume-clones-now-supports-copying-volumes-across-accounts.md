---
title: "Amazon EBS Volume Clones now supports copying volumes across accounts"
date: "2026-09-10"
service: "KMS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/ebs-volume-clones-cross-account-copy/"
tags: ["KMS", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon EBS Volume Clones now supports copying volumes across accounts

**날짜:** 2026년 09월 10일
**서비스:** KMS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/ebs-volume-clones-cross-account-copy/

## 내용

Amazon Elastic Block Store (Amazon EBS) Volume Clones now supports copying EBS volumes across AWS accounts with re-encryption. You can copy EBS volumes to any AWS account, re-encrypting with an AWS Key Management Service (AWS KMS) key in the target account. This enables organizations that separate production and development workloads into different accounts to copy data across those account boundaries. 
With cross-account copy, you can clone a production database volume into an isolated development account, giving developers a fresh copy of production data to experiment with safely. This capability also supports teams that require encryption key separation across environments, such as maintaining separate KMS keys for production and non-production accounts. Cross-account copy is supported for all volume types, including unencrypted volumes and volumes encrypted with customer managed keys. 
To copy a volume across accounts, you first share the volume with the target account using AWS Resource Access Manager (AWS RAM), and then the target account creates a copy of the shared volume in the same Availability Zone. You can access this capability using the AWS Management Console, AWS Command Line Interface (CLI), and AWS SDKs. It is available in all AWS Regions that support Amazon EBS Volume Clones, including all Commercial Regions, the AWS GovCloud (US) Regions, AWS China Regions, and supported Local Zones. 
To learn more, visit the Amazon EBS Volume Clones documentation.

## 핵심 요약

요약 미지원
