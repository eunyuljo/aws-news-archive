---
title: "Amazon Bedrock AgentCore Identity now offers a managed consent portal"
date: "2026-09-04"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-agentcore/"
tags: ["Bedrock", "2026", "new-region"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Identity now offers a managed consent portal

**날짜:** 2026년 09월 04일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-agentcore/

## 내용

Amazon Bedrock AgentCore Identity now offers a managed consent portal that eliminates the need for custom OAuth callback infrastructure when connecting agents to third-party tools and services. 
Developers using AgentCore Gateway to connect agents with services such as GitHub, Salesforce, and Slack previously had to build, host, and maintain custom OAuth callback infrastructure to complete OAuth 2.0 three-legged authorization (3LO) flows. The new managed consent portal eliminates this undifferentiated heavy lifting for agent developers and platform administrators. 
Each AgentCore Gateway receives its own managed consent portal with a dedicated hosted web client and credential provider list. Platform admins can share a portal URL with their team before sessions begin, granting consent for agents to call external tools on their behalf. End users can view their connection status at any time through a self-service interface without contacting an administrator. 
Developers using agent IDE-based clients, which cannot natively present OAuth consent URLs or handle post-consent session binding, can now use the managed consent portal as a dedicated authorization surface for these workflows. 
This feature is available in all commercial regions where Bedrock AgentCore Identity is available. 
To learn more, visit the Amazon Bedrock AgentCore Identity documentation.

## 핵심 요약

요약 미지원
