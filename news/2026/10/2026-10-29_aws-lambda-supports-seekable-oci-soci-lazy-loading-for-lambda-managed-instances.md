---
title: "AWS Lambda supports Seekable OCI (SOCI) lazy loading for Lambda Managed Instances"
date: "2026-10-29"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-seekable-oci-soci/"
tags: ["Lambda", "2026", "new-region", "performance"]
nav_exclude: true
---

# AWS Lambda supports Seekable OCI (SOCI) lazy loading for Lambda Managed Instances

**날짜:** 2026년 10월 29일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-seekable-oci-soci/

## 내용

AWS Lambda now supports Seekable OCI (SOCI)&nbsp;for lazy loading Event Functions packaged as Open Container Initiative (OCI) images running on Lambda Managed Instances. With SOCI support, Lambda fetches only the files needed at each stage of the execution environment startup rather than downloading the entire image upfront, reducing container startup times by up to 70%. 
Customers building compute-intensive applications such as data processing pipelines, high-throughput API backends, and batch computation workloads require substantial memory and CPU resources to process large datasets, serve low-latency responses at scale, and run complex computations efficiently. Container images for these workloads can reach several gigabytes, and downloading and preparing the full image can take several minutes when provisioning new execution environments. SOCI support on Lambda Managed Instances eliminates this bottleneck by streaming only the required files at each stage of the execution environment startup, so your functions start faster as you scale. 
To get started, create a SOCI index&nbsp;(a table of contents for the files in your image layers) for your container image and push it to Amazon ECR. When creating or updating your function, set the image URI to the SOCI-indexed tag in Amazon ECR (for example, my-function:v1-soci) and publish a function version. Lambda automatically detects the SOCI index and enables lazy loading with no additional configuration. If you use a coding assistant such as Kiro, Claude Code, or Codex, install the Lambda Managed Instances skill from the Agent Toolkit for AWS to configure and deploy functions through your agent. 
The feature is available in all AWS commercial Regions where Lambda Managed Instances is available. To learn more, visit the AWS Lambda Managed Instances developer guide.&nbsp;

## 핵심 요약

요약 미지원
