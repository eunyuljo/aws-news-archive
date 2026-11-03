---
title: "AWS Lambda now supports queues for Apache Kafka in self-managed Kafka event sources"
date: "2026-11-03"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-queue-kafka-esm/"
tags: ["Lambda", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# AWS Lambda now supports queues for Apache Kafka in self-managed Kafka event sources

**날짜:** 2026년 11월 03일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-queue-kafka-esm/

## 내용

AWS Lambda now supports queues for Apache Kafka in self-managed Kafka event source mappings (ESM), for Kafka clusters that customers run themselves and for managed offerings such as Confluent Cloud.&nbsp;Customers can now scale processing for Kafka workloads beyond the partition count of a topic, increasing throughput during traffic spikes and improving processing resilience. 
Customers building event-driven Kafka workloads for use cases such as image and video encoding, fraud detection, notification delivery, and telemetry ingestion treat each event as an independent unit of work, where processing speed matters more than strict ordering. Previously, Kafka ESMs used the Kafka consumer group protocol, which assigns each partition to exactly one consumer within a consumer group. Customers needing higher parallelism had to over-partition topics or move traffic to a separate queuing system, adding infrastructure to operate and producer code to maintain. Queue support for self-managed Kafka ESMs is built on Kafka share groups, which are generally available in Apache Kafka 4.2. This launch enables multiple event pollers to consume concurrently from the same partition, with each event poller supporting up to 10 concurrent invocations. This decouples parallelism from partition count with no changes to producers, topic configuration, or function code. As a result, customers get higher throughput during traffic spikes and more resilient processing, because a slow or failed event no longer holds up other events in the same partition. Queue mode does not preserve partition ordering and is intended for workloads that do not require it. 
This capability requires a Kafka cluster with share groups enabled, such as Apache Kafka 4.2 or later, and is available in all AWS commercial Regions where self-managed Kafka ESM is available. To get started, create a self-managed&nbsp;Kafka ESM with ConsumptionMode set to Queue through the AWS Management Console, Lambda API, AWS CLI, AWS CloudFormation, AWS SAM, or AWS CDK. Standard Lambda pricing applies. Customers who configure provisioned mode for their self-managed Kafka ESM also pay for Event Poller Unit (EPU) usage. To learn more, see the AWS Lambda Developer Guide and AWS Lambda pricing.&nbsp;&nbsp;&nbsp;&nbsp;

## 핵심 요약

요약 미지원
