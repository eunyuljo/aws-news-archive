---
title: "Amazon DynamoDB global tables with multi-Region strong consistency now supports additional AWS Regions and cross-continent configurations"
date: "2026-09-24"
service: "DynamoDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/dynamodb-mrsc-additional-regions/"
tags: ["DynamoDB", "2026", "new-region"]
nav_exclude: true
---

# Amazon DynamoDB global tables with multi-Region strong consistency now supports additional AWS Regions and cross-continent configurations

**날짜:** 2026년 09월 24일
**서비스:** DynamoDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/dynamodb-mrsc-additional-regions/

## 내용

Starting today, Amazon DynamoDB global tables with multi-Region strong consistency (MRSC) is available in five additional AWS Regions: Canada (Central), Europe (Stockholm), Europe (Spain), Asia Pacific (Mumbai), and Asia Pacific (Singapore), bringing the total number of supported Regions to 15. You can now create an MRSC global table in any three-Region configuration across the 15 supported AWS Regions, configured with either three replicas or two replicas and one witness Region. This includes configurations that span North America, Europe, and Asia Pacific.
MRSC lets you build highly available multi-Region applications with a recovery point objective (RPO) of zero. By choosing replica Regions closer to your users in more geographies, you can route applications to nearby DynamoDB endpoints for strongly consistent reads while keeping your application available during Regional impairments. MRSC is ideal for global applications with strict consistency requirements, such as user profile management, inventory tracking, order state, and entitlement management.
To get started and view the complete list of supported Regions and configuration options, see the DynamoDB Developer Guide. To learn more about building resilient multi-Region applications, visit the DynamoDB global tables page.

## 핵심 요약

요약 미지원
