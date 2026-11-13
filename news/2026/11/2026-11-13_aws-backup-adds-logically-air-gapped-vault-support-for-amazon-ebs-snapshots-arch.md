---
title: "AWS Backup adds logically air-gapped vault support for Amazon EBS Snapshots Archive"
date: "2026-11-13"
service: "EBS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-lag-vault-ebs-archive/"
tags: ["EBS", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS Backup adds logically air-gapped vault support for Amazon EBS Snapshots Archive

**날짜:** 2026년 11월 13일
**서비스:** EBS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-lag-vault-ebs-archive/

## 내용

AWS Backup logically air-gapped vault now supports Amazon EBS Snapshots Archive. Logically air-gapped vaults are a type of AWS Backup vault that allows secure sharing of backups across accounts and AWS Organizations, supporting direct restore to reduce recovery time from a data loss event. 
You can now archive Amazon EBS backups held in a logically air-gapped vault to Amazon EBS Snapshots Archive, a low-cost tier for snapshots you rarely access. A logically air-gapped vault stores immutable backups that are locked by default, and isolated with encryption using AWS owned keys or customer-managed keys. This helps you meet long-term retention and compliance requirements at lower storage cost. 
You can get started using the AWS Backup console, AWS Command Line Interface (CLI), or AWS SDKs. In a backup plan rule that runs monthly or less often, specify a logically air-gapped vault as the primary backup destination or copy destination. Then enable Archive Amazon EBS snapshots in the backup rule lifecycle or copy lifecycle and set the time in warm storage before the backup transitions. 
This support is available in all AWS Regions where both logically air-gapped vault and Amazon EBS Snapshots Archive are available. For more information and detailed regional availability, visit the AWS Backup documentation. To learn more about logically air-gapped vaults, visit the product documentation and pricing page.

## 핵심 요약

요약 미지원
