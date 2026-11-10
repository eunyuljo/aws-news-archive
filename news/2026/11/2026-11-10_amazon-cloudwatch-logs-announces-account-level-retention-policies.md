---
title: "Amazon CloudWatch Logs announces account-level retention policies"
date: "2026-11-10"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-log-retention/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon CloudWatch Logs announces account-level retention policies

**날짜:** 2026년 11월 10일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-log-retention/

## 내용

Amazon CloudWatch Logs now supports account-level retention policies, so you can use a single policy to set how long log data is kept across all or subset of log groups in an AWS account. Account-level policies allow platform and security teams to bring each log group in line with their retention standards. 
With today's launch, you can create policies that cover all log groups in the account or apply to a specific set of log groups with names that start with a prefix, such as /aws/lambda. You can additionally choose whether it applies to existing log groups or only new ones. When more than one policy matches a log group, the longest retention period applies. For example, a central platform team can set a 90-day baseline for the account and a 1-year policy for log groups that start with /security to meet audit requirements, without tracking individual log group names. 
Account-level retention policies are available in all commercial AWS Regions except Middle East (Bahrain), and Middle East (UAE) at no additional cost . You can create and manage up to 20 policies per account and region using the AWS Management Console, AWS CLI, and AWS SDKs. Learn more in the &nbsp;CloudWatch Logs documentation, and the &nbsp;API reference&nbsp;.

## 핵심 요약

요약 미지원
