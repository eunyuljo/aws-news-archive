---
title: "Amazon RDS for Db2 now supports new Canadian time zones"
date: "2026-11-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-db2-supports-new-canadian-time"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon RDS for Db2 now supports new Canadian time zones

**날짜:** 2026년 11월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-db2-supports-new-canadian-time

## 내용

​​Amazon RDS for Db2 now supports four new time zones, America/Vancouver, America/Edmonton, America/Inuvik, and America/Winnipeg, that reflect the updated local time rules for British Columbia, Alberta, the Northwest Territories, and Manitoba in Canada. As of November 1, 2026, these provinces and territories observe permanent daylight saving time and no longer set their clocks back by an hour.​ 
​Data stored in UTC is unaffected, but values based on the instance's local time, such as CURRENT TIMESTAMP, CURRENT DATE, default timestamp columns, scheduled jobs, and business-day batch logic, can be affected. With these new time zones, you can keep local time values accurate for workloads operating in these regions.&nbsp; 
​​You can select the new time zones when you create a new RDS for Db2 instance. To change the time zone of an existing instance, contact AWS Support, as modifying the time zone of an existing instance is not supported through the AWS CLI, API, or SDK. If your instances serve workloads in these regions, we recommend reviewing them and updating your time zone configuration to avoid incorrect local times in your applications.​ 
​The new time zones are available in all AWS Regions where Amazon RDS for Db2 is offered. To learn more and see the full list of supported time zones, visit the Amazon RDS for Db2 time zone documentation.​&nbsp;

## 핵심 요약

요약 미지원
