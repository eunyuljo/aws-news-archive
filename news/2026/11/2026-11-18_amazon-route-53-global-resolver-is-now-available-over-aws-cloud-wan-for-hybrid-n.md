---
title: "Amazon Route 53 Global Resolver is now available over AWS Cloud WAN for hybrid networks"
date: "2026-11-18"
service: "Route53"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-global-resolver-cloud-wan/"
tags: ["Route53", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon Route 53 Global Resolver is now available over AWS Cloud WAN for hybrid networks

**날짜:** 2026년 11월 18일
**서비스:** Route53
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-global-resolver-cloud-wan/

## 내용

Amazon Route 53 Global Resolver now supports anycast DNS resolution for private connections managed through your AWS Cloud WAN configuration. This enables organizations with hybrid networks to resolve DNS queries to public and private domains over existing AWS Direct Connect or AWS VPN connections, with automatic multi-region failover for high availability. 
Previously, customers had to either deploy and manage separate Resolver endpoints in each AWS Region and customer location, with no automatic failover between AWS Regions, or use Global Resolver with internet-reachable anycast IPs, making it hard for clients without internet access or those restricted by compliance requirements to take advantage of Global Resolver's anycast DNS resolution. With this launch, customers with clients configured with private connectivity over your Cloud WAN network get all the benefits of Global Resolver: automatic regional failover for higher availability, centralized DNS filtering with Route 53 DNS Firewall to prevent DNS-based data exfiltration, and simplified query resolution of both public internet domains and private domains (hosted on Route 53). 
You can get started by enabling Global Resolver, for two or more AWS Regions, and associating it with your Cloud WAN network configuration. You can select one or more privately routable IP addresses (IPv4, IPv6) that do not conflict with addresses already in use in your Cloud WAN and define DNS Views to specify which private hosted zones and DNS filtering rules apply to your Cloud WAN segments. Then configure your on-premises clients to forward DNS queries to the private IP address configured with your Global Resolver. 
This feature is available in AWS Regions where both Global Resolver and AWS Cloud WAN are available. To learn more about Global Resolver, see the product page. To get started, see Route 53 Global Resolver Developer Guide.

## 핵심 요약

요약 미지원
