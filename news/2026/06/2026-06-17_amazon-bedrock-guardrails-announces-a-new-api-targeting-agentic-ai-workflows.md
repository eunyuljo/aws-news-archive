---
title: "Amazon Bedrock Guardrails announces a new API targeting agentic AI workflows"
date: "2026-06-17"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-guardrails-api-ai/"
tags: ["RDS", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Bedrock Guardrails announces a new API targeting agentic AI workflows

**날짜:** 2026년 06월 17일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-guardrails-api-ai/

## 내용

Amazon Bedrock Guardrails now offers the InvokeGuardrailChecks API, a new resourceless API that lets you apply individual safeguards at any point in your agentic AI applications without creating guardrail resources. The API provides granular, per-request control over which safeguards to run at each step of your agent loop, returning numeric severity and confidence scores so you can implement custom thresholds and actions, whether to block, pass, retry, or log based on your specific requirements. 
Agentic AI applications operate through iterative loops; planning tasks, calling tools, processing outputs, and iterating again while often executing dozens of steps for a single request. Each step carries a different risk profile, making a one-size-fits-all guardrail difficult to scale. The InvokeGuardrailChecks API addresses this by operating in detect-only mode with no guardrail IDs to track and no versions to manage. You specify which safeguards to run directly in each request, making it straightforward to add, remove, or adjust checks as your workflows evolve. 
The API supports content filters (detecting harmful content across categories including hate, violence, sexual, insults, and misconduct), prompt attack detection (identifying jailbreak, prompt injection, and prompt leakage as independent standalone checks), and sensitive information filters (detecting supported PII entity types). Prompt attack detection is exposed as a separate safeguard, giving you the granularity to invoke each supported attack vector independently. 
The InvokeGuardrailChecks API is available today in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (London), Europe (Stockholm), Asia Pacific (Tokyo), and Asia Pacific (Sydney). 
To learn more, visit the Amazon Bedrock Guardrails technical documentation.

## 핵심 요약

요약 미지원
