---
title: "Amazon Route 53 Profiles now supports multiple Profiles per VPC"
date: "2026-11-10"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-profiles-multiple-per-vpc/"
tags: ["IAM", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon Route 53 Profiles now supports multiple Profiles per VPC

**날짜:** 2026년 11월 10일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-profiles-multiple-per-vpc/

## 내용

Amazon Route 53 Profiles now lets you associate more than one Profile with a VPC. Previously, a VPC could have only one Profile, so teams that managed Route 53 configurations separately (for example, security teams managing DNS Firewall rule groups while cloud infrastructure and network admin teams manage private hosted zones and Resolver forwarding rules) all had to share a single Profile and associate their private hosted zones, Resolver rules, and DNS Firewall rule groups with it. 
With this launch, you can now associate multiple Profiles with the same VPC and set a priority for every Profile. Route 53 evaluates a VPC's Profiles in priority order, starting with the lowest number, so you can keep shared Route 53 configurations in one Profile and team-specific configurations in another without merging them, while assigning them the right priority. Combined with the granular IAM permissions launched in March 2026, multiple Profiles per VPC improves security posture by letting each team own and manage its own Profile with least-privilege permissions. 
This capability is available in all AWS Regions where Route 53 Profiles is available. 
Each Profile-VPC association is billed at standard Route 53 Profiles pricing. For details, see Amazon Route 53 pricing. To learn more, see Route 53 Profiles in the Amazon Route 53 Developer Guide.

## 핵심 요약

요약 미지원
