---
title: "Amazon RDS for Oracle no longer requires automatic minor version upgrades for JVM, Spatial, Locator, and OLAP options"
date: "2026-10-31"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/oracle-jvm-spatial-locator-olap-options-amvu-optional/"
tags: ["RDS", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon RDS for Oracle no longer requires automatic minor version upgrades for JVM, Spatial, Locator, and OLAP options

**날짜:** 2026년 10월 31일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/oracle-jvm-spatial-locator-olap-options-amvu-optional/

## 내용

Amazon Relational Database Service (Amazon RDS) for Oracle now lets you turn off automatic minor version upgrades on new and existing DB instances that use the JVM, Spatial, Locator, or OLAP option. Previously, these options required automatic minor version upgrades to be enabled. 
With this change, you decide when to apply minor version upgrades to DB instances using these options. If you turn off automatic minor version upgrades, we recommend that you apply new minor versions regularly so your DB instances keep the latest Oracle security fixes. To keep automatic minor version upgrades turned on and still control the order in which your environments are upgraded, you can use AWS Organizations upgrade rollout policy. 
This change is available in all commercial AWS Regions and the AWS GovCloud (US) Regions where Amazon RDS for Oracle is available. To learn more about options available in Amazon RDS for Oracle, see Adding options to Oracle DB instances in the Amazon RDS User Guide.

## 핵심 요약

요약 미지원
