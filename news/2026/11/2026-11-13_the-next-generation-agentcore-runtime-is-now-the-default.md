---
title: "The next generation AgentCore runtime is now the default"
date: "2026-11-13"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/new-agentcore-runtime-default/"
tags: ["Bedrock", "2026", "new-region"]
nav_exclude: true
---

# The next generation AgentCore runtime is now the default

**날짜:** 2026년 11월 13일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/new-agentcore-runtime-default/

## 내용

Starting today, new runtimes in Amazon Bedrock AgentCore use the next generation of AgentCore runtime by default. The new runtime restores each session from a snapshot of your initialized agent, scales compute and memory with the work, and scales idle agents to zero. Every session still runs in its own hardware-isolated Firecracker microVM. Your agents can run heavy work like compiling a large codebase, driving a browser, or loading a local model inside the session.&nbsp; 
Sessions scale to 8 vCPU and 32 GB of memory and support container images up to 10 GB. On a 2 GB image, sessions start in under 2 seconds at P75, down from 29.7 seconds on the previous generation. Idle agents scale to zero, and memory is reclaimed within minutes of release. For multi-turn agents, that means up to 68% less billed memory per session. 
Existing runtimes stay on the current version until you move them. To move an existing runtime, or to use the next generation in a Region where it isn't the default yet, set platformVersion to V2 when you create or update a runtime. To keep a new runtime on the current version, set platformVersion to V1. 
The new AgentCore Runtime is now the default runtime in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), South America (São Paulo), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Asia Pacific (Malaysia), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Thailand), and Asia Pacific (Tokyo). &nbsp;To learn more, visit the AgentCore runtime documentation or the AWS Blog. For pricing details, visit AgentCore pricing.

## 핵심 요약

요약 미지원
