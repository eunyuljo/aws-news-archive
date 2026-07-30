---
title: "AWS WAF adds pre-parse text transformations and new text transformations"
date: "2026-07-30"
service: "WAF"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-waf/"
tags: ["WAF", "2026", "new-region"]
nav_exclude: true
---

# AWS WAF adds pre-parse text transformations and new text transformations

**날짜:** 2026년 07월 30일
**서비스:** WAF
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-waf/

## 내용

Today, AWS WAF adds pre-parse text transformations for query arguments and ten new text transformations for use in any rule statement. Both help you normalize request content so that AWS WAF inspects requests the same way your application interprets them. 
Pre-parse text transformations normalize a raw query string before AWS WAF parses it into key-value pairs, closing HTTP parameter pollution and parser differential evasion gaps. You can chain up to ten transformations, including URL decode, Combine Duplicate Query Arguments by Comma, and Replace Semicolons with Ampersands, then layer standard post-parse transformations on top within a single rule statement. 
The new text transformations give you more ways to normalize content before inspection, including industry-standard options such as Uppercase, Trim, Remove Whitespace, and SHA256, plus operating-system-aware command line and JavaScript decoding functions developed by the Amazon Threat Research Team. 
Each new transformation consumes 10 WCUs, with no additional charge beyond standard AWS WAF pricing, and is available in all AWS Regions. To get started, see the following resources: 
 
 Pre-parse text transformations in AWS WAF:&nbsp;https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-preparse-transformation.html  
 
 
 Text transformations in AWS WAF: https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-transformation.html  
 
 
 Getting started with AWS WAF: https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html

## 핵심 요약

요약 미지원
