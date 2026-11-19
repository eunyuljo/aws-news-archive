---
title: "Amazon Cognito now supports point-in-time recovery"
date: "2026-11-19"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-point-in-time-recovery/"
tags: ["RDS", "2026", "preview", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Cognito now supports point-in-time recovery

**날짜:** 2026년 11월 19일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-point-in-time-recovery/

## 내용

Amazon Cognito now supports point-in-time recovery (PITR), so you can restore the user data in a user pool to an earlier time. Amazon Cognito helps you implement secure sign-in and access control for users, AI agents, and microservices. Previously, you had to build and maintain your own export and restore process, and restored users received new identifiers and had to reset their passwords. 
With PITR, you choose a recovery point, preview how many users, groups, multi-factor authentication (MFA) settings, and passkeys the recovery will create, update, or delete, and then start or cancel the recovery. Recovered users keep their identifiers, passwords, MFA settings, and passkeys, so they can sign in without resetting their credentials. For example, if a script deletes or modifies users by mistake, you can restore the user data to the moment before it ran. 
PITR is enabled automatically for user pools on the Essentials and Plus feature plans at no additional charge. The recovery window is up to 1 day on Essentials and up to 14 days on Plus. You can initiate and manage a recovery using the AWS Management Console, the Amazon Cognito API, AWS Command Line Interface (AWS CLI), or AWS SDKs. PITR is available in all AWS Regions where Amazon Cognito is available. To learn more, see Point-in-time recovery in the Amazon Cognito Developer Guide.

## 핵심 요약

요약 미지원
