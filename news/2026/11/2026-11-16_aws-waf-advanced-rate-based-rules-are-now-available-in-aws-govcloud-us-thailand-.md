---
title: "AWS WAF advanced rate-based rules are now available in AWS GovCloud (US), Thailand, and Mexico"
date: "2026-11-16"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/waf-advanced-rate-rules-available/"
tags: ["CloudFormation", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS WAF advanced rate-based rules are now available in AWS GovCloud (US), Thailand, and Mexico

**날짜:** 2026년 11월 16일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/waf-advanced-rate-rules-available/

## 내용

AWS WAF advanced rate-based rules are now available in the Asia Pacific (Thailand), Mexico (Central), AWS GovCloud (US-East), and AWS GovCloud (US-West) Regions. Customers in these Regions can now aggregate requests using custom keys and choose a 1 or 2 minute evaluation window in addition to the existing 5 and 10 minute options, the same capabilities already available in other AWS Regions.
A rate-based rule counts requests and applies an action, such as Block or CAPTCHA, when the request rate exceeds a limit you set. Previously, rate-based rules in these Regions could aggregate requests only by IP address and used a 5 or 10 minute evaluation window. Now you can aggregate by request components such as HTTP headers, cookies, query strings, URI paths, HTTP methods, and label namespaces, and combine up to five of them into a composite key. For example, you can limit login attempts per IP address and User-Agent pair, or per session cookie, which helps against attacks spread across many IP addresses. A shorter evaluation window detects request floods sooner, and a longer window catches slower, sustained attacks.
You can configure these options in the AWS WAF console, the AWS CLI and SDKs, and AWS CloudFormation. There is no additional charge for these capabilities, and standard AWS WAF pricing applies. Advanced rate-based rules are now available in all commercial AWS Regions where AWS WAF is available and in the AWS GovCloud (US) Regions. To learn more, see Using rate-based rule statements in the AWS WAF Developer Guide.

## 핵심 요약

요약 미지원
