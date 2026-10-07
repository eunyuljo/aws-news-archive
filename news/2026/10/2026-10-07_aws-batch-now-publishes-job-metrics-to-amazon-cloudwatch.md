---
title: "AWS Batch now publishes job metrics to Amazon CloudWatch"
date: "2026-10-07"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-batch-job-cloudwatch-metrics/"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# AWS Batch now publishes job metrics to Amazon CloudWatch

**날짜:** 2026년 10월 07일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-batch-job-cloudwatch-metrics/

## 내용

AWS Batch now publishes job metrics to Amazon CloudWatch, providing native observability for batch workloads. AWS Batch emits metrics throughout the job lifecycle, giving you visibility into job queue health, failure rates, and job durations.
AWS Batch automatically publishes job state transition and duration metrics to the AWS/Batch namespace in Amazon CloudWatch, with JobQueueName dimension. State transition metrics track how many jobs entered a given state, such as submitted, running, succeeded, or failed. Duration metrics track how long jobs spent between states, such as time from submission to runnable or total execution time. You can view these metrics in the AWS Batch console, the Amazon CloudWatch console, or through the AWS CLI and AWS SDKs.
AWS Batch CloudWatch metrics are now published in all AWS Regions where AWS Batch is available. For more information, see CloudWatch Metrics page in the AWS Batch User Guide.

## 핵심 요약

요약 미지원
