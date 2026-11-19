---
title: "Amazon SageMaker HyperPod now supports higher pod density on EKS-orchestrated clusters"
date: "2026-11-19"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-higher-pod-density/"
tags: ["EKS", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker HyperPod now supports higher pod density on EKS-orchestrated clusters

**날짜:** 2026년 11월 19일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-higher-pod-density/

## 내용

Amazon SageMaker HyperPod now supports higher pod density per node on EKS-orchestrated clusters, allowing you to get more out of every instance. This leaves more room for your applications alongside system DaemonSets for monitoring, logging, and security, and helps increase GPU, CPU and memory utilization on nodes, allowing you to run the same work using fewer instances. 
As you schedule more pods, the Amazon VPC CNI automatically adds network capacity to the node. Autoscaling with Karpenter also supports the higher pod capacity, so new nodes take on more pods as your cluster scales out. 
Here are a few examples of workloads that benefit from higher pod density: 
 
 Model inference - Serve more model replicas or more models from each GPU instance, including on smaller types such as ml.g5 and ml.g6.  
 Interactive development - Host more notebooks, IDEs, and data science environments on each node.  
 GPU partitioning - Use all the Multi-Instance GPU (MIG) slices on instances such as ml.p5en.48xlarge, where each slice runs its own pod.  
 Operators and Controllers - Run operators, controllers, and observability agents on CPU nodes alongside your workloads, without crowding them out.  
 
This feature is available for HyperPod EKS-orchestrated clusters in all AWS Regions where SageMaker HyperPod is available. To get started, update your cluster's IAM permissions, cluster software, and Amazon VPC CNI add-on. To learn more, please check the documentation.

## 핵심 요약

요약 미지원
