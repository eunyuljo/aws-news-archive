---
title: "AWS Backup now supports incremental backups for Amazon DynamoDB"
date: "2026-11-21"
service: "DynamoDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-incremental-backups-dynamodb/"
tags: ["DynamoDB", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Backup now supports incremental backups for Amazon DynamoDB

**날짜:** 2026년 11월 21일
**서비스:** DynamoDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-incremental-backups-dynamodb/

## 내용

AWS Backup now supports incremental backups of Amazon DynamoDB tables, enabling you to reduce backup storage while maintaining backup schedules as frequent as one hour. 
Until now, AWS Backup created a full copy of your DynamoDB tables. With this launch, after an initial full backup, each incremental backup now captures only the data that changed, and AWS Backup takes a new full backup every 15 days. This lets you store less data and back up more often. You can restore from any recovery point in the chain, and you can schedule incremental backups anywhere from hourly to weekly frequencies. You can store incremental backups in both AWS Backup vaults and logically air-gapped vaults. Cross-Region backup copies are also incremental, further increasing your savings. 
AWS Backup turns on incremental backups automatically for new customers who protect DynamoDB. If you already back up DynamoDB with AWS Backup, you can turn on incremental backups under advanced features in AWS Backup settings, which lets you manage your backup preferences at the account and region level. You can create and manage incremental backups from the AWS Backup console, the AWS CLI, or the API. 
Incremental backups for DynamoDB are available in all AWS Regions where AWS Backup protects DynamoDB. To learn more, see working with supported services in the AWS Backup Developer Guide, read the launch blog, and visit the AWS Backup product page. To get started, open the AWS Backup console.

## 핵심 요약

요약 미지원
