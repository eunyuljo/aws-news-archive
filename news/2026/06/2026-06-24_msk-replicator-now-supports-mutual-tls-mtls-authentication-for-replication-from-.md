---
title: "MSK Replicator now supports mutual TLS (mTLS) authentication for replication from external Apache Kafka clusters to MSK Express brokers"
date: "2026-06-24"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-msk-replicator-mtls-support"
tags: ["Config", "2026", "GA", "new-region"]
nav_exclude: true
---

# MSK Replicator now supports mutual TLS (mTLS) authentication for replication from external Apache Kafka clusters to MSK Express brokers

**날짜:** 2026년 06월 24일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-msk-replicator-mtls-support

## 내용

Amazon MSK Replicator now supports mutual TLS (mTLS) authentication for data replication from external Apache Kafka clusters - including on-premises, self-managed on AWS, or other cloud providers - to Amazon MSK Express brokers. With this capability, external Apache Kafka clusters configured with mTLS authentication can now use MSK Replicator to migrate workloads to MSK Express brokers, support disaster recovery by using MSK Express-based clusters as a failover or backup target, and enable data distribution across hybrid and multi-cloud environments.  MSK Replicator is a feature of Amazon MSK that automates data replication between Kafka clusters, eliminating the need to manage custom replication infrastructure or configure open-source tools. Previously, MSK Replicator supported SASL/SCRAM authentication only for connecting to external Apache Kafka clusters. With this launch, you can now also use mTLS authentication with MSK Replicator to replicate data from external Kafka clusters to Express brokers on Amazon MSK. Unlike self-managed replication tools, MSK Replicator lets you retain your original Kafka topic names during replication while automatically avoiding infinite replication loops. It also synchronizes consumer group offsets bidirectionally, enabling you to move producers and consumers across clusters independently, in any order, without coordination constraints or the risk of data loss.  This new capability is supported in all AWS Regions where MSK Express brokers are available. Visit the MSK Replicator documentation, product page, pricing page, and this AWS blog post to learn more.

## 핵심 요약

요약 미지원
