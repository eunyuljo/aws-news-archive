---
title: "AWS IAM Identity Center now supports optimistic locking for users and groups in its identity store"
date: "2026-10-20"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/iam-identity-store-optimistic-locking/"
tags: ["IAM", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center now supports optimistic locking for users and groups in its identity store

**날짜:** 2026년 10월 20일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/iam-identity-store-optimistic-locking/

## 내용

IAM Identity Center helps you configure the single sign-on experience of your workforce to AWS accounts and applications. You can now use optimistic locking for users and groups in the identity store, so that update and delete requests succeed only if the user or group hasn't changed since you last read it. This helps when multiple administrators or automated workflows modify the same user or group at nearly the same time, where previously one write could silently overwrite another.
 
 
 Each user and group now has a Revision value that changes every time the user's or group's attributes are modified, including through SCIM provisioning, Active Directory sync, or the IAM Identity Center console. Create, describe, update, and list operations return the current Revision, and you can pass it on a later UpdateUser, UpdateGroup, DeleteUser, or DeleteGroup request. The request succeeds only if the supplied Revision matches the current Revision. Otherwise, it returns a ConflictException, so your workflow can re-read the user or group and retry with the latest values.
 
 
 Providing a Revision is optional. Requests that omit it behave as before, so existing integrations continue to work without changes. Conditional requests are supported through the Identity Store API, not the SCIM endpoint. Group membership operations don't accept a Revision, and adding or removing members doesn't change the Revision of the user or the group. This capability is available in all AWS Regions where IAM Identity Center is available. IAM Identity Center is provided at no additional cost.
 
 
 To learn more about IAM Identity Center, visit the product detail page. To get started, see UpdateUser in the Identity Store API Reference.

## 핵심 요약

요약 미지원
