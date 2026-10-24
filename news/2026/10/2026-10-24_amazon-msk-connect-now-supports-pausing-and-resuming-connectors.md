---
title: "Amazon MSK Connect now supports pausing and resuming connectors"
date: "2026-10-24"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-connect-pause-resume"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon MSK Connect now supports pausing and resuming connectors

**날짜:** 2026년 10월 24일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-connect-pause-resume

## 내용

Amazon MSK Connect (Amazon Managed Streaming for Apache Kafka Connect) now supports pausing and resuming connectors, letting you temporarily pause a connector from processing records and resume it later. This is useful when you need to stop data flow during maintenance on a source database or a sink target, or to pause processing while you investigate an upstream or downstream issue. 
Amazon MSK Connect is a fully managed service that allows you to deploy, monitor, and scale Apache Kafka Connect connectors with Amazon MSK (Managed Streaming for Apache Kafka). Previously, pausing a connector meant deleting it and recreating it - a more disruptive operation, adding risk and operational overhead. With this launch, you can pause a running connector and resume it in place when you are ready — a paused connector keeps its configuration, capacity settings, and committed offsets, and its tasks continue processing from the offsets they last committed when you resume. 
This capability is available at no additional cost through the Amazon MSK Console, AWS CLI, AWS SDK, and AWS CDK in all AWS Regions where Amazon MSK Connect is available. To learn more, visit the Amazon MSK Connect documentation. To get started, visit the Amazon MSK Console.

## 핵심 요약

요약 미지원
