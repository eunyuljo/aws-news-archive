---
title: "Amazon CloudWatch Alarms now supports tags in alarm actions payload"
date: "2026-10-21"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-cloudwatch-tags-on-alarm-actions-payload"
tags: ["Lambda", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch Alarms now supports tags in alarm actions payload

**날짜:** 2026년 10월 21일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-cloudwatch-tags-on-alarm-actions-payload

## 내용

Today, Amazon CloudWatch announces support for including alarm tags in action payloads and Amazon EventBridge events, enabling customers to route and filter alarm notifications by tag without additional lookups. When enabled on an alarm, CloudWatch adds the alarm tags to the messages it sends to Amazon SNS, AWS Lambda, and Amazon EventBridge each time the alarm changes state. This option is designed for customers who route many alarms through a shared notification pipeline and need to identify the owning team, environment, or service directly from the message. 
With tags in actions payloads, customers can avoid the extra work of correlating tag metadata with alarm events after the fact. For example, a team that routes hundreds of alarms through a single SNS topic to a Lambda function previously had to call ListTagsForResource for each event to find the owning team before paging. With this feature, the tags arrive in the notification, so the function can route directly from the message. The setting is off by default and configurable per alarm, and customers can include all tags, only selected tag keys, or all tags except selected keys. It is supported for metric, composite, and log alarms. 
Tags in actions and events for CloudWatch Alarms are available in all AWS Regions where Amazon CloudWatch is available except Middle East (UAE), and Middle East (Bahrain). 
To get started, see &nbsp;Alarm tags in action payloads&nbsp; in the Amazon CloudWatch User Guide. To learn more about Amazon CloudWatch Alarms, visit the &nbsp;Amazon CloudWatch&nbsp; product page.

## 핵심 요약

요약 미지원
