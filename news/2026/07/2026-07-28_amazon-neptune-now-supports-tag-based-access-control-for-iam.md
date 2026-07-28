---
title: "Amazon Neptune now supports tag-based access control for IAM"
date: "2026-07-28"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-neptune-tbac/"
tags: ["IAM", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Neptune now supports tag-based access control for IAM

**날짜:** 2026년 07월 28일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-neptune-tbac/

## 내용

Amazon Neptune Database now supports tag-based access control (TBAC) for IAM, enabling customers to use AWS resource tags and IAM principal tags as conditions in IAM policies and Service Control Policies (SCPs) to control access to Neptune data-plane operations. Neptune already provides robust security through VPC isolation, TLS encryption, and IAM authentication, but customers managing multiple clusters at scale needed a dynamic, attribute-based mechanism to enforce organizational access boundaries. TBAC addresses this by allowing administrators to govern cluster access without enumerating specific cluster ARNs in every policy.  With TBAC, IAM principals can only perform `neptune-db:*` actions against Neptune clusters whose tags match their own — for example, a principal tagged `Project=FraudDetection` is automatically restricted to clusters sharing that same tag. This eliminates lateral access risk within shared VPC environments, enforces team and environment-level isolation across projects, and supports federated identity workflows using SAML or OIDC session tags from external identity providers. Granular permissions like neptune-db:QueryLanguage can be used alongside TBAC for more fine-grained access control.  This feature is available in all AWS Regions where Amazon Neptune is available and requires Neptune engine version 1.2.0.0 or later with IAM authentication enabled.  To learn more about configuring tag-based access control for Amazon Neptune, including how to tag your DB clusters and IAM principals and deploy organization-wide guardrails using SCPs, visit the Amazon Neptune documentation.

## 핵심 요약

요약 미지원
