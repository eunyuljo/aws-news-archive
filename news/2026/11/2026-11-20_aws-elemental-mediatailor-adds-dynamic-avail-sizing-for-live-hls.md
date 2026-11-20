---
title: "AWS Elemental MediaTailor adds Dynamic Avail Sizing for live HLS"
date: "2026-11-20"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-elemental-mediatailor-dynamic-avail-sizing-live-hls"
tags: ["Config", "2026"]
nav_exclude: true
---

# AWS Elemental MediaTailor adds Dynamic Avail Sizing for live HLS

**날짜:** 2026년 11월 20일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-elemental-mediatailor-dynamic-avail-sizing-live-hls

## 내용

AWS Elemental MediaTailor now supports Dynamic Avail Sizing, which reduces the slate viewers see when ad breaks, also called avails, in live HLS streams go unfilled. MediaTailor is a server-side ad insertion and channel assembly service that personalizes ads in live and on-demand video streams. 
When the ad decision server returns fewer ads than a break allows, dynamic avail sizing omits the unfilled time and resumes programming early instead of showing slate. To keep playback continuous, MediaTailor holds back a configurable reserve of content behind the live edge and draws on it when a break ends early. When the reserve runs low, MediaTailor requests extra ad time in later breaks to refill it. Free ad-supported streaming TV (FAST) channel operators can use dynamic avail sizing to keep viewers watching programming instead of filler content. 
Customers turn on dynamic avail sizing for each playback session by adding query parameters to the session initialization URL, with no change to their playback configuration. To learn more, see Dynamic avail sizing in the AWS Elemental MediaTailor User Guide.

## 핵심 요약

요약 미지원
