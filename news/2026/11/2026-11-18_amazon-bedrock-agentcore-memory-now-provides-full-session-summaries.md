---
title: "Amazon Bedrock AgentCore Memory now provides full session summaries"
date: "2026-11-18"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-bedrock-agentcore-memory-full-session-summaries"
tags: ["Bedrock", "2026", "new-region"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Memory now provides full session summaries

**날짜:** 2026년 11월 18일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-bedrock-agentcore-memory-full-session-summaries

## 내용

Amazon Bedrock AgentCore Memory now keeps a full session summary for every session. It's a single record that gives a snapshot of what happened in the conversation. Summary chunks cover the conversation in more detail, while the full session summary captures the overall picture of where the session stands. AgentCore Memory updates it as new events arrive, so it always reflects the session so far. This works well for developers who want a quick recap rather than a play-by-play. 
Full session summaries come with the summary strategy and need no extra setup. Every memory that has a summary strategy gets them automatically, including existing sessions. Each summary is stored as a long-term memory record next to the session's summary chunks. You retrieve it with the Memory operations you already use, and you can filter by record type to return only full session summaries. 
This feature is available in all AWS Regions where AgentCore Memory is available. To get started, see the Summary strategy documentation.

## 핵심 요약

요약 미지원
