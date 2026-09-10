---
title: "AWS Lambda now supports 90-minute function timeout on Lambda Managed Instances"
date: "2026-09-10"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-90-minute-function/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda now supports 90-minute function timeout on Lambda Managed Instances

**날짜:** 2026년 09월 10일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-90-minute-function/

## 내용

AWS Lambda now supports a 90-minute function timeout for asynchronous and event source mapping (ESM) invocations on Lambda Managed Instances (LMI), a 6x increase from the previous 15-minute limit. You can now run data processing, media transcoding, financial calculations, AI inference, and batch workloads on Lambda for jobs that require longer continuous execution, without re-architecting your applications. 
Customers use Lambda to build serverless applications like event-driven processors, API backends, and data processing pipelines. For data-intensive workloads like media transcoding, financial calculations (such as Monte Carlo simulations), and AI inference that need longer continuous execution, Lambda's 15-minute function timeout limit required customers to adopt&nbsp;architectural workarounds. With today's launch, you can configure a function timeout of up to 90 minutes for asynchronous and ESM invocations on Lambda Managed Instances. Lambda Managed Instances lets you process multiple concurrent requests per instance, access specialized compute configurations, and drive cost efficiency through EC2 pricing advantages, without managing infrastructure. The increased function timeout also applies to invocations within Lambda durable functions, which allow you to checkpoint and replay steps for longer-running invocations. When invoked asynchronously, a multi-step durable execution can run for up to 1 year. 
You can configure up to a 90-minute function timeout for asynchronous and ESM invocations via the AWS Lambda Console, AWS CLI, Lambda APIs, Infrastructure as Code tooling, or the Agent Toolkit for AWS. Synchronous invocations retain the existing 15-minute maximum timeout. This feature is available in all AWS Regions where Lambda Managed Instances is available. 
To learn more about configuring the 90-minute function timeout, see the Lambda developer guide. For combining extended timeouts with checkpoint-and-replay resilience, see the durable functions documentation. For pricing details, see AWS Lambda Pricing. To learn more about AWS Lambda, visit aws.amazon.com/lambda.&nbsp;

## 핵심 요약

요약 미지원
