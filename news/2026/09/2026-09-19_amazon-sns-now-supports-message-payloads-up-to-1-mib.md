---
title: "Amazon SNS now supports message payloads up to 1 MiB"
date: "2026-09-19"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sns-1mib-support"
tags: ["Lambda", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon SNS now supports message payloads up to 1 MiB

**날짜:** 2026년 09월 19일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sns-1mib-support

## 내용

Amazon Simple Notification Service (Amazon SNS)&nbsp;now supports message payloads up to 1 MiB, a 4x increase from the previous 256 KiB limit, so you can publish larger messages to your SNS topics. 
Amazon SNS is a fully managed pub/sub messaging service that enables you to decouple and scale microservices, distributed systems, and serverless applications. As workloads such as application integration, IoT, and generative AI increasingly exchange larger volumes of data in a single message, the previous 256 KiB limit required customers to offload or split payloads before publishing. 
With this launch, you can publish message payloads up to 1 MiB by setting the new MaximumMessageSize topic attribute on both SNS Standard and SNS FIFO topics. Topics with MaximumMessageSize set above 256 KiB support Amazon SQS, Amazon Data Firehose, and AWS Lambda subscriptions, with up to 100 total subscriptions per topic. 
Amazon SNS 1 MiB support is available today in all AWS Regions where Amazon SNS is available. To learn more about sending large payloads with Amazon SNS, see the Amazon SNS Developer Guide.&nbsp; 
&nbsp;

## 핵심 요약

요약 미지원
