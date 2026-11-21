---
title: "Amazon MSK now supports in-place upgrade from Standard brokers to Express brokers"
date: "2026-11-21"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-msk-standard-brokers-to-express-brokers-in-place-upgrade"
tags: ["General", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon MSK now supports in-place upgrade from Standard brokers to Express brokers

**날짜:** 2026년 11월 21일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-msk-standard-brokers-to-express-brokers-in-place-upgrade

## 내용

You can now upgrade existing Amazon MSK Provisioned clusters from Standard brokers to Express brokers in place, with fully managed data migration and no application changes. Express brokers are designed to deliver up to 3x more throughput per broker, scale up to 20x faster, and recover up to 90% faster compared to Standard brokers. With in-place upgrade, you can get the performance and operational benefits of Express brokers in hours, without needing to create a new cluster or having to migrate your data and applications to it. The upgrade keeps cluster endpoints unchanged, eliminating application cutovers, and preserves consumer offsets, so stateful applications such as Apache Flink and Kafka Streams continue without reprocessing or duplicates. 
Express brokers make Apache Kafka simpler to manage and more cost-effective to run at scale, with pay-as-you-go storage that scales automatically and built-in best practice defaults for higher resilience. Previously, upgrading to Express brokers meant creating a new cluster and migrating workloads to it, which required careful planning and cross-team coordination. With this launch, you can upgrade your existing Standard brokers to Express brokers in-place, without interrupting your applications, while maintaining complete control over the upgrade process. The upgrade adds Express brokers to your cluster and moves your topics to them, either automatically or in batches you control. Your Standard brokers stay in the cluster until you choose to decommission them to complete the upgrade, so you can validate your applications and roll back if needed. 
In-place upgrade is available for MSK Provisioned clusters running Standard brokers on Apache Kafka version 3.9 with KRaft, in all AWS Regions where Express brokers are available. You can upgrade to Express brokers on M7g or M8g instances. Express brokers on M8g deliver up to 30% cost savings compared to Express brokers on M7g. There's no additional charge for the upgrade itself. You pay for both Standard and Express brokers while the upgrade is in progress. To get started, visit the Amazon MSK Developer Guide and the Migration to Express brokers product page.

## 핵심 요약

요약 미지원
