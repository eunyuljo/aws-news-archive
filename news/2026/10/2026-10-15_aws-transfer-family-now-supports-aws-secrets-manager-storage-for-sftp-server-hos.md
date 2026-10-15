---
title: "AWS Transfer Family now supports AWS Secrets Manager storage for SFTP server host keys"
date: "2026-10-15"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-secrets-host-keys/"
tags: ["IAM", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Transfer Family now supports AWS Secrets Manager storage for SFTP server host keys

**날짜:** 2026년 10월 15일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-secrets-host-keys/

## 내용

AWS Transfer Family now lets you store SFTP server host keys in AWS Secrets Manager in your own AWS account. This gives you greater control over your server identity and helps simplify server migrations and failover.
Previously, Transfer Family stored host keys within the service, so you could not retrieve the associated private key material. With this launch, you can choose Secrets Manager as the storage type when creating a server or importing a host key. You can then retrieve the private key material and reuse the same host key across servers and AWS Regions. For example, you can use it on a standby server for failover or on a replacement server during migration, without requiring clients to trust a new host key. AWS Identity and Access Management (IAM) policies let you control who can retrieve the stored keys. You can also migrate existing host keys to Secrets Manager, which may require additional steps; see the AWS Transfer Family User Guide for details.
This capability is available in all AWS Regions where AWS Transfer Family is available. To learn more, see Store SFTP server host keys in AWS Secrets Manager in the AWS Transfer Family User Guide. To get started, go to the AWS Transfer Family console.

## 핵심 요약

요약 미지원
