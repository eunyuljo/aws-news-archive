---
title: "Amazon API Gateway now supports 1 MB execution logs with configurable delivery destinations"
date: "2026-09-11"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-1-mb-execution-logs/"
tags: ["S3", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon API Gateway now supports 1 MB execution logs with configurable delivery destinations

**날짜:** 2026년 09월 11일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-1-mb-execution-logs/

## 내용

Amazon API Gateway now supports configurable delivery destinations and larger log events for REST API execution logs. Previously, execution logs were delivered to a single API Gateway-managed CloudWatch Logs log group with log events truncated at 1 KB, limiting visibility into request and response data.  You can now route execution logs up to 1 MB to your own Amazon CloudWatch Logs log groups, Amazon S3 buckets, or Amazon Data Firehose streams, and deliver to multiple destinations simultaneously. For example, you can route execution logs to Amazon S3 in Apache Parquet format for cost-efficient long-term storage and analysis with Amazon Athena, while simultaneously delivering structured JSON logs to CloudWatch Logs for real-time alerting.  This feature is available in all AWS Regions where API Gateway REST APIs are available, including the AWS GovCloud (US) Regions. Execution logs delivered through this feature are charged at vended logs rates. For pricing details, see Amazon CloudWatch Pricing. You can set up delivery through the API Gateway console, AWS CLI, or AWS CloudFormation. To get started, see Amazon API Gateway documentation and AWS blog post.&nbsp;

## 핵심 요약

요약 미지원
