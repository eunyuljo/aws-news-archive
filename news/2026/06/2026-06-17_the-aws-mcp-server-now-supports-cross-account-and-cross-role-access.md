---
title: "The AWS MCP Server now supports cross-account and cross-role access"
date: "2026-06-17"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-mcp-server/"
tags: ["Lambda", "2026", "new-region", "performance", "security", "ai-ml"]
nav_exclude: true
---

# The AWS MCP Server now supports cross-account and cross-role access

**날짜:** 2026년 06월 17일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-mcp-server/

## 내용

Today, AWS announced cross-account and cross-role access for the AWS Model Context Protocol (MCP) Server, part of the Agent Toolkit for AWS. This feature allows developers using AI coding agents like Kiro, Claude Code, or Codex to work across multiple AWS accounts and AWS Identity and Access Management (IAM) roles within a single session, with no restarts required. Previously, switching profiles required stopping the AI coding session, updating local AWS credentials, and restarting the MCP server for every account change. Now, AI agents using the AWS MCP Server can specify a profile on each command, allowing users to switch between accounts and roles seamlessly. 
 Cross-account access helps developers move faster across multi-account environments. For example, a DevOps engineer can query CloudWatch logs across production and staging accounts to diagnose a performance issue, or an application developer can update a Lambda configuration in one account and adjust an S3 bucket policy in another, all within the same conversation. Each request specifies which profile to use, so there is no risk of commands reaching the wrong account. 
To get started, see Multi-profile support in the Agent Toolkit for AWS user guide.&nbsp;The AWS MCP Server is available in the US East (N. Virginia) and Europe (Frankfurt) Regions.

## 핵심 요약

요약 미지원
