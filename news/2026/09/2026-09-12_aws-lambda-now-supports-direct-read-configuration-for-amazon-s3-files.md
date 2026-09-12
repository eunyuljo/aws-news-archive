---
title: "AWS Lambda now supports direct read configuration for Amazon S3 Files"
date: "2026-09-12"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-direct-read-s3files/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS Lambda now supports direct read configuration for Amazon S3 Files

**날짜:** 2026년 09월 12일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-direct-read-s3files/

## 내용

AWS Lambda now supports direct read&nbsp;configuration for Amazon S3 Files, letting you configure which storage your functions read from: S3 Files high-performance storage or your S3 bucket. With this launch, you can optimize the throughput and latency of file reads for your Lambda functions based on your application requirements. 
Customers use S3 Files with Lambda functions to build scalable data processing pipelines and stateful agentic workloads with the performance and simplicity of a file system, while benefiting from the scalability, durability, and cost-effectiveness of S3. S3 Files serves data from high-performance storage for low latency or directly from your S3 bucket for high throughput on large reads, automatically routing each operation to the storage best suited for it.&nbsp;By default, Lambda supports direct reads from your S3&nbsp;bucket only for functions configured with 512 MB of memory or higher. However, without control over the direct read configuration, you cannot optimize read performance for your specific application requirements. With this launch, you can explicitly enable or disable direct read for S3 Files on your Lambda functions, independent of function memory size. When you enable direct read, your function reads files 1 MB or larger directly from your S3 bucket for maximum throughput, and smaller files&nbsp;are&nbsp;served through the high-performance storage. When you disable it, all reads are served through the high-performance storage for the lowest latency. 
This capability is available in all AWS commercial Regions, AWS GovCloud (US-East), and AWS GovCloud (US-West) Regions, except Asia Pacific (New Zealand), Middle East (Bahrain), and Middle East (UAE).&nbsp;You can configure direct read for S3 Files using the AWS Management Console, AWS CLI, AWS SDKs, and AWS CloudFormation. There is no additional charge beyond standard Lambda and S3 Files pricing. To learn more about how to use S3 Files with your Lambda function, visit the AWS Lambda developer guide.

## 핵심 요약

요약 미지원
