---
title: "Amazon RDS for Oracle now supports copying option groups during cross-Region snapshot copy"
date: "2026-11-05"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-oracle-cross-region-snapshot-copy-option-group/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon RDS for Oracle now supports copying option groups during cross-Region snapshot copy

**날짜:** 2026년 11월 05일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-oracle-cross-region-snapshot-copy-option-group/

## 내용

Amazon RDS for Oracle now lets you copy the option group associated with a DB snapshot when you copy that snapshot to another AWS Region. 
Amazon RDS for Oracle uses option groups to enable and configure features that make it simple to manage your databases. Option groups are specific to the AWS Region where you create them. Previously, customers wanting to replicate RDS backups that had option groups to a different AWS Region had to copy the snapshot without the option group and then recreate the option group in the target Region before restoring the snapshot. Now, you no longer need to separate the steps and can instead initiate the snapshot copy and specify the option group copy in the same request as the snapshot copy. 
The existing boolean parameter CopyOptionGroup on the CopyDBSnapshot API and CLI commands now also support cross-Region copy, along with cross-account copy. You can now copy options groups to the destination snapshot in the target AWS Region from the source snapshot by setting this parameter to true. 
This capability is available on Amazon RDS for Oracle in all commercial AWS Regions and the AWS GovCloud (US) Regions. To learn more, review the Amazon RDS API Documentation.&nbsp;

## 핵심 요약

요약 미지원
