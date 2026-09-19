---
title: "AWS RTB Fabric now supports configurable Availability Zone affinity"
date: "2026-09-19"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-rtb-fabric-configurable-availability-zone-affinity/"
tags: ["Config", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS RTB Fabric now supports configurable Availability Zone affinity

**날짜:** 2026년 09월 19일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-rtb-fabric-configurable-availability-zone-affinity/

## 내용

AWS RTB Fabric now supports configurable Availability Zone (AZ) affinity for responder gateways. With this capability, you can configure how your partners connect to your responder gateway: either in their own Availability Zone or to any Availability Zone that the gateway spans. This launch helps advertising technology (AdTech) companies use their infrastructure more efficiently—with no extra charges on RTB Fabric. 
Demand-side platforms (DSPs) and supply-side platforms (SSPs) run their bidding systems across multiple Availability Zones. Previously, AWS RTB Fabric sent each request to available gateway capacity in the requester's own Availability Zone (AZ), so capacity in other AZs could go unused. Now you can set a client routing policy to control this: prefer the requester's own AZ to avoid added latency of crossing a boundary, or use every AZ that the responder gateway spans to give each requester access to more gateway capacity. Configurable Availability Zone affinity is available in all AWS Regions where AWS RTB Fabric is available.&nbsp;See the AWS RTB Fabric&nbsp;User Guide for fleet requirements before enabling. 
AWS RTB Fabric helps you connect with your AdTech partners such as Amazon Ads, GumGum, Kargo, MobileFuse, Sovrn, TripleLift, Viant, Yieldmo, and more in three steps while delivering single-digit millisecond latency through a private, high-performance network environment. RTB Fabric reduces standard cloud networking costs by up to 80% and does not require upfront commitments. AWS RTB Fabric is generally available in the following AWS Regions: US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (Ireland). See the&nbsp;AWS RTB Fabric Product Page to learn more.

## 핵심 요약

요약 미지원
