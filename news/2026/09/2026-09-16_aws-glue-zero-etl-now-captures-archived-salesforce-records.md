---
title: "AWS Glue zero-ETL now captures archived Salesforce records"
date: "2026-09-16"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/glue-zero-etl-archived-salesforce/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# AWS Glue zero-ETL now captures archived Salesforce records

**날짜:** 2026년 09월 16일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/glue-zero-etl-archived-salesforce/

## 내용

AWS Glue zero-ETL integrations for Salesforce now capture archived records in your target tables, giving you a complete replica of your Salesforce data for analytics and reporting. Archived records are identified and reflected accurately through the isArchived field, so your analytical data stays fully in sync with your Salesforce source. This is especially valuable for high-volume entities that Salesforce archives automatically, such as Events, Tasks, and Activities, giving you complete visibility into this data in your analytical data stores. 
This feature applies to your zero-ETL integrations with no action required. New integrations capture archived records automatically from the moment the integration is created. For existing integrations, AWS Glue automatically backfills archived record status, with no re-sync, reconfiguration, or schema change needed. Your existing pipelines continue running uninterrupted while the isArchived field is populated accurately on your behalf. 
This feature is available in all AWS Commercial and AWS GovCloud (US) Regions where AWS Glue zero-ETL integrations for Salesforce are supported. 
To get started, create or continue using an AWS Glue zero-ETL integration for Salesforce using the AWS Glue console, CLI, or SDK. To learn more, see AWS Glue zero-ETL documentation.

## 핵심 요약

요약 미지원
