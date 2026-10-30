---
title: "Amazon RDS for Oracle and SQL Server now support storage autoscaling on additional storage volumes"
date: "2026-10-30"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-rds-oracle-sqlserver-autoscaling-additional-storage-volumes"
tags: ["RDS", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon RDS for Oracle and SQL Server now support storage autoscaling on additional storage volumes

**날짜:** 2026년 10월 30일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-rds-oracle-sqlserver-autoscaling-additional-storage-volumes

## 내용

Amazon RDS for SQL Server and Amazon RDS for Oracle now support RDS storage autoscaling on additional storage volumes. RDS storage autoscaling automatically scales storage capacity in response to growing database workloads, with zero downtime. 
Additional storage volumes allow you to add up to three additional volumes to increase your storage capacity up to 256 TiB. Previously, you had to manually provision storage capacity on the additional storage volumes based on anticipated application capacity demands while autoscaling could be enabled on the primary storage volume. Under-provisioning could result in application downtime, and over-provisioning could result in under-utilized resources and&nbsp;higher costs. With RDS storage autoscaling, you simply set your desired maximum storage limit for each additional storage volume, and autoscaling takes care of the rest. 
RDS storage autoscaling continuously monitors actual storage consumption, and scales capacity up automatically when actual utilization approaches provisioned storage capacity. Autoscaling works with new and existing database instances. Autoscaling has no additional charges and you only pay for the provisioned storage resources. You can enable it by using the AWS Management Console, AWS CLI, or Amazon RDS API. 
RDS storage autoscaling for additional storage volumes is available for Amazon RDS for SQL Server and Amazon RDS for Oracle in all commercial AWS Regions and the AWS GovCloud (US) Regions. To learn more, please visit&nbsp;the Amazon RDS storage autoscaling documentation.&nbsp;

## 핵심 요약

요약 미지원
