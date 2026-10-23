---
title: "AgentCore Gateway now supports Bedrock InvokeModel APIs and model fallback"
date: "2026-10-23"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-gateway-invokemodel-fallback/"
tags: ["Bedrock", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# AgentCore Gateway now supports Bedrock InvokeModel APIs and model fallback

**날짜:** 2026년 10월 23일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-gateway-invokemodel-fallback/

## 내용

Amazon Bedrock AgentCore Gateway now supports the Amazon Bedrock InvokeModel and InvokeModelWithResponseStream APIs on its inference endpoint, along with model fallback routing for inference traffic. With InvokeModel support, you can point your existing Amazon Bedrock SDK integration at the gateway and reach any model provider through one governed endpoint, without rewriting client code for each provider. With model fallback, the gateway automatically routes a request to an alternative model or provider when the primary destination is throttled, out of capacity, or unreachable, so your agents stay available without each client implementing its own retry logic. 
For fallback routing, you define an ordered chain of alternative destinations in a gateway rule, along with the conditions that trigger a switch, such as throttling, server errors, or response timeouts. A built-in circuit breaker skips destinations that are currently failing, so requests reach a healthy destination faster and you avoid added latency for failed attempts. Fallback routing happens behind the scenes, which means you send one request and receive one response, regardless of the internal trial and error on a given request. 
These features are available in all AWS Regions where Amazon Bedrock AgentCore Gateway is available (except those in China). To learn more, see the Amazon Bedrock AgentCore Gateway User Guide.

## 핵심 요약

요약 미지원
