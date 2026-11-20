---
title: "AWS Network Firewall launches explicit proxy functionality and NAT Gateway association"
date: "2026-11-20"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-proxy-nat-gateway/"
tags: ["EKS", "2026", "GA", "security"]
nav_exclude: true
---

# AWS Network Firewall launches explicit proxy functionality and NAT Gateway association

**날짜:** 2026년 11월 20일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-proxy-nat-gateway/

## 내용

You can now associate AWS Network Firewall with NAT Gateway and use it both as an explicit proxy and a transparent firewall with native network address translation. You can use this capability with existing Network Firewall features to filter traffic to and from your applications and prevent data exfiltration and malware injection.
AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention service for your VPC. Customers use it to filter their traffic and secure AWS resources. With this launch, you can configure Network Firewall with native NAT Gateway association and use it for both explicit proxy and routed filtering functionalities. Both these functionalities are governed by a single security policy that you maintain centrally. This capability works with existing Network Firewall features including managed rule groups from Amazon or Marketplace, active threat defense, Geo-IP filtering, URL and domain category filtering, container attribute-based rules for Amazon EKS and Amazon ECS, etc. You can access Network Firewall from any VPC in your environment, even the ones with overlapping IP CIDR space, using VPC endpoints. Your traffic reaches the firewall via the VPC endpoint and the filtered traffic exits directly from the NAT Gateway using its IP address.
This capability is available in US East (N. Virginia), US West (Oregon), US East (Ohio), US West (N. California), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Europe (Stockholm), Asia Pacific (Thailand), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Mumbai), Asia Pacific (Malaysia), Europe (Spain). To learn more about Network Firewall proxy and NAT Gateway association, please visit Network Firewall documentation and pricing page

## 핵심 요약

요약 미지원
