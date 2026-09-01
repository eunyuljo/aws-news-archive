---
title: "Amazon CloudWatch now supports warm-up periods for alarms"
date: "2026-09-01"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-alarms-warmup-period"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch now supports warm-up periods for alarms

**날짜:** 2026년 09월 01일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-alarms-warmup-period

## 내용

Amazon CloudWatch now lets you configure a warm-up period for metric alarms and log alarms, delaying alarm evaluation for a set time after the alarm is created. This reduces noise from missing data while a new resource or service starts up and begins publishing metrics. For example, a team that provisions a new microservice and its alarms together through a CI/CD pipeline can attach a warm-up period so alarms do not page the on-call engineer while the service is still starting up and has not yet published metrics. 
  
Previously, when you created an alarm before the underlying metric was reporting data, CloudWatch evaluated the alarm right away using its "treat missing data" setting. For resources that take time to begin emitting metrics, such as a newly deployed application or service, this could cause the alarm to transition state and run actions on missing data during startup, triggering unnecessary notifications. A warm-up period fixes this by giving you two ways to hold off evaluation during startup: wait a fixed duration you set before evaluation begins, or let CloudWatch start evaluating automatically as soon as the metric actually has enough data to fill the alarm's evaluation window. 
  
You set the warm-up period with the WarmUpConfiguration parameter when you create or update an alarm. Specify a warm-up duration from 1 to 2,880 minutes (2 days). By default, the alarm ends warm-up early and begins evaluating as soon as enough data fills its evaluation window. Additionally, you can optionally require the alarm to wait the full duration before evaluating. 
  
Warm-up periods are available in all AWS Regions where Amazon CloudWatch is offered at no additional charge beyond standard CloudWatch alarm pricing. 
  
To get started, see &nbsp;Alarm warm-up periods&nbsp; and &nbsp;Create an alarm that uses a warm-up period&nbsp; in the Amazon CloudWatch User Guide.

## 핵심 요약

요약 미지원
