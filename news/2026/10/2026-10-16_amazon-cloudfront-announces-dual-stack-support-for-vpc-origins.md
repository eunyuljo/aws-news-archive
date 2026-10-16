---
title: "Amazon CloudFront announces dual-stack support for VPC origins"
date: "2026-10-16"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-vpc-origin-dualstack/"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon CloudFront announces dual-stack support for VPC origins

**날짜:** 2026년 10월 16일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-vpc-origin-dualstack/

## 내용

Amazon CloudFront now supports end-to-end IPv6 delivery to origins inside your Amazon Virtual Private Cloud (Amazon VPC), with the new dual-stack VPC origins. With VPC origins, customers keep their Application Load Balancers (ALB), Network Load Balancers (NLB), and EC2 instances in private subnets that only their CloudFront distributions can reach. With dual-stack support, customers can now send IPv6 traffic all the way to these private origins to meet their IPv6 architecture and regulatory requirements, without exposing origins to the internet.
Previously, CloudFront supported dual-stack for public origins but connected to VPC origins over IPv4 only. Customers faced a tradeoff: move origins to public subnets for IPv6 and give up VPC origin security or keep them private and stay on IPv4. Now, with this launch, customers can configure their VPC origins as dual-stack and get end-to-end IPv6 without sacrificing security.
Dual-stack VPC origins are available in all AWS Commercial Regions where VPC origins are supported. The full list of supported Regions is available here. There is no additional cost for using dual-stack VPC origins. To learn more, visit CloudFront VPC origins.
&nbsp;

## 핵심 요약

요약 미지원
