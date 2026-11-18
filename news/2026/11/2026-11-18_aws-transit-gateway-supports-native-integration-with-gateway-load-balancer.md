---
title: "AWS Transit Gateway supports native integration with Gateway Load Balancer"
date: "2026-11-18"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/transit-gateway-gwlb-integration/"
tags: ["VPC", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Transit Gateway supports native integration with Gateway Load Balancer

**날짜:** 2026년 11월 18일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/transit-gateway-gwlb-integration/

## 내용

AWS Transit Gateway now supports network function attachments of type Gateway Load Balancer, simplifying the deployment and management of network security across your AWS network. 
With a network function attachment, you can connect your transit gateway to a Gateway Load Balancer VPC endpoint service that fronts firewalls and other security appliances without complex VPC configurations. Transit Gateway creates and manages the Gateway Load Balancer endpoints in the Availability Zones you choose, removing the need to create dedicated endpoint subnets and route tables. The endpoint service can be in another AWS account. 
Network function attachments also support context sharing with security services. Transit Gateway adds resource context to traffic sent to your firewall, including the transit gateway attachment, VPC, subnet, and security groups. Your firewall can use this context alongside IP addresses to enforce segmentation policies. 
This capability is available in all commercial AWS Regions where both AWS Transit Gateway and Gateway Load Balancer are available, except Middle East (Bahrain) and Middle East (UAE). It is also available in the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions. 
To get started, see Network function attachments in the AWS Transit Gateway Guide and visit the AWS Transit Gateway product page.

## 핵심 요약

요약 미지원
