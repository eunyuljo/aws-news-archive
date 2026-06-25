---
title: "Amazon CloudWatch now supports tags on dashboards"
date: "2026-06-25"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-tags-on-dashboards"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon CloudWatch now supports tags on dashboards

**날짜:** 2026년 06월 25일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-tags-on-dashboards

## 내용

Amazon CloudWatch now supports tagging for CloudWatch dashboards, enabling you to organize, categorize, and control access to your dashboards using tags. Tags are key-value pairs that help you identify and manage AWS resources across your environment.  With this launch, the PutDashboard API now accepts an optional Tags parameter, allowing you to assign up to 50 tags when creating a new dashboard. The TagResource, UntagResource, and ListTagsForResource APIs now support dashboard ARNs, enabling you to add, remove, and list tags on existing dashboards. You can also manage dashboard tags using AWS CloudFormation. This new capability allows you to group dashboards by team by team, project, or environment, implement attribute-based access control by scoping IAM permissions to dashboards with specific tag values, and filter dashboards by tag in AWS Resource Explorer.  CloudWatch Dashboard tagging support is available at no additional cost in all AWS Regions where Amazon CloudWatch is available.  To learn more, see TagResource in the Amazon CloudWatch API Reference. To get started with CloudWatch dashboards, see Amazon CloudWatch features.

## 핵심 요약

요약 미지원
