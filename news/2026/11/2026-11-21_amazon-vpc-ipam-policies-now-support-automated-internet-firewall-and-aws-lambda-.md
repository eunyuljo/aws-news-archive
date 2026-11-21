---
title: "Amazon VPC IPAM policies now support automated internet firewall and AWS Lambda Web Functions and MicroVMs"
date: "2026-11-21"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/vpc-ipam-policies-firewall-lambda/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon VPC IPAM policies now support automated internet firewall and AWS Lambda Web Functions and MicroVMs

**날짜:** 2026년 11월 21일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/vpc-ipam-policies-firewall-lambda/

## 내용

Amazon Virtual Private Cloud (VPC) IP Address Manager (IPAM) policies now support AWS Network Firewall automated internet firewall and AWS Lambda Web Functions and MicroVMs. You can centrally configure IPAM policies across AWS accounts and AWS Regions to allocate public IPv4 addresses to these resources from specific IPAM pools, such as Bring Your Own IP (BYOIP) addresses or Amazon-provided contiguous IPv4 blocks. This enables a stronger security posture, simplifies network and security operations, and can reduce public IPv4 costs when you use BYOIP. 
Many customers allowlist the public IPs of their AWS resources in network access control lists (ACLs) and firewalls. Previously, keeping these resources on allowlisted addresses depended on each application team. With this launch, you can define allocation rules for them alongside existing resource types, so security teams can add IP-based filters with confidence that these resources draw addresses from approved ranges. For Lambda Web Functions and MicroVMs, this covers the public IPv4 addresses used for outbound traffic through Lambda Network Connectors. If a pool runs out of addresses, resources fall back to Amazon-provided addresses. You can also share allocated ranges with partners through IPAM integration with AWS prefix lists. 
The feature is available in all AWS commercial Regions, in both the Free Tier and Advanced Tier of VPC IPAM. To learn more, see the IPAM policies documentation page and the IPAM documentation. For pricing details, see the IPAM tab on the Amazon VPC Pricing page

## 핵심 요약

요약 미지원
