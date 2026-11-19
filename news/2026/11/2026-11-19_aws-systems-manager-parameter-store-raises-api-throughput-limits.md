---
title: "AWS Systems Manager Parameter Store raises API throughput limits"
date: "2026-11-19"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/parameter-store-raises-api-throughput-limits/"
tags: ["Lambda", "2026", "performance"]
nav_exclude: true
---

# AWS Systems Manager Parameter Store raises API throughput limits

**날짜:** 2026년 11월 19일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/parameter-store-raises-api-throughput-limits/

## 내용

AWS Systems Manager Parameter Store&nbsp;has increased the default throughput limits for five API operations. For accounts that have turned on the higher throughput setting, the quotas have changed as follows, in transactions per second (TPS): 
 
 GetParametersByPath (from 100 to 500 TPS) 
 PutParameter (10 to 50) 
 DeleteParameter (5 to 50) 
 DescribeParameters (10 to 100) 
 GetParameterHistory (10 to 100) 
 
Parameter Store provides powerful, hierarchical storage for configuration data. The higher quotas give more headroom to workloads that call these operations in bursts. Examples include applications that load configuration by path when many AWS Lambda functions start at once, infrastructure as code deployments that create or update many parameters, and cleanup jobs that bulk-delete stale parameters.

## 핵심 요약

요약 미지원
