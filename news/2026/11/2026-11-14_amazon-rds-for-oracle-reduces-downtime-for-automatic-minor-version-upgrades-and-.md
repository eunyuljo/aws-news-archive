---
title: "Amazon RDS for Oracle reduces downtime for automatic minor version upgrades and scheduled maintenance"
date: "2026-11-14"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-reduces-maintenance-downtime-for-amvu-scheduled-upgrades/"
tags: ["RDS", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon RDS for Oracle reduces downtime for automatic minor version upgrades and scheduled maintenance

**날짜:** 2026년 11월 14일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-reduces-maintenance-downtime-for-amvu-scheduled-upgrades/

## 내용

Amazon Relational Database Service (Amazon RDS) for Oracle now reduces downtime for automatic minor version upgrades, as well as minor version upgrades and operating system updates scheduled for your maintenance window. Shorter maintenance makes it easier to stay current on the latest Oracle minor versions and operating system updates with less disruption to your applications. If you turned on automatic minor version upgrade, your DB instances benefit automatically. 
To apply these upgrades and updates, RDS has to set up new resources as part of the maintenance. Previously, RDS set up these resources after the maintenance started, which made your downtime longer. Now, RDS prepares them up to 30 minutes before your maintenance window, while your DB instance keeps serving your workload. When the maintenance window opens, your DB instance is offline for less time because resources required for the maintenance are already prepared. This applies to both Enterprise Edition and Standard Edition 2 DB instances. 
The preparation never blocks or delays your own operations, and your DB instance stays available while RDS prepares. If a change that you make conflicts with the preparation, RDS rolls back the staged resources, and your change goes ahead. If the preparation can't finish, RDS still applies the maintenance in your window, without the preparation. New RDS events tell you when the preparation starts, when it finishes, and when it can't finish.&nbsp;RDS for Oracle will continue to introduce improvements that further reduce maintenance downtime. 
This capability is available at no additional cost in all commercial AWS Regions and the AWS GovCloud (US) Regions where Amazon RDS for Oracle is available. To learn more, see Maintenance preparation, Amazon RDS event categories and event messages, and Maintaining a DB instance in the Amazon RDS User Guide.

## 핵심 요약

요약 미지원
