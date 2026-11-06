---
title: "AWS WAF AI traffic monetization now supports fiat payouts through Stripe"
date: "2026-11-06"
service: "CloudFront"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-waf-stripe-fiat-payouts/"
tags: ["CloudFront", "2026", "GA", "ai-ml"]
nav_exclude: true
---

# AWS WAF AI traffic monetization now supports fiat payouts through Stripe

**날짜:** 2026년 11월 06일
**서비스:** CloudFront
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-waf-stripe-fiat-payouts/

## 내용

AWS WAF AI traffic monetization now integrates with Stripe. Publishers, content owners, and API providers can collect stablecoin payments from AI bots and agents that settle in local currency directly to their Stripe balance. With this launch, customers can monetize agent access without holding stablecoins or managing a crypto wallet. Stripe is now available as a new payout method alongside existing stablecoin payouts. 
To get started, connect your Stripe account to AWS WAF through Stripe Connect in the AWS WAF console. Your existing pricing and agent policies work unchanged. When an agent requests protected content, AWS WAF returns an HTTP 402 response with the valid payment credential types that it accepts. Once the agent returns with a valid payment credential and makes the request again, the content is returned ungated. Revenue from all payment providers appears in the AWS WAF console revenue analytics. 
The Stripe integration is available at no additional charge to all AWS WAF customers using Amazon CloudFront, in all edge locations where AWS WAF web ACLs are associated with CloudFront distributions. Standard AWS WAF and Stripe processing fees apply. See AWS WAF pricing for details. 
To get started, visit the AWS WAF console or explore the AWS WAF Developer Guide.

## 핵심 요약

요약 미지원
