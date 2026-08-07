---
title: "Amazon SES now helps identify automated open and click events in event notifications"
date: "2026-08-07"
service: "SNS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ses-automated-email-interactions/"
tags: ["SNS", "2026", "new-region"]
nav_exclude: true
---

# Amazon SES now helps identify automated open and click events in event notifications

**날짜:** 2026년 08월 07일
**서비스:** SNS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ses-automated-email-interactions/

## 내용

Amazon Simple Email Service (SES) now helps you identify automated email interactions. Open and Click event notifications now include an isBotEvent field that indicates whether the event was likely triggered by an automated system or a human recipient.  Customers who publish Open or Click events through a configuration set event destination will now see an isBotEvent field with a value of Likely or Unlikely in event notifications. You can use this field as a signal to help you better understand how much of your engagement is driven by human recipients versus automated systems.  This feature is available in all AWS Regions where Amazon SES is available. If you already publish Open or Click events to an event destination, the isBotEvent field is automatically included, no additional configuration is needed.  To learn more, see Contents of event data that Amazon SES publishes to Amazon SNS and Contents of event data that Amazon SES publishes to Firehose in the Amazon SES Developer Guide.

## 핵심 요약

요약 미지원
