---
title: "AWS Elemental MediaLive adds support for A/B forensic watermarking"
date: "2026-09-11"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/medialive-ab-forensic-watermarking/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# AWS Elemental MediaLive adds support for A/B forensic watermarking

**날짜:** 2026년 09월 11일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/medialive-ab-forensic-watermarking/

## 내용

AWS Elemental MediaLive now supports A/B forensic watermarking, enabling content owners to trace the source of unauthorized redistribution of live video content. A single MediaLive channel produces two synchronized output variants, each carrying a distinct visually transparent watermark that persists through re-encoding and screen capture. Downstream packaging and CDN infrastructure assembles these variants into unique per-session sequences that identify the origin of leaked content. 
Forensic watermarking follows the DASH Industry Forum (DASH-IF) specification for A/B watermarking (European Telecommunications Standards Institute (ETSI) TS 104 002), ensuring interoperability with standards-compliant packagers and CDN infrastructure. Customers can configure watermarking on Common Media Application Format (CMAF) Ingest output groups through the MediaLive API or console. MediaLive delivers watermarked A and B variants via CMAF ingest to AWS Elemental MediaPackage or third-party packagers, enabling downstream per-session watermark assembly through compatible CDN infrastructure including Amazon CloudFront. 
To learn more, visit the AWS Elemental MediaLive User Guide. 
A/B forensic watermarking is available in all AWS Regions where AWS Elemental MediaLive is available.

## 핵심 요약

요약 미지원
