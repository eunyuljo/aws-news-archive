---
title: "AWS introduces Lambda MicroVMs for isolated execution of user and AI-generated code"
date: "2026-06-23"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-microvms/"
tags: ["Lambda", "2026", "GA", "new-region", "performance", "security", "ai-ml"]
nav_exclude: true
---

# AWS introduces Lambda MicroVMs for isolated execution of user and AI-generated code

**날짜:** 2026년 06월 23일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-microvms/

## 내용

AWS introduces Lambda MicroVMs, a new serverless compute primitive that provides VM-level isolation, near-instant launch and resume speeds, and state preservation for executing user or AI-generated code. You can now give each user or job their own compute environment to securely run code without managing virtualization infrastructure or choosing between isolation, speed, and state retention. 
Developers are increasingly building multi-tenant applications that execute code supplied by end users or AI for use cases such as interactive coding environments, data analytics platforms, coding assistants, and vulnerability scanning platforms. For these applications, developers need to allocate a separate, isolated execution environment per user or session to limit the impact of incorrect or malicious code on other concurrently running users or jobs. Previously, developers needed to choose between strong isolation, fast launch times, and state retention when building these applications. Starting today, Lambda MicroVMs provides you these capabilities without any trade-offs. You get VM-level isolation, near-instant launch speeds, and the ability to suspend and resume execution for up to 8 hours. Lambda MicroVMs is built on Firecracker virtualization, the technology powering more than 15 trillion monthly Lambda Function invocations.&nbsp; 
To get started, create a MicroVM image from your Dockerfile, then launch MicroVMs from that image. Give each user or job their own MicroVM with a dedicated HTTPS URL that supports popular connectivity protocols such as HTTP/2, gRPC, and WebSockets.&nbsp; 
Lambda MicroVMs is available today in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Tokyo), and Europe (Ireland). To learn more, visit the AWS Lambda MicroVMs developer guide&nbsp;and the launch blog post. Get started with MicroVMs through the AWS Lambda console, AWS CloudFormation, AWS Cloud Development Kit, or use the Agent Toolkit for AWS&nbsp;with your preferred Agentic development tools. You pay for baseline compute resources while your MicroVM is running, and only for the active duration of additional resources consumed when your workload exceeds the baseline. To learn more about pricing, see Lambda MicroVMs pricing.

## 핵심 요약

요약 미지원
