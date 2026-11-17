---
title: "AWS Backup adds logically air-gapped vault support for Amazon RDS"
date: "2026-11-17"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-air-gapped-vault-rds/"
tags: ["RDS", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Backup adds logically air-gapped vault support for Amazon RDS

**날짜:** 2026년 11월 17일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-air-gapped-vault-rds/

## 내용

AWS Backup logically air-gapped vault now supports Amazon Relational Database Service (Amazon RDS) DB instances. Logically air-gapped vaults are a type of AWS Backup vault that stores immutable, isolated backups, which are locked by default with AWS Backup Vault Lock in compliance mode. Secure sharing across accounts and AWS Organizations enables direct restore, reducing recovery time from a data loss event. 
You can now protect your Amazon RDS DB instances in logically air-gapped vaults. A logically air-gapped vault stores immutable backups that are locked by default, and isolated with encryption using AWS owned keys or customer-managed keys. This helps reduce the risk of downtime, ensure business continuity, and meet compliance requirements. 
To get started, use the AWS Backup console, AWS Command Line Interface (CLI), or AWS SDKs. Assign your RDS DB instances to a backup plan and specify a logically air-gapped vault in the same AWS Region as the copy destination. Share the vault for recovery or restore testing with other accounts using AWS Resource Access Manager (RAM), or safeguard vault access during account compromise using Multi-party approval. Once shared, you can initiate direct restore jobs from that account. 
This support is available in most AWS Regions where both logically air-gapped vault and Amazon RDS are available. For more information and detailed regional availability, visit the AWS Backup documentation. To learn more about logically air-gapped vaults for RDS, read the launch blog and visit the feature documentation and pricing page.

## 핵심 요약

요약 미지원
