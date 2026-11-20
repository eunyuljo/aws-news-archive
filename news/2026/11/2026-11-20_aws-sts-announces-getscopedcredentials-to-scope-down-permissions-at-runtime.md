---
title: "AWS STS announces GetScopedCredentials to scope down permissions at runtime"
date: "2026-11-20"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/sts-getscopedcredentials/"
tags: ["IAM", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS STS announces GetScopedCredentials to scope down permissions at runtime

**날짜:** 2026년 11월 20일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/sts-getscopedcredentials/

## 내용

AWS Security Token Service (AWS STS) announces GetScopedCredentials, a new API that lets you scope down the permissions of existing temporary security credentials. With GetScopedCredentials, you can give your agents, sub agents and workloads their own set of credentials with only the permissions they need. 
You can call GetScopedCredentials with the temporary security credentials you already use to reduce permissions, session duration, or both. The resulting credentials preserve the caller's original identity, and permissions and session duration are monotonically narrowed so they never exceed those of the caller. Access to the API is controlled with IAM policies, and each call is logged to AWS CloudTrail for traceability. These capabilities make it easier to scope down permissions at runtime without changing how you manage identities. 
GetScopedCredentials is available in all AWS commercial Regions, AWS GovCloud (US) Regions, AWS European Sovereign Cloud (Germany) Regions and China Regions. To get started, see the GetScopedCredentials API reference and Permissions for GetScopedCredentials.

## 핵심 요약

요약 미지원
