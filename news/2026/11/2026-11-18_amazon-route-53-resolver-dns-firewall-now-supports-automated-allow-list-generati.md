---
title: "Amazon Route 53 Resolver DNS Firewall now supports automated allow-list generation"
date: "2026-11-18"
service: "Route53"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-dns-firewall-auto-allowlists/"
tags: ["Route53", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon Route 53 Resolver DNS Firewall now supports automated allow-list generation

**날짜:** 2026년 11월 18일
**서비스:** Route53
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-dns-firewall-auto-allowlists/

## 내용

Amazon Route 53 Resolver DNS Firewall now automatically generates domain allow-lists from your VPCs' observed DNS query traffic, helping you enforce least-privilege DNS access and reduce the risk of DNS-based data exfiltration.
Previously, implementing a least-privilege model required security teams to manually analyze DNS query logs to identify the domains their VPCs depend on before deploying allow-list rules. This created operational overhead and delayed enforcement of a deny-by-default (walled-garden) posture.
With automated allow-list generation, DNS Firewall analyzes DNS query traffic using a lookback window configurable from 1 hour to 7 days to create an allow-list of observed domains. It then continuously monitors DNS queries and flags newly observed domains, so you can review them before adding them to the allow-list. You can deploy the rule across multiple VPCs and accounts using AWS Firewall Manager or Route 53 Profiles.
This capability is available at no additional cost to DNS Firewall Advanced customers, in all AWS Regions where Route 53 DNS Firewall is supported, except in AWS GovCloud (US) and Amazon Web Services China Regions. To get started, use the Route 53 DNS Firewall console, AWS CLI, or API.
To learn more, visit the Amazon Route 53 Resolver DNS Firewall product page and the Route 53 DNS Firewall Developer Guide.

## 핵심 요약

요약 미지원
