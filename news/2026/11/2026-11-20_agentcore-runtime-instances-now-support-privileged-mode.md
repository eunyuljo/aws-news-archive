---
title: "AgentCore runtime instances now support privileged mode"
date: "2026-11-20"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-elevated-privileges/"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# AgentCore runtime instances now support privileged mode

**날짜:** 2026년 11월 20일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-elevated-privileges/

## 내용

Amazon Bedrock AgentCore runtime instances now support privileged mode, which lets your agents install system-level software and run nested containers. Runtime instances run your agents on Amazon EC2 instances while AgentCore handles provisioning, patching, scaling, and lifecycle management. 
You turn on privileged mode when you create or update an agent runtime that runs on runtime instances. For example, a coding agent can start its service dependencies, such as Postgres and Redis, as containers and run its integration tests against them. A code-modernization agent can install the compilers and libraries that a migration needs. A session that runs a privileged agent runs only that agent, so elevated privileges stay with one agent on its instance. Agents that don't use privileged mode keep the default standard mode, so existing agents don't change. Standard mode suits most agents. Use privileged mode only if your agent needs to install system-level software or run containers. 
Privileged mode is available in all AWS Regions where AgentCore runtime instances are available. 
To get started, see the following resources: 
 
 Configure the privilege mode for runtime instances in the Amazon Bedrock AgentCore Developer Guide 
 AgentCore pricing

## 핵심 요약

요약 미지원
