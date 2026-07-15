---
title: "AWS Security Hub now provides AI inventory for organization-wide visibility of AI assets"
date: "2026-07-15"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-ai/"
tags: ["EC2", "2026", "price-reduction", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# AWS Security Hub now provides AI inventory for organization-wide visibility of AI assets

**날짜:** 2026년 07월 15일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-ai/

## 내용

Today, AWS announces that AWS Security Hub now provides an AI inventory, giving central security teams a continuously updated, organization-wide view of AI assets and their security posture. As organizations rapidly deploy AI agents, models, and pipelines, security teams may lack visibility into what AI assets exist across their organization. Without centralized visibility connecting AI assets to active threats and misconfigurations, organizations cannot secure what they don't know exists. 
Security Hub AI inventory automatically discovers and catalogs AI workloads across your AWS environment through three discovery methods. For managed AI services, Security Hub inventories AWS Config resources from Amazon Bedrock, Bedrock AgentCore and Amazon SageMaker, with no additional configuration. For self-hosted AI workloads, Security Hub leverages the software bill of materials (SBOM) analysis from Amazon Inspector, which has been enhanced to identify inference endpoints, models and AI agents installed on Amazon EC2 instances and Amazon ECR container images, including frameworks such as Ollama, vLLM, Hugging Face TGI, and others. Security Hub also leverages Amazon GuardDuty DNS telemetry to discover external AI API endpoints (such as calls to third-party model providers) being accessed from your EC2 instances, revealing third-party AI dependencies that may not have been previously identified. 
&nbsp;Each discovered AI asset is mapped to its underlying infrastructure and correlated with security findings from across the AWS security stack, including threat findings from Amazon GuardDuty. Teams can filter, group, and query their AI inventory by account, resource type, discovery method, and specific model identity, enabling them to prioritize remediation based on which AI workloads are actively under threat and carry the highest organizational risk. 
AI Inventory is included with Security Hub Essentials at no additional cost and requires no new enablement. It is available in all AWS commercial Regions where Security Hub is offered. To learn more, see the AWS Security Hub User Guide and the AWS Security Hub product page.

## 핵심 요약

요약 미지원
