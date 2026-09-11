---
title: "AWS Lambda recursive loop detection is now available in Europe Sovereign Cloud"
date: "2026-09-11"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/lambda-recursion-europe-sovereign-cloud"
tags: ["Lambda", "2026", "GA"]
nav_exclude: true
---

# AWS Lambda recursive loop detection is now available in Europe Sovereign Cloud

**날짜:** 2026년 09월 11일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/lambda-recursion-europe-sovereign-cloud

## 내용

AWS Lambda recursive loop detection is now supported for functions running in Europe Sovereign Cloud. Recursive loop detection automatically detects and stops recursive invocations between Lambda functions and other supported services, preventing unexpected billing caused by unintended recursive loops.  
Customers use event sources such as Amazon S3, Amazon SQS, and Amazon SNS to build event driven applications that trigger Lambda functions. Misconfiguration or code defect can cause events to be sent back to the same source that triggered the Lambda function, causing recursive loops and unintended usage. When such a loop is detected, recursive loop detection automatically stops processing the event and sends you an AWS Health Dashboard notification with troubleshooting steps. 
Recursive loop detection is enabled by default for Lambda functions using a supported SDK version. If your function intentionally uses recursive loops, you can use the PutFunctionRecursionConfig API to turn off recursive loop detection on your Lambda function.&nbsp; 
To learn about recursive loop detection, visit&nbsp;Lambda documentation.

## 핵심 요약

요약 미지원
