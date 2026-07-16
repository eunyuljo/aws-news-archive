---
title: "Amazon CloudWatch Logs announces intelligent tiering for storage"
date: "2026-07-16"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-intelligent-tiering/"
tags: ["CloudWatch", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch Logs announces intelligent tiering for storage

**날짜:** 2026년 07월 16일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-intelligent-tiering/

## 내용

Amazon CloudWatch Logs now supports intelligent storage tiering, which automatically classifies your log data across three storage tiers - Standard (existing), Infrequent Access, and Archive Instant Access based on access patterns. This allows you to store logs in Amazon CloudWatch for extended periods at lower-cost tiers without any operational overhead. 
With today's launch, customers can now retain high-volume verbose logs needed to be stored for longer periods at a lower cost in Amazon CloudWatch. Instead of filtering these logs or exporting them, you can now keep them natively in Amazon CloudWatch and benefit from the same query experience regardless of which tier your data resides in. Amazon CloudWatch monitors access patterns and automatically reclassifies data not accessed for 30 days to the Infrequent Access tier, and data not accessed for 90 days to the Archive Instant Access tier. When you access older data, it is automatically promoted back to the Standard tier for 30 days. By consolidating all your logs in CloudWatch, you get full visibility in one tool, thereby eliminating the operational overhead of managing multiple storage solutions and reducing your Mean Time to Resolution (MTTR) by analyzing, and alerting on all your logs in a single place. 
Amazon CloudWatch Logs Intelligent-Tiering is available in all AWS commercial regions except Middle East (Bahrain) and Middle East (UAE). You can enable intelligent tiering at the account level in the AWS Management Console, AWS SDKs or through AWS CLI. Learn more about CloudWatch Logs intelligent tiering pricing&nbsp;and documentation.

## 핵심 요약

요약 미지원
