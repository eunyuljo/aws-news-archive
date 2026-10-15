---
title: "AWS Lambda durable functions increases durable operation and checkpoint payload limits"
date: "2026-10-15"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-gen-limit-increase/"
tags: ["Lambda", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda durable functions increases durable operation and checkpoint payload limits

**날짜:** 2026년 10월 15일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-gen-limit-increase/

## 내용

Starting today, AWS Lambda durable functions increases the maximum number of durable operations per execution from 3,000 to 30,000, and the maximum checkpoint payload size from 256 KB to 1 MB. Higher operation limits let you safely do more work in a single execution including expanding iterative loops, polling for longer time periods, and building more complex rollback paths that run when a step fails. At 1 MB, checkpoint payloads match the maximum payload size of asynchronous Lambda invocations, and integration services such as Amazon SQS, and Amazon EventBridge, so a workflow can persist a full event from any of these sources in a single operation.
AWS Lambda durable functions helps you build resilient multi-step applications and AI workflows that execute for up to one year, with built-in checkpointing, automatic retries, and waits that suspend execution without incurring compute charges. Every durable operation counts toward the per-execution limit, including each step attempt, each poll of a wait-for-condition, and each branch of a parallel or map operation. With 30,000 operations, a single execution has more room to coordinate complex, multi-step workflows, iterate across thousands of items, or poll an external system for weeks, without exceeding checkpoint limits.
An agentic application can reason over thousands of model and tool calls, and with 1 MB checkpoints it persists larger conversation histories, model responses, and outputs from tools directly in the checkpoint instead of writing to external storage. For state larger than 1 MB, the JavaScript and Python SDKs include a FileSystem serializer that writes the payload to an Amazon EFS or Amazon S3 Files mount and checkpoints a pointer instead.
&nbsp;The new limits apply in all AWS Regions where AWS Lambda durable functions is available. To learn more about these service limits, see the&nbsp;AWS Lambda developer guide.

## 핵심 요약

요약 미지원
