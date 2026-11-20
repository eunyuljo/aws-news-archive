---
title: "Amazon MSK Connect now supports restarting existing connectors"
date: "2026-11-20"
service: "Connect"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-msk-connect-restart-existing-connectors"
tags: ["Connect", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon MSK Connect now supports restarting existing connectors

**날짜:** 2026년 11월 20일
**서비스:** Connect
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-msk-connect-restart-existing-connectors

## 내용

Amazon MSK Connect (Amazon Managed Streaming for Apache Kafka Connect) now supports restarting both existing and newly created connectors and their tasks in place, enabling fast recovery for streaming data pipelines. 
Amazon MSK Connect is a fully managed service that allows you to deploy, monitor, and scale Apache Kafka Connect connectors with Amazon MSK (Managed Streaming for Apache Kafka). Previously, recovering from failures required deleting and recreating the connector, resulting in downtime and operational overhead. With this feature, you can restart your connector and all its tasks in place, or selectively restart only the failed tasks, making recovery seamless. You can also restart connectors that have no failed tasks to recover from transient issues or to pick up changes in external systems or dependencies. 
This restart capability is available at no additional cost through the Amazon MSK Console, AWS CLI, AWS SDK, and AWS CDK in all AWS Regions where Amazon MSK Connect is available. To learn more, visit the Amazon MSK Connect documentation. To get started, visit the Amazon MSK Console.

## 핵심 요약

요약 미지원
