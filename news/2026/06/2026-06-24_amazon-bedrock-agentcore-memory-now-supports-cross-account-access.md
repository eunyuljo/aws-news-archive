---
title: "Amazon Bedrock AgentCore Memory now supports cross-account access"
date: "2026-06-24"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/agentcore-memory-cross-account-access"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Memory now supports cross-account access

**날짜:** 2026년 06월 24일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/agentcore-memory-cross-account-access

## 내용

Amazon Bedrock AgentCore Memory now enables cross-account access, allowing you to build multi-account architectures where memory resources and consuming agents span multiple AWS accounts. You can grant principals in one account permission to call memory data plane APIs against resources in another account using resource-based policies, and configure memory delivery destinations (Amazon S3, Amazon SNS, Amazon Kinesis Data Streams) that reside in a separate account. 
Cross-account access is configured by attaching a resource-based policy to your memory resource. Once configured, principals in the consuming account can create events, write memory records, retrieve records, and perform semantic search by referencing the full memory ARN. Cross-account delivery destinations allow your memory resource to deliver payloads and stream events to S3 buckets, SNS topics, and Kinesis Data Streams in other accounts. 
To get started, see Cross-account memory access in the Amazon Bedrock AgentCore Developer Guide. Amazon Bedrock AgentCore Memory cross-account access is available in all AWS Regions where Amazon Bedrock AgentCore Memory is supported.&nbsp;&nbsp;&nbsp;&nbsp;

## 핵심 요약

요약 미지원
