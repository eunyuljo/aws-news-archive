---
title: "AWS PCS now supports custom GRES, hardware topology, and MIG"
date: "2026-09-17"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-pcs-gres-hardware-topology-mig/"
tags: ["Config", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# AWS PCS now supports custom GRES, hardware topology, and MIG

**날짜:** 2026년 09월 17일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-pcs-gres-hardware-topology-mig/

## 내용

AWS Parallel Computing Service (AWS PCS) now supports custom Generic Resource (GRES) settings and hardware topology, and adds support for Slurm version 26.05. These capabilities give you finer control over how Slurm sees and schedules your cluster hardware, improving task placement for HPC and machine learning workloads. They also enable NVIDIA Multi-Instance GPU (MIG), which partitions a single GPU into isolated instances that Slurm schedules independently.
With Slurm 26.05, AWS PCS configures hardware topology by default, treating each node's NUMA domains as Slurm sockets. It also autodetects and configures GPU core affinity and GPU-to-GPU interconnect on GPU nodes. Tightly-coupled MPI jobs can now optimize rank placement using socket affinity, and GPU jobs land on cores local to their allocated GPUs. Custom Slurm and GRES settings add flexibility when you need it. You can declare additional accelerators, partition a GPU with MIG, use L3 cache domains as sockets, or override the AWS PCS defaults.
AWS PCS is a managed service that simplifies running and scaling high performance computing (HPC) workloads on AWS using Slurm. You can build complete, elastic environments that integrate compute, storage, networking, and visualization tools, and the service manages cluster updates and provides built-in observability.
These capabilities are available in all AWS Regions where AWS PCS is available. Slurm 26.05 also brings broader scheduling and observability improvements, described in the Slurm 26.05 release notes. To learn more, see Configuring custom GRES settings, Configuring hardware topology, and Configuring Multi-Instance GPU (MIG) in the AWS PCS User Guide.

## 핵심 요약

요약 미지원
