---
title: "Amazon EBS now supports associating additional KMS keys with snapshots"
date: "2026-11-17"
service: "KMS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/ebs-snapshots-associate-kms-keys/"
tags: ["KMS", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon EBS now supports associating additional KMS keys with snapshots

**날짜:** 2026년 11월 17일
**서비스:** KMS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/ebs-snapshots-associate-kms-keys/

## 내용

Amazon Elastic Block Store (EBS) now supports associating additional AWS Key Management Service (KMS) keys with EBS snapshots. This new capability enables you to share and copy encrypted snapshots across accounts without first re-encrypting them, simplifying your disaster recovery and backup workflows. 
 

 Customers use EBS snapshots as durable, point-in-time backups of EBS volumes. By associating an additional customer-managed KMS key (CMK) with a snapshot encrypted with an AWS managed key (AMK), for example, you enable cross-account sharing for that snapshot without re-encrypting its data. This feature accelerates your disaster recovery workflows and enhances operational efficiency for enterprise backup administrators and disaster recovery teams. 
 

 Support for associating additional KMS keys with Amazon EBS snapshots is available in all AWS commercial, China, AWS GovCloud (US), and AWS European Sovereign Cloud (Germany) Regions, plus AWS Local Zones and AWS Outposts. You can access this capability through the AWS Console, AWS Command Line Interface (CLI), and AWS SDKs. To learn more, see the Amazon EBS documentation.

## 핵심 요약

요약 미지원
