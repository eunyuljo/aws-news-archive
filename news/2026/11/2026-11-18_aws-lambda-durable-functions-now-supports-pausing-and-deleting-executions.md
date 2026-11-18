---
title: "AWS Lambda durable functions now supports pausing and deleting executions"
date: "2026-11-18"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-pause-delete/"
tags: ["Lambda", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda durable functions now supports pausing and deleting executions

**날짜:** 2026년 11월 18일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-pause-delete/

## 내용

AWS Lambda durable functions now lets you pause a running durable execution and resume it later without losing its progress. When you resume an execution, it continues from its last checkpoint on the same function version. By default, time spent paused doesn't count toward the execution timeout. You can also now delete a completed execution's data before its retention period ends.
With Lambda durable functions, you can build resilient multi-step applications and AI workflows that run for up to one year, with built-in checkpointing and automatic retries. With this launch, when a downstream service is degraded or a model provider's rate limit is reached, you can pause affected executions while you resolve the issue instead of letting the retries run out. You can also delete an execution's history, checkpoint data, and input and output payloads after it succeeds, fails, stops, or times out. For example, you can delete an execution whose input contains personal data, or clean up failed executions that a bug left behind.
You can pause, resume, and delete executions using the Lambda console, the AWS CLI, or the AWS SDKs in all AWS Regions where AWS Lambda durable functions is available.
To learn more, see Managing durable executions in the AWS Lambda Developer Guide, or visit the AWS Lambda durable functions product page. If you build with an AI coding assistant such as Kiro, the Agent Toolkit for AWS gives it skills and guidance for building on AWS.

## 핵심 요약

요약 미지원
