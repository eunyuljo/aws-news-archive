---
title: "Amazon MSK Connect now supports updating connector plugins and worker configurations"
date: "2026-10-30"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-connect-update-plugin-worker-configurations"
tags: ["Config", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon MSK Connect now supports updating connector plugins and worker configurations

**날짜:** 2026년 10월 30일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-connect-update-plugin-worker-configurations

## 내용

Amazon MSK Connect (Amazon Managed Streaming for Apache Kafka Connect) now lets you update the custom plugin and worker configuration of an existing connector. This is useful when you need to update the custom plugin to run a new version of your connector code, for example one with updated dependencies. You can also update the worker configuration to change worker-level settings, such as switching key and value converters or tuning producer and consumer properties for throughput and latency. 
Amazon MSK Connect is a fully managed service that allows you to deploy, monitor, and scale Apache Kafka Connect connectors with Amazon MSK (Managed Streaming for Apache Kafka). Previously, updating a connector's plugin or worker configuration meant deleting the connector and recreating it - a disruptive operation that added risk and operational overhead. With this launch, you can update a connector's plugin and worker configuration in place. The connector keeps its committed offsets, so its tasks continue processing from where they left off once the update completes. 
This capability is available at no additional cost in all AWS Regions where Amazon MSK Connect is supported. To learn more, visit Amazon MSK Connect developer guide.

## 핵심 요약

요약 미지원
