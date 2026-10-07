---
title: "AWS Control Tower AFT now supports plan-only customization runs"
date: "2026-10-07"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-control-tower-aft/"
tags: ["Config", "2026", "preview", "new-region"]
nav_exclude: true
---

# AWS Control Tower AFT now supports plan-only customization runs

**날짜:** 2026년 10월 07일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-control-tower-aft/

## 내용

AWS Control Tower Account Factory for Terraform (AFT) now supports plan-only customization runs, giving administrators the ability to preview Terraform changes before applying them across their managed accounts.
 
 AFT is an open-source Terraform module that automates account provisioning and customization in AWS Control Tower environments. Previously, invoking customizations always triggered a full Terraform apply with no way to preview changes, making it difficult to validate expected outcomes or catch unintended configuration drift before a broad rollout. With plan-only runs, administrators can now trigger a Terraform plan for global and account customizations without applying any changes. This capability supports safe pre-rollout validation, drift detection, and integration into CI/CD review workflows. Plan-only runs are compatible across all AFT-supported Terraform distributions, including open source, Terraform Cloud, and Terraform Enterprise.
This feature is available in all AWS Regions where&nbsp;AWS Control Tower Account Factory for Terraform is supported. To get started, see the AFT documentation and the AFT 1.22.0 release notes for configuration details. For more information, see the AWS Control Tower User Guide.

## 핵심 요약

요약 미지원
