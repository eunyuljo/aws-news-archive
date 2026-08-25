---
title: "Amazon SageMaker HyperPod enhances support for Ray"
date: "2026-08-25"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-sagemaker-hyperpod-ray"
tags: ["RDS", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker HyperPod enhances support for Ray

**날짜:** 2026년 08월 25일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-sagemaker-hyperpod-ray

## 내용

Amazon SageMaker HyperPod now enhances support for Ray with built-in observability, resilient training, accelerated inference and managed development environments. Ray is a popular open-source framework for scaling AI workloads on a unified compute layer, from data processing and distributed training to reinforcement learning and model serving. Running Ray on Kubernetes at production scale can be an operational burden: job hangs, low GPU utilization from static team allocations, and multi-step observability setup. Also, lack of interactive development environment means every code change needs another job submission and familiarity with kubectl. 
HyperPod now brings easier development, resilient training, and accelerated inference to Ray. Data scientists create, edit, monitor, and delete Ray clusters from a web-based interface in Amazon SageMaker Studio, then attach JupyterLab, Code Editor, or a local IDE to a running Ray cluster and iterate interactively against cluster-scale compute. A multi-node Ray cluster behaves like a local development environment, so you test each change immediately, without waiting for a new job to queue and start. For Observability, HyperPod provisions Grafana dashboards with metrics in Amazon Managed Service for Prometheus and allows one-click access to the Ray Dashboard through a secure browser link, giving you visibility into your workloads from the first run. For training at scale, HyperPod node auto recovery and hung job detection handle GPU faults, job hangs, loss spikes, and degraded throughput. Tiered checkpointing restores state from cluster memory to maximize goodput, and task governance improves compute utilization through quotas, priorities, and preemption. Together, these keep your long training runs progressing through failures and maximize the useful work done per GPU-hour. For inference with Ray Serve, a tiered KV cache reuses cached prefixes to reduce time to first token, and you can deploy Amazon SageMaker JumpStart models directly. 
Open-source Ray code runs unchanged and you can either adopt the purpose-built experience in SageMaker Studio or take individual capabilities to integrate into your own ML platform. 
Ray support is available for HyperPod clusters orchestrated by Amazon EKS, in AWS Regions where SageMaker HyperPod is supported. To learn more, see the SageMaker HyperPod documentation, and explore the&nbsp;interactive demo.

## 핵심 요약

요약 미지원
