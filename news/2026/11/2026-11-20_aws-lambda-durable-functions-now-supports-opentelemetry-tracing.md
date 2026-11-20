---
title: "AWS Lambda durable functions now supports OpenTelemetry tracing"
date: "2026-11-20"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-otel/"
tags: ["Lambda", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# AWS Lambda durable functions now supports OpenTelemetry tracing

**날짜:** 2026년 11월 20일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-otel/

## 내용

AWS Lambda announces OpenTelemetry (OTel) support for Lambda durable functions. You can now trace your durable executions and emit traces to Amazon CloudWatch and other industry-standard observability tools.&nbsp;This helps you find bottlenecks in your system, root cause failures faster, and understand how your workflows behave in production. 
With Lambda durable functions, you can build resilient, multi-step applications and AI workflows that run for up to one year, with built-in checkpointing and automatic retries. Durable functions can run for&nbsp;hours, or days, suspending and resuming across many Lambda invocations. The new OpenTelemetry plugin emits a unified trace that spans a full durable execution, including steps, waits, callbacks, and chained function invocations. You can use the trace to gain operational insights across your executions including step durations, retries, and failures across executions.&nbsp;&nbsp; 
The OpenTelemetry plugin is available for the TypeScript, Python, and Java SDKs. You can enable OpenTelemetry support by adding the OpenTelemetry plugin package alongside the Durable Execution SDK and register it on your durable handler or using an environment variable. OpenTelemetry support for Lambda durable functions is available in all AWS Regions that support Lambda durable functions. 
To get started, see the&nbsp; OpenTelemetry plugin documentation, the plugin interface documentation, and the sample application. To learn more, read the blog post.&nbsp;

## 핵심 요약

요약 미지원
