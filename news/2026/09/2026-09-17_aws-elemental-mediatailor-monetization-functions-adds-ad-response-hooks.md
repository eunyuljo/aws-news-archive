---
title: "AWS Elemental MediaTailor Monetization Functions adds ad response hooks"
date: "2026-09-17"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-elemental-mediatailor-functions-ad-response-hooks"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# AWS Elemental MediaTailor Monetization Functions adds ad response hooks

**날짜:** 2026년 09월 17일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-elemental-mediatailor-functions-ad-response-hooks

## 내용

AWS Elemental MediaTailor now supports two additional lifecycle hooks for monetization functions: post ad decision server (ADS) response, and pre manifest insertion. MediaTailor is a video service that personalizes and inserts ads into live and on-demand streams. Monetization functions run customer-defined logic at defined points in an ad-personalized playback session, removing the need for a middleware tier between MediaTailor and the ADS. 
The post ADS response hook runs after MediaTailor parses an ADS response and resolves all Video Ad Serving Template (VAST) wrappers, before ads are selected and transcoded. Customers use it to call a secondary ad source when the primary ADS returns less demand than the ad break can hold, remove ads that their content or brand policies do not permit, and add house ads or promotions from their own marketing systems. The pre manifest insertion hook runs at the last point before MediaTailor returns the ad pod to the viewer, and receives every newly personalized ad break in a single invocation. Customers use it as a final check on what is about to play, including inserting a personalized slate when a break cannot be filled any other way. Pre-built recipes in the MediaTailor console give customers a starting point for each of these use cases. Both hooks are fail-open: on a timeout, expression error, or resource limit, MediaTailor discards the function output and continues with default ad insertion, so viewer playback is unaffected. 
The new hooks are available in all AWS Regions where AWS Elemental MediaTailor is available. To learn more, see Monetization Functions in the AWS Elemental MediaTailor User Guide and the MediaTailor pricing page. To get started, sign in to the AWS Elemental MediaTailor console.

## 핵심 요약

요약 미지원
