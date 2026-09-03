---
title: "Amazon SageMaker Unified Studio CI/CD adds notebook promotion and AI-assisted manifest generation"
date: "2026-09-03"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-cicd-notebook-ai-manifest/"
tags: ["S3", "2026", "new-region", "performance", "security", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker Unified Studio CI/CD adds notebook promotion and AI-assisted manifest generation

**날짜:** 2026년 09월 03일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-cicd-notebook-ai-manifest/

## 내용

Amazon SageMaker Unified Studio CI/CD expands its open-source deployment toolkit with two new capabilities: (1) an AI agent skill that automates manifest authoring, and (2) native notebook promotion across environments. Together, they help data teams go from project to production faster while maintaining best-practice defaults across stages. 
AI-assisted manifest generation. The new generate-bundle-manifest agent skill inspects a project's connections, storage, and workflows and produces a ready-to-use deployment manifest. It applies least-privilege IAM guidance, substitutes environment variables in place of hardcoded resource identifiers, and sets safe defaults such as opt-in catalog handling. Teams can import the skill into their own agents to standardize how they package and promote SageMaker Unified Studio projects across development, test, and production accounts. 
Native notebook promotion. The CI/CD toolkit now supports promoting native SMUS Notebooks alongside code, workflows, and catalog assets. Notebook promotion uses an in-place synchronization model that creates a notebook on first deployment and updates it on subsequent deployments, preserving run history across releases. Teams can promote every notebook in a project or select specific notebooks by ID, and a dry-run mode validates S3 connectivity, IAM permissions, and notebook counts before deployment. Notebook promotion integrates with the existing bundle, deploy, destroy, and dry-run commands and requires no changes to current pipeline structure. 
Both capabilities are open source and available in all AWS Regions where Amazon SageMaker Unified Studio is offered. 
To get started, visit the CICD-for-SageMakerUnifiedStudio repository on GitHub. For more information, see the CI/CD for Amazon SageMaker Unified Studio documentation.

## 핵심 요약

요약 미지원
