---
title: "AWS Lambda Durable Execution SDK for Go is now generally available"
date: "2026-10-16"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-go-sdk-support/"
tags: ["Lambda", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda Durable Execution SDK for Go is now generally available

**날짜:** 2026년 10월 16일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-go-sdk-support/

## 내용

Today, AWS announces the general availability of the AWS Lambda Durable Execution SDK for Go, enabling Go developers to build resilient, long-running workflows using Lambda durable functions. With this SDK, developers can create multi-step applications like infrastructure automation, deployment rollouts with approval gates, and pipelines that call AI models and pause for human review directly in their Go code without implementing custom progress tracking.
Lambda durable functions extend Lambda's event-driven programming model with operations that checkpoint progress automatically and pause execution for up to an year when waiting on external events. The AWS Lambda Durable Execution SDK for Go provides a native Go experience for building with Lambda durable functions. It includes steps for progress tracking, callback integration for human and agent-in-the-loop workflows, durable invocation for reliable function chaining, and waits for efficient suspension.
The SDK works with the Go tools developers already use. Developers add it to a Go module with go get and deploy their function as a single static binary on the provided.al2023 runtime, like any other Go function on Lambda. Before deploying, they can locally test complete workflows on their own machine with the durabletest package, without requiring network access or AWS credentials, and use the durablelint analyzer to catch code that could break a workflow when it resumes.
To get started, see the Lambda durable functions developer guide and the&nbsp;AWS Lambda Durable Execution SDK for Go on GitHub. For Regional availability and pricing details for Lambda durable functions, see the AWS Capabilities by Region page and AWS Lambda Pricing.

## 핵심 요약

요약 미지원
