---
title: "Amazon CloudWatch Alarms now supports wall clock evaluation windows"
date: "2026-08-12"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/cloudwatch-alarms-wallclock-evaluation"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch Alarms now supports wall clock evaluation windows

**날짜:** 2026년 08월 12일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/cloudwatch-alarms-wallclock-evaluation

## 내용

Today, Amazon CloudWatch announces wall clock evaluation windows for metric alarms, enabling customers to align alarm evaluations to fixed calendar boundaries such as the top of the hour, midnight, or the start of the week. This new option complements the existing sliding window behavior and is designed for customers who monitor scheduled or business-aligned workloads.  With wall clock evaluation windows, customers can avoid false alarms that occur when events cross rolling window boundaries. For example, a daily backup alarm using a sliding window can trigger incorrectly if consecutive backups are slightly more than 24 hours apart, even though each calendar day had a successful backup. A wall clock window evaluates each calendar day independently, eliminating this issue. Customers can also specify a time zone so that daily alarms align to their local business day, with daylight saving time transitions handled automatically.  Wall clock evaluation windows for CloudWatch Alarms are available in all AWS Regions where Amazon CloudWatch is available, except the Middle East (UAE) and Middle East (Bahrain) Regions.  To get started, see Alarm evaluation window in the Amazon CloudWatch User Guide. To learn more about Amazon CloudWatch Alarms, visit the Amazon CloudWatch product page.

## 핵심 요약

요약 미지원
