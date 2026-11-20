---
title: "Amazon CloudFront adds IP based routing and connection logs to SaaS Manager"
date: "2026-11-20"
service: "CloudFront"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-ip-based-routing-connection-logging"
tags: ["CloudFront", "2026"]
nav_exclude: true
---

# Amazon CloudFront adds IP based routing and connection logs to SaaS Manager

**날짜:** 2026년 11월 20일
**서비스:** CloudFront
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-ip-based-routing-connection-logging

## 내용

Amazon CloudFront now allows web development and SaaS platforms to serve different tiers of customers on the same wildcard domain by using IP addresses to route them to the right configuration. For example, these platforms can serve premium and pro customers from dedicated Anycast static IP address lists, each with its own configuration, and serve free-tier customers on the shared CloudFront IP addresses, all under *.example.com. Additionally, these customers also have visibility into viewer connections with connection logging. 
Previously, CloudFront chose the configuration from the domain name alone, so the same domain always went to the same configuration. With address-based selection, you can register the same wildcard domain on several IP lists and send each list to its own tenant. Because you control which clients resolve to which IP list, you can shift traffic between your service tiers without your customers needing to make any changes. You can also serve IoT devices, embedded SDKs, and older TLS clients that connect by IP address without sending a domain name in the TLS handshake (Server Name Indication, or SNI). With viewer fallback, you choose a distribution to accept these connections, and CloudFront uses the Host header in each request to serve the right content. Connection logs now also record HTTPS connections to these tenants which helps you troubleshoot how clients connect. 
These features are available at all CloudFront edge locations. To learn more, see Address-based selection and Connection Logs in the Amazon CloudFront Developer Guide.

## 핵심 요약

요약 미지원
