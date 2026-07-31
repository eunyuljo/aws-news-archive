---
title: "AWS Parallel Computing Service now supports node lifecycle actions"
date: "2026-07-31"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-pcs-node-lifecycle-actions/"
tags: ["S3", "2026", "new-region", "performance"]
nav_exclude: true
---

# AWS Parallel Computing Service now supports node lifecycle actions

**날짜:** 2026년 07월 31일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-pcs-node-lifecycle-actions/

## 내용

Today, AWS announces the general availability of node lifecycle actions in AWS Parallel Computing Service (PCS). With node lifecycle actions, you can run custom scripts automatically at defined points in a compute node's lifecycle. You can use them to prepare your nodes for work. For example, you can mount shared storage, join a directory service, install software, or set up monitoring. 
You define node lifecycle actions in your PCS compute node group configuration when you create or update the group, and you can reuse the same script across multiple compute node groups and clusters. For each script, you set its location as an Amazon S3 or HTTPS URI, the arguments to pass, which lifecycle stage it runs in, whether it re-runs on reboot, and its error-handling behavior. AWS PCS writes the output to a dedicated log file, giving you visibility into what ran. 
AWS PCS is a managed service that simplifies running and scaling high performance computing (HPC) workloads on AWS using Slurm. You can build complete, elastic environments that integrate compute, storage, networking, and visualization tools, and the service manages cluster updates and provides built-in observability. 
Node lifecycle actions are available in all AWS Regions that support AWS PCS. To learn more, see the AWS PCS User Guide.

## 핵심 요약

요약 미지원
