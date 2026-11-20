---
title: "Amazon CloudFront simplifies domain moves and onboarding for SaaS Manager"
date: "2026-11-20"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-domain-moves-distribution-tenants"
tags: ["RDS", "2026", "price-reduction"]
nav_exclude: true
---

# Amazon CloudFront simplifies domain moves and onboarding for SaaS Manager

**날짜:** 2026년 11월 20일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-domain-moves-distribution-tenants

## 내용

Amazon CloudFront now lets web development platforms and SaaS providers move a customer's domain to their platform in a single request with no downtime, and serve requests to the domain while the TLS certificate is being configured. The CloudFront multi-tenant distributions allow these platforms to serve many customer domains from one shared configuration. Together, these features help move existing AWS customers to multi-tenant distributions without impacting their traffic. 
Previously, moving a domain that was already in use required disabling the original distribution, using a wildcard workaround, or contacting AWS Support. Now you can bring customer domains onto your multi-tenant setup as part of creating or updating a tenant. With the new OnDomainTakeover option, CloudFront checks domain ownership through DNS records and then moves one or more domains in a single request. This works within an AWS account or across accounts. If you add a domain before its certificate is issued, CloudFront serves it over HTTP until you attach a certificate. That gives you time to validate the domain with AWS Certificate Manager (ACM) or another certificate authority and attach the certificate once it's issued. 
These features are available in all edge locations at no additional cost. To learn more, see Move domains and Domains without a certificate in the Amazon CloudFront Developer Guide.

## 핵심 요약

요약 미지원
