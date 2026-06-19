---
title: "AWS Compute Optimizer enhances EBS volume recommendations with additional performance metrics"
date: "2026-06-19"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-compute-optimizer-enhances-ebs-recommendations/"
tags: ["EC2", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS Compute Optimizer enhances EBS volume recommendations with additional performance metrics

**날짜:** 2026년 06월 19일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-compute-optimizer-enhances-ebs-recommendations/

## 내용

AWS Compute Optimizer now includes improved visibility into IOPS and throughput spikes when deliverings Amazon EBS volume rightsizing recommendations. Compute Optimizer analyzes two additional Amazon CloudWatch metrics, VolumeIOPSExceededCheck and VolumeThroughputExceededCheck, which report whether your workload consistently attempted to drive IOPS or throughput beyond your volume's provisioned performance in any given minute. By factoring in these signals, Compute Optimizer helps you make rightsizing decisions to balance cost with performance for workloads that experience bursts of high IOPS or throughput. 
This enhancement is available in all AWS Regions where AWS Compute Optimizer is available, except the AWS GovCloud (US) Regions, and the China Regions. The underlying CloudWatch metrics are available at no additional charge for all EBS volumes attached to Nitro-based EC2 instances, excluding standard and Multi-Attach enabled volumes. To get started, go to AWS Compute Optimizer in the AWS Management Console. To learn more, visit the AWS Compute Optimizer User Guide.

## 핵심 요약

요약 미지원
