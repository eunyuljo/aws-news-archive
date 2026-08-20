---
title: "Amazon CloudWatch log Centralization now supports log group tag propagation"
date: "2026-08-20"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-centralization-tag-propogation/"
tags: ["CloudWatch", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon CloudWatch log Centralization now supports log group tag propagation

**날짜:** 2026년 08월 20일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-centralization-tag-propogation/

## 내용

Amazon CloudWatch Centralization now copies log group tags from source accounts to the destination log groups created by centralization rules. CloudWatch Centralization aggregates log data from multiple accounts and Regions into one destination account. With tag propagation, the cost, ownership, and compliance tags you maintain at the source now apply to the copied log groups. 
With today's launch, CloudWatch copies the tags of each source log group to its destination log group and keeps them in sync based on the tag propogation behaviour selected as part of the centralization rule setup. For example, a platform team can preserve Application and CostCenter tags on centralized log groups, then use those tags to scope access with IAM conditions and report centralized log spend by team in AWS Cost Explorer. 
Tag propagation is available in all AWS Regions where CloudWatch Centralization is available. For a list of Regions, see the AWS Regions table. 
To get started, turn on tag propagation for a centralization rule in the Amazon CloudWatch console, or by using the AWS CLI or AWS SDKs. To learn more about centralizing logs while preserving their tags, see Log Centralization User Guide. For Centralization pricing, see Amazon CloudWatch pricing.

## 핵심 요약

요약 미지원
