---
title: "Amazon SageMaker AI now supports SOCI-indexed images to start training jobs in seconds"
date: "2026-10-30"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-ai-soci-images-training/"
tags: ["SageMaker", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI now supports SOCI-indexed images to start training jobs in seconds

**날짜:** 2026년 10월 30일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-ai-soci-images-training/

## 내용

Today, Amazon SageMaker AI announces support for Seekable OCI (SOCI)-indexed container images for training and processing jobs, so your jobs start running your code sooner. SOCI-indexed images start Amazon SageMaker AI training containers in seconds, cutting GPU idle time during image pulls by up to 90%, with no impact on training performance. Before a training or processing job can run, SageMaker AI downloads its container image to the instance. For deep learning images, which routinely exceed 10 GB, that download adds minutes to the start of every job, and you pay for that time. Now, when your image includes a SOCI index, SageMaker AI lazy-loads the image, fetching only the files needed to start the container and streaming the rest in the background as your code runs. 
To use this feature, reference a SOCI-indexed image from a private Amazon ECR repository in your training or processing job. You can use a pre-indexed AWS Deep Learning Container by changing the image tag to its -soci variant, or add a SOCI index to your own image in Amazon ECR with open-source tools, without rebuilding the image. No changes to your job definition, entry point, or data channels are needed. SageMaker AI checks for an index automatically and images without an index download as before. If an index can't be used, the job falls back to a standard download and continues running. 
SOCI-indexed images for SageMaker AI training and processing jobs are available today in all AWS Regions where SageMaker AI is available, through the SageMaker AI APIs, CLIs, SDKs, and Console. To learn more, see the documentation for training jobs and processing jobs, or read the launch blog.

## 핵심 요약

요약 미지원
