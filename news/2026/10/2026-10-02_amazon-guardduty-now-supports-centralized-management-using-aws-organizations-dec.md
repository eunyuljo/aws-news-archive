---
title: "Amazon GuardDuty now supports centralized management using AWS Organizations declarative policies"
date: "2026-10-02"
service: "GuardDuty"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/guardduty-org-enablement-policies/"
tags: ["GuardDuty", "2026", "new-region"]
nav_exclude: true
---

# Amazon GuardDuty now supports centralized management using AWS Organizations declarative policies

**날짜:** 2026년 10월 02일
**서비스:** GuardDuty
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/guardduty-org-enablement-policies/

## 내용

Amazon GuardDuty now supports AWS Organizations declarative policies, enabling you to centrally enable GuardDuty threat detection across every account and Region in your AWS organization. Using an organization policy, you can now apply a centrally managed GuardDuty enablement configuration. The configuration applies to existing accounts and is automatically maintained as new accounts join your organization.
Enabling GuardDuty across all relevant accounts and Regions helps ensure comprehensive threat detection coverage. Previously, keeping enablement aligned across a large multi-account, multi-Region environment meant configuring GuardDuty's enablement settings separately in each Region, which could drift over time. Now you can define a central GuardDuty policy from your delegated administrator account that sets an enablement baseline across your organization (at the organization root, OUs, or individual accounts). The policy supports a default configuration that applies in every Region where GuardDuty is available, as well as per-Region overrides for Regions that require different enablement. Enablement set by a policy cannot be overridden via the GuardDuty console or API.
GuardDuty declarative policy support is available in all AWS commercial Regions and the AWS GovCloud (US) Regions. To get started, make sure the delegated administrator has permission to manage GuardDuty policies. Then, sign in to the GuardDuty console and choose Organization policies, or create a policy programmatically using AWS Organizations APIs. To learn more, see Managing accounts using organization policies in the Amazon GuardDuty User Guide and Amazon GuardDuty policies in the AWS Organizations User Guide.

## 핵심 요약

요약 미지원
