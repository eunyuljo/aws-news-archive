---
title: "Amazon CloudWatch announces log routing and chained log parsers"
date: "2026-10-15"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/cloudwatch-pipelines-log-routing/"
tags: ["CloudWatch", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch announces log routing and chained log parsers

**날짜:** 2026년 10월 15일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/cloudwatch-pipelines-log-routing/

## 내용

Amazon CloudWatch now supports conditional log routing and chained parsers via pipelines, giving you more control over how log data is transformed and which CloudWatch log group it's sent to. CloudWatch pipelines is a fully managed service that ingests, transforms, and routes telemetry to CloudWatch without managing infrastructure.
Log pipelines often carry a mix of event types that belong in different places, and individual events can nest one log format inside another. With conditional log routing, you define routes that send each event to a different CloudWatch log group based on conditions evaluated against processed fields, so you can separate events by severity, source, or type and apply the right retention and access controls to each. With chained parsers, you can apply multiple parser processors in sequence, where later parsers consume fields produced by earlier ones. For example, you can parse a JSON envelope first, then apply a Grok parser to a field it extracts. Together, these capabilities let you structure diverse log formats and route them to the right log groups in a single pipeline.
Conditional routing and chained parsers are available in all commercial AWS Regions where CloudWatch pipelines is generally available. You can configure these capabilities using the AWS Management Console, AWS CLI, or AWS SDKs. To get started, see the Amazon CloudWatch pipelines documentation.

## 핵심 요약

요약 미지원
