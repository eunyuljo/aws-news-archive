---
title: "AWS Network Firewall now supports Route 53 Resolved IP Validation"
date: "2026-10-22"
service: "Route53"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/network-firewall-route-53-ip-validation/"
tags: ["Route53", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Network Firewall now supports Route 53 Resolved IP Validation

**날짜:** 2026년 10월 22일
**서비스:** Route53
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/network-firewall-route-53-ip-validation/

## 내용

AWS Network Firewall now supports IP validation, extending domain-based filtering beyond HTTP/HTTPS to protocols such as SFTP and SSH. This new capability validates that a connection's destination IP address was resolved through your VPC's Amazon Route 53 VPC Resolver, closing security gaps where clients could bypass domain rules. 
This feature enables Network Firewall customers to implement domain filtering rules for any protocol, not just HTTP/HTTPS, providing more flexible security policies than IP-based rules alone. It simplifies protection against Server Name Identifier (SNI) spoofing by validating the IPs resolved by the Route 53 VPC Resolver against the SNI, ensuring traffic only reaches legitimately resolved destinations. Organizations can now enforce consistent domain-based security policies across all outbound traffic types, from web applications to file transfer protocols, without complex workarounds. Additionally, Route 53 Resolver DNS Firewall can be used with your VPC Resolver for extended DNS security. 
Resolved IP validation is available in all AWS commercial regions where AWS Network Firewall and Route 53 Resolver DNS Firewall are available, at no additional charge. For a full list of supported regions, visit the AWS Capabilities by Region page. 
To learn more, visit AWS Network Firewall product page and service documentation.

## 핵심 요약

요약 미지원
