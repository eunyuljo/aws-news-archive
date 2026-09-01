---
title: "AWS Workload Credentials Provider is now available as a one-click install for Linux and Windows"
date: "2026-09-01"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/workload-credentials-provider-install/"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Workload Credentials Provider is now available as a one-click install for Linux and Windows

**날짜:** 2026년 09월 01일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/workload-credentials-provider-install/

## 내용

Today, AWS Secrets Manager announces one-click installation for the AWS Workload Credentials Provider (AWCP) on Amazon Linux and Windows, reducing setup from a multi-step build-from-source process to a single command.&nbsp; &nbsp; AWCP resolves secrets from AWS Secrets Manager and caches them locally, enabling applications to retrieve secrets over a local HTTP endpoint. AWCP also enables you to pull your certificates from AWS Certificate Manager. Previously, customers who wanted to use AWCP on Amazon EC2 instances had approximately 6 steps, starting from cloning the Github repository to compiling the binary and setting up configurations. This multi-step process required every developer to learn Rust expertise and build infrastructure.&nbsp; &nbsp; Now, customers can download pre-built, signed binaries for Linux (x86_64 and ARM64) and Windows (x64) directly from a public download URL. Along with this, AWCP is now available in the Amazon Linux repository. Amazon Linux EC2 customers can install it in one command. All binaries are code-signed to ensure integrity and authenticity, and deliver a ready-to-run agent with in-memory secret caching.&nbsp; &nbsp; AWS Workload Credentials Provider one-click install is available on Amazon Linux 2023 (x86_64 and ARM64) and Windows Server (x64) in all AWS Regions where AWS Secrets Manager is available, at no additional cost beyond standard Secrets Manager pricing. To get started, see the following resources - AWS Workload Credentials Provider documentation , ACM documentation, and AWCP on GitHub.

## 핵심 요약

요약 미지원
