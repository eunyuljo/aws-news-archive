---
title: "Amazon CloudFront announces API support for flat-rate pricing plans"
date: "2026-09-04"
service: "CloudFront"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/cloudfront-flat-rate-pricing-plans-api/"
tags: ["CloudFront", "2026", "price-reduction"]
nav_exclude: true
---

# Amazon CloudFront announces API support for flat-rate pricing plans

**날짜:** 2026년 09월 04일
**서비스:** CloudFront
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/cloudfront-flat-rate-pricing-plans-api/

## 내용

Starting today, customers can subscribe and manage flat-rate pricing plans programmatically using the AWS CLI, AWS SDKs, CloudFormation, CDK, or the PricingPlanManager API. 
CloudFront flat-rate plans give you one monthly price covering global content delivery, WAF, DDoS, DNS, logging, and edge compute, with no usage-based overage charges regardless of traffic spikes or attacks. Previously, customers could only subscribe to flat-rate pricing plans using the console, which required manual steps when using the API or infrastructure as code (IaC) like CloudFormation to create and manage distributions. Now, customers can programmatically subscribe, upgrade, downgrade, and cancel flat-rate pricing plans using the API or IaC tools. 
Paid plans support an optional two-phase activation flow: you first create the plan, then approve it to begin billing. This prevents you from being committed to charges before you confirm, and makes the API well-suited for automated workflows and agents that provision infrastructure on your behalf. Free plans activate immediately and don’t require approval. To learn more, refer to the Getting started with the PricingPlanManager API. There are no additional fees for using the API to manage flat-rate pricing plans.

## 핵심 요약

요약 미지원
