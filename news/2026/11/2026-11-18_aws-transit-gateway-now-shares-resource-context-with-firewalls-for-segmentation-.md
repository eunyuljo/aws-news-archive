---
title: "AWS Transit Gateway now shares resource context with firewalls for segmentation policies"
date: "2026-11-18"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/transit-gateway-firewall-context-sharing/"
tags: ["Lambda", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Transit Gateway now shares resource context with firewalls for segmentation policies

**날짜:** 2026년 11월 18일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/transit-gateway-firewall-context-sharing/

## 내용

AWS Transit Gateway now supports context sharing with security services, such as attached firewalls, allowing you to use Amazon Virtual Private Clouds (VPCs), VPC subnets, VPC security groups, and transit gateway attachments in firewall policies alongside IP addresses. Until now, attached firewalls segmented traffic by IP address, which is hard to plan and maintain, or by resource tags, which firewalls periodically synchronize with IP addresses and can miss new workloads in between. With this feature, you can enforce segmentation based on how workloads and attachments are defined in AWS.
Transit Gateway embeds resource context in the traffic it sends to your firewall, which can enforce the right policy from the first packet. For example, you can apply threat protection to traffic between web-tier and database-tier security groups, block development VPCs from reaching production VPCs, apply a common inspection policy to traffic entering AWS through AWS Direct Connect and AWS Site-to-Site VPN attachments, or apply policies to short-lived AWS Lambda functions as soon as they send traffic, all without updating rules as IP addresses change.
AWS Network Firewall and Palo Alto Networks Software Firewalls support policies using resource context alongside IP-based rules. To get started, create a context store in AWS Network Manager and associate your transit gateways. The context store monitors resources connected to those transit gateways and shares their context with firewalls.
Context sharing with security services is available in all commercial AWS Regions where AWS Transit Gateway is available, except Middle East (Bahrain) and Middle East (UAE). It is also available in the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions.
To learn more, visit the AWS Transit Gateway product page and context sharing with security services documentation.

## 핵심 요약

요약 미지원
