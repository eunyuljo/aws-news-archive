---
title: "CloudWatch Application Signals now supports Dynamic Instrumentation"
date: "2026-07-07"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/cloudwatch-dynamic-instrumentation/"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# CloudWatch Application Signals now supports Dynamic Instrumentation

**날짜:** 2026년 07월 07일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/cloudwatch-dynamic-instrumentation/

## 내용

Today, AWS announces Dynamic Instrumentation for Amazon CloudWatch Application Signals, a capability that captures runtime state from live applications without requiring restarts or redeployments. Developers debugging production issues can now inspect variable values, method arguments, return values, and stack traces at specific code locations. Dynamic Instrumentation eliminates the need to add logging statements, redeploy, and wait to reproduce a problem, making it practical to investigate issues that are difficult to replicate locally. 
Customers start by instrumenting their application with the AWS Distro for OpenTelemetry (ADOT) SDKs. Customers then configure which code locations to monitor using the CloudWatch Application Signals MCP server or manually via the AWS CLI and SDK. When execution reaches an instrumented location, the agent captures a snapshot containing the runtime context and delivers it to CloudWatch Logs, correlated with the active trace. Customers can tune how much data to capture, including which arguments and local variables to collect. 
Dynamic Instrumentation is available in all commercial AWS regions. Supported languages are Java, Python, and JavaScript/TypeScript. The feature is disabled by default in the ADOT SDKs and must be enabled via a flag, see documentation for more. 
To learn more, see Debug applications with Dynamic Instrumentation in the Amazon CloudWatch User Guide. Dynamic instrumentation data is captured as logs. Standard CloudWatch Logs ingestion and storage rates apply. For details, see CloudWatch pricing.

## 핵심 요약

요약 미지원
