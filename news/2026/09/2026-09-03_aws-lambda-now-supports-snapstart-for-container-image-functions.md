---
title: "AWS Lambda now supports SnapStart for container image functions"
date: "2026-09-03"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-snapstart-container/"
tags: ["Lambda", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# AWS Lambda now supports SnapStart for container image functions

**날짜:** 2026년 09월 03일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-snapstart-container/

## 내용

Starting today, AWS Lambda supports SnapStart for functions packaged as container images, reducing startup times from several seconds to as low as sub-second. Lambda SnapStart is an opt-in capability that makes it easier for you to build highly responsive and scalable applications without provisioning resources or implementing complex performance optimizations. 
Customers deploy Lambda functions with container images to align with their organization's container-based deployment standards, or to package larger dependencies up to 10 GB. However, larger container images can experience startup times of several seconds as Lambda downloads image layers and initializes the runtime and application code. SnapStart addresses this by taking a snapshot of the initialized execution environment during function deployment, caching it, and resuming from it on invocation, instead of initializing from scratch. Previously, SnapStart was only supported for managed runtimes (Python, .NET, and Java). Starting today, customers can use SnapStart for container images to improve startup times for latency-sensitive workloads such as ML inference and interactive APIs. 
Lambda SnapStart for container images is available in all commercial AWS Regions, except Asia Pacific (New Zealand) and Asia Pacific (Taipei).&nbsp; 
You can activate SnapStart for new or existing container image functions using AWS Lambda API, AWS Console, AWS Command Line Interface (AWS CLI), AWS CloudFormation, AWS Serverless Application Model (AWS SAM), AWS SDK, and AWS Cloud Development Kit (AWS CDK). If you use an AWS base image for Lambda with Java (version 11+), Python (version 3.12+), or .NET (version 8+), the experience remains the same as with functions deployed as .zip file archives. For all other AWS base images for Lambda (for example, Node.js or Ruby) or custom base images, refer to the developer guide. For more information about SnapStart, see Lambda documentation. To learn more about pricing for SnapStart for container image functions, visit AWS Lambda Pricing.

## 핵심 요약

요약 미지원
