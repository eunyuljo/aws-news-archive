---
title: "Amazon DynamoDB global tables now support disassociating replicas"
date: "2026-10-21"
service: "DynamoDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/dynamodb-global-tables-disassociate/"
tags: ["DynamoDB", "2026", "new-region"]
nav_exclude: true
---

# Amazon DynamoDB global tables now support disassociating replicas

**날짜:** 2026년 10월 21일
**서비스:** DynamoDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/dynamodb-global-tables-disassociate/

## 내용

Amazon DynamoDB global tables now support disassociating a replica without deleting its table or data. Global tables provide fully managed, multi-Region, multi-active replication. You can now stop replication to and from a replica and continue using the same table as a single-Region table. 
An account can leave a shared multi-account global table and continue using its table independently. You can also stop replication to a Region while keeping its table for local workloads, validation, or audit, without creating a replacement table or copying data. 
DynamoDB supports disassociating replicas in all AWS Regions for same-account and multi-account global tables that use multi-Region eventual consistency (MREC). 
To get started, use the AWS Management Console, AWS CLI, DynamoDB API, or AWS CloudFormation. For more information, see Disassociating replicas in the Amazon DynamoDB&nbsp;Developer Guide.

## 핵심 요약

요약 미지원
