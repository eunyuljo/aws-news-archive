---
title: "AWS IAM Identity Center's Identity Store now supports change notifications through Amazon EventBridge"
date: "2026-10-29"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-identity-store-change-notifications/"
tags: ["Lambda", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center's Identity Store now supports change notifications through Amazon EventBridge

**날짜:** 2026년 10월 29일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-identity-store-change-notifications/

## 내용

AWS IAM Identity Center's Identity Store now delivers real-time events to Amazon EventBridge when users, groups, or group memberships or the identity store itself is created, updated, or deleted. AWS IAM Identity Center Identity Store is a central repository that allows you to manage identities and access across AWS accounts and applications, serving as the identity source for AWS IAM Identity Center. This new capability helps you automatically respond to identity lifecycle events and support your security and compliance processes by detecting changes as they happen. 
With Identity Store change notifications, you can build automated workflows that respond to identity changes in your organization. For example, security teams can create EventBridge rules that trigger AWS Lambda functions to audit user provisioning activity, send alerts to security information and event management (SIEM) systems, or update access in downstream applications when users or groups change. Organizations that manage large workforces can also use this data to automate onboarding and offboarding when users are added to or removed from specific groups. 
Change notifications are available in all AWS Regions where IAM Identity Center is available, and events are sent in each enabled Region of your instance. For the list of Regions, see AWS capabilities by Regions. Change notifications are available at no additional cost beyond standard Amazon EventBridge usage charges. To learn more, see Event notifications in the AWS IAM Identity Center User Guide and Identity Store events in the Amazon EventBridge Events Reference.

## 핵심 요약

요약 미지원
