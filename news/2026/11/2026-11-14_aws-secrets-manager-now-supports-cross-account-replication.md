---
title: "AWS Secrets Manager now supports cross-account replication"
date: "2026-11-14"
service: "SecretsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-manager-cross-account/"
tags: ["SecretsManager", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Secrets Manager now supports cross-account replication

**날짜:** 2026년 11월 14일
**서비스:** SecretsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-manager-cross-account/

## 내용

AWS Secrets Manager now supports cross-account replication, enabling you to maintain a synchronized copy of a primary secret in a secondary AWS account for cross-account access, backup, and disaster recovery. Cross-account replication extends the existing multi-Region replication capability across account boundaries. 
With cross-account replication, platform or security teams can own and rotate a secret centrally, and each consuming account gets a local, always-current copy without any shared KMS keys or cross-account secret policies. The replica secret is a full, independent resource, encrypted with a customer managed KMS key owned by the replica account. Secrets Manager updates it automatically whenever the primary secret's value changes, including rotations. 
You can keep a live copy of critical secrets in a dedicated recovery or failover account, isolated from ransomware or a compromised primary account. If needed, the replica can be promoted to a standalone secret. 
Cross-account replication is available in all AWS Regions where Secrets Manager is available. For a list of regions where Secrets Manager is available, see the AWS Region table. 
To learn more, see Replicate secrets across AWS accounts in the Secrets Manager User Guide and the AssociateCrossAccountReplica API reference. For pricing details, see AWS Secrets Manager pricing.

## 핵심 요약

요약 미지원
