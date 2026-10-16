---
title: "AWS Lambda recursive loop detection now supports Amazon EventBridge Custom event buses"
date: "2026-10-16"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/lambda-recursive-loops-eventbridge-custom"
tags: ["Lambda", "2026", "new-region"]
nav_exclude: true
---

# AWS Lambda recursive loop detection now supports Amazon EventBridge Custom event buses

**날짜:** 2026년 10월 16일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/lambda-recursive-loops-eventbridge-custom

## 내용

AWS Lambda recursive loop detection now automatically detects and stops recursive loops between Lambda Event Functions and Amazon EventBridge Custom event buses, helping protect you against unintended usage and unexpected charges from runaway workloads. Lambda recursive loop detection, enabled by default on your AWS account, automatically identifies when a Lambda Event Function is invoked recursively by a supported AWS service and stops the loop.
You can use EventBridge Custom event buses to invoke Lambda Event Functions, building automation workflows and scheduling recurring tasks without managing any infrastructure. However, a misconfiguration or code defect can cause EventBridge rules to trigger your Event Functions recursively, resulting in runaway usage. Now, recursive loop detection supports EventBridge Custom buses, automatically stopping such loops and sending you an AWS Health Dashboard notification with troubleshooting instructions.
EventBridge Custom event buses now support recursive loop detection in every commercial AWS Region where they are available. This feature is enabled by default on your account and requires no configuration. If your Event Function uses recursive loops intentionally, you can use the PutFunctionRecursionConfig API to turn off recursive loop detection for that function.
To learn more about recursive loop detection, visit Lambda documentation.

## 핵심 요약

요약 미지원
