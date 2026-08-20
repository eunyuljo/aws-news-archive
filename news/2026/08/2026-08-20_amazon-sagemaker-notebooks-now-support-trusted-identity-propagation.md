---
title: "Amazon SageMaker notebooks now support trusted identity propagation"
date: "2026-08-20"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-sagemaker/"
tags: ["IAM", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon SageMaker notebooks now support trusted identity propagation

**날짜:** 2026년 08월 20일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-sagemaker/

## 내용

Amazon SageMaker Notebooks now support Trusted Identity Propagation (TIP) with Amazon Athena, Amazon Redshift, and Amazon EMR Serverless, enabling per-user access control for data analytics. 
When connected to a TIP-enabled compute in a TIP-enabled Project, each notebook user's IAM Identity Center identity flows through to AWS Lake Formation, ensuring they see only the tables, columns, and rows their permissions allow, without sharing a single broad execution role. With TIP, enterprises get per-user data boundaries enforced based on who is running the query, full audit attribution with CloudTrail recording which user accessed data, and reduced admin friction since identity propagates automatically through the existing compute connection with no extra login, token, or role management required. 
To get started, use a notebook in a TIP enabled Project with the supported engines.&nbsp;&nbsp;This feature is available in all AWS Regions where Amazon SageMaker Unified Studio is available.&nbsp;To learn more, see Trusted identity propagation in the Amazon SageMaker Unified Studio Administrator Guide and Notebooks in the Amazon SageMaker Unified Studio User Guide.

## 핵심 요약

요약 미지원
