---
title: "Amazon GameLift Streams now supports Custom Aspect Ratio and Dynamic Resolution"
date: "2026-07-28"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# Amazon GameLift Streams now supports Custom Aspect Ratio and Dynamic Resolution

**날짜:** 2026년 07월 28일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams/

## 내용

Amazon GameLift Streams now supports Custom Aspect Ratio and Dynamic Resolution, giving you greater control over the streaming experience across diverse player devices and network conditions. 
With Custom Aspect Ratio, you can configure a specific resolution per stream session to match your player's device — including portrait, landscape, ultra-wide, and square aspect ratios. This eliminates letterboxing or pillarboxing, delivering native full-screen experiences on mobile phones, tablets, and non-standard displays. Specify any resolution from 320 to 4096 pixels per dimension (up to 1080p total pixel budget) using the DisplayConfiguration parameter in the StartStreamSession API. You can also try custom resolution from the AWS Console. 
Dynamic Resolution automatically adapts stream quality when a player's network bandwidth fluctuates. When bandwidth drops, the stream gracefully reduces resolution to maintain smooth playback without frame drops or disconnections — and automatically recovers to full quality when conditions improve. Dynamic Resolution is enabled by default for all new stream groups with no configuration required. Customers will need to download the new Web SDK. 
Both features are available in all AWS Regions where Amazon GameLift Streams is offered. To learn more, see Custom stream resolution in the Amazon GameLift Streams Developer Guide.&nbsp; &nbsp; https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/custom-stream-resolution.html

## 핵심 요약

요약 미지원
