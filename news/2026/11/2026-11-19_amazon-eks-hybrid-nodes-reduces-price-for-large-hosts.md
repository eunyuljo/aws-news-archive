---
title: "Amazon EKS Hybrid Nodes reduces price for large hosts"
date: "2026-11-19"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-hybrid-nodes-pricing-change/"
tags: ["EKS", "2026", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon EKS Hybrid Nodes reduces price for large hosts

**날짜:** 2026년 11월 19일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-hybrid-nodes-pricing-change/

## 내용

Amazon&nbsp;Elastic Kubernetes Service (Amazon EKS) Hybrid Nodes now has lower pricing for large nodes, capping the billed vCPU per node at 32 vCPU, so you are no longer charged for vCPUs above that per node threshold. Amazon EKS Hybrid Nodes lets you use your existing on-premises and edge infrastructure as nodes in Amazon EKS clusters. You can now use your largest servers, including those with GPUs, with Amazon EKS Hybrid Nodes at lower cost. 
With this change, the Amazon EKS Hybrid Nodes cost of a large server no longer grows with its vCPU count. At the first pricing tier, a 64 vCPU node now costs 50% less than before, and a 256 vCPU node costs 88% less, as both are now billed only for 32 vCPUs. This makes Amazon EKS Hybrid Nodes more cost-effective for large bare-metal and GPU servers running compute-intensive workloads, such as AI/ML training and inference, that must stay on-premises for data residency, latency, or regulatory reasons. The pricing change applies automatically to all new hybrid nodes. For the new pricing to take effect for existing hybrid nodes attached to clusters, delete and reattach them. Nodes with 32 vCPUs or fewer are still billed for their actual vCPUs, and existing tiered pricing still applies, so your effective rate falls as monthly usage grows. 
The new pricing is available in all AWS Regions where Amazon EKS Hybrid Nodes is available. To learn more about getting started and updated pricing details, visit the Amazon EKS Hybrid Nodes documentation and Amazon EKS pricing page.

## 핵심 요약

요약 미지원
