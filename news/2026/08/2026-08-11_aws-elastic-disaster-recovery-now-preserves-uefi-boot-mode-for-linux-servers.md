---
title: "AWS Elastic Disaster Recovery now preserves UEFI boot mode for Linux servers"
date: "2026-08-11"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-drs-linux-uefi"
tags: ["Config", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Elastic Disaster Recovery now preserves UEFI boot mode for Linux servers

**날짜:** 2026년 08월 11일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-drs-linux-uefi

## 내용

AWS Elastic Disaster Recovery (AWS DRS) now preserves UEFI boot mode when recovering Linux source servers that boot with UEFI firmware. Previously, DRS launched these Linux servers in legacy BIOS mode, which could require extra configuration after recovery. Now your recovered Linux instances launch with the same UEFI boot mode as your source servers. This means your recovery instances more closely match your source environment, so applications that depend on UEFI boot behavior come back exactly as you expect — with no additional post-recovery steps. Boot mode preservation is automatic, with nothing to configure. 
This capability is available in all AWS Regions where AWS DRS is offered, at no additional cost. To learn more, visit the AWS Elastic Disaster Recovery User Guide.

## 핵심 요약

요약 미지원
