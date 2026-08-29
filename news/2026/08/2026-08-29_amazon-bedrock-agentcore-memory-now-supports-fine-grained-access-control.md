---
title: "Amazon Bedrock AgentCore Memory now supports fine-grained access control"
date: "2026-08-29"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/agentcorememory-fine-grained-access-control"
tags: ["RDS", "2026"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Memory now supports fine-grained access control

**날짜:** 2026년 08월 29일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/agentcorememory-fine-grained-access-control

## 내용

Amazon Bedrock AgentCore Memory now supports fine-grained access control (FGAC), enabling you to enforce per-user and per-tenant memory isolation through AgentCore Gateway without building custom authorization logic. 
 With FGAC, you can front your Memory resource with an AgentCore Gateway configured for OAuth (JWT) authentication and attach Cedar policies that restrict access based on the authenticated caller's identity. You can enforce that each user only accesses their own actor's data, restrict memory records to namespaces derived from the user's token claims, and allow or deny specific Memory operations per caller. This lets you move access control enforcement from application code to the infrastructure layer using cryptographic proof of identity. FGAC for Memory is built on the AgentCore Memory connector, a managed gateway connector that wires a gateway target to the Memory data plane and exposes 12 Memory operations as Cedar actions with their request attributes available for policy conditions. 
To get started, see Fine-grained access control for Memory in the Amazon Bedrock AgentCore Developer Guide.

## 핵심 요약

요약 미지원
