---
title: "Amazon Kinesis Data Streams announces queues to simplify and reduce costs of real-time processing"
date: "2026-11-18"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/kinesis-data-streams-queues/"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Kinesis Data Streams announces queues to simplify and reduce costs of real-time processing

**날짜:** 2026년 11월 18일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/kinesis-data-streams-queues/

## 내용

Amazon Kinesis Data Streams now supports queues, a simpler and more cost-effective way to process a stream. Because queues track the delivery state of each record, your consumer instances receive records instead of leasing shards, acknowledge each record when processing is complete, and scale beyond the number of shards. Kinesis Data Streams consumers can reduce the cost of processing data by up to 43% by using queues instead of the Kinesis Client Library.&nbsp;You no longer run a DynamoDB table or custom metrics, and you use compute more efficiently. 
Queues in Kinesis Data Streams are powered by Amazon SQS. Built on that foundation, a queue delivers records at least once, redelivers records your consumers do not acknowledge, and provides built-in dead-letter handling for records that keep failing. Each queue publishes its own CloudWatch metrics, so you can scale consumer instances on records waiting to be received and alarm on records that repeatedly fail. 
Use queues for applications that process each record independently, such as log processing, order fulfillment, and notifications. Use a stream consumer when processing one record depends on the records before it, such as live analytics, personalization, and anomaly detection. You ingest data once and let each application consume records through a queue or directly from the stream, with no change to your producers or existing stream consumers. For point-to-point messaging between application components, start with Amazon SQS. Choose queues in Kinesis Data Streams when the same records are needed by multiple applications. 
Queues are available for data streams in On-demand capacity mode. For regional availability, see Supported AWS Regions. To get started, see the developer guide, install the Kinesis Data Streams skill from the Agent Toolkit for AWS, read the launch blog, and see the pricing page.

## 핵심 요약

요약 미지원
