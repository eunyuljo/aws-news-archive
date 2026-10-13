---
title: "Announcing consumption-based pricing for short-term memory in Amazon Bedrock AgentCore"
date: "2026-10-13"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-memory-consumption-based-pricing"
tags: ["Bedrock", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Announcing consumption-based pricing for short-term memory in Amazon Bedrock AgentCore

**날짜:** 2026년 10월 13일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-memory-consumption-based-pricing

## 내용

Announcing consumption-based pricing for short-term memory in Amazon Bedrock AgentCore
Amazon Bedrock AgentCore memory now prices short-term memory (STM) based on the data your agents ingest, retrieve, and store, replacing the previous flat rate per event. AgentCore memory gives agents in-session context through short-term memory and persistent knowledge across sessions through long-term memory. With consumption-based pricing, developers building agents that write frequent, small events pay in proportion to what they use.
STM is priced across three dimensions: ingestion at $1.00 per GB, retrieval at $0.20 per GB, and storage at $0.10 per GB-month. Ingestion and retrieval are billed per event with a 12 KB minimum and 64 KB maximum billable size, while storage is billed on each event's actual size. Most workloads see lower costs, with small-payload use cases seeing the largest reductions. You can manage storage costs by setting a shorter time to live (TTL) on your memory resources. Long-term memory pricing is unchanged.
Consumption-based pricing for AgentCore Memory short-term memory is available in all AWS Regions where AgentCore Memory is offered. To get started, visit the Amazon Bedrock AgentCore pricing page.

## 핵심 요약

요약 미지원
