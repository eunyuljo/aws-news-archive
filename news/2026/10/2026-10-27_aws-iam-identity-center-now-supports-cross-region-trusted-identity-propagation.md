---
title: "AWS IAM Identity Center now supports cross-Region trusted identity propagation"
date: "2026-10-27"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-iam-identity-center-cross-region-tip/"
tags: ["IAM", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center now supports cross-Region trusted identity propagation

**날짜:** 2026년 10월 27일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-iam-identity-center-cross-region-tip/

## 내용

Trusted identity propagation carries a user's identity with their request, so AWS services can grant permissions based on who the user is and their underlying group associations, and log that user's access for auditing. With cross-Region support, this identity context can now be propagated to AWS services running in different AWS Regions, giving you greater flexibility in how you architect and deploy across AWS Regions. 
Customers often distribute workloads across AWS Regions for many reasons including separating the compute from the data it queries, to running workloads where capacity is available, or for disaster recovery and global scale. Previously, trusted identity propagation required all of the AWS services accessing a user's identity to reside in the same AWS Region. To reach services in another AWS Region, customers had to either grant access through broad IAM roles that cannot distinguish individual users or consolidate all their services into a single AWS Region. With cross-Region trusted identity propagation, a user's identity travels with the request across AWS Regions automatically, so you can grant access based on who the user is and their underlying group associations, and audit who accessed which resources, while preserving fine-grained access control for every individual user. 
Cross-Region trusted identity propagation is available at no additional cost in all AWS Regions where IAM Identity Center is available. For the list of Regions where IAM Identity Center is available, see AWS Capabilities by Region.&nbsp; For more information, see Trusted identity propagation in the IAM Identity Center User Guide.

## 핵심 요약

요약 미지원
