---
title: "AWS Transit Gateway and AWS Cloud WAN now support 1:1 NAT"
date: "2026-10-24"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-transit-gateway-cloud-wan-1-1-nat/"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# AWS Transit Gateway and AWS Cloud WAN now support 1:1 NAT

**날짜:** 2026년 10월 24일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-transit-gateway-cloud-wan-1-1-nat/

## 내용

AWS Transit Gateway and AWS Cloud WAN now provide managed one-to-one network address translation (NAT) directly on their attachments, through integration with Regional Private NAT Gateway. This enables customers to connect private networks that share the same IP address ranges without renumbering either network, deploying a NAT appliance, or writing return-traffic rules. 
Networks with overlapping Classless Inter-Domain Routing (CIDR) blocks have long been unable to communicate, a common blocker during mergers and acquisitions, when connecting partner networks over AWS Site-to-Site VPN, in multicloud connectivity, and when independently provisioned VPCs need to interconnect. Using this capability, customers can define address-translation rules on a AWS Transit Gateway or AWS Cloud WAN attachment, specifying the private IP range each source CIDR translates to, across Amazon VPC, AWS Site-to-Site VPN, AWS Direct Connect, and SD-WAN appliances connected through Transit Gateway Connect. Both services apply translation automatically in both directions, with no separate return-traffic rule and no NAT appliance to deploy. AWS operates, scales, and manages the NAT capability as part of the attachment. For example, if a customer acquires a business and both VPCs use 10.0.0.0/16, they translate one VPC's addresses to a non-overlapping range on its attachment and connect the networks immediately. Customers set it up in minutes using the AWS Management Console, AWS Command Line Interface (AWS CLI), AWS SDKs, and AWS CloudFormation, and monitor translated traffic through Amazon CloudWatch metrics and Amazon EventBridge events. 
AWS Transit Gateway and AWS Cloud WAN offer 1:1 NAT through Regional Private NAT Gateway in all AWS commercial&nbsp;regions where they operate. For full pricing details, see &nbsp;Amazon VPC pricing&nbsp;. To learn more, see the &nbsp;AWS Transit Gateway&nbsp; and &nbsp;AWS Cloud WAN&nbsp; product pages, and the AWS Transit Gateway&nbsp; and AWS Cloud WAN&nbsp; documentation.

## 핵심 요약

요약 미지원
