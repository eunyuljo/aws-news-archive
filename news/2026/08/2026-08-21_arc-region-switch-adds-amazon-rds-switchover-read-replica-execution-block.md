---
title: "ARC Region switch adds Amazon RDS Switchover Read Replica execution block"
date: "2026-08-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/region-switch-rds-switchover-execution-block/"
tags: ["RDS", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# ARC Region switch adds Amazon RDS Switchover Read Replica execution block

**날짜:** 2026년 08월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/region-switch-rds-switchover-execution-block/

## 내용

Today, we are launching the Amazon RDS Switchover Read Replica execution block in ARC Region switch, which automates recovery orchestration for Amazon RDS databases running Oracle Data Guard in multi-Region workloads. Amazon Application Recovery Controller (ARC) Region switch helps customers orchestrate the failover of their multi-Region applications to achieve a bounded recovery time in the event of a Regional impairment. 
To recover an Amazon RDS database running Oracle Data Guard during a Regional failover, customers perform manual steps to reverse the roles of the primary database and its read replica or to promote a read replica to a primary database instance. Region switch now allows you to automate this recovery with the RDS Switchover Read Replica execution block. The same execution block automates the role transition between the primary database and read replica with zero data loss during a planned failover scenario, or promotion of the read replica to a primary database during an unplanned failover where recovery speed is of the essence. With native cross-account support, you can orchestrate recovery of Amazon RDS instances that are hosted in a different account from your Region switch plan, enabling centralized management of recovery across your organization. 
To get started, see the documentation for&nbsp;Amazon RDS Switchover Read Replica execution block&nbsp;. To learn more about ARC Region switch, visit the Application Recovery Controller page&nbsp;.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;

## 핵심 요약

요약 미지원
