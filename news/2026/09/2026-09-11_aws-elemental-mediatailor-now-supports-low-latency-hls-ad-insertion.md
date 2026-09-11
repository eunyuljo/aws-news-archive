---
title: "AWS Elemental MediaTailor now supports Low-Latency HLS ad insertion"
date: "2026-09-11"
service: "Personalize"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-elemental-mediatailor-low-latency-hls-ad-insertion"
tags: ["Personalize", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# AWS Elemental MediaTailor now supports Low-Latency HLS ad insertion

**날짜:** 2026년 09월 11일
**서비스:** Personalize
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-elemental-mediatailor-low-latency-hls-ad-insertion

## 내용

AWS Elemental MediaTailor now supports Low-Latency HTTP Live Streaming (LL-HLS) ad insertion using HLS Interstitials. MediaTailor is a channel assembly and personalized ad insertion service for video providers that monetizes live streams, linear channels, and video-on-demand content. With this launch, video providers can insert ads into low-latency live streams while holding the reduced latency their viewers expect. 
LL-HLS reduces live latency by delivering partial segments and letting players hold a playlist request open until the next segment part is ready, which requires media playlists to be cacheable at the content delivery network (CDN) edge. MediaTailor supports this using HLS Interstitials, which reference ads as a separate playlist instead of stitching them into each viewer's media playlist. Every viewer receives the same cacheable playlist, so MediaTailor sustains low-latency playback at scale and moves the ad decision server call off the manifest request path. This capability has been proven in production on live sporting events with multi-million views, and is ideal for live sports, news, betting and wagering, watch-party, and interactive live formats where latency is a product requirement. 
Low-Latency HLS ad insertion is available in all AWS Regions where AWS Elemental MediaTailor is available. To learn more, visit the AWS Elemental MediaTailor product page and the MediaTailor server-guided ad insertion documentation. To get started, sign in to the MediaTailor console..

## 핵심 요약

요약 미지원
