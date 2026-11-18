---
title: "Amazon MSK Express Brokers now support Graviton4-based M8g instances"
date: "2026-11-18"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-msk-express-brokers-graviton4-m8g-instances/"
tags: ["General", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon MSK Express Brokers now support Graviton4-based M8g instances

**날짜:** 2026년 11월 18일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-msk-express-brokers-graviton4-m8g-instances/

## 내용

AWS Graviton4-based M8g instances are now generally available for Express Brokers in Amazon Managed Streaming for Apache Kafka (Amazon MSK). Compared to Express Brokers on M7g, M8g delivers 15% lower compute costs, up to 45% lower P99 produce latency, and 2x faster catch-up for consumers that fall behind. Additionally, customers no longer pay the broker-side cost when moving data across Availability Zones between clients and brokers, reducing total cross-AZ data transfer costs by 50%. Together, lower data transfer and broker-hour charges result in up to 30% cost savings compared to Express Brokers on M7g. 
MSK Express Brokers are designed to deliver up to 3x more throughput per broker, scale up to 20x faster, and reduce recovery time by 90% compared to Standard Brokers running Apache Kafka. Express Brokers on M8g further improve on M7g with better economics and performance along with existing Express capabilities. Customers running Apache Kafka on external clusters, including on-premises, self-managed on AWS, or other cloud providers, can use Amazon MSK Replicator to seamlessly migrate to Express Brokers on M8g and immediately benefit from the improved price and performance. Existing Express customers can upgrade from M7g to M8g through in-place migration while client applications keep producing and consuming without interruption. 
Express Brokers on M8g are available today across all AWS regions where MSK Express Brokers and M8g instances are available. For pricing, refer to the Amazon MSK pricing page. To get started, use the AWS Management Console or API to create a new cluster with Express Brokers on M8g, start an in-place migration of an existing cluster from Express Brokers on M7g to M8g, or set up a replicator from an external Kafka cluster with Amazon MSK Replicator. To learn more, see the Amazon MSK Developer Guide.

## 핵심 요약

요약 미지원
