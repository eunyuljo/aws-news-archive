---
title: "Introducing the Apache Spark Optimization Agent for Amazon EMR Serverless"
date: "2026-11-18"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-optimization-agent/"
tags: ["IAM", "2026", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# Introducing the Apache Spark Optimization Agent for Amazon EMR Serverless

**날짜:** 2026년 11월 18일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-optimization-agent/

## 내용

Amazon EMR Serverless now offers the Apache Spark optimization agent, which analyzes completed Spark job runs and delivers cost and performance optimization recommendations in seconds. You can select a cost or performance goal, and the agent returns specific configuration changes with the telemetry evidence and plain-language reasoning behind each suggestion. The agent can analyze a single run or compare it against a known-good baseline to pinpoint what changed. You access it from the EMR Serverless console or through the SageMaker Unified Studio MCP Server. 
The agent takes the job's configuration, logs, and Spark telemetry together with your chosen intent and returns recommendations computed by a deterministic recommendation engine. The engine reads all job artifacts together to identify what is driving runtime and cost: too little parallelism, a skewed join key, memory pressure forcing spill, idle executors, or capacity provisioned beyond what the job uses. The configurations the engine targets are the settings most commonly tuned across millions of Spark jobs running on AWS. When cost and performance trade off, the recommendation improves the metric you asked for while keeping degradation of the other within defined limits. The engine also evaluates a best practices checklist covering platform-level improvements such as upgrading to a newer Spark version or using Graviton processors. Each recommendation is labeled by the surface it modifies: infrastructure, Spark configuration, code, or data layout. Data engineers can also use the agent during development to tune configurations before promoting to production. All access is authenticated with AWS IAM and logged in AWS CloudTrail. 
The Apache Spark Optimization Agent is available at no additional charge in all Regions where EMR Serverless is available, except GovCloud (US) and China Regions, for EMR release versions 7.6 and later. To get started, see Apache Spark Optimization Agent for Amazon EMR Serverless.

## 핵심 요약

요약 미지원
