---
title: "AWS Lambda durable functions increases default execution and API quotas"
date: "2026-11-06"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-functions-default-quotas/"
tags: ["Lambda", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda durable functions increases default execution and API quotas

**날짜:** 2026년 11월 06일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-functions-default-quotas/

## 내용

AWS Lambda durable functions has increased default quotas for running executions and API request rates. The new quotas below apply in all AWS Regions except US East (N. Virginia), US West (Oregon), and Europe (Ireland), which have twice these quotas. 
 
 Running durable executions per account (1 million to 5 million) 
 Function invocation rate to start durable executions (300 to 3,000 requests per second) 
 CheckpointDurableExecution and GetDurableExecutionState (1,000 to 10,000 requests per second) 
 SendDurableExecutionCallbackSuccess, SendDurableExecutionCallbackFailure, and SendDurableExecutionCallbackHeartbeat (300 to 3,000 requests per second) 
 GetDurableExecution and StopDurableExecution (30 to 300 requests per second) 
 GetDurableExecutionHistory and ListDurableExecutionsByFunction (15 to 150 requests per second) 
 
AWS Lambda durable functions helps you build resilient multi-step applications and AI workflows that execute for up to one year, with built-in checkpointing, automatic retries, and waits that suspend execution without incurring compute charges. With this increase, workloads such as order processing and document pipelines can run more executions in parallel without requesting quota increases. When many executions wait on external work, such as payment confirmations or batch jobs, more can resume together. If you monitor and manage executions with your dashboards or scripts, they can now check status, list executions, read history, and stop executions at least ten times as often. 
The new quotas apply in all AWS Regions where AWS Lambda durable functions is available. To learn more, see Lambda quotas in the AWS Lambda Developer Guide.

## 핵심 요약

요약 미지원
