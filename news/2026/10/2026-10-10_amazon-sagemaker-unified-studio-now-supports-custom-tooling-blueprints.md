---
title: "Amazon SageMaker Unified Studio now supports custom Tooling blueprints"
date: "2026-10-10"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-custom-tooling-blueprints/"
tags: ["RDS", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon SageMaker Unified Studio now supports custom Tooling blueprints

**날짜:** 2026년 10월 10일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-custom-tooling-blueprints/

## 내용

Amazon SageMaker Unified Studio now supports custom Tooling blueprints, giving domain administrators the ability to define the foundation of every project by using their own AWS CloudFormation templates. Administrators can tailor project environments to meet organization-specific requirements, such as IAM role names that comply with company naming standards or custom permissions boundaries instead of AWS managed policies.
Amazon SageMaker Unified Studio administrators start by authoring a CloudFormation template that describes the project environment they need, then register it as a custom Tooling blueprint. The service validates the template at registration and again after each project deployment, confirming that the required resources exist before any team member uses the project. Templates can include any CloudFormation-supported resource, such as AWS Lake Formation grants, Amazon Athena workgroups, or VPC security groups, and work across multiple AWS accounts and Regions without per-project edits. At deployment time, the service automatically populates reserved template parameters, such as the project ID and domain ID, so administrators define the template once and apply it everywhere.
This feature is available in all AWS Regions where Amazon SageMaker Unified Studio is available. To learn more, visit the Custom blueprints as Tooling documentation.

## 핵심 요약

요약 미지원
