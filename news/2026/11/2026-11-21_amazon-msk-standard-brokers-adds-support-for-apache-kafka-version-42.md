---
title: "Amazon MSK Standard Brokers adds support for Apache Kafka version 4.2"
date: "2026-11-21"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-msk-standard-version-42/"
tags: ["General", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon MSK Standard Brokers adds support for Apache Kafka version 4.2

**날짜:** 2026년 11월 21일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-msk-standard-version-42/

## 내용

Amazon Managed Streaming for Apache Kafka (Amazon MSK) now supports Apache Kafka version 4.2 on Standard brokers. A key highlight of this release is Queues for Kafka, which is now production ready. With Queues, multiple consumers can process messages from the same topic partitions, which improves parallelism and throughput for workloads that need point-to-point message delivery. This release also includes Eligible Leader Replicas (ELR) enhancements that improve leader election correctness and strengthen availability. The new consumer rebalance protocol makes consumer group rebalances smoother and faster. The new Streams Rebalance Protocol extends broker-side coordination to Kafka Streams applications so tasks get assigned more efficiently. For the full list of improvements and bug fixes, see the Apache Kafka 4.2 release notes. 
To start using Apache Kafka 4.2 on Amazon MSK, select version 4.2.x when creating a new cluster with the AWS Management Console, AWS CLI, or AWS SDKs. You can also upgrade existing MSK provisioned clusters with an in-place rolling update. Amazon MSK orchestrates broker restarts to maintain availability and protect your data during the upgrade. Kafka version 4.2 support is available today in all AWS regions where Amazon MSK Standard brokers is offered. To learn how to get started, see the Amazon MSK Developer Guide.

## 핵심 요약

요약 미지원
