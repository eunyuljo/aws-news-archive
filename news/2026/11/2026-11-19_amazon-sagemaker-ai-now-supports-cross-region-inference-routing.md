---
title: "Amazon SageMaker AI now supports cross-Region inference routing"
date: "2026-11-19"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-cross-region-routing/"
tags: ["CloudWatch", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI now supports cross-Region inference routing

**날짜:** 2026년 11월 19일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-cross-region-routing/

## 내용

Today, Amazon SageMaker AI announces cross-Region inference routing, which helps keep inference applications available when a region runs short of capacity by sending requests to endpoints deployed in other AWS Regions and AWS accounts. Models served on accelerated instances can reach capacity limits in a single Region, and an unhealthy endpoint can lead to throttling and errors for end users. Previously, teams had to build and maintain their own routing, health checks, and retry logic across Regions.  With cross-Region inference routing in SageMaker AI, developers create an inference router, register the real-time endpoints, asynchronous endpoints, and inference components they already run, and point their applications at the router. The router prefers endpoints in its own Region, shifts new requests to healthy destinations in other Regions as errors rise, and returns traffic gradually after the local endpoint recovers. Existing endpoints, models, and containers do not change. Endpoint owners stay in control: an endpoint policy determines which routers in other accounts can use an endpoint, and an optional cross-Region traffic cap reserves capacity for the endpoint’s local callers. Each real-time response identifies the endpoint that served the request and the reason, and router metrics in Amazon CloudWatch show where traffic went.  Cross-Region inference routing is available for real-time inference in 32 commercial AWS Regions, and for asynchronous inference in 25 Regions. There is no additional charge for cross-Region inference routing. Customers pay standard SageMaker AI pricing for the endpoints that serve requests and standard Amazon CloudWatch rates for router metrics. To learn more, see the Amazon SageMaker AI Developer Guide and SageMaker AI Deployment page.

## 핵심 요약

요약 미지원
