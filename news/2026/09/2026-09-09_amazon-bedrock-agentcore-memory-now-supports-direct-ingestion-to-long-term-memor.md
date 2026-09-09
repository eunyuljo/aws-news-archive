---
title: "Amazon Bedrock AgentCore Memory now supports direct ingestion to long-term memory"
date: "2026-09-09"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/agentcore-memory-direct-ingest"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Memory now supports direct ingestion to long-term memory

**날짜:** 2026년 09월 09일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/agentcore-memory-direct-ingest

## 내용

Amazon Bedrock AgentCore Memory now lets developers submit content directly for long-term memory extraction without persisting it as a short-term memory event. The new IngestData API accepts content, fans it out to the memory's configured long-term memory strategies, and makes the resulting memory records available through the same retrieval operations used for any other long-term memory records, all without creating a short-term event.  Until now, all content had to be stored as a short-term memory event before extraction strategies could process it into long-term memory records. IngestData removes this requirement, enabling developers to adopt long-term memory independently of short-term memory.  IngestData supports both conversational payloads (messages with USER/ASSISTANT roles) and JSON payloads (behavioral events, activity logs, system events), and accepts optional metadata that feeds the same extraction pipeline as CreateEvent. After processing, developers can verify extraction results with ListMemoryRecords or RetrieveMemoryRecords, stream real-time notifications via Kinesis, and redrive failed extractions with ListMemoryExtractionJobs. To get started, see Direct ingestion to long-term memory in the Amazon Bedrock AgentCore Developer Guide. IngestData is available in all AWS Regions where Amazon Bedrock AgentCore Memory is supported.

## 핵심 요약

요약 미지원
