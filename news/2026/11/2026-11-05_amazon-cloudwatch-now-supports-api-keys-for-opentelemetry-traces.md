---
title: "Amazon CloudWatch now supports API keys for OpenTelemetry traces"
date: "2026-11-05"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-api-keys-opentelemetry/"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch now supports API keys for OpenTelemetry traces

**날짜:** 2026년 11월 05일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-api-keys-opentelemetry/

## 내용

Amazon CloudWatch now supports bearer token authentication, using API keys (bearer tokens), as an additional option for sending OpenTelemetry traces to the AWS X-Ray OpenTelemetry Protocol (OTLP) traces endpoint. Any OTLP/HTTP client that can set an Authorization header, including the OpenTelemetry Collector and OpenTelemetry SDK exporters, can now authenticate with a bearer token instead of signing requests with AWS Signature Version 4 (SigV4). This helps teams send traces from workloads that can't use the AWS SDK or short-term credentials, such as applications running on premises or in other clouds, CI/CD pipelines, and third-party tools that support only a static Authorization header. 
SigV4 remains the recommended authentication method for sending traces to CloudWatch, and the AWS Distro for OpenTelemetry (ADOT) SDKs continue to use SigV4 by default with no changes required. Traces sent with either method get the same CloudWatch capabilities, including Transaction Search, Amazon CloudWatch Application Signals, and Amazon CloudWatch Omni. 
Bearer token&nbsp;authentication for traces is available in all commercial AWS Regions where the AWS X-Ray OTLP traces endpoint is available. 
To learn more, see Setting up bearer token authentication for traces in the AWS X-Ray Developer Guide.

## 핵심 요약

요약 미지원
