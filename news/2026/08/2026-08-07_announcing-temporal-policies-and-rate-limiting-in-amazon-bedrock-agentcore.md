---
title: "Announcing temporal policies and rate limiting in Amazon Bedrock AgentCore"
date: "2026-08-07"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/"
tags: ["IAM", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Announcing temporal policies and rate limiting in Amazon Bedrock AgentCore

**날짜:** 2026년 08월 07일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/temporal-policies-agentcore/

## 내용

Amazon Bedrock AgentCore announces two new controls: temporal policies for stateful agent authorization and rate limiting for AI traffic. 
Temporal policies let you define stateful authorization rules that evaluate each request in the context of an agent's prior actions within a session, because a single tool call can be safe in isolation yet harmful given what preceded it. With temporal policies you can enforce workflow sequencing, require that a tool argument exactly matches the output of a prior call, require human approval before taking privileged actions, and enforce data freshness. 
Rate limiting enables per-user or per-group controls over how much traffic flows to the tools, models, and agents connected to your gateway. Using rules scoped by OAuth or AWS IAM, you can set rate limits on requests across all target types, tokens for inference targets, and concurrent connections to cap long-lived concurrent sessions, aiding downstream service availability and enforcing fair limit distribution.&nbsp; 
For regional availability and to learn more, see the documentation, read the announcement blog, and explore the Dogwood reference implementation.&nbsp;

## 핵심 요약

요약 미지원
