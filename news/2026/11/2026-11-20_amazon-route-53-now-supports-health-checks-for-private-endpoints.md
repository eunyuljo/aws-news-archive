---
title: "Amazon Route 53 now supports health checks for private endpoints"
date: "2026-11-20"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-private-endpoint-health-checks/"
tags: ["Lambda", "2026", "new-region"]
nav_exclude: true
---

# Amazon Route 53 now supports health checks for private endpoints

**날짜:** 2026년 11월 20일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-private-endpoint-health-checks/

## 내용

Amazon Route 53 now offers Private Endpoint Health Checks, enabling business-critical workloads that never touch the public internet, such as internal APIs, databases, and self-hosted nodes behind internal load balancers or in private subnets, to use native health monitoring and automatic DNS failover. Customers can health-check any reachable private target by IP address, domain, or port over HTTP, HTTPS, or TCP. Customers can associate these health checks with Route 53 DNS records across routing policies in private hosted zones, so Route 53 routes traffic only to healthy endpoints and manages failover automatically.&nbsp; 
 

 Previously, teams built custom control loops using Amazon CloudWatch alarms, AWS Lambda functions, and the Route 53 API to achieve DNS failover for private resources. With this approach, failover took several minutes and added operational burden. Detection and DNS failover with Private Endpoint Health Checks are designed to complete in seconds rather than minutes, the service is fully managed, and nothing is exposed to the public internet.&nbsp; 
 

 The feature supports on-premises and hybrid endpoints reachable from the VPC over AWS Direct Connect or AWS Site-to-Site VPN, enabling resilience patterns such as active-passive disaster recovery and cross-Region DR over AWS Transit Gateway or AWS Cloud WAN. Amazon Route 53 Private Endpoint Health Checks is available today in all AWS commercial regions. To learn more, visit the Amazon Route 53 Developer Guide and the Route 53 pricing page.&nbsp; 
 
&nbsp;

## 핵심 요약

요약 미지원
