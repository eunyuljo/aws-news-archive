---
title: "Announcing AWS for Fluent Bit 3.0.0 based on Fluent Bit 4.1.1"
date: "2026-11-03"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2025/10/aws-fluent-bit-3-0-0-based-4-1-1"
tags: ["S3", "2026", "GA", "performance", "security"]
nav_exclude: true
---

# Announcing AWS for Fluent Bit 3.0.0 based on Fluent Bit 4.1.1

**날짜:** 2026년 11월 03일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2025/10/aws-fluent-bit-3-0-0-based-4-1-1

## 내용

AWS for Fluent Bit announces version 3.0.0, based on Fluent Bit version 4.1.1 and Amazon Linux 2023. Container logging using AWS for Fluent Bit is now more performant and more feature-rich for AWS customers, including those using Amazon Elastic Container Services (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS).  AWS for Fluent Bit enables Amazon ECS and Amazon EKS customers to collect, process, and route container logs to destinations including Amazon CloudWatch Logs, Amazon Data Firehose, Amazon Kinesis Data Streams, and Amazon S3 without changing application code. AWS for Fluent Bit 3.0.0 upgrades the Fluent Bit version to 4.1.1, and upgrades the base image to Amazon Linux 2023. These updates deliver access to the latest Fluent Bit features, significant performance improvements, and enhanced security. New features include native OpenTelemetry (OTel) support for ingesting and forwarding OTLP logs, metrics, and traces with AWS SigV4 authentication. Performance improvements include faster JSON parsing, processing more logs per vCPU with lower latency. Security enhancements include TLS min version and cipher controls, which enforce your TLS policy on outputs from AWS for Fluent Bit for stronger protocol posture.  You can use AWS for Fluent Bit 3.0.0 on both ECS and EKS. On ECS, update the FireLens log-router container image in your task definition to the 3.0.0 tag from the Amazon ECR Public Gallery. On EKS, upgrade by either updating the Helm release or setting the DaemonSet image to the 3.0.0 version.  The AWS for Fluent Bit image is available in the Amazon ECR Public Gallery and in the Amazon ECR repository. You can also find it on GitHub for source code and additional guidance. 
&nbsp; 
10/29/2025 - This post has been updated to accurately reflect the Fluent Bit version at launch. 11/02/2026 - This post has been updated to clarify the scope of OpenTelemetry support. 
&nbsp;

## 핵심 요약

요약 미지원
