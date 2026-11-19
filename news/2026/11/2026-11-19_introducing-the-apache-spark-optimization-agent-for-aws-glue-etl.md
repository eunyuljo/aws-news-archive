---
title: "Introducing the Apache Spark Optimization Agent for AWS Glue ETL"
date: "2026-11-19"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-aws-glue-etl/"
tags: ["IAM", "2026", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# Introducing the Apache Spark Optimization Agent for AWS Glue ETL

**날짜:** 2026년 11월 19일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-aws-glue-etl/

## 내용

AWS Glue ETL now offers the Apache Spark Optimization Agent, which analyzes completed Spark job runs and delivers cost and performance optimization recommendations within minutes. You can select a cost or performance goal, and the agent returns specific configuration changes with the telemetry evidence and reasoning behind each suggestion. You can use the agent on any completed job run from the AWS Glue console, or from your own tools through the Amazon SageMaker Unified Studio MCP Server. 
The agent takes the job's configuration, logs, and Spark telemetry together with your chosen goal and returns recommendations computed by a deterministic recommendation engine. The engine reads all job artifacts together to identify what is driving runtime and cost: too little parallelism, a skewed join key, memory pressure forcing spill, idle executors, or capacity provisioned beyond what the job uses. When cost and performance trade off, the agent improves the metric you chose while keeping any regression of the other within defined limits. The engine also checks best practices such as platform-level improvements like upgrading to a newer AWS Glue version or using AWS Graviton processors. Each recommendation is labeled by the area it modifies: infrastructure, Spark configuration, code, or data layout. All access is authenticated with AWS Identity and Access Management (IAM) and logged in AWS CloudTrail. 
The Apache Spark Optimization Agent is available at no additional charge for AWS Glue versions 4.0 and later in all Regions where AWS Glue is available, except the AWS GovCloud (US) and China Regions. To get started, see Apache Spark Optimization Agent for Amazon EMR and AWS Glue and the blog post - Introducing the Apache Spark optimization agent for Amazon EMR Serverless and AWS Glue ETL.

## 핵심 요약

요약 미지원
