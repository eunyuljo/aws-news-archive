---
title: "AWS Lambda now supports Java 8, 11, and 17 on Amazon Linux 2023"
date: "2026-08-01"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-java-amazon-linux/"
tags: ["Lambda", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# AWS Lambda now supports Java 8, 11, and 17 on Amazon Linux 2023

**날짜:** 2026년 08월 01일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-java-amazon-linux/

## 내용

AWS Lambda now supports Java 8, Java 11, and Java 17 runtimes on Amazon Linux 2023 (AL2023), available as both managed runtimes and container base images. These new runtimes enable customers running Lambda functions on Java 8, 11, or 17 to migrate from Amazon Linux 2 (AL2) to AL2023 without requiring a simultaneous Java version upgrade.  The existing Lambda runtimes for Java 8, 11 and 17 run on AL2, which reached end of life on June 30, 2026. To maintain support coverage and SLA eligibility, customers must migrate their functions to an AL2023-based runtime. AWS recommends that customers upgrade to Java 21 or Java 25 on AL2023 as the preferred migration path. These runtimes offer the latest language features and performance improvements. For customers who are not yet ready to upgrade their Java version, the new Java 8, 11, and 17 runtimes on AL2023 provide an alternative forward path. In addition, the existing AL2-based Lambda runtimes for Java 8, 11, and 17 will remain supported and continue to receive patches for critical and selected important security issues until June 30, 2027, giving customers a full year after AL2's end of life to complete their migration.  The Java 8, 11, and 17 runtimes on AL2023 are available in all AWS Regions where Lambda is available, including the AWS GovCloud (US) Regions and the China Regions.  To learn more about AL2023 support in Lambda, see our blog post. For customers ready to upgrade to Java 21 or Java 25, you can use AWS Transform custom to assist with the migration. To learn more about Lambda runtimes, visit the Lambda runtimes documentation.

## 핵심 요약

요약 미지원
