---
title: "Amazon SageMaker HyperPod now supports custom AMIs (Amazon Machine Images) for Slurm clusters"
date: "2026-07-14"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/hyperpod-custom-ami-slurm/"
tags: ["RDS", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon SageMaker HyperPod now supports custom AMIs (Amazon Machine Images) for Slurm clusters

**날짜:** 2026년 07월 14일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/hyperpod-custom-ami-slurm/

## 내용

Amazon SageMaker HyperPod now supports custom AMIs for Slurm-orchestrated clusters, enabling customers to deploy clusters with pre-configured, security-hardened environments that meet their specific organizational requirements. Customers deploying AI/ML workloads on HyperPod Slurm clusters need customized environments that meet strict security, compliance, and operational requirements while maintaining fast cluster startup times, but often struggle with complex lifecycle configuration scripts that slow deployment and create inconsistencies across cluster nodes.  This capability allows customers to build upon HyperPod's performance-optimized base AMIs while incorporating customized security agents, compliance tools, proprietary libraries, and specialized drivers directly into the image, delivering faster startup times, improved reliability, and enhanced security compliance. Security teams can embed organizational policies directly into base images, allowing AI/ML teams to use pre-approved environments that accelerate time-to-training while meeting enterprise security standards. You can specify custom AMIs when creating new HyperPod Slurm clusters using the CreateCluster API, adding instance groups with the UpdateCluster API, or patching existing clusters with the UpdateClusterSoftware API. Custom AMIs must be built using HyperPod's public base AMIs to maintain compatibility with distributed training libraries and cluster management capabilities.  This feature is available in all AWS Regions where Amazon SageMaker HyperPod is supported. To learn more about custom AMI support for Slurm clusters, see the Amazon SageMaker HyperPod User Guide.

## 핵심 요약

요약 미지원
