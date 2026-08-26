---
title: "IAM Roles Anywhere now provides a Java plugin for the AWS SDK"
date: "2026-08-26"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/iam-roles-anywhere-java/"
tags: ["IAM", "2026", "new-region", "security"]
nav_exclude: true
---

# IAM Roles Anywhere now provides a Java plugin for the AWS SDK

**날짜:** 2026년 08월 26일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/iam-roles-anywhere-java/

## 내용

AWS Identity and Access Management (IAM) Roles Anywhere now provides a plugin for the AWS SDK for Java v2 that enables workloads running outside of AWS to obtain temporary AWS credentials directly within the Java application process. The plugin runs in the same Java Virtual Machine (JVM) as your application, removing the need to run the IAM Roles Anywhere credential helper as a separate process or configure credential_process in your AWS profile.  You configure the plugin on your AWS SDK for Java v2 service client builder to automatically resolve temporary credentials without writing credential-fetching logic. The plugin handles calling CreateSession and automatically refreshing credentials before they expire. It supports RSA, Elliptic Curve (EC), and ML-DSA key types and requires Java 8 or higher. There is no additional charge for using the plugin.  IAM Roles Anywhere is available in all AWS Regions, including the AWS GovCloud (US) Regions, AWS European Sovereign Cloud (Germany) Region, and China Regions. To get started with the Java plugin, see the IAM Roles Anywhere Java plugin documentation. For the current version, release notes, and signature verification instructions, see the plugin's page on the Maven Central website and the roles-anywhere-java repository on GitHub.

## 핵심 요약

요약 미지원
