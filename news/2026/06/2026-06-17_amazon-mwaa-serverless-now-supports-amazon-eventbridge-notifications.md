---
title: "Amazon MWAA Serverless now supports Amazon EventBridge notifications"
date: "2026-06-17"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-eventbridge/"
tags: ["S3", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon MWAA Serverless now supports Amazon EventBridge notifications

**날짜:** 2026년 06월 17일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-eventbridge/

## 내용

Amazon Managed Workflows for Apache Airflow (MWAA) Serverless now supports workflow and task state change events to Amazon EventBridge, enabling data engineering and platform teams to build event-driven automation for their Apache Airflow workflows. 
Previously, monitoring workflow execution required custom polling logic or manual observation. With this launch, MWAA Serverless can emit events when workflows transition between states, including started, running, succeeded, or failed, and when individual tasks change state, such as scheduled, succeeded, failed, or up for retry. With this feature, you can further automate your existing workflows - for example, using EventBridge notifications to trigger alerts when a production workflow fails, automatically restart dependent pipelines when an upstream workflow succeeds, or log state transitions to Amazon S3 for compliance and auditing. 
This feature is available in all AWS Regions where Amazon MWAA Serverless is available. For the complete list of supported Regions, see Regions in the Amazon MWAA Serverless User Guide. For pricing details, see Amazon EventBridge pricing. To learn more, see Monitoring Amazon MWAA Serverless in the Amazon MWAA Serverless User Guide and Amazon MWAA Serverless events in the Amazon EventBridge Events Reference.

## 핵심 요약

요약 미지원
