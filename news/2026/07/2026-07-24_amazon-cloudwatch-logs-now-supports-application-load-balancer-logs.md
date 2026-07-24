---
title: "Amazon CloudWatch Logs now supports Application Load Balancer logs"
date: "2026-07-24"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-logs/"
tags: ["S3", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon CloudWatch Logs now supports Application Load Balancer logs

**날짜:** 2026년 07월 24일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-logs/

## 내용

Amazon CloudWatch Logs now supports Application Load Balancer (ALB) logs as vended logs, improving observability and simplifying debugging for network traffic patterns. You can now analyze ALB access, connection and health check logs directly in CloudWatch to gain insights into client connections, traffic distribution, connection status and target health, helping you identify and troubleshoot network issues faster. Additionally, you can set up CloudWatch telemetry enablement rules to automatically configure logging of both existing and newly created ALB resources, for your organization, specific accounts, or specific resources, ensuring consistent monitoring coverage without manual setup.  With this CloudWatch Logs integration, you can track detailed access patterns using CloudWatch Logs Insights queries, create metric filters for monitoring and alarming, and review traffic patterns in real time using Live Tail. ALB logs can be configured through the integrations tab of your application load balancer in AWS Management Console, AWS CLI, or SDKs. You can also configure delivery of ALB logs to Amazon Data Firehose or Amazon S3 with support for Apache Parquet format.  ALB logs delivery to CloudWatch is available in all AWS Commercial and GovCloud regions where Application Load Balancer and CloudWatch are available. ALB logs are charged as vended logs when delivered to CloudWatch Logs and Data Firehose, while delivery to Amazon S3 is free (Parquet conversion is charged at $0.035/GB - N. Virginia).  To learn more about configuring ALB logs in CloudWatch Logs, please visit our documentation. For pricing information, see CloudWatch pricing page.

## 핵심 요약

요약 미지원
