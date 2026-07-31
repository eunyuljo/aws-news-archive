---
title: "AWS Direct Connect now supports BGP route visibility on Virtual Interfaces"
date: "2026-07-31"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-direct-connect-bgp-visibility/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# AWS Direct Connect now supports BGP route visibility on Virtual Interfaces

**날짜:** 2026년 07월 31일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-direct-connect-bgp-visibility/

## 내용

AWS Direct Connect now provides Border Gateway Protocol (BGP) route visibility, allowing you to view the routes exchanged between AWS and your on-premises routers across your private, transit, and public virtual interfaces (VIFs). You can now see which routes AWS accepted from your router and which routes AWS is advertising to your router, along with their AS path and BGP community values. This visibility helps network administrators troubleshoot routing issues, verify route propagation, and monitor their hybrid network connectivity. 
With this feature, you can view accepted routes (routes AWS received from your router) and advertised routes (routes AWS sends to your router) directly in the Direct Connect console or programmatically using the ListVirtualInterfaceRoutes API action. Each route displays its prefix, address family, AS path, community values, and installation timestamp, giving you comprehensive insight into your routing topology. You can filter routes by prefix, AS path, community, or address family to quickly identify specific routing behaviors. This capability is particularly valuable when managing complex multi-region architectures, validating BGP policy configurations, or diagnosing unexpected traffic patterns. 
This feature is available in all AWS commercial Regions and the AWS China Regions (Beijing, operated by Sinnet, and Ningxia, operated by NWCD). 
To learn more about BGP route visibility, visit the AWS Direct Connect documentation or access the feature through the Direct Connect console. 
&nbsp;

## 핵심 요약

요약 미지원
