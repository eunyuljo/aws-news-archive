---
title: "AWS Parallel Computing Service supports in-place Slurm major version upgrades"
date: "2026-07-01"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-parallel-computing-service-upgrade/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# AWS Parallel Computing Service supports in-place Slurm major version upgrades

**날짜:** 2026년 07월 01일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-parallel-computing-service-upgrade/

## 내용

AWS Parallel Computing Service (PCS) now supports managed in-place Slurm version upgrades for existing clusters. You can move your clusters up to three Slurm major versions ahead with no disruption to running jobs.  To upgrade, update your Cluster configuration with your target Slurm version using the AWS Management Console, AWS CLI, or UpdateCluster API. PCS handles the upgrade of all managed Slurm components — the controller, accounting database, and REST API. Running jobs continue uninterrupted during the upgrade, queued jobs resume once the operation completes, and any accounting data is preserved in the database. You can then update your compute nodes to the new Slurm version at your convenience. Refer to the PCS User Guide for more information on the steps to follow and considerations to review based on your cluster configuration.  AWS PCS is a managed service that simplifies running and scaling HPC workloads on AWS using Slurm. You can build complete, elastic environments that integrate compute, storage, networking, and visualization tools, while the service handles cluster operations with managed updates and built-in observability features.  This feature is available in all AWS Regions where PCS is available. To get started, see the PCS User Guide.

## 핵심 요약

요약 미지원
