---
title: "The new AgentCore Runtime is now available in Amazon Bedrock AgentCore"
date: "2026-09-19"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/new-agentcore-runtime-generally-available"
tags: ["Bedrock", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# The new AgentCore Runtime is now available in Amazon Bedrock AgentCore

**날짜:** 2026년 09월 19일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/new-agentcore-runtime-generally-available

## 내용

Today, AWS announces the availability of&nbsp;the next generation of AgentCore Runtime, the serverless microVM compute within Amazon Bedrock AgentCore. The new Runtime delivers elastic memory management that reclaims unused memory throughout the session so you pay for actual usage rather than the peak, and consistent cold start times regardless of container image size or concurrency. You get the serverless model you already rely on: no pre-provisioning, scale to zero, hardware-enforced session isolation, and pay only for what you use - now with lower costs and faster starts. 
With the new Runtime, each session starts with a small, efficient memory profile. Additional memory is allocated on demand as the workload needs it, and memory that is no longer actively used is reclaimed rather than held until the session ends. For cold starts, the new Runtime prepares the agent environment once and snapshots it. Every new instance restores from that snapshot instead of repeating the full startup sequence, keeping start times consistent regardless of image size. In testing, the new Runtime delivered a P75 cold start of 1.9 to 2.0 seconds for container images from 200 MB to 2 GB, compared to 5.4–30 seconds with V1. 
The new AgentCore Runtime is available in the following regions: us-east-1, us-east-2, us-west-2, eu-west-1, and ap-northeast-1.&nbsp;To get started, set platformVersion to V2 when creating or updating a runtime. 
To learn more, visit the AgentCore Runtime documentation or the AWS News Blog. For pricing details, visit AgentCore pricing.

## 핵심 요약

요약 미지원
