---
title: "Run interactive workloads on Amazon EMR on EKS with Spark Connect"
date: "2026-09-25"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/emr-eks-spark-connect-interactive/"
tags: ["EKS", "2026", "new-region", "security"]
nav_exclude: true
---

# Run interactive workloads on Amazon EMR on EKS with Spark Connect

**날짜:** 2026년 09월 25일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/emr-eks-spark-connect-interactive/

## 내용

Amazon EMR on EKS now supports interactive Apache Spark sessions with Spark Connect. Data engineers and data scientists can develop and debug Apache Spark applications interactively from managed notebooks in Amazon SageMaker Unified Studio and their own IDEs, such as Jupyter and Visual Studio Code, with Spark running on the Amazon EKS clusters they already operate. &nbsp;
An interactive session provides a persistent Spark context that spans across cells and scripts, letting you blend local Python code execution with remote Spark operations. Spark Connect's client-server architecture decouples your application client from the Spark driver and allows you to maintain your preferred development environment and tooling while Spark runs on your Amazon EKS cluster. This architecture supports workflows including ad hoc data exploration and incremental PySpark job development before deploying to production. Each session runs as pods on a virtual cluster, secured with your AWS Identity and Access Management (IAM) execution role and tagged by project and user.
Spark Connect on Amazon EMR on EKS is available with EMR release 7.14 (Apache Spark 3.5) and emr-spark-8.1.0 (Apache Spark 4.1), in all AWS Commercial Regions. The Amazon SageMaker Unified Studio experience is available in supported AWS Regions.
To get started, visit the Spark Connect on Amazon EMR on EKS documentation or the Amazon SageMaker Unified Studio Getting Started guide.

## 핵심 요약

요약 미지원
