---
title: "AWS Backup adds restore testing support for Amazon Redshift"
date: "2026-10-29"
service: "Redshift"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-backup-adds-redshift-restore-testing/"
tags: ["Redshift", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Backup adds restore testing support for Amazon Redshift

**날짜:** 2026년 10월 29일
**서비스:** Redshift
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-backup-adds-redshift-restore-testing/

## 내용

AWS Backup restore testing now supports Amazon Redshift. Restore testing helps you automate and periodically run restore tests of your backups, so you can confirm that your Amazon Redshift backups restore successfully and measure how long the restores take. 
You can now include Amazon Redshift in your restore testing plans alongside other supported AWS resources across storage, compute, and database services. Restore testing plans automatically select recovery points, run restores on a schedule, and measure restore job completion time against your recovery time objectives (RTO). This helps you evaluate recovery readiness and meet regulatory and compliance requirements for disaster recovery and business continuity. 
To get started, create a restore testing plan and assign your Amazon Redshift resources by Amazon Resource Name (ARN) or tag. Choose whether each test restores the latest or a random eligible recovery point. Optionally, use restore testing validation to confirm the restored resource before AWS Backup deletes the test resources. 
This support is available in all AWS Regions where both restore testing and Amazon Redshift are supported by AWS Backup. You can use the AWS Backup console, AWS Command Line Interface (CLI), or AWS SDKs. For a complete list of supported Regions and features, visit the AWS Backup documentation. To learn more about restore testing, visit the product page and pricing page.

## 핵심 요약

요약 미지원
