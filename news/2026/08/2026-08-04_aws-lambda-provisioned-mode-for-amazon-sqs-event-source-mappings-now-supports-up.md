---
title: "AWS Lambda Provisioned Mode for Amazon SQS event source mappings now supports up to 10,000 event pollers"
date: "2026-08-04"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-Lambda-provisioned-sqs-esm-max-pollers/"
tags: ["Lambda", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# AWS Lambda Provisioned Mode for Amazon SQS event source mappings now supports up to 10,000 event pollers

**날짜:** 2026년 08월 04일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-Lambda-provisioned-sqs-esm-max-pollers/

## 내용

AWS Lambda now supports a maximum of 10,000 event pollers for Provisioned Mode for Amazon SQS event source mappings (ESMs), a 5x increase from the previous limit of 2,000. This enables you to reach up to 100,000 concurrent invocations, so you can build highly responsive and scalable event-driven applications with stringent performance requirements. 
 Customers use Amazon SQS as an event source for Lambda to build mission-critical applications such as real-time order processing, financial transaction pipelines, IoT telemetry ingestion, and large-scale fan-out workloads, where delays in event processing can directly impact business outcomes. Provisioned Mode for SQS ESM allows you to configure a minimum and maximum number of event pollers and optimize the throughput for your application.&nbsp;However, the maximum number of pollers was previously limited to 2,000, which constrained the number of concurrent invocations that could be reached per ESM, and required customers to split their workload across multiple ESMs. With this launch, customers can reach up to 10,000 event pollers and 100,000 concurrent invocations per ESM, enabling them to build at-scale workloads with stringent latency and throughput requirements. 
 This feature is generally available in all AWS Commercial Regions. You can activate Provisioned Mode for SQS ESM by configuring a minimum and maximum number of event pollers using the ESM API, AWS Console, AWS CLI, AWS SDK, AWS CloudFormation, and AWS SAM. You pay for the usage of event pollers based on a billing unit called Event Poller Unit (EPU). To learn more, read the Lambda ESM documentation and AWS Lambda pricing.

## 핵심 요약

요약 미지원
