---
title: "Amazon EKS Provisioned Control Plane now offers a 24 GB etcd database on 4XL and 8XL tiers"
date: "2026-11-12"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-provisioned-control-plane-larger-etcd-database/"
tags: ["EKS", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon EKS Provisioned Control Plane now offers a 24 GB etcd database on 4XL and 8XL tiers

**날짜:** 2026년 11월 12일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-provisioned-control-plane-larger-etcd-database/

## 내용

Amazon Elastic Kubernetes Service (Amazon EKS) now offers a larger 24 GB etcd database, up from 16 GB, for 4XL and 8XL Provisioned Control Plane clusters. etcd is the key-value store in the Kubernetes control plane that holds your cluster state, so its size limits how many Kubernetes objects your cluster can store. With 50% more capacity, you can run bigger clusters with more pods, jobs, events, and custom resources. 
The larger database gives more headroom to workloads that create and update many Kubernetes objects, such as large-scale AI/ML training and inference, batch processing, and CI/CD pipelines. When the etcd database fills up, you can’t add or change objects in your cluster, so the extra headroom helps keep these workloads running as they scale. 
To get the larger database,&nbsp;choose the 4XL or 8XL tier of Provisioned Control Plane on a cluster running EKS version 1.34 or later. Existing clusters on the 4XL and 8XL tiers running these versions get the larger database automatically, with no action required. The 24 GB etcd database is available in all commercial AWS Regions where Provisioned Control Plane is available. To learn more, see the Amazon EKS Provisioned Control Plane user guide.&nbsp;

## 핵심 요약

요약 미지원
