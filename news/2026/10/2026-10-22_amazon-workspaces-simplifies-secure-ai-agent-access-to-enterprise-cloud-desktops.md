---
title: "Amazon WorkSpaces simplifies secure AI agent access to enterprise cloud desktops with less infrastructure to operate and manage"
date: "2026-10-22"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/workspaces-ai-agents-oauth-connection-management"
tags: ["VPC", "2026", "GA", "price-reduction", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon WorkSpaces simplifies secure AI agent access to enterprise cloud desktops with less infrastructure to operate and manage

**날짜:** 2026년 10월 22일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/workspaces-ai-agents-oauth-connection-management

## 내용

WorkSpaces for AI agents now handles authentication and desktop connections as part of the managed Model Context Protocol (MCP) service, so you can connect agents to governed cloud desktops, removing the need to write custom code. This makes it easy to use WorkSpaces with any client that supports MCP. 
Connecting an agent to a desktop previously required you to manage presession requirements; generate, invoke, and rotate streaming URLs manually, adding complexity every time a session expired. You can now create sessions with your existing AWS credentials through OAuth 2.0, and the service handles the connection lifecycle. You configure once which desktop stack to use, and your agents reach the right desktop without ever seeing or handling the underlying streaming connection. You can also query session state to see which desktop stack, fleet, and session an agent is connected to, and generate a link for real-time observability of your agent. This gives you visibility and auditability over active agent work to know what your agents are doing and where. 
To help your agents work with multiple applications, they can now discover and launch applications through a catalog&nbsp;MCP Tool rather than navigating menus. Using these new tools, agents can list the available applications, launch one or several at runtime, and switch between them, replacing the start-menu and taskbar navigation with a programmatic, deterministic path that improves accuracy and reduces token cost.&nbsp; 
WorkSpaces for AI agents runs agent sessions inside the same network isolation and compliance boundaries that govern your human workforce, inheriting the VPC controls, data-loss prevention policies, and session-level security posture that enterprises have already configured. The service is also now available in four additional AWS Regions: South America (São Paulo), Europe (Milan), Europe (Spain), and Asia Pacific (Malaysia). 
To get started operating AI agents on WorkSpaces, visit: https://docs.aws.amazon.com/appstream2/latest/developerguide/agent-access.html.

## 핵심 요약

요약 미지원
