---
title: "AWS Lambda now supports a batch size of up to 10,000 messages for Amazon SQS FIFO queues"
date: "2026-11-21"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-10K-batch-size-SQSFIFO/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS Lambda now supports a batch size of up to 10,000 messages for Amazon SQS FIFO queues

**날짜:** 2026년 11월 21일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-10K-batch-size-SQSFIFO/

## 내용

AWS Lambda now supports a batch size of up to 10,000 messages for Amazon Simple Queue Service (Amazon SQS) FIFO queue event source mappings (ESMs) in provisioned mode, up from 10 messages previously. With larger batches, you can process high-volume, ordered workloads such as financial transactions, order processing, and inventory updates with fewer invocations and higher throughput. Lambda continues to preserve message ordering within each message group. 
Customers use SQS FIFO queues with Lambda to build event-driven applications that need strict message ordering and deduplication. With provisioned mode for SQS ESMs, you can use throughput controls to set a minimum and maximum number of event pollers to&nbsp;meet strict performance requirements. Previously, provisioned mode customers who needed higher throughput for SQS FIFO queues were limited by the maximum batch size of 10 messages. This required them to scale out invocations or add custom buffering logic, which added operational overhead and cost. With this launch, you can set a batch size of up to 10,000 messages and a batching window of up to 300 seconds for FIFO queues, so you can process large volumes of ordered messages in fewer invocations without re-architecting your applications. 
This feature is available for SQS FIFO ESMs in provisioned mode in all AWS commercial Regions. You can configure the batch size and the batching window when you create new ESMs or update existing ESMs by using the Lambda console, AWS CLI, AWS SDKs, AWS CloudFormation, AWS CDK, or AWS SAM. You can also use coding assistants such as Kiro, Claude Code, or Codex with the Agent Toolkit for AWS. To learn more, visit the AWS Lambda Developer Guide and the AWS Lambda pricing.&nbsp;&nbsp;&nbsp;&nbsp;

## 핵심 요약

요약 미지원
