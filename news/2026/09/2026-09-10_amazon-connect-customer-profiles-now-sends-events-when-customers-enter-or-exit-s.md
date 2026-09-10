---
title: "Amazon Connect Customer Profiles now sends events when customers enter or exit segments"
date: "2026-09-10"
service: "Kinesis"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/connect-customer-profiles-segment-events/"
tags: ["Kinesis", "2026", "new-region"]
nav_exclude: true
---

# Amazon Connect Customer Profiles now sends events when customers enter or exit segments

**날짜:** 2026년 09월 10일
**서비스:** Kinesis
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/connect-customer-profiles-segment-events/

## 내용

Amazon Connect Customer Profiles now sends segment membership events, providing the ability to receive real-time and scheduled notifications when customer profiles enter or exit a segment, such as high-value customers or low-satisfaction customers. Previously, detecting when customer profiles joined or left a segment required exporting entire segments at regular intervals and running custom scripts to identify differences. This manual process consumed resources, introduced errors, and created multi-hour delays between a customer qualifying for a segment and downstream systems acting on it.
With segment membership events, Customer Profiles automatically evaluates and streams membership changes directly to your Amazon Kinesis Data Stream. For segments built with standard conditions, changes are detected in near real-time as profile attributes update. For enhanced segments (using Spark SQL), periodic snapshots evaluate membership at configurable intervals and notify you of changes. Each event includes the profile ID, segment name, operation type (joined or left), and whether the change detected occurred in real-time or during a scheduled run, giving you everything needed to activate outbound campaigns, personalization workflows, or retention actions within seconds instead of hours.
You can start using segment membership events in all AWS Regions where Amazon Connect Customer Profiles is available. To get started, configure an Amazon Kinesis Data Stream in your domain settings and subscribe your segments. For more information, see our admin guide. For more information about Amazon Connect Customer Profiles, visit our product page.

## 핵심 요약

요약 미지원
