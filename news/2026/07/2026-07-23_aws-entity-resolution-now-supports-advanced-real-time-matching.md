---
title: "AWS Entity Resolution now supports advanced real-time matching"
date: "2026-07-23"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-entity-resolution/"
tags: ["RDS", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Entity Resolution now supports advanced real-time matching

**날짜:** 2026년 07월 23일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-entity-resolution/

## 내용

AWS Entity Resolution now supports real-time matching with advanced matching workflows, enabling customers to match records in milliseconds using complex rulesets through the GenerateMatchId API. Previously, real-time matching was limited to simple rule-based workflows, while advanced rulesets—which support operators like Exact and ExactManyToMany combined with AND/OR logic—could only be used for batch processing that took minutes to hours. This created a critical gap for customers needing real-time entity resolution with sophisticated matching logic. 
With this launch, customers performing fraud detection, real-time account lookup, or website personalization can define advanced matching rules and get results in real-time without maintaining separate matching infrastructure or re-architecting applications. To enable advanced real-time matching, customers set the enableRealTimeMatching parameter to true on their matching workflow, then call the existing GenerateMatchId API—no new endpoints or migration required. 
Advanced real-time matching is available in all AWS Regions where AWS Entity Resolution is available.&nbsp; 
To get started, see Using GenerateMatchId in the AWS Entity Resolution User Guide.&nbsp;&nbsp; 
For more information about AWS Entity Resolution, visit the product page.

## 핵심 요약

요약 미지원
