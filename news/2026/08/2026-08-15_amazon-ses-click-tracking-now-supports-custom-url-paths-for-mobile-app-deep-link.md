---
title: "Amazon SES click tracking now supports custom URL paths for mobile app deep linking"
date: "2026-08-15"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ses-supports-customurl-deeplinking"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# Amazon SES click tracking now supports custom URL paths for mobile app deep linking

**날짜:** 2026년 08월 15일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ses-supports-customurl-deeplinking

## 내용

Amazon Simple Email Service (SES)&nbsp;now makes it easier to support mobile deep linking with the new ses:custom-path HTML attribute. When you add this attribute to an &lt;a&gt; tag, SES carries your path segment through to the tracking URL, so mobile operating systems can match it to your app's Universal Links (iOS) or App Links (Android) configuration. This enables you to use mobile deep linking without disabling engagement tracking. 
This feature is available in all AWS Regions where Amazon SES is available. To use this feature, you need a custom redirect domain for click tracking with an Apple App Site Association (AASA) or Digital Asset Links verification file hosted on that domain. Then, add the ses:custom-path attribute to links in your HTML emails. 
To learn more, see Configuring custom domains to handle open and click tracking and the Amazon SES email sending metrics FAQs in the Amazon SES Developer Guide.

## 핵심 요약

요약 미지원
