---
title: "Amazon Bedrock AgentCore now delivers unified observability with traces and logs in a single log group"
date: "2026-07-24"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/"
tags: ["CloudWatch", "2026", "GA", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon Bedrock AgentCore now delivers unified observability with traces and logs in a single log group

**날짜:** 2026년 07월 24일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/

## 내용

Amazon Bedrock AgentCore now delivers agent traces and prompts to the same log group as your agent's logs, giving you unified observability for AI agents in a single Amazon CloudWatch log group. 
Previously, AgentCore split agent telemetry across multiple destinations trace spans went to the shared `aws/spans` log group while event logs containing prompts, inputs, and outputs went to a separate resource-specific log group. This meant debugging an agent invocation required searching across multiple log groups, and customers could not apply fine-grained access control or customer-managed key (CMK) encryption at the individual agent level. With today's launch, all of an agent's telemetry traces, prompts, structured logs, and standard output is delivered to a single per-agent log group (`/aws/bedrock-agentcore/runtimes/&lt;agent_id&gt;-&lt;endpoint_name&gt;`). You can now correlate traces and logs in one place, scope IAM policies and CMK encryption to individual agents, and export all telemetry by subscribing to a single log group. For multi-agent systems, each agent's complete execution history stays together, making end-to-end debugging straightforward. 
All newly created agents starting July 20, 2026 in supported AWS Regions use unified observability by default starting no configuration needed. For existing agents, set the `UNIFIED_TRACES_DESTINATION_ENABLED=true` environment variable on your agent runtime and upgrade ADOT to version 0.17.1 or later. This feature is available in all AWS commercial regions where AgentCore runtime is supported. Learn more in the AgentCore Developer Guide.

## 핵심 요약

요약 미지원
