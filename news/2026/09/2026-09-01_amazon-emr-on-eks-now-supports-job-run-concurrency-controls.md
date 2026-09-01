---
title: "Amazon EMR on EKS now supports job run concurrency controls"
date: "2026-09-01"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-emr-eks/"
tags: ["EKS", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon EMR on EKS now supports job run concurrency controls

**날짜:** 2026년 09월 01일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-emr-eks/

## 내용

Amazon EMR on EKS lets you run open-source big data frameworks such as Apache Spark and Flink on AWS EKS(Elastic Kubernetes Service) clusters. You submit jobs to a virtual cluster, which maps to a namespace on an EKS cluster, and EMR on EKS handles packaging, scheduling, and running your applications. Today, we are excited to announce job run admission control on EMR EKS with support for job run concurrency and backpressure signals from StartJobRun API.  
With this launch, you can now set concurrent job limits on a virtual cluster, giving you fine-grained control over how many job runs execute at once and how many can wait in queue. This is a logical queue representing jobs in PENDING/SUBMITTED state. These controls help you protect shared EKS clusters from being overloaded in multi-tenant shared environments and avoid noisy-neighbor scheduling failures, so your critical workloads keep running predictably even under heavy demand.&nbsp;You configure two optional limits on a virtual cluster: maxConcurrentJobRuns, the maximum number of jobs running at any time, and maxInQueueJobRuns, the maximum queue depth for job runs that EMR on EKS has accepted but not yet started running. When the queue is full, StartJobRun returns an HTTP ValidationException, so you can gracefully shed or reroute traffic to another cluster instead of overwhelming a single one. You can view current limits and live job counts at any time with DescribeVirtualCluster. No limits are applied by default, so existing workloads are unaffected until you opt in.&nbsp; 
Concurrent job limits are available in all AWS Regions where EMR on EKS is offered. To get&nbsp;started, see managing virtual clusters.

## 핵심 요약

요약 미지원
