---
title: "Amazon Route 53 private hosted zones now support public DNS fallback"
date: "2026-11-21"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-public-dns-fallback/"
tags: ["CloudFormation", "2026", "new-region"]
nav_exclude: true
---

# Amazon Route 53 private hosted zones now support public DNS fallback

**날짜:** 2026년 11월 21일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-public-dns-fallback/

## 내용

Amazon Route 53 private hosted zones now support public DNS fallback. When a query for a name in your private hosted zone's domain doesn't match a record in the zone, Route 53 returns the answer from public DNS instead of a "name not found" (NXDOMAIN) error. Public DNS fallback is part of the Advanced Hosted Zones offering.
Until now, Route 53 treated an associated private hosted zone as fully authoritative for its domain, so queries for names that weren't in the zone returned NXDOMAIN. To resolve a few names privately, customers also had to copy every other record from their public zone into the private hosted zone and keep the two in sync. With public DNS fallback, you add only the names you need privately, and every other name resolves from your existing public DNS. For example, your private hosted zone for example.com points example.com to a private endpoint, while partner.example.com exists only in public DNS. Before, a lookup for partner.example.com returned NXDOMAIN. Now it resolves from public DNS.
To get started, create a private Advanced Hosted Zone or upgrade an existing private hosted zone, and then turn on public DNS fallback. You can use the Route 53 console, API, AWS CLI, AWS SDKs, or AWS CloudFormation.
Public DNS fallback is available in all AWS commercial Regions where Route 53 private hosted zones are available. To learn more, see Enabling public DNS fallback for a private hosted zone in the Route 53 Developer Guide and the Route 53 pricing page.

## 핵심 요약

요약 미지원
