---
title: "Amazon RDS for Oracle now supports Replica First Patching for reduced downtime"
date: "2026-11-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-replica-first-patching/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon RDS for Oracle now supports Replica First Patching for reduced downtime

**날짜:** 2026년 11월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-replica-first-patching/

## 내용

Amazon Relational Database Service (Amazon RDS) for Oracle now supports Replica First Patching, which reduces downtime during minor version upgrades. Replica First Patching is available for Enterprise Edition DB instances. With Replica First Patching, you apply a minor version upgrade to a replica in the same AWS Region first while your primary DB instance continues to serve traffic, and then switch over to the replica when you're ready to complete the upgrade. If the replica is in read-only mode, you can validate the new minor engine version with your read traffic. 
Replica First Patching helps you keep mission-critical Oracle workloads current on minor versions with less disruption. You choose when to switch over within the switchover window, for example during a low-traffic period. If you don't switch over within the window, Amazon RDS rolls back the replica to its original minor engine version. After the switchover, Amazon RDS completes the upgrade on the new primary DB instance. Amazon RDS then upgrades your other replicas, including your former primary DB instance, to the same minor engine version. 
We recommend that you connect your applications through the Primary Endpoint when you use Replica First Patching. The Primary Endpoint is a DNS name that resolves to the current primary DB instance, so your applications reach the new primary DB instance after the switchover without connection string changes. 
Replica First Patching is available at no additional charge in all commercial AWS Regions where Amazon RDS for Oracle is available. Standard pricing applies to the replica DB instance. To learn more, see Upgrading with Replica First Patching in the Amazon RDS User Guide.

## 핵심 요약

요약 미지원
