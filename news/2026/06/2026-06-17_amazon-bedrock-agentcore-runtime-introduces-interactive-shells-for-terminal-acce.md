---
title: "Amazon Bedrock AgentCore Runtime introduces interactive shells for terminal access into agent sessions"
date: "2026-06-17"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-runtime/"
tags: ["Bedrock", "2026"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Runtime introduces interactive shells for terminal access into agent sessions

**날짜:** 2026년 06월 17일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-runtime/

## 내용

Amazon Bedrock AgentCore Runtime now supports interactive shells through a new InvokeAgentRuntimeCommandShell API, opening a persistent, PTY-backed terminal directly into a running agent session over WebSocket. This complements the existing InvokeAgentRuntimeCommand API for one-shot execution, giving developers a full terminal experience inside an isolated microVM with colors, tab completion, Ctrl+C, terminal resize, and automatic reconnect on network drop.  This is particularly important for developers hosting coding agents such as Claude Code, OpenAI Codex, Amazon Kiro on AgentCore Runtime. In addition to the asynchronous command execution they already had, they can now authenticate, drop into the microVM hosting their coding agent, and interact with it like a local terminal: interact with the agent, inspect files, run ad-hoc commands, or debug the environment state. The shell carries persistent state across commands within the same session, so environment variables, working directory, and command history all behave as expected.  Each interactive session is identified by a runtime session ID and a shell ID. Passing both back when reconnecting lands you in the exact same shell. Brief network drops reconnect automatically, and longer disconnects can be resumed manually using the same IDs. A single agent runtime supports up to 10 concurrent shells, allowing developers to open multiple terminals against the same or multiple microVMs and watch agents work different branches in parallel.  To get started using the AgentCore CLI: `agentcore exec --it --runtime &lt;runtime-arn&gt;`. To learn more, see Interactive Shells (Terminals) and Shell execution in AgentCore Runtime for a comparison of both shell modes.

## 핵심 요약

요약 미지원
