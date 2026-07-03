---
title: "Amazon SageMaker HyperPod now supports AMI versioning and auto-patching"
date: "2026-07-03"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-sagemaker-hyperpod-ami-version-auto-patch"
tags: ["EKS", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker HyperPod now supports AMI versioning and auto-patching

**날짜:** 2026년 07월 03일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-sagemaker-hyperpod-ami-version-auto-patch

## 내용

Amazon SageMaker HyperPod now gives you visibility into the Amazon Machine Image (AMI) versions running across your clusters and automatically applies security patches without disrupting your workloads. SageMaker HyperPod is purpose-built infrastructure for training and deploying foundation models at scale. Cluster administrators previously had limited insight into which AMI versions were running, making drift hard to detect and security patching a manual, reactive process that was difficult to run on long multi-day training jobs and that risked changing bundled software in the AMI such as NVIDIA drivers or CUDA. These new capabilities on HyperPod help you keep clusters secure and consistent while removing the operational burden of manual patching. 
With AMI versioning, you can see the exact AMI version on every instance group and node in the semantic versioning (major.minor.patch) format, quickly detect version drift, and roll back to a previous version—including the prior NVIDIA driver, CUDA, and other software stack—using the UpdateClusterSoftware API. Auto-patching is an opt-in, per-instance-group capability that applies only backward-compatible security patches as nodes become idle, so your running workloads stay undisrupted and critical AI/ML packages such as NVIDIA driver, CUDA version, and operating system kernels are never upgraded to a different major or minor version; you can enable it through the CreateCluster or UpdateCluster API. A new AMI support policy also publishes support timelines for different AMI versions after which HyperPod stops publishing security patches. 
Both AMI versioning and auto-patching are available for HyperPod clusters orchestrated by Amazon EKS, in all AWS Regions where SageMaker HyperPod is supported. To learn more, see the HyperPod AMI management documentation and the new HyperPod AMI support policy.

## 핵심 요약

요약 미지원
