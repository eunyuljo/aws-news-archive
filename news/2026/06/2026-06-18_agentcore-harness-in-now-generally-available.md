---
title: "AgentCore harness in now generally available"
date: "2026-06-18"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available"
tags: ["Bedrock", "2026", "GA", "new-region", "performance", "security"]
nav_exclude: true
---

# AgentCore harness in now generally available

**날짜:** 2026년 06월 18일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available

## 내용

Today, AWS announces the general availability of the managed agent harness in Amazon Bedrock AgentCore, taking teams from idea to working agents in minutes. An agent is more than a model. If the model is the brain, the harness is the body: everything the brain needs to get work done. It runs the orchestration loop, executes tools, manages the context window, persists state across turns, recovers from failures, and isolates each session. The harness shapes how well an agent performs as much as the model does, and building a durable one is where most teams spend their time today. AgentCore harness provides that layer as a managed capability. Instead of coding the loop, customers define an agent in configuration: the model it uses, the tools it calls, the skills it accesses, and the instructions it follows, and AgentCore assembles and runs that loop. From that single definition, a production-grade agent runs in minutes in its own isolated environment, with a filesystem and shell, memory across sessions, skills including the AWS-curated catalog, and web browsing. This is not a starter tool teams outgrow: the configuration they start with is what they operate at scale, and when custom orchestration is needed, the harness exports to code on the same platform without rebuilding anything.  Besides speed, AgentCore decouples the harness from the model. Customers can choose any model and switch providers mid-session without losing context or touching agent logic, for example planning with one model and writing code with another. The harness is also one piece of a single platform, not a hosting layer wrapped around a framework. It reaches tools through the same gateway that enforces security policies, and connects the agent to organizational knowledge and web search. Identity, memory, and observability come from that same platform, so every agent action is governed and traced from the first call without additional wiring. When a use case needs custom orchestration, a single CLI command exports the harness to Strands-based code on the same compute and primitives, with Claude Agent SDK coming soon as an export target. The agent declared on day one is the agent that runs at the thousandth, on the same foundation throughout.  AgentCore harness is generally available today in all AWS Commercial Regions where AgentCore is available. Learn more using the documentation.&nbsp;

## 핵심 요약

요약 미지원
