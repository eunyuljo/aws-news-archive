---
title: "AWS Network Firewall now supports context-aware rules with AWS Transit Gateway-attached firewalls"
date: "2026-11-18"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-context-aware-rules/"
tags: ["VPC", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Network Firewall now supports context-aware rules with AWS Transit Gateway-attached firewalls

**날짜:** 2026년 11월 18일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-context-aware-rules/

## 내용

AWS Network Firewall attached to AWS Transit Gateway now allows you to use context-aware rules in your firewall policy. Network Firewall is a managed firewall and intrusion prevention service that inspects and filters traffic across your virtual private clouds (VPCs). With context-aware rules, you write rules that reference context from VPC resources instead of IP addresses. This makes it easier to apply consistent security controls as your organization grows. Existing rules automatically cover new workloads, so you don't need to update rules manually. 
Context-aware rules match traffic using VPCs, subnets, security groups, and Transit Gateway attachment identifiers, collectively known as context identifiers. You can reference context identifiers in a rule's source for any protocol, and in its destination for TCP-based protocols such as HTTP, TLS, and SSH. Flow and alert logs include context identifiers, so you can investigate activity based on context. 
Context-aware rules are available at no additional charge in all commercial and AWS GovCloud (US) Regions. For a full list of supported Regions, see the AWS Capabilities by Region page. 
To learn more, see the AWS Network Firewall product page and documentation.

## 핵심 요약

요약 미지원
