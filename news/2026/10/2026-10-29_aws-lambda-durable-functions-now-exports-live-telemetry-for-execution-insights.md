---
title: "AWS Lambda durable functions now exports live telemetry for execution insights"
date: "2026-10-29"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/lambda-durable-telemetry/"
tags: ["Lambda", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda durable functions now exports live telemetry for execution insights

**날짜:** 2026년 10월 29일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/lambda-durable-telemetry/

## 내용

AWS Lambda announces the Durable Execution Telemetry Exporter plugin for Lambda durable functions. This new observability plugin captures the step-by-step history of your durable executions and sends them to one or more destinations of your choice. You can use the exported data to gather operational and business insights and keep history beyond the standard retention period. We are also releasing a companion Model Context Protocol (MCP) server that lets AI agents such as Kiro query your exported telemetry data using natural language. 
Lambda durable functions helps you build resilient multi-step applications and AI workflows that run for up to one year. The new Telemetry Exporter sends data such as execution status, operation timing, step input and output, and errors to 13 built-in destinations. Destinations include Amazon CloudWatch Logs, Amazon S3 for Amazon Athena, Amazon DynamoDB, Amazon Aurora, and Amazon OpenSearch Service. You can redact sensitive fields before export and set a sampling rate to control data volume. With the MCP server, an on-call engineer can ask an AI agent to list recent failed executions and find the cause of a failure, and a business analyst can find all transactions for a specific customer. 
The exporter is available for TypeScript, Python, Java, and Go. To get started, install the exporter, register the plugin in your function handler, then add the MCP server to your agent. 
The Durable Execution Telemetry Exporter is available at no additional charge in all AWS Regions that support Lambda durable functions. To learn more, see the Durable Execution SDK documentation and the blog post.

## 핵심 요약

요약 미지원
