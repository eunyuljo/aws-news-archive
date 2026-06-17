---
title: "AWS Transform now supports model-to-model migration assessment for generative AI workloads"
date: "2026-06-17"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-transform-model-to-model-assessments"
tags: ["CloudWatch", "2026", "price-reduction", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# AWS Transform now supports model-to-model migration assessment for generative AI workloads

**날짜:** 2026년 06월 17일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-transform-model-to-model-assessments

## 내용

AWS Transform now offers a model-to-model migration custom transformation that assesses your generative AI workloads and produces a comprehensive migration plan for moving from third-party providers to Amazon Bedrock. The AI-powered agent scans your codebase, identifies every AI SDK and model in use, gathers your migration requirements through interactive questions, and maps models to Bedrock equivalents with transparent cost comparisons and production-ready code changes. This managed custom transformation helps organizations consolidate their AI workloads on AWS to gain IAM-based security, VPC endpoint isolation, prompt caching, Amazon Bedrock Guardrails, and unified operational tooling through Amazon CloudWatch. &nbsp;  The transformation supports migrations from OpenAI, Google Gemini, direct Anthropic SDK usage, and open-source models via LiteLLM or Ollama. It handles direct SDK integrations, framework-wrapped patterns such as LangChain and LlamaIndex, agentic architectures including CrewAI and LangGraph, and multi-provider routing layers — preserving your application architecture while swapping only the model layer. The agent includes intelligent cost optimization with tiered model routing recommendations, prompt caching analysis, and model lifecycle awareness that excludes models within 90 days of end-of-life from all recommendations. For some workloads, it recommends Amazon Bedrock's OpenAI-compatible endpoints as a zero-code-change migration path. 
AWS Transform model-to-model migration is available in all AWS Regions where AWS Transform&nbsp;is offered, at no additional charge beyond standard AWS Transform pricing. To get started, install the ATX CLI and run the mke-genai-model-migration custom transformation against your codebase. To learn more, see the AWS Transform Custom Transformations documentation&nbsp;and the announcement blog.

## 핵심 요약

요약 미지원
