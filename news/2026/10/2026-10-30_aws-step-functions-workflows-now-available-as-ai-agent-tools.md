---
title: "AWS Step Functions workflows now available as AI agent tools"
date: "2026-10-30"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/step-functions-workflows-ai-agent-tools/"
tags: ["Bedrock", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Step Functions workflows now available as AI agent tools

**날짜:** 2026년 10월 30일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/step-functions-workflows-ai-agent-tools/

## 내용

You can now use your AWS Step Functions workflows as tools for AI agents through Amazon Bedrock AgentCore Gateway. Your agent decides when to run a workflow and what input to pass, and Step Functions runs each step exactly as you defined it. Agents can use your existing Standard and Express workflows as tools.
AWS Step Functions is a visual workflow service capable of orchestrating over 220 AWS services to help customers build distributed applications at scale. AgentCore Gateway connects AI agents to tools through the Model Context Protocol (MCP). With this launch, your agents can run multi-step business processes in the same order every time. For example, a customer support agent can start your refund workflow, and Step Functions runs the eligibility check, manager approval, and credit steps, so every refund follows your policy. Agents can also look up workflow runs, so an operations agent can tell your on-call engineer which order runs failed overnight and where, letting them go straight to fixing the step that broke.
This capability is available in all AWS Regions where Amazon Bedrock AgentCore Gateway is available. You pay standard rates for Step Functions and AgentCore Gateway.
To get started, follow the tutorial in the Step Functions Developer Guide. For all supported operations and setup options, see Step Functions connector targets in the AgentCore Gateway documentation. If you build with an AI coding assistant such as Kiro, the Agent Toolkit for AWS gives it skills and guidance for building on AWS.

## 핵심 요약

요약 미지원
