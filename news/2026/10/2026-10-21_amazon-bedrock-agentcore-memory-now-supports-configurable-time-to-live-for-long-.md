---
title: "Amazon Bedrock AgentCore Memory now supports configurable time-to-live for long-term memory"
date: "2026-10-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-memory-long-term-memory-ttl"
tags: ["RDS", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Memory now supports configurable time-to-live for long-term memory

**날짜:** 2026년 10월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-memory-long-term-memory-ttl

## 내용

Amazon Bedrock AgentCore Memory now lets you set a time-to-live (TTL) on long-term memory records, so they are automatically deleted after a retention period you define. By default, long-term memory records do not expire. With this launch, you can configure a TTL to meet data-retention requirements, control storage growth, and ensure that stale insights age out of a memory over time. 
You can configure retention on the resource or specific records. Configuring or removing a TTL requires the new bedrock-agentcore:UpdateMemoryRecordExpirySpecification permission, giving you independent control over who can set record retention. 
To learn more, see Set a time-to-live for long-term memory records in the Amazon Bedrock AgentCore Developer Guide. This feature is available in all AWS Regions where Amazon Bedrock AgentCore Memory is supported.

## 핵심 요약

요약 미지원
