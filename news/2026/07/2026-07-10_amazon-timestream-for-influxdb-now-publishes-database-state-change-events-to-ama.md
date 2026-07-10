---
title: "Amazon Timestream for InfluxDB now publishes database state change events to Amazon EventBridge"
date: "2026-07-10"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/timestream-influxdb-eventbridge/"
tags: ["Lambda", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Timestream for InfluxDB now publishes database state change events to Amazon EventBridge

**날짜:** 2026년 07월 10일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/timestream-influxdb-eventbridge/

## 내용

Amazon Timestream for InfluxDB now publishes events to Amazon EventBridge when your database instances or clusters undergo state changes. Events are emitted for lifecycle operations including creation, deletion, compute and storage scaling, parameter group updates, maintenance windows, and reboot — covering both successful completions and failures.  With this capability, customers can use Amazon EventBridge rules to programmatically react to database operations without polling the API for status. DevOps teams can build automation workflows that trigger when a scaling operation completes, operations teams can route failure events for immediate alerting, and compliance teams can persist all events to Amazon CloudWatch Logs or Amazon S3 for audit trails. Events are published to the default Amazon EventBridge event bus in your account with source aws.timestream-influxdb, supporting content-based filtering and routing to any EventBridge target including AWS Lambda functions, AWS Step Functions, Amazon SQS queues, Amazon SNS topics, and cross-account event buses.  This capability is available in all AWS Regions where Amazon Timestream for InfluxDB is available. Standard Amazon EventBridge pricing applies for rule evaluation and target delivery. To get started, open the Amazon EventBridge console and create a rule with source aws.timestream-influxdb. For more information, see the Amazon Timestream for InfluxDB documentation and pricing page.

## 핵심 요약

요약 미지원
