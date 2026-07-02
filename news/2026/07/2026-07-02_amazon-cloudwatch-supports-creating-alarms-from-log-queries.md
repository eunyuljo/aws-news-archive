---
title: "Amazon CloudWatch supports creating alarms from log queries"
date: "2026-07-02"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-log-alarms/"
tags: ["CloudWatch", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch supports creating alarms from log queries

**날짜:** 2026년 07월 02일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-log-alarms/

## 내용

Amazon CloudWatch allows you to create alarms on log data using log queries, and get alerted on anomalies without leaving your log analysis workflow. 
With today's launch, you can configure an alarm on log query and specify the alarm threshold directly, thereby eliminating the need to first create metric filters or custom metrics as intermediate steps. This streamlines the path to actively monitoring the data in your logs, and monitoring and alerting on it. For example, you can write a query to count error rates by service, set a threshold, and receive an alarm notification with log context when errors spike - all in a single workflow. Alarms created from log queries support all standard CloudWatch Alarm actions, including Amazon SNS notifications, and Amazon EventBridge integrations. 
This feature is available in all commercial AWS Regions except Middle East (UAE), and Middle East (Bahrain). You can create log query-based alarms using the Amazon CloudWatch console, AWS Command Line Interface (AWS CLI), AWS CloudFormation, and AWS SDKs. For pricing details and documentation, see the Amazon CloudWatch pricing&nbsp;and visit the Amazon CloudWatch documentation.

## 핵심 요약

요약 미지원
