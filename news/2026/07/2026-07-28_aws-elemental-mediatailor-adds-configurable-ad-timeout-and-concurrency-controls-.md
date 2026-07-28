---
title: "AWS Elemental MediaTailor adds configurable ad timeout and concurrency controls for improved ad fill and faster startup"
date: "2026-07-28"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/mediatail-configurable-ad-timeout-and-concurrency"
tags: ["Config", "2026", "new-region", "performance"]
nav_exclude: true
---

# AWS Elemental MediaTailor adds configurable ad timeout and concurrency controls for improved ad fill and faster startup

**날짜:** 2026년 07월 28일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/mediatail-configurable-ad-timeout-and-concurrency

## 내용

AWS Elemental MediaTailor now gives you direct control over ad decision server (ADS) timeout. Previously, changing these settings required contacting AWS Support. You can now configure individual HTTP ad request timeouts, total ad personalization time budgets for live, VOD, and live ad prefetch, and enable parallel ADS requests. 
These settings allow you to optimize ad delivery performance for your specific workflows. For example, you can increase the personalization time budget for live events to improve ad fill rates or enable parallel ADS requests in VOD workflows to reduce overall response time for faster video startup. New prefetch-specific timeout settings give you additional granularity for livestream ad retrieval. 
You can configure these settings through the AWS Elemental MediaTailor console, AWS CLI, or AWS SDKs using the new AdsPersonalizationTimeouts and AdsPersonalizationConcurrency parameters on your playback configurations. 
This feature is available in all AWS Regions where AWS Elemental MediaTailor is available.&nbsp; 
To learn more about configuring ADS request timeouts, personalization time budgets, and concurrency, see Advanced settings in the AWS Elemental MediaTailor User Guide.

## 핵심 요약

요약 미지원
