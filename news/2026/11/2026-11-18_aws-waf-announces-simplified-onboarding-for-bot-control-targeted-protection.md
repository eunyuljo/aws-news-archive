---
title: "AWS WAF announces simplified onboarding for Bot Control targeted protection"
date: "2026-11-18"
service: "CloudFront"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-waf-bot-control-onboarding/"
tags: ["CloudFront", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# AWS WAF announces simplified onboarding for Bot Control targeted protection

**날짜:** 2026년 11월 18일
**서비스:** CloudFront
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-waf-bot-control-onboarding/

## 내용

Today, AWS WAF announces a simplified console experience for Bot Control at the targeted inspection level. A single setting, Targeted bot control, turns on targeted protection for your Amazon CloudFront distributions with the configuration AWS recommends. It comes with two additions to the Bot Control managed rule group: bot confidence levels, which summarize the targeted detections on each request as High, Medium, or Low, and a LATEST version that keeps you on the newest detections automatically. Together, they help you protect your applications against sophisticated and AI-powered bots without writing label match rules or changing application code. 
The targeted inspection level uses machine learning and client-side signals to detect evasive bots. Previously, acting on those signals meant integrating the AWS WAF JavaScript SDK into every page, learning dozens of labels, and writing label match rules to combine them. Now, the rule group combines the detections into one confidence level per request, with one rule per level, and the Targeted bot control setting adds the rule group, applies the recommended action for each level, sets the version to LATEST, and turns on automatic SDK integration so CloudFront adds the SDK to your pages. You can change any action or start in Count. 
The Targeted bot control setting is available today for protection packs (web ACLs) used with Amazon CloudFront. Bot confidence levels and the LATEST version are available in all AWS Regions where AWS WAF Bot Control is available. Standard pricing for the targeted inspection level applies, with no additional charge for the setting or automatic SDK integration. To get started, open the AWS WAF console. To learn more, see Turning on Targeted bot control and Bot confidence levels in the AWS WAF Developer Guide, and read the AWS Security Blog post.

## 핵심 요약

요약 미지원
