---
title: "AWS Quick now supports group assignments for custom permissions and limit profiles"
date: "2026-11-21"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-group-assignments-custom-permissions-limit-profiles/"
tags: ["General", "2026", "new-region"]
nav_exclude: true
---

# AWS Quick now supports group assignments for custom permissions and limit profiles

**날짜:** 2026년 11월 21일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-group-assignments-custom-permissions-limit-profiles/

## 내용

AWS Quick now supports assignments for custom permissions and limit profiles to groups from your enterprise identity provider (IdP).&nbsp;Administrators can now apply feature restrictions and per-user resource limits to IdP groups, in addition to the existing user, role, and account assignments. Organizations can align governance with their enterprise identity structure without maintaining assignments for individual users.  Administrators manage user, account or group assignments in the Quick administration console or through new policy assignment APIs. For example, an organization can assign its finance group a custom permissions profile that blocks members from creating agents, or apply Deny by Default so that, within selected feature categories, the group can use only capabilities an administrator explicitly allows. Administrators can also assign a limit profile to a group to set each member’s index capacity and agent hours. Quick enforces these limits automatically as users consume resources.  When group-level assignments apply to a user who belongs to multiple groups, Quick resolves overlapping assignments as follows: for custom permissions, a capability denied by any group stays denied, and for limit profiles, the user receives the highest value for each limit type across those groups.  Group assignments are available in Quick for Professional and Enterprise plans. For feature availability by AWS Region, see AWS Quick Regions. To learn more, see the custom permissions and limit profiles documentation.

## 핵심 요약

요약 미지원
