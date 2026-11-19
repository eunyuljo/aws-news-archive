---
title: "AWS IAM account access manager is now even easier to deploy and use"
date: "2026-11-19"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/iam-account-access-manager-easier/"
tags: ["CloudFormation", "2026", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# AWS IAM account access manager is now even easier to deploy and use

**날짜:** 2026년 11월 19일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/iam-account-access-manager-easier/

## 내용

Deploying and using AWS Identity and Access Management (IAM) account access manager is now even easier: you can use AWS managed policies to enable and administer it; you can include it in your infrastructure-as-code (IaC) configurations; and its role assignments are integrated in a growing number of third-party identity and entitlement management solutions. 
Administering workforce access with account access manager requires permissions across several services, including AWS IAM Identity Center, AWS Organizations, AWS KMS, and AWS IAM. Previously, defining administrative access required hand-assembling multi-service IAM policies. The new AWS managed policies enable faster ramp up with broadly scoped job-aligned permissions for: 1/ Full administrator (AWSAccountAccessManagerAdministrator) - used to enable and manage account access manager in the AWS organization management account and to map users/groups to IAM roles; 2/ Entitlement Manager (AWSAccountAccessManagerEntitlementManager) - used to assign and remove user access without the ability to change service configuration; and 3/ ReadOnly (AWSAccountAccessManagerReadOnlyAccess) - used by auditors and compliance reviewers for visibility into user access. 
Account access manager streamlines assignment of IAM roles to workforce users and groups in IAM Identity Center, bringing together access management flexibility, user awareness, and a single point of federation. You can include account access manager in your IaC configurations managed through Terraform, Pulumi, or AWS CloudFormation. The entitlements that you assign with account access manager are reflected in your identity provider (IdP) and entitlements management system, including those offered by AWS partners Okta, PingIdentity, Cisco Duo, Apono, BeyondTrust, Britive, Sonrai Security, C1.ai, Lumos, and SailPoint. 
IAM account access manager is provided at no additional cost and available in all AWS Commercial Regions enabled by default. To learn more and get started, visit the AWS Identity and Access Management User Guide.

## 핵심 요약

요약 미지원
