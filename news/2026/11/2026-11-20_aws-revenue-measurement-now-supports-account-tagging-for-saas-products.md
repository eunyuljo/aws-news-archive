---
title: "AWS Revenue Measurement now supports Account Tagging for SaaS Products"
date: "2026-11-20"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/revenue-measurement-account-tagging/"
tags: ["General", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Revenue Measurement now supports Account Tagging for SaaS Products

**날짜:** 2026년 11월 20일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/revenue-measurement-account-tagging/

## 내용

AWS Revenue Measurement (previously Partner Revenue Measurement) provides measurement of AWS consumption driven by Partner solutions. Today, AWS announces Account Tagging for SaaS Products for AWS Revenue Measurement. Partners can now measure the AWS revenue impact of their SaaS solutions by tagging the AWS accounts that host them, instead of tagging individual resources. 
Until now, Partners with SaaS listings measured that impact through Resource Tagging, User Agent strings, or AWS Marketplace Metering. With Account Tagging for SaaS products, a Partner uses AWS Organizations to tag partner-owned member accounts dedicated to a single SaaS product. The tag key is aws-apn-id-&lt;partner-central-aws-account-id&gt; and the tag value is pc:&lt;AWS Marketplace product-code&gt;. AWS Revenue Measurement then attributes all eligible AWS consumption in each tagged account to that product. 
Account Tagging for SaaS Products is available for products with a SaaS listing on AWS Marketplace. Each tagged account must be dedicated to one product. Partners whose products share an account can continue to use Resource Tagging, User Agent string, or Identity Tagging. AWS Revenue Measurement is generally available in all commercial regions. To learn more about implementing AWS Revenue Measurement, review the onboarding guide for more information.

## 핵심 요약

요약 미지원
