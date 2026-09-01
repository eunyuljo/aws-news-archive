---
title: "AWS Lambda recursive loop detection is now available in all commercial AWS Regions"
date: "2026-09-01"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/lambda-recursion-regions"
tags: ["Lambda", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Lambda recursive loop detection is now available in all commercial AWS Regions

**날짜:** 2026년 09월 01일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/lambda-recursion-regions

## 내용

AWS Lambda recursive loop detection has expanded support to all commercial AWS Regions. This feature, which is enabled by default, is a guardrail that automatically detects and stops recursive invocations between Lambda functions and other supported services, preventing runaway workloads. 
When using event sources such as Amazon S3, Amazon SQS, and Amazon SNS to trigger Lambda functions, a misconfiguration or code defect can cause events to be sent back to the same source that triggered the Lambda function, causing recursive loops, unintended usage, and unexpected billing. When such a loop is detected, Lambda recursive loop detection automatically stops processing the event and sends you an AWS Health Dashboard notification with troubleshooting steps.&nbsp; 
With this expansion, you now benefit from recursive loop detection in all commercial AWS Regions when using a supported SDK version or later. If your function uses intentional recursive loops, you can use the PutFunctionRecursionConfig API to turn off recursive loop detection on your Lambda function.&nbsp; &nbsp; To learn more about Lambda recursive loop detection, please refer to Lambda documentation.

## 핵심 요약

요약 미지원
