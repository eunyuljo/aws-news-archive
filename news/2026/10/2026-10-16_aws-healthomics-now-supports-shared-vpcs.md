---
title: "AWS HealthOmics now supports shared VPCs"
date: "2026-10-16"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/omics-workflows-shared-vpcs/"
tags: ["VPC", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS HealthOmics now supports shared VPCs

**날짜:** 2026년 10월 16일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/omics-workflows-shared-vpcs/

## 내용

AWS HealthOmics now supports sharing VPCs across accounts, enabling your workflows to access resources in Amazon Virtual Private Clouds (VPCs) managed by other AWS accounts with AWS Resource Access Manager (RAM).&nbsp;AWS HealthOmics is a HIPAA-eligible service that helps healthcare and life sciences customers accelerate scientific breakthroughs at scale with fully managed bioinformatics workflows.
With shared VPCs, customers can centralize networking administration by sharing subnets and security groups from a single VPC across multiple accounts in their organization, and HealthOmics then places each account's workflows directly into those shared subnets. With cross-account VPC sharing, multiple accounts run inside one centrally managed VPC, instead of duplicating endpoints across VPCs. Workflows in participating accounts can access data privately without separate VPC peering connections or duplicated VPC endpoints. Previously, customers with centralized networking had to create separate AWS PrivateLink VPC endpoints in each VPC and maintain individual route tables using VPC peering. Cross-account VPC sharing reduces infrastructure overhead and simplifies network management for organizations with centralized networking while allowing researchers and developers to run bioinformatics workflows in their own accounts.
Shared VPCs is available in all Regions where AWS HealthOmics is available: US East (N. Virginia, Ohio), US West (Oregon), Europe (Frankfurt, Ireland, London), Israel (Tel Aviv), and Asia Pacific (Singapore, Seoul, Tokyo). To get started, see the AWS HealthOmics User Guide.

## 핵심 요약

요약 미지원
