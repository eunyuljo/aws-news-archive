---
title: "AWS improves regional resiliency for root user sign-in"
date: "2026-09-16"
service: "CloudTrail"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/root-user-regional-resiliency/"
tags: ["CloudTrail", "2026", "new-region"]
nav_exclude: true
---

# AWS improves regional resiliency for root user sign-in

**날짜:** 2026년 09월 16일
**서비스:** CloudTrail
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/root-user-regional-resiliency/

## 내용

AWS root user sign-in is now served across US East (N. Virginia), US East (Ohio), and US West (Oregon), with sign-in traffic distributed across all three Regions. This change reduces reliance on US East (N. Virginia) and improves resiliency during service disruptions. AWS automatically routes your root user sign-in to a supported Region without requiring you to select a Region or change how you sign in. This improvement is available now for all AWS accounts. 
In AWS CloudTrail, ConsoleLogin events for root user sign-ins are recorded in the Region that processed the sign-in request. To maintain full visibility into root user sign-in activity, update your monitoring and alerting to cover US East (N. Virginia), US East (Ohio), and US West (Oregon). 
To learn more, see the AWS Sign-In documentation and the CloudTrail ConsoleLogin event reference.

## 핵심 요약

요약 미지원
