---
title: "AWS Parallel Computing Service now supports scaling logs"
date: "2026-10-01"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-pcs-scaling-logs/"
tags: ["S3", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Parallel Computing Service now supports scaling logs

**날짜:** 2026년 10월 01일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-pcs-scaling-logs/

## 내용

AWS Parallel Computing Service (AWS PCS) now supports scaling logs, which record how AWS PCS scales the compute node groups in your cluster. Each log entry records one state transition for one compute node—for example, an instance launch, a node registration, a scale-down, or a launch failure with its reason. Using scaling logs, you can more easily troubleshoot scaling issues. For example, you can determine why a compute node group did not reach its target size, which launches failed for capacity reasons, and when a specific node started or stopped. Scaling log delivery is opt-in, and you can configure AWS PCS to emit scaling logs to Amazon CloudWatch Logs, Amazon S3, and Amazon Data Firehose.
AWS PCS is a managed service that simplifies running and scaling HPC workloads on AWS using Slurm. You can build complete, elastic environments that integrate compute, storage, networking, and visualization tools, while the service handles cluster operations with managed updates and built-in observability features.
This feature is available in all AWS Regions where AWS PCS is available. To get started, see the AWS PCS User Guide.

## 핵심 요약

요약 미지원
