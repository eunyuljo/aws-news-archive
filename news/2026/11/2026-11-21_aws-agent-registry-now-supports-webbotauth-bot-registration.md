---
title: "AWS Agent Registry now supports WebBotAuth bot registration"
date: "2026-11-21"
service: "WAF"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/agent-registry-webbotauth-support/"
tags: ["WAF", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Agent Registry now supports WebBotAuth bot registration

**날짜:** 2026년 11월 21일
**서비스:** WAF
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/agent-registry-webbotauth-support/

## 내용

AWS Agent Registry now supports registering WebBotAuth (WBA) bots as a new record type, making it easier to verify legitimate bot traffic through a standardized protocol. Previously, organizations lacked a standardized way to distinguish verified bots from malicious traffic. Now, bots can prove domain ownership through WebBotAuth, and you can integrate this verification with AWS WAF Bot Control to write rules that combine verification status and bot identity.
This new capability gives content providers and application developers fine-grained control over which bots can access your resources. You can enhance security and improve traffic management by distinguishing legitimate bots from malicious actors. For example, you can allow WBA verified search engine crawlers while blocking unverified traffic or create custom access policies based on both bot identity and verification status.
This feature is available in all AWS Regions where AWS Agent Registry is available. To learn more, visit the AWS Agent Registry documentation and the AWS WAF Bot Control documentation.

## 핵심 요약

요약 미지원
