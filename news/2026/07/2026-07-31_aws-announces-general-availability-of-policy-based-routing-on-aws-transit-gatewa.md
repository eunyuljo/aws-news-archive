---
title: "AWS announces general availability of Policy-Based Routing on AWS Transit Gateway"
date: "2026-07-31"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-transit-gateway-policy-based-routing/"
tags: ["VPC", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS announces general availability of Policy-Based Routing on AWS Transit Gateway

**날짜:** 2026년 07월 31일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-transit-gateway-policy-based-routing/

## 내용

AWS Transit Gateway now supports Policy-Based Routing (PBR), giving network administrators granular control over how traffic is forwarded across their AWS network. With PBR, forwarding decisions can be based on a combination of packet attributes including source and destination IP addresses, ports, and protocol rather than destination IP address alone.  Previously, customers needing traffic steering or workload isolation had to build multi-VPC architectures with additional routing hops, adding complexity and operational overhead. PBR eliminates this by extending Transit Gateway's native routing capabilities, enabling security architects and enterprise network teams to classify and direct traffic inline without extra infrastructure. Customers associate a policy table with a Transit Gateway attachment and define an ordered set of rules. Each rule classifies traffic and directs matching packets to a specified route table using first-match-wins logic. This supports use cases such as steering sensitive workloads through AWS Network Firewall or third-party inspection appliances, routing application traffic over AWS Direct Connect or AWS VPN paths based on source, port, or protocol, and isolating production and development environments into separate routing domains to limit lateral movement.  Policy-Based Routing for AWS Transit Gateway is available in all commercial AWS Regions where Transit Gateway is available. You can configure PBR using the AWS Management Console, AWS Command Line Interface (CLI), and the AWS Software Development Kit (SDK). PBR incurs no additional charge beyond standard Transit Gateway fees. To learn more about Policy-Based Routing for AWS Transit Gateway, visit the AWS Transit Gateway product page .

## 핵심 요약

요약 미지원
