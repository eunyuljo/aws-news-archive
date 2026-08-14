---
title: "AWS Clean Rooms supports minimum aggregation thresholds in custom analysis rules"
date: "2026-08-14"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-clean-rooms-minimum-aggregation-custom-analysis-rules"
tags: ["Config", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Clean Rooms supports minimum aggregation thresholds in custom analysis rules

**날짜:** 2026년 08월 14일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-clean-rooms-minimum-aggregation-custom-analysis-rules

## 내용

AWS Clean Rooms now supports minimum aggregation thresholds for the Custom analysis rule type. Minimum aggregation helps protect the privacy of individual data subjects by preventing queries from returning results about individuals or small groups. With this launch, organizations can enforce minimum aggregation on custom SQL queries, ensuring that every row a query outputs represents at least the specified number of distinct values (e.g., user IDs). Data providers in a collaboration can specify their identity column and a minimum identity count to enforce on a query’s output, with the option to set a higher threshold for specific columns. 
Previously, enforcing minimum aggregation thresholds on custom SQL required data providers to rely on pre-approved analysis templates and manual code reviews before queries could run. Now, data providers can configure the minimum aggregation threshold for custom SQL using the Custom analysis rule type, without using pre-structured queries or manual approval processes. Additionally, data providers can specify which columns can be filtered or joined across datasets. For example, a publisher collaborating with an advertiser for media planning use cases can enable ad-hoc queries to run on their data—and small, rural zip codes with fewer than 1,000 common users can be automatically filtered out from the result to help protect user privacy.&nbsp; 
AWS Clean Rooms helps companies and their partners easily analyze and collaborate on their collective datasets without revealing or copying one another’s underlying data. For more information about the AWS Regions where AWS Clean Rooms is available, see the AWS Regions table. To learn more about collaborating with AWS Clean Rooms, visit AWS Clean Rooms.

## 핵심 요약

요약 미지원
