---
title: "Run interactive workloads on Amazon EMR on EC2 with Spark Connect"
date: "2026-08-05"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-emr-ec2-spark-connect/"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# Run interactive workloads on Amazon EMR on EC2 with Spark Connect

**날짜:** 2026년 08월 05일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-emr-ec2-spark-connect/

## 내용

Amazon EMR on EC2 now supports interactive Apache Spark sessions with Spark Connect. Data engineers and data scientists can develop and debug Apache Spark applications interactively from managed notebooks in Amazon SageMaker Unified Studio and their own IDEs, such as Jupyter and Visual Studio Code, with each session running on dedicated EMR on EC2 clusters. You can also monitor and debug active and completed sessions in the EMR console. 
&nbsp; 
An interactive session provides a persistent Spark context that spans across cells and scripts, letting you blend local Python code execution with remote Spark operations. Spark Connect's client-server architecture decouples your application client from the Spark driver and allows you to maintain your preferred development environment and tooling while Spark infrastructure runs on the cluster. This architecture supports workflows including ad hoc data exploration, iterative step-by-step debugging, and incremental PySpark job development before deploying to production. For observability, you get real-time session monitoring via the Spark UI, history tracking through the Spark History Server, and session management from the EMR console or API/CLI/SDK. 
&nbsp; 
Interactive Sessions is available on Amazon EMR on EC2 with AWS runtime for Apache Spark (emr-spark-8.0) and later, in all AWS Regions where Amazon EMR is available, except the AWS GovCloud Regions and the China Regions. The Amazon SageMaker Unified Studio experience is available in supported regions. To get started, visit the Interactive sessions with Spark Connect guide or the Amazon SageMaker Unified Studio Getting Started guide.

## 핵심 요약

요약 미지원
