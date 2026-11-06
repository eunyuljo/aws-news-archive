---
title: "IAM Roles Anywhere now supports automatic certificate revocation checking"
date: "2026-11-06"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/iam-roles-anywhere-cdp/"
tags: ["IAM", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# IAM Roles Anywhere now supports automatic certificate revocation checking

**날짜:** 2026년 11월 06일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/iam-roles-anywhere-cdp/

## 내용

AWS Identity and Access Management (IAM) Roles Anywhere now supports automatic revocation checking using certificate revocation list (CRL) distribution points (CDPs). This helps keep revocation checks in sync with your certificate authority (CA) and can help improve your security posture. When you enable this capability on a trust anchor, IAM Roles Anywhere reads the CDP URLs embedded in authenticating certificates, downloads the corresponding CRLs, and denies credential requests that use revoked certificates. 
Previously, to check revocation status, you had to import CRLs into IAM Roles Anywhere and re-import them each time your CA published an update, which added operational overhead. With this launch, IAM Roles Anywhere downloads CRLs from your CDPs and refreshes them periodically, so you no longer need to re-import them. You can use this capability with AWS Private Certificate Authority or your own public key infrastructure (PKI), provided your certificates include publicly accessible CDP URLs that meet the distribution point requirements. To enable it on a trust anchor, use the IAM Roles Anywhere console, AWS SDKs, or AWS CLI. 
This feature is available at no additional cost in all commercial AWS Regions. To learn more, see Automatic revocation checking with CRL distribution points in the IAM Roles Anywhere User Guide.

## 핵심 요약

요약 미지원
