---
title: "AWS WAF now supports a Salt Security managed rule group for API and MCP threat detection"
date: "2026-08-08"
service: "WAF"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-waf-salt-security-managed-rules/"
tags: ["WAF", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# AWS WAF now supports a Salt Security managed rule group for API and MCP threat detection

**날짜:** 2026년 08월 08일
**서비스:** WAF
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-waf-salt-security-managed-rules/

## 내용

AWS WAF now supports the Salt Security managed rule group, available through AWS Marketplace: Salt Managed Rules for AWS WAF - AI Agent &amp; API Security. This rule group gives AWS WAF customers detection and mitigation for API-focused attacks and for traffic from AI agents and Model Context Protocol (MCP) endpoints, without writing or maintaining custom rules.  The rule group detects common and complex API attack vectors, including credential brute force, excessive GraphQL queries, server-side request forgery (SSRF), prototype pollution, and JSON Web Token (JWT) anomalies. It identifies and labels traffic from Model Context Protocol (MCP) endpoints, blocks unauthenticated MCP access, and adds observability into MCP interactions in AWS WAF. The rule group also applies rate limiting to sensitive request parameters, such as user identifiers and email addresses, to help mitigate enumeration and abuse. To support detection and downstream analysis, it labels request attributes including authorization headers, user identifiers, and GraphQL queries.  You can subscribe to the rule group and add it to a web ACL directly in the AWS WAF console through AWS Marketplace, with no additional configuration. The rule group supports versioning, and pricing is set by Salt Security through AWS Marketplace. For a full list of supported Regions, visit the AWS Regional Services page.  To get started, visit the AWS WAF console or find the Salt Security rule group in AWS Marketplace. For more information, see the AWS WAF Developer Guide.

## 핵심 요약

요약 미지원
