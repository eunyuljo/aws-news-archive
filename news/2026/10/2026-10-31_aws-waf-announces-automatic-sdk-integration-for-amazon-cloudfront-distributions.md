---
title: "AWS WAF announces automatic SDK integration for Amazon CloudFront distributions"
date: "2026-10-31"
service: "CloudFront"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-waf-automatic-sdk-integration-amazon-cloudfront/"
tags: ["CloudFront", "2026", "security"]
nav_exclude: true
---

# AWS WAF announces automatic SDK integration for Amazon CloudFront distributions

**날짜:** 2026년 10월 31일
**서비스:** CloudFront
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-waf-automatic-sdk-integration-amazon-cloudfront/

## 내용

AWS WAF announces automatic SDK integration for Amazon CloudFront distributions. When you enable it, CloudFront adds the script tag for the AWS WAF JavaScript SDK to the HTML it serves, with no change to your application code, build process, or deployment. The SDK supplies the client-side signals used by three AWS WAF managed rule groups: Bot Control at the targeted inspection level, Fraud Control account takeover prevention (ATP), and Fraud Control account creation fraud prevention (ACFP).  Previously, supplying those signals required you to add a script tag to every page of every application you wanted to protect, and to maintain that tag across releases. For teams running many applications, or serving pages produced by systems they do not control, this created recurring work and a common source of misconfiguration, where a protection was enabled in AWS WAF but the client-side integration was missing. Enabling automatic SDK integration on the web ACL protecting your CloudFront distribution removes that per-application work.  Automatic SDK integration is available for web ACLs that are used with Amazon CloudFront and contain at least one of those managed rule groups. You can configure it using the AWS Management Console, CLI, SDK, CDK, or CloudFormation. In the AWS WAF console, the setting appears with the managed rule group settings and is on by default for new web ACLs that you create with one of those rule group. When you create a web ACL programmatically, the setting is off by default. Web ACLs created before this release are unchanged.  There is no additional charge for automatic SDK integration. For requirements, limitations, and Content Security Policy guidance, see Automatic SDK integration for CloudFront distributions in the AWS WAF Developer Guide.

## 핵심 요약

요약 미지원
