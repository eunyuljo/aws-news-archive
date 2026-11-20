---
title: "AgentCore runtime instances now support Nested Virtualization"
date: "2026-11-20"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-nested-virtualization/"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# AgentCore runtime instances now support Nested Virtualization

**날짜:** 2026년 11월 20일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-nested-virtualization/

## 내용

Amazon Bedrock AgentCore runtime instances now support nested virtualization, so your agents can run their own virtual machines and emulators inside a session with Kernel-based Virtual Machine (KVM). Runtime instances run your agents on Amazon EC2 instances while AgentCore handles provisioning, patching, scaling, and lifecycle management. Nested virtualization serves agents that rely on tools that run in a virtual machine, such as mobile emulators or virtual machine sandboxes. 
You turn on nested virtualization when you create a Linux capacity provider, and agents in every session on its instances can use KVM. For example, your agents can run Android emulators to build and test mobile apps, or start lightweight virtual machines to isolate the code that they run. Nested virtualization works on supported Intel-based instance types, including the C7i, C8i, M7i, M8i, R7i, and R8i families. 
Nested virtualization is available on supported instance types in all AWS Regions where AgentCore runtime instances are available. 
To get started, see the following resources: 
 
 Run virtual machines in agents on runtime instances in the Amazon Bedrock AgentCore Developer Guide 
 AgentCore pricing

## 핵심 요약

요약 미지원
