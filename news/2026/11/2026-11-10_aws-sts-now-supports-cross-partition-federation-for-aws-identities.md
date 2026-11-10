---
title: "AWS STS now supports cross-partition federation for AWS identities"
date: "2026-11-10"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-sts-cross-partition"
tags: ["IAM", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS STS now supports cross-partition federation for AWS identities

**날짜:** 2026년 11월 10일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-sts-cross-partition

## 내용

AWS Security Token Service (AWS STS) now lets your workloads use their AWS Identity and Access Management (IAM) identity in one partition to get temporary credentials for an IAM role in a different partition, without storing long-term credentials, which can help improve your security posture. Partitions are groups of AWS Regions, such as the commercial and AWS GovCloud (US) Regions, and each partition has an independent instance of IAM, creating a hard boundary between them. Previously, organizations that run workloads across partitions commonly relied on long-term credentials, such as IAM user access keys, that don't expire automatically. 
With this launch, your workload requests a short-lived token from AWS STS in its own partition and exchanges it for temporary AWS credentials in the other partition, using the existing GetWebIdentityToken and AssumeRoleWithWebIdentity APIs. You control which identities can access each role, apply governance across your organization, and audit token use in AWS CloudTrail in both partitions. This launch helps with scenarios such as consolidated security and compliance reporting, and centralized operations tooling. If your organization already operates a public key infrastructure (PKI), IAM Roles Anywhere is another option for cross-partition access. 
Cross-partition federation is available at no additional charge in all commercial AWS Regions, the AWS GovCloud (US) Regions, the China Regions, and the AWS European Sovereign Cloud (Germany) Region. To learn more, see Federating AWS identities across AWS partitions in the IAM User Guide and the blog post Simplify cross-partition access with AWS IAM outbound identity federation.

## 핵심 요약

요약 미지원
