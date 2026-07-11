---
title: "Amazon EMR on EKS now supports Apache Spark troubleshooting agent"
date: "2026-07-11"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-emr-eks-spark-troubleshooting/"
tags: ["EC2", "2026", "GA", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon EMR on EKS now supports Apache Spark troubleshooting agent

**날짜:** 2026년 07월 11일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-emr-eks-spark-troubleshooting/

## 내용

Amazon EMR on EKS now supports the Apache Spark troubleshooting agent. Data engineers can now diagnose EMR on EKS job failures through natural language, receiving automated root cause analysis and PySpark code recommendations without manually navigating distributed logs and Spark History Server data.  The agent analyzes Spark History Server data, distributed executor logs, and cluster configurations to identify issues such as memory errors, data skew, resource contention, and connectivity failures. With this launch, the Spark troubleshooting agent now covers all EMR deployment options: EMR on EC2, EMR Serverless, and EMR on EKS. The agent is accessible directly from the EMR on EKS console through a "Troubleshoot with AI" option on failed jobs. Additionally, the agent is available through MCP (Model Context Protocol) using any compatible AI coding agent, including Kiro, Claude Code, and Cursor. All operations are read-only, authenticated with IAM roles, and logged in AWS CloudTrail.  The Spark troubleshooting agent for Amazon EMR on EKS is available in all AWS Regions where the SageMaker Unified Studio is available. To get started, go to EMR on EKS console, or set up the MCP server in your preferred AI coding agent. For detailed guidance, see the EMR troubleshooting agent documentation.

## 핵심 요약

요약 미지원
