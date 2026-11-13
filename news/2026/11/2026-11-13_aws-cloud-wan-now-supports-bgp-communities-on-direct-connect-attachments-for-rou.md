---
title: "AWS Cloud WAN now supports BGP communities on Direct Connect attachments for routing policy"
date: "2026-11-13"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloud-wan-bgp-community-directconnect/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# AWS Cloud WAN now supports BGP communities on Direct Connect attachments for routing policy

**날짜:** 2026년 11월 13일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloud-wan-bgp-community-directconnect/

## 내용

AWS Cloud WAN now supports BGP communities on Direct Connect attachments, enabling advanced routing controls for enterprise hybrid networks. Previously, Cloud WAN Routing Policy evaluated BGP communities only on Site-to-Site VPN and Connect attachments. Now, customers can tag routes with routing intent on-premises, apply filtering and path preference rules inside Cloud WAN, and propagate communities back to their on-premises routers over Direct Connect. 
With this capability, enterprises can simplify hybrid network orchestration by signaling routing policies dynamically from on-premises environments. Customers can match community tags to filter production versus disaster recovery traffic, prioritize preferred paths, or restrict regional propagation. This eliminates the need for VPN overlay workarounds and manual policy replication, reducing operational complexity and misconfiguration risk. 
BGP community support on AWS Cloud WAN Direct Connect attachments is available in all AWS Regions where both AWS Direct Connect and AWS Cloud WAN are available. For the complete list of available Regions, see the Cloud WAN Routing Policies documentation.

## 핵심 요약

요약 미지원
