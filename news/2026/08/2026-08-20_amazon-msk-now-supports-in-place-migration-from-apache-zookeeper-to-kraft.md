---
title: "Amazon MSK now supports in-place migration from Apache ZooKeeper to KRaft"
date: "2026-08-20"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-msk-zk-kraft-migration/"
tags: ["Config", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon MSK now supports in-place migration from Apache ZooKeeper to KRaft

**날짜:** 2026년 08월 20일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-msk-zk-kraft-migration/

## 내용

Amazon Managed Streaming for Apache Kafka (Amazon MSK) now supports in-place migration from Apache ZooKeeper to KRaft, enabling customers to migrate existing clusters to KRaft without provisioning new infrastructure, migrating data, or reconfiguring client applications.  KRaft is Apache Kafka's consensus protocol that eliminates the dependency on Apache ZooKeeper for metadata management. KRaft shifts metadata management from external ZooKeeper nodes to a group of controllers within Kafka itself, allowing metadata to be stored and replicated as topics within Kafka brokers, resulting in faster metadata propagation, improved scalability, and a simplified cluster architecture. Kafka 3.9.x is the last version to support ZooKeeper, and Kafka 4.x only supports KRaft. This in-place migration gives customers an easy path to move to KRaft on their existing clusters and upgrade to Kafka 4.x.  To get started, customers first upgrade to Kafka 3.9.x if they are on an older version, then customers can initiate the migration and the cluster remains available throughout the process. All steps can be performed through the MSK console, AWS CLI, or APIs. The in-place migration from Apache Zookeeper to Kraft is available today across all AWS regions where Amazon MSK provisioned is offered except European Sovereign Cloud (Germany). To learn how to get started, see the Amazon MSK Developer Guide.

## 핵심 요약

요약 미지원
