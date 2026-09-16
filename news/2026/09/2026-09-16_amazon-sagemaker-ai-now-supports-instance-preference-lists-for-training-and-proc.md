---
title: "Amazon SageMaker AI now supports instance preference lists for training and processing jobs"
date: "2026-09-16"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sagemaker-training-processing-instance-pref-lists/"
tags: ["SageMaker", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI now supports instance preference lists for training and processing jobs

**날짜:** 2026년 09월 16일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sagemaker-training-processing-instance-pref-lists/

## 내용

Today, Amazon SageMaker AI announces instance preference lists for training and processing jobs, making it easier and faster to find compute capacity for your workloads. Many AI training, fine-tuning, and data processing workloads run comparably well on any of several instance types or sizes. However, before now, you had to name only one instance type at the time of job submission and wait for SageMaker to find that specific instance for your job. For high-demand GPUs during peak periods, where wait times can be unpredictable, customers sometimes had to build complex retry logic or concurrently submit multiple jobs with different instance types to find the first available option. Now you can simply provide a prioritized list of the instance types your workload accepts, and SageMaker automatically runs your job on the first available configuration from your preferences. With this solution, your training or processing job will likely start sooner. 
To use this feature, you specify your instance type and count preferences in priority order when submitting the training or processing job. For example, your list might contain a preference of two instances of ml.g6.48xlarge or four instances of ml.g5.48xlarge. SageMaker works through the list and launches your job on the first configuration where capacity is available. You can also configure the capacity sourcing from on-demand sources or from your reserved SageMaker Flexible Training Plans within the same job submission. This feature simplifies the process of getting compute for your jobs during high-demand periods and reduces the undifferentiated manual retrying you would otherwise do, all within the SageMaker training and processing job APIs you already use. 
Instance preference lists for SageMaker training and processing jobs is available today in all AWS Regions where SageMaker is available through the SageMaker CLIs, APIs, SDKs and Console UI. To learn more, see our documentation&nbsp;or our launch blog.

## 핵심 요약

요약 미지원
