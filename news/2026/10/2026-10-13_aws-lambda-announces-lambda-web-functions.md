---
title: "AWS Lambda announces Lambda Web Functions"
date: "2026-10-13"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-web-functions/"
tags: ["Lambda", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# AWS Lambda announces Lambda Web Functions

**날짜:** 2026년 10월 13일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-web-functions/

## 내용

AWS Lambda announces Lambda Web Functions, a new serverless compute primitive where your code handles HTTP requests directly. Your code listens on a port and handles requests as it would on any HTTP server. You use frameworks you already know, such as Express or Hono, with no adapters or custom configuration. This enables you to serve workloads such as AI inference endpoints, server-side rendered (SSR) web apps, streaming API endpoints, microservices, and webhooks. You pay for active CPU time and the memory your environment holds, not for idle CPU time your code spends waiting on databases or downstream services. With this launch, we are also renaming existing Lambda functions to Lambda Event Functions, a naming change only that requires no code changes or redeployments for your existing functions.
Builders use Lambda to go from code to production quickly and without managing servers, across event-driven pipelines, request-response APIs, and data processing. As AI-driven development accelerates, they want to build locally and deploy with a familiar programming model and pay for workloads based on active CPU usage, while serving users with low latency. Lambda Web Functions delivers this. Today, Lambda Web Functions supports the Node.js runtime. A single warm execution environment can serve multiple concurrent requests, which reduces cold starts by orders of magnitude. You can stream results to clients incrementally with native HTTP streaming.
You can create and configure Lambda Web Functions using the AWS Lambda API, Agent Toolkit for AWS, AWS Management Console, AWS CLI, AWS CloudFormation, AWS SAM, AWS CDK, or the AWS SDKs. With multi-Region routing, you can deploy once and serve each request from the Region closest to the end user. Web Functions support Amazon Virtual Private Cloud (VPC) connectivity, allowing your function to access resources that exist within a VPC.
Lambda Web Functions is available today in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Tokyo), and Europe (Ireland). For the current list, see the AWS Capabilities by Region page. To learn more, see the Lambda Web Functions developer guide. For pricing details, see AWS Lambda Pricing.  To see Lambda Web Functions in action, see the AWS News Blog announcement.

## 핵심 요약

요약 미지원
