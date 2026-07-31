---
title: "IAM Policy Simulator moves to the IAM console and adds additional capabilities"
date: "2026-07-31"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/iam-policy-simulator-iam-console/"
tags: ["IAM", "2026", "new-region", "security"]
nav_exclude: true
---

# IAM Policy Simulator moves to the IAM console and adds additional capabilities

**날짜:** 2026년 07월 31일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/iam-policy-simulator-iam-console/

## 내용

AWS Identity and Access Management (IAM) announces a major update to IAM Policy Simulator, the tool you use to test and validate the permissions your IAM policies grant before you deploy them. This update changes the simulator in three ways: it now lives in the IAM console, it can test service control policies (SCPs), and it adds flexibility to model more of the scenarios that security and platform teams simulate in practice. 
IAM Policy Simulator is now part of the IAM console, replacing the standalone simulator site, so you can test policies in the same place you manage your identities and policies.&nbsp;You can also now include SCPs in your simulation to test how your organization's SCP hierarchy interacts with identity and resource policies, and through the API, test how condition keys such as Region restrictions and tag requirements affect the outcome. Finally, new flexibility lets you exclude specific policies to model "what if I remove this policy?" scenarios, and cross-account simulations now report per-policy decisions for identity and resource-based policies, with the matched statements returned for a denied request reflecting only the policies that drove the decision. Together, these changes help teams automate policy unit testing, detect over-permissive access, and validate guardrails with greater confidence. 
These features are available in all AWS Regions where IAM Policy Simulator is available. You can access IAM Policy Simulator in the IAM console by choosing Policy simulator in the navigation pane. 
To learn more, see the following resources: 
 
 Testing IAM policies with the IAM policy simulator  
 API reference on SimulatePrincipalPolicy and SimulateCustomPolicy

## 핵심 요약

요약 미지원
