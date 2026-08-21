---
title: "Amazon DynamoDB Streams now supports attribute-based access control"
date: "2026-08-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-dynamodb-streams-abac/"
tags: ["RDS", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon DynamoDB Streams now supports attribute-based access control

**날짜:** 2026년 08월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-dynamodb-streams-abac/

## 내용

Amazon DynamoDB Streams now supports attribute-based access control (ABAC), enabling you to use tag-based conditions in your Identity and Access Management (IAM) policies to control access to your data streams. ABAC is an authorization strategy that simplifies access management by allowing you to enforce different access levels for multiple teams and applications using fewer IAM policies. This capability is built for teams that manage DynamoDB Streams access across multiple applications and environments and need finer-grained, scalable access control. 
With ABAC for DynamoDB Streams, you can attach up to 50 tags to each stream and use these tags in IAM policy conditions to grant or deny access to specific actions. For example, you can allow users to read records only from streams tagged with "environment:production" while restricting access to other environments. Stream tags are managed independently from their parent table tags, giving you flexibility to implement environment segregation, team-based isolation, and compliance requirements without creating numerous individual IAM policies. 
ABAC for DynamoDB Streams is in all commercial AWS Regions and AWS GovCloud (US) Regions where Amazon DynamoDB Streams is available. There is no additional cost to use ABAC for DynamoDB Streams. To learn more, visit the Amazon DynamoDB page and see the Amazon DynamoDB Streams ABAC.

## 핵심 요약

요약 미지원
