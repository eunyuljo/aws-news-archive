---
title: "AWS Elemental introduces Dynamic Multiview for live video"
date: "2026-09-11"
service: "ECS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-elemental-dynamic-multiview-video/"
tags: ["ECS", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Elemental introduces Dynamic Multiview for live video

**날짜:** 2026년 09월 11일
**서비스:** ECS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-elemental-dynamic-multiview-video/

## 내용

AWS Elemental MediaPackage now offers Dynamic Multiview, a server-side capability that composes multiple live video sources into viewer-selected tiled layouts on demand. Content providers can deliver multi-angle, multi-game, and personalized viewing experiences as standard HLS (HTTP Live Streaming) and DASH (Dynamic Adaptive Streaming over HTTP) streams playable on most modern consumer devices, televisions, and set top boxes without custom player development. 
Dynamic Multiview operates entirely in the compressed domain, combining individually encoded sources without re-encoding or compositing. Customers encode each source once through AWS Elemental MediaLive, and MediaPackage assembles compositions on demand - only when viewers request them, eliminating the need to pre-encode combinations. Because the output is standard HLS and DASH, it plays natively on existing devices and players with no app changes or SDK integration required. The feature supports AVC and HEVC codecs, DRM encryption, SCTE-35 ad marker passthrough, and full-screen ad replacement. 
To learn more, visit the Elemental Dynamic Multiview Reference Guide. 
Dynamic Multiview is available in all AWS Regions where AWS Elemental MediaPackage and MediaLive are available.

## 핵심 요약

요약 미지원
