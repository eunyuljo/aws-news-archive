---
title: "AWS Parallel Computing Service supports P6e-GB200 and P6e-GB300 UltraServers"
date: "2026-06-23"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-parallel-computing-service/"
tags: ["EC2", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Parallel Computing Service supports P6e-GB200 and P6e-GB300 UltraServers

**날짜:** 2026년 06월 23일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-parallel-computing-service/

## 내용

AWS Parallel Computing Service (PCS) now supports Amazon EC2 P6e-GB200 and P6e-GB300 UltraServer instances, enabling customers to run large-scale GPU workloads using the NVIDIA Blackwell architecture within Slurm-managed clusters. You can reserve UltraServers through EC2 Capacity Blocks for ML, associate them with a PCS compute node group via an EC2 launch template, and PCS automatically configures Slurm with the correct topology plugin.  With P6e-GB200 UltraServers, you can access up to 72 NVIDIA Blackwell GPUs within one NVLink domain to use 360 petaflops of FP8 compute (without sparsity) and 13.4 TB of total high bandwidth memory (HBM3e). P6e-GB300 UltraServers provide 1.5x GPU memory and 1.5x FP4 compute (without sparsity) compared to P6e-GB200.  AWS PCS is a managed service that simplifies running and scaling HPC workloads on AWS using Slurm. You can build complete, elastic environments that integrate compute, storage, networking, and visualization tools, while the service handles cluster operations with managed updates and built-in observability features.  You can use P6e UltraServers with PCS in all AWS Regions where both PCS and EC2 Capacity Blocks for UltraServers are available. To learn more about P6e UltraServers, visit Amazon EC2 P6 instances. To reserve P6e UltraServers, contact your AWS sales representative. Read more about PCS support for P6e UltraServers in the PCS User Guide and make sure to set the right Permissions.

## 핵심 요약

요약 미지원
