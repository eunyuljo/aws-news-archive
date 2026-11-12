---
title: "AWS Lambda MicroVMs now supports the x86 CPU architecture"
date: "2026-11-12"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-microvms-x86-architecture/"
tags: ["Lambda", "2026", "GA", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# AWS Lambda MicroVMs now supports the x86 CPU architecture

**날짜:** 2026년 11월 12일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-microvms-x86-architecture/

## 내용

AWS Lambda MicroVMs now supports the x86 CPU architecture, so you can run your existing x86 applications, tools, and software dependencies without recompiling or porting them. When you create a MicroVM image, you can now choose between x86 and Arm (AWS Graviton) to give each user or job an isolated MicroVM on the architecture your workload uses. 
Lambda MicroVMs is a serverless compute primitive that provides VM-level isolation, near-instant launch and resume, and state preservation for running user or AI-generated code, in applications such as AI coding assistants, CI/CD runners, interactive development environments, and vulnerability scanners. Today’s launch enables you to run x86-based workloads on Lambda MicroVMs as-is. For workloads that run on Arm, you can continue using AWS Graviton processors which is the default CPU architecture option. 
To start building x86 workloads on Lambda MicroVMs, choose the x86 architecture when you create a MicroVM image from your Dockerfile, then launch MicroVMs from that image. You can use&nbsp;MicroVMs through the AWS Lambda console, AWS CloudFormation, AWS Cloud Development Kit, or with your preferred agentic development tools using the Agent Toolkit for AWS. 
Support for the x86&nbsp;CPU architecture is available in all AWS Regions where Lambda MicroVMs is available, except Asia Pacific (Hong Kong), Asia Pacific (Malaysia), Asia Pacific (Thailand), and Europe (Spain). To learn more, visit the AWS Lambda MicroVMs developer guide. For information on pricing, see Lambda MicroVMs pricing.

## 핵심 요약

요약 미지원
