---
title: "IAM Roles Anywhere now supports aliases to simplify workload configuration"
date: "2026-11-21"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/iam-roles-anywhere-alias/"
tags: ["IAM", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# IAM Roles Anywhere now supports aliases to simplify workload configuration

**날짜:** 2026년 11월 21일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/iam-roles-anywhere-alias/

## 내용

AWS Identity and Access Management (IAM) Roles Anywhere now supports aliases, which are readable names that you assign to trust anchors, profiles, and certificate revocation lists (CRLs). Your workloads can request temporary credentials using a trust anchor or profile alias Amazon Resource Name (ARN) instead of an ARN with a system-generated ID, and you can use alias ARNs in many of the operations that manage these resources. Aliases make configurations easier to read and review: an alias ARN that ends in alias/trust-anchor/production-ca can show which certificate authority (CA) a workload uses. 
Previously, workload configurations, such as credential helper settings in machine images and configuration management templates, referenced trust anchors and profiles by ARNs that contain system-generated IDs, which differ in every account and Region. With this launch, you can assign the same alias in each account and Region, so one configuration template works across them with only the account and Region values changed. To set an alias, specify an alias name when you create, import, or update a resource using the IAM Roles Anywhere console, AWS SDKs, or AWS CLI. 
This feature is available at no additional cost in all commercial AWS Regions, the AWS GovCloud (US) Regions, the China Regions, and the AWS European Sovereign Cloud (Germany) Region. To learn more, see Using aliases for trust anchors, profiles, and CRLs in the IAM Roles Anywhere User Guide.

## 핵심 요약

요약 미지원
