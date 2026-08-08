---
title: "Amazon VPC IPAM now supports BGP route protection monitoring and delegated RPKI for BYOIP prefixes"
date: "2026-08-08"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-vpc-ipam-bgp-rpki-byoip/"
tags: ["RDS", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon VPC IPAM now supports BGP route protection monitoring and delegated RPKI for BYOIP prefixes

**날짜:** 2026년 08월 08일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-vpc-ipam-bgp-rpki-byoip/

## 내용

Amazon Virtual Private Cloud (VPC) IP Address Manager (IPAM) now supports BGP route protection monitoring and delegated Resource Public Key Infrastructure (RPKI) management for Bring Your Own IP (BYOIP) prefixes. Network administrators can centrally monitor BGP route protection and automate Route Origin Authorization (ROA) management across their organization. 
Using BGP route monitoring, you can view RPKI validity status, ROA strength, and route overlap detection for all BYOIP prefixes across accounts and regions from a single dashboard. Administrators can identify prefixes with invalid or missing ROAs, detect route overlaps that may indicate hijacking, and distinguish between strict and permissive ROA configurations. With Delegated RPKI, administrators perform a one-time setup with their Regional Internet Registry (ARIN, RIPE, APNIC, or LACNIC), after which IPAM automatically creates ROAs during BYOIP provisioning, renews them before expiration, and manages ROAs for on-premises prefixes. Before this feature, customers had to manually create and renew ROAs at their Regional Internet Registry (RIR), validate ownership through WHOIS or DNS records, and rely on third-party tools to monitor route security. 
&nbsp; 
The feature is available within Amazon VPC IPAM in all commercial AWS Regions, excluding the AWS GovCloud (US) Regions, and China (Beijing, operated by Sinnet) and China (Ningxia, operated by NWCD). To get started, please see the BGP route protection documentation. To learn more about IPAM, view the &nbsp;IPAM documentation&nbsp;. For details on pricing, refer to the IPAM tab on the &nbsp;Amazon VPC Pricing Page&nbsp;.

## 핵심 요약

요약 미지원
