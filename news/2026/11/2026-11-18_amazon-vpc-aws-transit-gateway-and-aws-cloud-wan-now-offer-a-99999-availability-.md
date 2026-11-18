---
title: "Amazon VPC, AWS Transit Gateway, and AWS Cloud WAN now offer a 99.999% availability SLA for cross-Region traffic"
date: "2026-11-18"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/vpc-tgw-cloudwan-99999-sla/"
tags: ["RDS", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon VPC, AWS Transit Gateway, and AWS Cloud WAN now offer a 99.999% availability SLA for cross-Region traffic

**날짜:** 2026년 11월 18일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/vpc-tgw-cloudwan-99999-sla/

## 내용

AWS now offers a 99.999% availability service level agreement (SLA) for cross-Region traffic over Amazon Virtual Private Cloud (Amazon VPC) cross-Region peering, AWS Transit Gateway, and AWS Cloud WAN, with a new capability called Multipath Resilience. Multipath Resilience makes it easier to improve the resilience of mission-critical applications that send traffic across Regions, such as payment processing, financial trading, telephony, and live media streaming. 
The AWS backbone is highly resilient and connects Regions over physically diverse fiber paths. When a path fails, such as during a fiber cut, the network's automatic sub-second rerouting moves traffic to a healthy path. In the rare event that such mechanisms do not resolve the issue in a timely manner, such as when there's a partial degradation, it might take minutes for connectivity to be reestablished. Some applications, such as payment processing, financial trading, telephony, and live media streaming, can't tolerate single-digit seconds interruptions, let alone minutes of unavailability. Until now, customers running these applications relied on workarounds, including modifying their applications and operating systems to split a single connection into multiple connections, or replicating data into every Region to avoid cross-Region calls. These workarounds add complexity and don't always work, because applications can't control which network paths their traffic takes. 
Now, when you turn on Multipath Resilience for a cross-Region VPC peering connection, cross-Region Transit Gateway peering attachment, or cross-Region traffic on Cloud WAN, the network sends copies of each packet across physically diverse paths. It delivers whichever copy reaches your resources in the destination Region first and discards the duplicates. If one path drops packets, a copy is already in flight on another path, so your applications stay connected without waiting for the network protocols to reroute. Multipath Resilience moves this work out of your applications and into the network. Your applications keep using a single connection, with no changes to application code or operating systems, and no need to duplicate data to keep calls within a single Region. 
Multipath Resilience is now generally available in US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), and Europe (Ireland). 
To learn more, visit the Multipath Resilience documentation. For SLA details, visit the Multipath Resilience SLA. For pricing, visit the Amazon VPC pricing page.

## 핵심 요약

요약 미지원
