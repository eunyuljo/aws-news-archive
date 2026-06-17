---
title: "Amazon Bedrock AgentCore Memory now supports strictly consistent metadata for long-term memory"
date: "2026-06-17"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/05/agentcore-memory-scmetadata"
tags: ["RDS", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Memory now supports strictly consistent metadata for long-term memory

**날짜:** 2026년 06월 17일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/05/agentcore-memory-scmetadata

## 내용

Amazon Bedrock AgentCore Memory extracts useful information from short-term memory and stores it as long-term memory records. Metadata on these records helps organize, filter, and route them for retrieval. Previously, metadata values could only be inferred by the LLM during extraction. Now, you can also attach metadata values directly from your application, ensuring they pass through extraction and consolidation exactly as supplied with no LLM inference. When you set a metadata key's extraction type to STRICTLY_CONSISTENT, the value you provide on the short-term memory event is the value that lands on the resulting long-term memory record unchanged. 
Strictly consistent metadata also isolates how events are grouped. Events sharing the same values are extracted together and consolidated together. Records with different values are never merged, even if semantically similar. This enables department-scoped retrieval, compliance boundaries between regulated and standard records, and multi-tenant memory where each tenant's data is processed independently. 
You can configure up to three strictly consistent keys per strategy. The feature is supported on semantic, user preference, and episodic strategies, including custom overrides. Keys must be of type STRING and declared in the memory's indexed keys. Both LLM-inferred and strictly consistent keys can coexist on the same memory resource. To get started, see Long-term memory metadata. Amazon Bedrock AgentCore Memory strictly consistent metadata is available in all AWS Regions where AgentCore Memory is supported.

## 핵심 요약

요약 미지원
