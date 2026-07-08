---
title: "Amazon GameLift Streams introduces secure terminal access for stream sessions"
date: "2026-07-08"
service: "SystemsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams-terminal-access/"
tags: ["SystemsManager", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon GameLift Streams introduces secure terminal access for stream sessions

**날짜:** 2026년 07월 08일
**서비스:** SystemsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams-terminal-access/

## 내용

Amazon GameLift Streams now supports Stream Session Admin Shell, a secure terminal connection to the live runtime environment of a stream session for real-time troubleshooting. You can inspect logs, query running processes, check GPU utilization, and examine application state — all without managing SSH keys, open ports, or infrastructure credentials.  Stream Session Admin Shell provides a terminal connection with the same level of access as your Amazon GameLift Streams applications. To connect, call the new CreateStreamSessionAdminShell API with your stream group and stream session identifiers, then use the returned credentials with the SSM Session Manager plugin for the AWS CLI. The feature supports Linux (Ubuntu 22.04), Proton, and Windows Server 2022 runtimes. The terminal connection is scoped to your application environment and automatically closes when the stream session ends.  Stream Session Admin Shell is available at no additional cost in all AWS Regions where Amazon GameLift Streams is offered. For a full list of supported Regions, see the AWS Region table.  To get started, see the Stream Session Admin Shell developer guide and CreateStreamSessionAdminShell API reference.

## 핵심 요약

요약 미지원
