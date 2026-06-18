---
title: "AWS Secrets Manager introduces safe secrets handling in the Agent Toolkit for AWS"
date: "2026-06-18"
service: "SecretsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/safe-secrets-handling-in-agent-toolkit-for-aws/"
tags: ["SecretsManager", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Secrets Manager introduces safe secrets handling in the Agent Toolkit for AWS

**날짜:** 2026년 06월 18일
**서비스:** SecretsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/safe-secrets-handling-in-agent-toolkit-for-aws/

## 내용

AWS Secrets Manager now offers a secret safety skill as part of the aws-core plugin in the Agent Toolkit for AWS, an open-source repository that equips AI coding agents with tools, knowledge, and guardrails for building on AWS. The skill lets developers use secrets within agentic workflows without ever exposing secret values to the underlying model or session logs.  Until now, developers using AI coding agents could retrieve secrets as plain text without any guardrails, bringing sensitive values into agent context. With this skill, agents can securely retrieve and consume secrets without passing secret values through the context window, adding a layer of protection. To achieve this, the skill uses a two-layer approach. First, it steers the agent so the model never requests or receives a raw secret value—instead prompting the developer to clarify intent and constructing a command that uses the secret rather than retrieving it. Second, a child process resolves secret references to actual values only at execution time, outside the agent process. Together, these layers ensure plaintext secrets never appear in model context, session logs, or agent memory—without disrupting the developer's workflow.  The secret safety skill is available today for all agent harnesses supported by the Agent Toolkit for AWS—including Claude Code, Codex, and Cursor—and in all AWS Regions where Secrets Manager is available. To get started, visit the Agent Toolkit for AWS repository on GitHub and install the aws-core plugin for your preferred coding agent. For details, refer to the documentation.

## 핵심 요약

요약 미지원
