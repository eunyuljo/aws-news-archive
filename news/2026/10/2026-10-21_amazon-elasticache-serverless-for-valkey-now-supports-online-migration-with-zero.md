---
title: "Amazon ElastiCache Serverless for Valkey now supports online migration with zero downtime"
date: "2026-10-21"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-elasticache-serverless-valkey-online-migration/"
tags: ["EC2", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon ElastiCache Serverless for Valkey now supports online migration with zero downtime

**날짜:** 2026년 10월 21일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-elasticache-serverless-valkey-online-migration/

## 내용

Amazon ElastiCache Serverless for Valkey now supports online migration from self-managed Valkey and Redis OSS on Amazon EC2 with zero downtime. Zero downtime means zero Errors returned to the client during migration, measured the same way the ElastiCache SLA measures availability. Your application continues reading and writing through cutover, and you do not need third-party replication tools. 
Online migration runs in three steps. You prepare the migration, start the data sync, and complete the cutover. ElastiCache gives you a migration endpoint your application can point to when you prepare the migration, and data replicates continuously from your source once you start the sync. You choose when writes move to the serverless cache, with a manual cutover or an automatic one once your data is in sync. ElastiCache records each step as an event on the cache’s Events tab, with the reason for any failed step. 
Online migration connects to your source using encryption in transit (TLS) and authentication, and reads credentials from AWS Secrets Manager, so your existing security controls stay in place. Online migration supports self-managed caches in cluster mode on Amazon EC2 running Redis OSS 4.0 through 7.2 or Valkey 7.2 through 8.1, and you can migrate them straight to Valkey 9.0. 
Migration usage is free for the first 180 days per AWS account, starting when the account first prepares a migration. After that, you pay per node-hour for the migration nodes that ElastiCache runs to replicate your data, for as long as a migration is active. The ElastiCache Serverless cache is billed separately at standard data storage and ECPU rates, including during the free period. For pricing details, see Amazon ElastiCache pricing. Online migration is available in all commercial AWS Regions, the China Regions, and the AWS GovCloud (US) Regions.&nbsp; 
To get started, create or select an empty ElastiCache Serverless cache to migrate into, then start the migration from the ElastiCache console or the AWS CLI. To learn more, see the documentation.

## 핵심 요약

요약 미지원
