---
title: "AWS Config announces managed conformance packs"
date: "2026-11-18"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-config-managed-conformance-packs"
tags: ["Config", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# AWS Config announces managed conformance packs

**날짜:** 2026년 11월 18일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-config-managed-conformance-packs

## 내용

AWS Config now offers managed conformance packs. AWS builds and maintains these packs for specific compliance and governance frameworks. When you deploy one, you choose a framework, and AWS Config evaluates your resources against it. AWS keeps the pack up to date as things change. When new AWS Config managed rules map to the framework's controls, or when the framework itself is revised, AWS updates your deployed pack automatically. Because AWS maintains a consistent pack definition in every supported Region, you can deploy the same framework across Regions without building or maintaining Region-specific rule sets. With managed conformance packs you no longer have to track framework changes or update rules yourself. 
Previously, to evaluate resources against a framework such as PCI DSS or SOC 2, you started from a sample conformance pack template, customized it for your environment, and then updated it yourself whenever new rules became available or the framework changed. Managed conformance packs remove that work, so your coverage stays current without manual template changes. Each pack includes the managed rules available in the Region where you deploy it and adds new rules as they become available there, so you don't need a separate template for each Region. You can set rule parameters to fit your environment. Compliance results and compliance scores appear in the AWS Config console alongside your other rules and conformance packs. 
Managed conformance packs cover frameworks including PCI DSS v4, SOC 2, NIST SP 800-53 Rev. 5, ISO/IEC 27001:2022, and CIS Controls, along with AI governance frameworks such as the EU AI Act and NIST AI RMF 1.0.&nbsp;For the full list, see the AWS Config documentation page. 
Managed conformance packs are available in all AWS commercial Regions except Middle East (UAE) and Middle East (Bahrain). For the full list of supported Regions, see AWS Capabilities by Region. Evaluations are billed at standard conformance pack evaluation rates. To get started, open the AWS Config console and choose Conformance packs. To learn more, see the AWS Config Developer Guide and the AWS Config pricing page.

## 핵심 요약

요약 미지원
