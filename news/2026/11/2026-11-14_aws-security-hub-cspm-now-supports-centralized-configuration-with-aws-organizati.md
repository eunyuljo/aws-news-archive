---
title: "AWS Security Hub CSPM now supports centralized configuration with AWS Organizations declarative policies"
date: "2026-11-14"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-cspm-org-policies/"
tags: ["RDS", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS Security Hub CSPM now supports centralized configuration with AWS Organizations declarative policies

**날짜:** 2026년 11월 14일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-cspm-org-policies/

## 내용

AWS Security Hub CSPM now supports AWS Organizations declarative policies. You can use them to enable Security Hub CSPM across all accounts and Regions in your organization and to define which security standards and controls are enabled.
Policies can apply broadly to every account and Region, or target specific account and Region combinations. Declarative policies help keep each account's configuration aligned with its attached policy, which helps prevent configuration drift. You can also apply them automatically to new accounts, so each account starts with a baseline configuration as soon as it's created.
Declarative policies are now the recommended way to manage Security Hub CSPM across an organization. They align with how other security services, such as Amazon GuardDuty, Amazon Inspector, and AWS Security Hub allow customers to manage configuration of the service. They also provide more flexibility, such as configuring Region-specific settings. You can continue to use central configuration until you're ready to migrate. When you are, use the migration process in the Security Hub CSPM console. It converts your existing central configuration policies into declarative policies and applies them to the appropriate accounts and regions.
Declarative policies for Security Hub CSPM are available in all commercial, AWS GovCloud (US), and China Regions. To get started, see Migrating central configuration policies. To learn more, see Declarative policies in the AWS Security Hub CSPM User Guide and Security Hub CSPM policies in the AWS Organizations User Guide. To receive notifications about new Security Hub CSPM features and controls, subscribe to the Security Hub SNS topic. You can also try Security Hub CSPM at no cost for 30 days with the AWS Free Tier offering.

## 핵심 요약

요약 미지원
