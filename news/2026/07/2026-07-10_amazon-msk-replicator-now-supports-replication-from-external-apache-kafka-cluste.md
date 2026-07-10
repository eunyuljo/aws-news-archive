---
title: "Amazon MSK Replicator now supports replication from external Apache Kafka clusters to MSK Standard brokers"
date: "2026-07-10"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-msk-replicator-external-kafka-standard-broker-support"
tags: ["Config", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon MSK Replicator now supports replication from external Apache Kafka clusters to MSK Standard brokers

**날짜:** 2026년 07월 10일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-msk-replicator-external-kafka-standard-broker-support

## 내용

Amazon MSK Replicator now supports data replication from external Apache Kafka clusters - including on-premises, self-managed on AWS, or other cloud providers to Amazon MSK Standard brokers. This capability extends replication support to MSK Standard brokers, in addition to the existing support for MSK Express brokers. With this launch, you can migrate workloads to MSK Standard brokers, support disaster recovery by using MSK clusters as a failover or backup target, and enable data distribution across hybrid and multi-cloud environments.  MSK Replicator is a feature of Amazon MSK that automates data replication between Kafka clusters, eliminating the need to manage custom replication infrastructure or configure open-source tools. Previously, MSK Replicator supported replication from external Apache Kafka clusters to MSK Express brokers only. With this launch, you can now also replicate data from external Kafka clusters to MSK Standard brokers, using either SASL/SCRAM or mutual TLS (mTLS) authentication to connect to your external clusters. You can also use MSK Replicator to replicate data from Amazon MSK Standard to external Kafka clusters for reliable failback or multi-cloud data distribution. Unlike self-managed replication tools, MSK Replicator lets you retain your original Kafka topic names during replication while automatically avoiding infinite replication loops. It also synchronizes consumer group offsets bidirectionally, enabling you to move producers and consumers across clusters independently, in any order, without coordination constraints or the risk of data loss.  This new capability is supported in all AWS Regions where Amazon MSK Replicator is available. Visit the MSK Replicator documentation, product page, pricing page, and this AWS blog post to learn more.

## 핵심 요약

요약 미지원
