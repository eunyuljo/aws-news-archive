---
title: "AWS announces Nx Plugin for AWS for scaffolding full-stack applications"
date: "2026-09-09"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/nx-plugin-for-aws/"
tags: ["CloudWatch", "2026", "GA", "security", "ai-ml"]
nav_exclude: true
---

# AWS announces Nx Plugin for AWS for scaffolding full-stack applications

**날짜:** 2026년 09월 09일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/nx-plugin-for-aws/

## 내용

Version 1.0 of the Nx Plugin for AWS, an open source toolkit for scaffolding full-stack applications on AWS, is now available. AI assistants can stand up an application on AWS in minutes, but rarely get security, observability, and type-safety right in one pass. The plugin extends Nx, an open source, language-agnostic build system for monorepos, with generators that each build one part of an application on request, alongside the infrastructure to run it. 
Generators cover AI agents and Model Context Protocol servers on Amazon Bedrock AgentCore, plus APIs, websites, and databases, built on proven open source frameworks in TypeScript and Python. Each writes out a working, deployable piece of your application, defining infrastructure as either AWS Cloud Development Kit (AWS CDK) constructs or Terraform modules, with recommended practices in place such as AWS WAF protection, access logging to Amazon CloudWatch, and AWS X-Ray tracing. The connection generator wires projects together with type-safe clients, so a breaking API change becomes a build error instead of a failed request in production. 
Each generator produces the same result every time, making it a dependable foundation for an AI assistant to build on. The generated code belongs to you, with no runtime dependency on the plugin, and Nx migrations bring later improvements to workspaces you have customized. 
The plugin is available under the Apache 2.0 license at no additional charge; you pay only for the AWS resources your applications use. To learn more, see the launch blog post and documentation.

## 핵심 요약

요약 미지원
