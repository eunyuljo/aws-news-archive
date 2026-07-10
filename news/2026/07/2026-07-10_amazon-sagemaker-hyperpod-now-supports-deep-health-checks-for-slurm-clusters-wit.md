---
title: "Amazon SageMaker HyperPod now supports deep health checks for Slurm clusters with continuous provisioning"
date: "2026-07-10"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/deep-health-check-continuous-slurm/"
tags: ["SageMaker", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon SageMaker HyperPod now supports deep health checks for Slurm clusters with continuous provisioning

**날짜:** 2026년 07월 10일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/deep-health-check-continuous-slurm/

## 내용

Amazon SageMaker HyperPod now supports deep health checks for Slurm-orchestrated clusters created with continuous provisioning, enabling you to proactively verify GPU accelerator health on running instances at any time. Continuous provisioning lets you start training quickly and scale instance groups asynchronously without all-or-nothing failures, and you can now pair that flexibility with comprehensive hardware validation as instances come online. This capability addresses a critical challenge where even a single unhealthy node can waste hours of compute time and delay critical workloads.  With deep health checks, you can target entire instance groups or specific instances to run comprehensive hardware stress tests and connectivity tests before committing compute resources to a job. Because continuous provisioning adds worker nodes to your Slurm cluster asynchronously as capacity becomes available, you can run deep health checks on each new node as it comes online, validating hardware before scheduling jobs on it and without interrupting workloads already running on healthy nodes. Progress and results are visible at both the instance group and instance level through the SageMaker console and APIs, providing complete visibility into GPU health, network connectivity, and multi-node communication performance. Instances undergoing checks are automatically isolated from workload scheduling and returned to service upon passing. When paired with HyperPod's automatic node recovery capability, instances that fail are automatically rebooted or replaced, ensuring cluster health.  This capability is available in all regions where Amazon SageMaker HyperPod is available. To learn more about on-demand deep health checks and continuous provisioning, see the Amazon SageMaker HyperPod User Guide.

## 핵심 요약

요약 미지원
