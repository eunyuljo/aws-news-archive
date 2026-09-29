---
title: "Amazon Rekognition Face Liveness now returns Feedback Codes"
date: "2026-09-29"
service: "Rekognition"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/rekognition-liveness-feedback-codes/"
tags: ["Rekognition", "2026"]
nav_exclude: true
---

# Amazon Rekognition Face Liveness now returns Feedback Codes

**날짜:** 2026년 09월 29일
**서비스:** Rekognition
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/rekognition-liveness-feedback-codes/

## 내용

Amazon Rekognition Face Liveness now returns Feedback Codes that help customers understand why a liveness check&nbsp;received a low score and how users could retry successfully. The codes are returned in the GetFaceLivenessSessionResults API response, and they identify the specific conditions that contributed to the low score, such as poor lighting, face obstruction, closed eyes, or low video quality. Customers can surface these codes to their end users who can then make targeted corrections and retry with confidence. A single session can return multiple Feedback Codes at once, allowing users to resolve all contributing issues in one retry.&nbsp;This feature is especially useful in identity verification onboarding, re-authentication flows, and accessibility scenarios.
Amazon Rekognition Face Liveness verifies that the person in front of the camera is a real, live human (instead of a photo, video replay, mask, or deepfake) through a short, guided selfie-video check. It returns a confidence score, a reference image for face matching, and session audit images.&nbsp;
 
 
 Rekognition Face Liveness is available in US East (N. Virginia), US West (Oregon), Europe (Ireland), Asia Pacific (Tokyo, Mumbai, Malaysia, Thailand), and South America (São Paulo). To learn more, visit the Amazon Rekognition Face Liveness API documentation and Face Liveness FAQ.

## 핵심 요약

요약 미지원
