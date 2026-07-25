---
title: "Amazon Kinesis Data Streams now supports scaling down ingest capacity with warm throughput"
date: "2026-07-25"
service: "Kinesis"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/kinesis/on-demand-scale-down"
tags: ["Kinesis", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon Kinesis Data Streams now supports scaling down ingest capacity with warm throughput

**날짜:** 2026년 07월 25일
**서비스:** Kinesis
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/kinesis/on-demand-scale-down

## 내용

Amazon Kinesis Data Streams is a serverless streaming data service that makes it easy to capture, process, and store data streams at any scale. On-demand streams automatically increase ingest capacity in response to rising data ingest usage. With On-demand Advantage mode, you can proactively manage stream capacity using warm throughput to prepare streams for sudden changes in data traffic. We are extending warm throughput with the ability to also scale down ingest capacity, giving you full control to scale your stream's write throughput up or down.  
To scale down, simply set a lower warm throughput value on your on-demand stream. The stream adjusts to the requested capacity or the amount needed to support peak data ingest usage in the last hour, whichever is higher. This ensures your stream always retains sufficient capacity for current traffic while releasing excess capacity you no longer need. As a result, you get optimal stream-processing performance and cost efficiency.&nbsp; 
Warm throughput scale-down is available at no additional cost for all on-demand streams with On-demand Advantage mode enabled.&nbsp; For more information about On-demand Advantage, see Choose the right mode to stream in in the Amazon Kinesis Data Streams Developer Guide. To get started with the feature, see Update a stream. For pricing details, see Amazon Kinesis Data Streams pricing. 
The feature is available in all AWS Regions where Amazon Kinesis Data Streams On-demand Advantage is supported.&nbsp; 
&nbsp;

## 핵심 요약

요약 미지원
