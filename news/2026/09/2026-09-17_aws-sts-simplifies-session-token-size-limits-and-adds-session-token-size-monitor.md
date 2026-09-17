---
title: "AWS STS simplifies session token size limits and adds session token size monitoring"
date: "2026-09-17"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts/"
tags: ["CloudWatch", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS STS simplifies session token size limits and adds session token size monitoring

**날짜:** 2026년 09월 17일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts/

## 내용

AWS Security Token Service (STS) now enforces a single 4,096-byte size limit on session tokens. Previously, STS enforced separate limits on session token size and passed-in parameters (i.e., inline policies, managed policies, and session tags). STS has removed that separation, providing more flexibility for larger combinations of session policies and session tags. 
Additionally, STS now returns response elements indicating session token size and percentage utilization relative to the token size limit. STS logs these values in AWS CloudTrail and publishes corresponding metrics in Amazon CloudWatch. A new optional API parameter also lets you generate larger session tokens (up to the 4,096-byte limit) to test whether your applications and infrastructure can handle them. 
These capabilities are available in all commercial AWS Regions, the AWS GovCloud (US) Regions, and the AWS European Sovereign Cloud Region. 
To learn more, please read the AWS Security Blogpost, AWS IAM User Guide, and AWS STS API Reference.

## 핵심 요약

요약 미지원
