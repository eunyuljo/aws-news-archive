---
title: "AWS Lambda announces scalable network bandwidth up to 3,000 Mbps for functions outside a VPC"
date: "2026-08-06"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-lambda-network-bandwidth/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS Lambda announces scalable network bandwidth up to 3,000 Mbps for functions outside a VPC

**날짜:** 2026년 08월 06일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-lambda-network-bandwidth/

## 내용

AWS Lambda now supports scalable network bandwidth for Lambda functions, enabling faster data transfer to and from your execution environment for latency-sensitive workloads. This feature enables functions outside a VPC configured with 2 GB of memory or more to access network bandwidth that scales proportionally, from 625 Mbps at 2 GB up to 3,000 Mbps at 10 GB.  Customers use Lambda to build latency-sensitive data processing workloads, which need to transfer large volumes of data - up to several terabytes - from external data sources into the function’s execution environment for processing. As data volume and performance requirements grow, the existing limit of 625 Mbps can constrain data transfer speeds to and from an execution environment.&nbsp;With this launch, network throughput increases proportionally from 625 Mbps at 2 GB up to 3,000 Mbps at 10 GB, helping reduce function execution times and per-invocation costs while improving end-user experience.  To get started, submit a request through AWS Service Quotas under the Network bandwidth per execution environment quota to enable scalable network bandwidth on your account. Once enabled, bandwidth will scale automatically based on your function's memory configuration for all functions outside a VPC in your account.  Scalable network bandwidth for functions outside a VPC is available at no additional charge in all commercial AWS Regions. To learn more, visit the Lambda quotas page.&nbsp;

## 핵심 요약

요약 미지원
