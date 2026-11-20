---
title: "AWS Lambda Durable Execution SDK for Rust is now generally available"
date: "2026-11-20"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-execution-sdk-rust/"
tags: ["Lambda", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda Durable Execution SDK for Rust is now generally available

**날짜:** 2026년 11월 20일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-execution-sdk-rust/

## 내용

Today, AWS announces the general availability of the open source AWS Lambda Durable Execution SDK for Rust. Rust developers can use the SDK to build resilient, long-running workflows using Lambda durable functions, to create multi-step applications like infrastructure automation, deployment rollouts with approval gates, and pipelines that call AI models and pause for human review directly in their Rust code without implementing custom progress tracking.
Lambda durable functions extend Lambda's event-driven programming model with operations that checkpoint progress automatically and pause execution for up to one year when waiting on external events. With the SDK, developers write a durable function as an ordinary async Rust function that awaits each durable operation like any other future and can run independent operations concurrently. The SDK includes steps that save their results, callbacks for human-in-the-loop and agent-in-the-loop workflows, invocations of other durable functions, and timed waits.
The SDK works with the Rust tools developers already use. Developers add the aws-durable-execution-sdk crate with cargo add, build with Cargo Lambda, and deploy a single binary on the provided.al2023 runtime. Before deploying, they can test complete workflows with cargo test and the SDK's LocalRunner without requiring network access or AWS credentials.
To get started, see the Lambda durable functions developer guide, the Rust SDK guide, and the AWS Lambda Durable Execution SDK for Rust on GitHub. For Regional availability and pricing details for Lambda durable functions, see the AWS Capabilities by Region page and AWS Lambda Pricing.

## 핵심 요약

요약 미지원
