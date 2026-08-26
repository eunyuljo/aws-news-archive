---
title: "MSK Replicator now supports OAuth 2.0 (SASL/OAUTHBEARER) authentication for replication from external Apache Kafka clusters to Amazon MSK"
date: "2026-08-26"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-msk-replicator-OAuth-support"
tags: ["Config", "2026", "GA", "new-region"]
nav_exclude: true
---

# MSK Replicator now supports OAuth 2.0 (SASL/OAUTHBEARER) authentication for replication from external Apache Kafka clusters to Amazon MSK

**날짜:** 2026년 08월 26일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-msk-replicator-OAuth-support

## 내용

Amazon MSK Replicator now supports OAuth 2.0 (SASL/OAUTHBEARER) authentication for data replication from external Apache Kafka clusters - including on-premises, self-managed on AWS, or other cloud providers - to Amazon MSK Provisioned clusters. With this capability, external Apache Kafka clusters configured with OAuth/OIDC authentication can now use MSK Replicator to migrate workloads to Amazon MSK, support disaster recovery by using MSK-based clusters as a failover or backup target and enable data distribution across hybrid and multi-cloud environments. 
MSK Replicator is a feature of Amazon MSK that automates data replication between Kafka clusters, eliminating the need to manage custom replication infrastructure or configure open-source tools. Previously, MSK Replicator supported SASL/SCRAM and mTLS authentication for connecting to external Apache Kafka clusters. With this launch, you can now also use OAuth 2.0 authentication with MSK Replicator to replicate data from external Kafka clusters to Amazon MSK. Unlike self-managed replication tools, MSK Replicator lets you retain your original Kafka topic names during replication while automatically avoiding infinite replication loops. It also synchronizes consumer group offsets bidirectionally, enabling you to move producers and consumers across clusters independently, in any order, without coordination constraints or the risk of data loss. 
This new capability is supported in all AWS Regions where MSK Replicator is available. Visit the MSK Replicator documentation, product page, pricing page, and this AWS blog post to learn more.

## 핵심 요약

요약 미지원
