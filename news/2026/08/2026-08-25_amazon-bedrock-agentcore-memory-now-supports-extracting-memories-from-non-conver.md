---
title: "Amazon Bedrock AgentCore Memory now supports extracting memories from non-conversational JSON payloads"
date: "2026-08-25"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/agentcore-memory-json-payloads"
tags: ["Bedrock", "2026", "new-region"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Memory now supports extracting memories from non-conversational JSON payloads

**날짜:** 2026년 08월 25일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/agentcore-memory-json-payloads

## 내용

Amazon Bedrock AgentCore memory now accepts a JSON payload type on the CreateEvent API, so agents can extract and consolidate long-term memories from structured data as well as from multi-turn conversations. Developers can pass behavioral events, activity logs, system events, and other JSON data (up to 100 KB per payload) straight into the extraction pipeline. There is no need to reshape it into synthetic conversation messages first.  The extraction pipeline treats a JSON payload the same way it treats a conversation, generating long-term memories across all four extraction strategies: semantic, user preference, summarization, and episodic. 
Non-conversational JSON payload ingestion is available today in all regions where AgentCore Memory is supported. It is fully compatible with existing features. To get started, just add json payloads to your events.

## 핵심 요약

요약 미지원
