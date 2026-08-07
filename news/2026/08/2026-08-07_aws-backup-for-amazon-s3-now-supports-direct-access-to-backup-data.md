---
title: "AWS Backup for Amazon S3 now supports direct access to backup data"
date: "2026-08-07"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-backup-amazon-s3-direct-access/"
tags: ["S3", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Backup for Amazon S3 now supports direct access to backup data

**날짜:** 2026년 08월 07일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-backup-amazon-s3-direct-access/

## 내용

AWS Backup for Amazon S3 now supports creating S3 Access Points, providing immediate read-only access to backup data using standard S3 APIs without initiating a restore. This enables targeted file recovery, data validation, compliance auditing, and forensic investigation while your backup data remains protected in your backup vault. 
You can create an access point for an S3 recovery point and read backup data using standard S3 operations such as GetObject, HeadObject, and ListObjectsV2. Access points work with both snapshot and continuous (point-in-time) recovery points stored in standard backup vaults or logically air-gapped vaults, including recovery points shared across accounts through AWS Resource Access Manager or Multi-party approval. While an access point is active, the associated recovery point is protected from deletion. 
Get started with this capability by creating access points for your S3 recovery points using the AWS Backup console, API, or CLI. This capability is available in select AWS Regions. 
To learn more, see Access points and Amazon S3 backups in the AWS Backup Developer Guide and read the launch blog. For pricing information, see AWS Backup pricing.

## 핵심 요약

요약 미지원
