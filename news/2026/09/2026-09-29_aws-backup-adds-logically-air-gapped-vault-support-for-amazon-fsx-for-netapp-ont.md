---
title: "AWS Backup adds logically air-gapped vault support for Amazon FSx for NetApp ONTAP"
date: "2026-09-29"
service: "FSx"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-backup-air-gapped-vault-fsx-ontap/"
tags: ["FSx", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Backup adds logically air-gapped vault support for Amazon FSx for NetApp ONTAP

**날짜:** 2026년 09월 29일
**서비스:** FSx
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-backup-air-gapped-vault-fsx-ontap/

## 내용

AWS Backup logically air-gapped vault now supports Amazon FSx for NetApp ONTAP. Logically air-gapped vaults are a type of AWS Backup vault that allows secure sharing of backups across accounts and AWS Organizations, supporting direct restore to reduce recovery time from a data loss event.
You can now protect your Amazon FSx for NetApp ONTAP volumes in logically air-gapped vaults. A logically air-gapped vault stores immutable backups that are locked by default, and isolated with encryption using AWS owned keys or customer-managed keys. You can store your FSx for NetApp ONTAP backups in a logically air-gapped vault in the same account or across other accounts and Regions. This helps reduce the risk of downtime, ensure business continuity, and meet compliance and disaster recovery requirements.
You can get started using the AWS Backup console, AWS Command Line Interface (CLI), or AWS SDKs. Target FSx for NetApp ONTAP backups to a logically air-gapped vault by specifying it as the primary target or copy destination in your backup plan. Share the vault for recovery or restore testing with other accounts using AWS Resource Access Manager (RAM), or safeguard vault access during account compromise using Multi-party approval. Once available, you can initiate direct restore jobs from that account, eliminating the overhead of copying backups first.
This support is available in all AWS Regions where both logically air-gapped vault and Amazon FSx for NetApp ONTAP are available. For more information and detailed regional availability, visit the AWS Backup documentation. To learn more about logically air-gapped vaults, visit the feature documentation and pricing page.

## 핵심 요약

요약 미지원
