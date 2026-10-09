---
title: "Amazon RDS for Oracle now supports minor version upgrade prechecks and a new RDS event to help reduce patching downtime"
date: "2026-10-09"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-rds-oracle-minor-version-upgrade-precheck-new-patching-rds-event/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon RDS for Oracle now supports minor version upgrade prechecks and a new RDS event to help reduce patching downtime

**날짜:** 2026년 10월 09일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-rds-oracle-minor-version-upgrade-precheck-new-patching-rds-event/

## 내용

Amazon Relational Database Service (Amazon RDS) for Oracle now lets you run a minor version upgrade precheck yourself, before you start an upgrade or before your scheduled maintenance window. RDS for Oracle now also emits a new event during patching that tells you when your DB instance is accepting connections again. With this event, you can bring your applications back while the remaining maintenance tasks are still in progress, which can reduce your application downtime during patching.
At the start of every minor version upgrade, RDS for Oracle checks for conditions that would prevent the upgrade from completing, such as insufficient free storage, invalid Oracle-maintained objects, or invalid triggers. If a check finds a problem, the upgrade stops, and you must fix the problem and schedule the upgrade again. Previously, these checks ran only as part of the upgrade itself. With the new rdsadmin.rdsadmin_precheck_tasks.precheck_minor_upgrade procedure, you can run the checks at any time. The precheck is read-only and doesn't affect your workload. It reports every issue it finds in a single log so you can fix them and run the precheck again until it passes before your maintenance window.
During a minor version upgrade or an operating system update, RDS for Oracle now emits RDS-EVENT-0596 as soon as your DB instance is accepting connections. Any remaining maintenance tasks then complete while your database is online. You can subscribe to this event through Amazon RDS event notifications or Amazon EventBridge to automate application reconnection or notify your teams that the database is back online.
These capabilities are available in all AWS commercial and AWS GovCloud (US) Regions where Amazon RDS for Oracle is available. To learn more, see Running minor version upgrade prechecks in Amazon RDS for Oracle, Amazon RDS event categories and event messages, and Monitoring Amazon RDS events in the Amazon RDS User Guide.

## 핵심 요약

요약 미지원
