---
title: "Amazon GameLift Servers adds CPU burstability for container fleets"
date: "2026-10-09"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-gamelift-servers-cpu-burstability"
tags: ["Config", "2026", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon GameLift Servers adds CPU burstability for container fleets

**날짜:** 2026년 10월 09일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-gamelift-servers-cpu-burstability

## 내용

Amazon GameLift Servers now supports CPU burstability for container fleets, giving game developers greater flexibility in how compute resources are allocated and consumed at runtime. Previously, container fleets relied on a fixed CPU value that simultaneously controlled both container packing density and imposed a hard runtime cap. This dual constraint forced developers to choose between efficient resource utilization and maintaining performance headroom for their game server workloads.
Game server workloads are inherently bursty, CPU demand stays low during most of a match but spikes sharply during physics calculations, AI processing, or collision detection. With CPU burstability, developers can now pack containers based on typical CPU needs while still allowing game server processes to burst into available idle instance CPU during peak demand moments. This opt-in feature is configured per container group definition, supports high-density deployments without sacrificing peak performance, and is included at no additional cost as part of standard container fleet pricing.
CPU burstability for Amazon GameLift Servers container fleets is available in all AWS Regions where container fleets are supported, excluding China Regions.
To learn more about CPU burstability for Amazon GameLift Servers container fleets, visit the Amazon GameLift Servers Developer Guide or explore the Amazon GameLift Servers product page.

## 핵심 요약

요약 미지원
