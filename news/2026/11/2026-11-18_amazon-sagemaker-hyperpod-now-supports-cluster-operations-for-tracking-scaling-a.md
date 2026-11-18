---
title: "Amazon SageMaker HyperPod now supports cluster operations for tracking scaling and on-demand Deep Health Check requests"
date: "2026-11-18"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-cluster-ops/"
tags: ["RDS", "2026", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker HyperPod now supports cluster operations for tracking scaling and on-demand Deep Health Check requests

**날짜:** 2026년 11월 18일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-cluster-ops/

## 내용

Amazon SageMaker HyperPod introduces cluster operations, giving you visibility into every scaling and on-demand deep health check request from submission to completion. When a request runs into errors, the SageMaker AI console shows an alert that links directly to that request's error events. 
With continuous provisioning, HyperPod brings capacity online in the background as it becomes available, retries failed nodes automatically, and lets you run multiple scaling requests at the same time. Cluster operations show you when each request finishes and which request caused the activity on your cluster. When a scale-up falls short of its target, you can go directly to the failure reason. 
Each scaling or on-demand deep health check request creates a cluster operation that tracks the request from submission to completion, including whether it is still in progress and what it changed on each instance group. Events that HyperPod records while working on the request are linked to its operation. For example, if a scale-up of your training instance group doesn't reach its target, you can open the operation and see only the events for that request, without sorting through unrelated cluster activity. If you or an autoscaler such as Karpenter send several requests to the same instance group, for example during a burst of inference traffic, each operation shows whether it completed or was replaced by a newer request. That way you can tell which request actually changed your cluster. After you run an on-demand deep health check before a large training job, you can follow its operation to confirm when it finished and which instances it affected. In the SageMaker AI console, operations appear on the cluster's Events tab. To build the same visibility into your own dashboards, alerting, or CI/CD pipelines, use the new ListClusterOperations and DescribeClusterOperation APIs, and filter ListClusterEvents by operation. 
Cluster operations are created automatically for every request, with no changes to your existing workflows. 
Cluster operations are available at no additional cost for SageMaker HyperPod clusters that use continuous provisioning, in all AWS Regions where SageMaker HyperPod is available. To learn more, please check the documentation.

## 핵심 요약

요약 미지원
