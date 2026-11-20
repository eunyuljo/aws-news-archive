---
title: "Amazon VPC Flow Logs now supports Amazon EKS metadata"
date: "2026-11-20"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-vpc-flow-logs-amazon-eks-metadata/"
tags: ["EC2", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon VPC Flow Logs now supports Amazon EKS metadata

**날짜:** 2026년 11월 20일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-vpc-flow-logs-amazon-eks-metadata/

## 내용

Amazon VPC Flow Logs now adds Amazon Elastic Kubernetes Service (Amazon EKS) metadata to flow log records. Each record identifies the pod that sent or received the traffic, along with its cluster, namespace and labels. This makes it faster to investigate security events, understand traffic patterns, and troubleshoot network issues in your EKS clusters, without running monitoring software on your nodes.
Amazon EKS runs pods on Amazon EC2 instances, called nodes, and many pods can share one node's network interfaces. Previously, flow log records showed the network interface and IP address for each flow, not the pod behind it. Pods are short-lived, so by the time you investigated unexpected traffic, that IP address could belong to a different pod. To trace traffic back to the right pod, teams built custom tools or ran monitoring software on every node. Now, each record names the pod that sent or received the traffic, so one log gives you both VPC and Kubernetes context. For example, if a pod sends unexpected traffic to a database in your VPC, the record shows the pod and its namespace, even after that pod is replaced.
To get started, create a flow log for your cluster's VPC or subnets, and add the EKS fields to the log format. You don't need to change your cluster or applications. The fields are available for pods on Amazon EC2 instances, including EKS Auto Mode, managed node groups and self-managed nodes, that use the Amazon VPC CNI plugin for Kubernetes. Logs go to the same destinations as before, so your existing analytics tools keep working. EKS metadata is available at no additional charge. Standard VPC Flow Logs charges for log delivery and storage still apply. This feature is supported in all AWS Regions where Amazon EKS is available. For more information, visit the Amazon VPC Flow Logs.

## 핵심 요약

요약 미지원
