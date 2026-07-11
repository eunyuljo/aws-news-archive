---
title: "Amazon SageMaker HyperPod now supports AMI-based node lifecycle configuration for Slurm clusters using continuous provisioning"
date: "2026-07-11"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2025/06/ami-configuration-continuous-slurm/"
tags: ["S3", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker HyperPod now supports AMI-based node lifecycle configuration for Slurm clusters using continuous provisioning

**날짜:** 2026년 07월 11일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2025/06/ami-configuration-continuous-slurm/

## 내용

Amazon SageMaker HyperPod now supports AMI-based configuration for Slurm clusters that use continuous provisioning. Continuous provisioning adds nodes to the cluster as capacity becomes available, and this launch extends AMI-based configuration to clusters using this mode. With this support, clusters using continuous provisioning can be created without downloading, configuring, or uploading lifecycle configuration scripts to Amazon S3.  AMI-based configuration provisions nodes with the software and configurations needed for a production-ready environment to run AI/ML training workloads, including required software such as Docker, Enroot, and Pyxis, and configurations such as Slurm accounting, SSH key generation, and log rotation. When using continuous provisioning, each node is configured from the AMI as it is added to the cluster, without the need to manage lifecycle configuration scripts, so nodes become available to schedule jobs sooner. To enable AMI-based configuration, omit the LifeCycleConfig block from the instance group configuration when creating clusters via the API, or select "None" under Lifecycle scripts in Custom setup when using the SageMaker AI console. For additional customization on top of the AMI-based configuration baseline, an extension script can be provided by specifying the OnInitComplete parameter and SourceS3Uri in the LifeCycleConfig block via the API, or by providing the S3 URI in the "Extension script file in S3" field in Custom setup when using the console. Custom lifecycle configuration scripts remain fully supported for use cases that require full control over provisioning.  AMI-based node lifecycle configuration for Slurm clusters using continuous provisioning is available in all AWS Regions where SageMaker HyperPod is available. To get started, see Getting started with SageMaker HyperPod using the AWS CLI or Getting started with SageMaker HyperPod using the SageMaker AI console in the SageMaker user guide.

## 핵심 요약

요약 미지원
