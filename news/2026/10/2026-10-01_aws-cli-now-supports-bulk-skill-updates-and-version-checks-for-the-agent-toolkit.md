---
title: "AWS CLI now supports bulk skill updates and version checks for the Agent Toolkit for AWS"
date: "2026-10-01"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-cli-agent-toolkit-update-skill/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# AWS CLI now supports bulk skill updates and version checks for the Agent Toolkit for AWS

**날짜:** 2026년 10월 01일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-cli-agent-toolkit-update-skill/

## 내용

Today, AWS expanded the AWS Command Line Interface (CLI) commands for the Agent Toolkit for AWS with two new capabilities that make it easier to keep agent skills up to date. Customers can now run aws agent-toolkit check-skill-updates to compare all installed skills against the latest versions available in the registry, and use aws agent-toolkit update-skill --all to update every outdated skill in a single command.
The Agent Toolkit for AWS consists of the AWS MCP Server (which provides a secure, auditable agent interface to 15,000+ AWS APIs), agent skills (which give agents expert guidance across storage, networking, analytics, and more), and plugins (which bundle the MCP server and curate sets of skills into a single install). Previously, customers needed to check and update each skill individually. With these additions to AWS CLI, developers can quickly identify which skills have newer versions available and bring their entire skill set current without managing updates one at a time. This is especially useful for teams that have installed many skills across serverless, storage, networking, analytics, and other domains, and want to ensure their coding agents always operate with the latest guidance. These new commands are added to the existing set of AWS CLI capabilities for the Agent Toolkit, which already allows customers to install, search, and configure the AWS MCP Server and agent skills across Kiro, Claude Code, Codex, Cursor, and other popular coding agents.&nbsp;
To get started, see AWS CLI in the Agent Toolkit for AWS user guide. Make sure you have AWS CLI version 2.37.0 or later installed. The AWS MCP Server is available in the US East (N. Virginia) and Europe (Frankfurt) Regions.

## 핵심 요약

요약 미지원
