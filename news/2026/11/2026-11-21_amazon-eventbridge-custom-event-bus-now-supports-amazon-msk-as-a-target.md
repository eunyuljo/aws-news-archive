---
title: "Amazon EventBridge Custom event bus now supports Amazon MSK as a target"
date: "2026-11-21"
service: "EventBridge"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eventbridge-msk-target/"
tags: ["EventBridge", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon EventBridge Custom event bus now supports Amazon MSK as a target

**날짜:** 2026년 11월 21일
**서비스:** EventBridge
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eventbridge-msk-target/

## 내용

Amazon EventBridge now supports Amazon Managed Streaming for Apache Kafka (Amazon MSK) as a target for the enhanced Custom event bus, so you can deliver events to Kafka topics without running your own producer. 
The EventBridge Custom event bus is a serverless event broker that enables you to create scalable event-driven applications by routing events between your applications, SaaS integrations, and AWS services. To deliver events to MSK, you create a Subscriber that specifies the cluster ARN and topic. You can also configure Kafka producer settings such as partition key, acknowledgment level, and record headers. EventBridge supports both public and private, serverless and provisioned clusters. When you create a Subscriber for a private cluster, EventBridge automatically sets up a private connection to the cluster. For example, teams that publish to a shared Custom event bus can now deliver purchase-order events to the MSK topics their payments team already consumes from. 
Amazon MSK targets are available in all AWS Regions where the enhanced Custom event bus is available. Delivery to MSK is billed as standard Custom event bus egress. EventBridge also supports compression before delivery, which is billed as an Event Evaluation. 
To learn more, see Amazon MSK cluster target in the Amazon EventBridge User Guide and the Amazon EventBridge product page. Install the Agent Toolkit for AWS to start building with your AI coding agent.

## 핵심 요약

요약 미지원
