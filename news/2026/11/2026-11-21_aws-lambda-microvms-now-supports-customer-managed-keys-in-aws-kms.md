---
title: "AWS Lambda MicroVMs now supports customer managed keys in AWS KMS"
date: "2026-11-21"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-microvms-customer-managed-keys/"
tags: ["Lambda", "2026", "GA", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# AWS Lambda MicroVMs now supports customer managed keys in AWS KMS

**날짜:** 2026년 11월 21일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-microvms-customer-managed-keys/

## 내용

AWS Lambda MicroVMs now supports customer managed keys (CMK) in AWS Key Management Service (KMS) for data encryption at rest. CMK gives you full control over the lifecycle and usage of your KMS keys, helping meet compliance requirements in regulated industries like financial services and healthcare. 
Lambda MicroVMs is a serverless compute primitive that provides VM-level isolation, near-instant launch and resume, and state preservation for executing user or AI generated code. Use MicroVMs to build applications like AI coding assistants, interactive development environments, and vulnerability scanners. 
To get started, create a CMK in AWS KMS and configure its cryptographic properties, metadata, and AWS IAM access permissions.&nbsp;Then, specify this CMK as a parameter when you create a MicroVM image or run a MicroVM. Lambda uses this CMK to encrypt your MicroVM image, MicroVM image environment variables, and the payload passed to the MicroVM run hook.&nbsp; You can use CMK with Lambda MicroVMs&nbsp;through the AWS Lambda console, AWS CloudFormation, AWS Cloud Development Kit, or with your preferred Agentic development tools using the Agent Toolkit for AWS. 
​​CMK support for MicroVMs is available in the following AWS Regions:&nbsp;Asia Pacific (Hong Kong), Asia Pacific (Malaysia), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Thailand), Asia Pacific (Tokyo), Europe (Frankfurt), Europe (Ireland), Europe (Spain), Europe (Stockholm), South America (São Paulo),&nbsp;US East (N. Virginia), US East (Ohio), and US West (Oregon). To learn more about Lambda MicroVMs, visit the AWS Lambda MicroVMs developer guide. For information on pricing for&nbsp;CMK, see AWS KMS pricing.​

## 핵심 요약

요약 미지원
