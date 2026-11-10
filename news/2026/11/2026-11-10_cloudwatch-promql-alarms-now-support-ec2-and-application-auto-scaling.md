---
title: "CloudWatch PromQL alarms now support EC2 and Application Auto Scaling"
date: "2026-11-10"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-alarms-autoscaling-group-actions"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# CloudWatch PromQL alarms now support EC2 and Application Auto Scaling

**날짜:** 2026년 11월 10일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-alarms-autoscaling-group-actions

## 내용

Amazon CloudWatch alarms that use Prometheus Query Language (PromQL) can now trigger Amazon EC2 and Application Auto Scaling step and simple scaling policies. You can scale your EC2 Auto Scaling groups on CloudWatch OpenTelemetry metrics using the same kind of PromQL queries you use for dashboards and alerting. 
  
In this release, PromQL alarms also support EC2 Auto Scaling simple and step scaling policies. Target tracking is not currently a supported policy type for PromQL alarms. Teams moving to OpenTelemetry can scale capacity on the same metrics as the rest of their monitoring, instead of keeping separate classic metric alarms for scaling. For step scaling, how far the value is past the threshold in your PromQL query decides which step applies. The query must return a single series and compare it to a threshold. 
  
You can add EC2 Auto Scaling and Application Auto Scaling actions in the CloudWatch console when you create or edit an alarm, or with the PutMetricAlarm API, AWS CLI, AWS SDKs, or AWS CloudFormation. You can also use the PutMetricAlarm API, AWS CLI, AWS SDKs, or AWS CloudFormation. 
This feature is available in all AWS Regions where CloudWatch PromQL alarms are available. Standard CloudWatch alarm pricing applies. To get started, see &nbsp;Using PromQL in alarms&nbsp; and &nbsp;Alarm actions&nbsp; in the Amazon CloudWatch User Guide.

## 핵심 요약

요약 미지원
