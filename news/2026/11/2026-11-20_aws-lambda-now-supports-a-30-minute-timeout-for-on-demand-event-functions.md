---
title: "AWS Lambda now supports a 30-minute timeout for on-demand Event Functions"
date: "2026-11-20"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-30-minute-ondemand-event-functions/"
tags: ["Lambda", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda now supports a 30-minute timeout for on-demand Event Functions

**날짜:** 2026년 11월 20일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-30-minute-ondemand-event-functions/

## 내용

AWS Lambda now supports a 30-minute function timeout for Event Functions that run on demand, doubling the 15-minute limit for synchronous, asynchronous, and event source mapping (ESM) invocations. On Lambda Managed Instances, synchronous invocations also support up to 30 minutes, while asynchronous and ESM invocations keep the 90-minute timeout launched in September 2026. You can now run long-running workloads such as AI inference, media transcoding, and financial calculations for spiky or steady-state traffic without re-architecting your applications. 
Customers use&nbsp;Event Functions to build event-driven processors, API backends, and data pipelines. By default, Event Functions run on demand, and Lambda scales them automatically to handle spiky traffic. For steady-state traffic, you can also run them on Lambda Managed Instances, which runs functions on Amazon EC2 instances and&nbsp;maintains&nbsp;the operational simplicity of Lambda.&nbsp;For data-intensive workloads such as AI inference and media processing that run on demand and need longer continuous execution, the 15-minute function timeout had required customers to adopt&nbsp;architectural workarounds. With today's launch, these workloads can run for up to 30 minutes, including when you use Lambda durable functions or invoke your functions from AWS Step Functions Standard workflows. 
For Event Functions that run on demand, the 30-minute timeout is available in all&nbsp;commercial AWS Regions. On Lambda Managed Instances, it is available for synchronous invocations in all Regions where Lambda Managed Instances is available. You can set the function timeout by using the Lambda console, AWS CLI, AWS SDKs, AWS CloudFormation, AWS CDK, or AWS SAM. You can also use coding assistants such as Kiro, Claude Code, or Codex with the Agent Toolkit for AWS. Standard AWS Lambda pricing applies. To learn more, visit the AWS Lambda Developer Guide.&nbsp;&nbsp;&nbsp;&nbsp;

## 핵심 요약

요약 미지원
