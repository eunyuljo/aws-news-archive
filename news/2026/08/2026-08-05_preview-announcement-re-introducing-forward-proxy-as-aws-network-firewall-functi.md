---
title: "[Preview Announcement] Re-introducing Forward Proxy as AWS Network Firewall Functionality"
date: "2026-08-05"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-network-firewall-forward-proxy-preview/"
tags: ["EKS", "2026", "GA", "preview", "new-region", "security"]
nav_exclude: true
---

# [Preview Announcement] Re-introducing Forward Proxy as AWS Network Firewall Functionality

**날짜:** 2026년 08월 05일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-network-firewall-forward-proxy-preview/

## 내용

You can now use your Network Firewall with all its existing filtering capabilities and features as an explicit forward proxy.  On Nov 25, 2025, AWS introduced Network Firewall proxy in public preview to help customers exert centralized security controls against data exfiltration and malware injection. At the time, the Network Firewall proxy was introduced as a standalone product, separate from Network Firewall transparent firewall and used its own separate proxy security policy. Customers who tested it in preview shared that they want the Network Firewall proxy to maintain parity with Network Firewall’s existing set of capabilities and use the same security policy across the two functionalities. In keeping with customer feedback, we are reintroducing explicit proxy as a functionality of Network Firewall. With this launch, you can configure Network Firewall with your existing Firewall policy in a new no-source-preservation deployment where it can be used as an explicit proxy with all its existing features including managed rule groups, active threat defense, Geo-IP filtering, URL and domain category filtering, container attribute-based rules for Amazon EKS and Amazon ECS, etc. You can create a single security policy and use it for both explicit proxy and transparent firewall functionalities.  Try out AWS Network Firewall in no-source-preservation deployment with proxy functionality in your test environment today in US East (Ohio) region. no-source-preservation Network Firewall is available for free during public preview. For more information, check no-source-preservation Network Firewall documentation.

## 핵심 요약

요약 미지원
