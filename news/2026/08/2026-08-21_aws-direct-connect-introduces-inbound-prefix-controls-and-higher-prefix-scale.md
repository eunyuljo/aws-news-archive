---
title: "AWS Direct Connect introduces inbound prefix controls and higher prefix scale"
date: "2026-08-21"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-direct-connect-new-prefix-controls"
tags: ["Config", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS Direct Connect introduces inbound prefix controls and higher prefix scale

**날짜:** 2026년 08월 21일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-direct-connect-new-prefix-controls

## 내용

Today, AWS Direct Connect announced inbound prefix controls, a new capability that lets you allocate and manage inbound route-prefix allocations for your private and transit virtual interfaces (VIFs) based on your workload's needs. You can now allocate up to 1,000 prefixes each for IPv4 and IPv6 on your VIFs on dedicated and hosted connections. 
Previously, Direct Connect VIFs accepted a maximum of 100 route prefixes advertised from your on-premises network to AWS on a private or transit VIF. If you had a larger or growing network, you had to architect around this ceiling, for example, by summarizing routes or segmenting across multiple VIFs or connections. With inbound prefix controls, you can allocate up to 1,000 prefixes to a single VIF and advertise your routes directly. 
Inbound prefix controls introduce new prefix capacity pools at the dedicated connection level and at the Direct Connect gateway (DXGW) level. When you create or update a VIF, you allocate a specific number of prefixes to it, and that allocation draws from the dedicated connection's pool and the DXGW's pool when you attach it. This lets you right-size prefix capacity per workload—for example, a large allocation for a transit VIF carrying many routes and a smaller allocation for a private VIF on the same connection. Connection pool sizes scale with connection speed, and link aggregation group (LAG) pools scale with the number of member connections. 
You can configure prefix allocations using the AWS Direct Connect console or CLI/API. Inbound prefix controls are available at no additional cost in all commercial AWS Regions where AWS Direct Connect is available, AWS GovCloud Regions (US-East and US-West), as well as the Amazon Web Services China (Beijing) Region, operated by Sinnet, and the Amazon Web Services China (Ningxia) Region, operated by NWCD. 
To learn more, see Inbound prefix controls for AWS Direct Connect in the AWS Direct Connect User Guide.

## 핵심 요약

요약 미지원
