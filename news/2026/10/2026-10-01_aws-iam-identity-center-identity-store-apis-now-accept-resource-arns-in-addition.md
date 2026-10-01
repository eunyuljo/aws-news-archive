---
title: "AWS IAM Identity Center Identity Store APIs now accept resource ARNs in addition to resource IDs"
date: "2026-10-01"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/iam-identity-center-apis-arns/"
tags: ["IAM", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center Identity Store APIs now accept resource ARNs in addition to resource IDs

**날짜:** 2026년 10월 01일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/iam-identity-center-apis-arns/

## 내용

AWS IAM Identity Center's Identity Store APIs now accept the Amazon Resource Name (ARN) for a user, group, group membership, or identity store anywhere the APIs previously accepted the resource ID. ARN support is additive and existing integrations continue to work unchanged.
If you build on the Identity Store APIs, you may already hold resource ARNs — for example, from IAM policy evaluation, CloudTrail events, or cross-service integrations. Previously, you had to strip the ARN down to the resource ID before calling Identity Store APIs. With this change, you can pass either form directly, simplifying application code and eliminating potential parsing errors.
The change applies to every request identifier field across the Identity Store API surface. Responses continue to return resource IDs as they did before. Malformed or wrong-resource-type ARNs return a ValidationException.
This capability is available in all AWS Regions where AWS IAM Identity Center is offered, at no additional cost. To learn more, see the Identity Store API Reference.

## 핵심 요약

요약 미지원
