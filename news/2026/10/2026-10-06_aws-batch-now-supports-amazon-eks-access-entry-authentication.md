---
title: "AWS Batch now supports Amazon EKS access entry authentication"
date: "2026-10-06"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-batch-access-entries/"
tags: ["EKS", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Batch now supports Amazon EKS access entry authentication

**날짜:** 2026년 10월 06일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-batch-access-entries/

## 내용

AWS Batch now supports Amazon EKS access entry authentication for compute environments. EKS access entries provide an API-driven approach to granting IAM principals access to Kubernetes clusters, complementing the existing aws-auth ConfigMap. AWS Batch can now authenticate to your cluster through the access entry mechanism, simplifying cluster setup and authentication lifecycle management.
 
 
 To get started, use the CreateComputeEnvironment or UpdateComputeEnvironment APIs to set accessEntry.desiredState to ENABLED on all AWS Batch compute environments targeting your cluster. AWS Batch creates one access entry per cluster and associates the AWSBatchClusterPolicy with it. You can configure access entries through the AWS CLI, AWS SDKs, or AWS Management Console.
 
 
 Access entry authentication for AWS Batch on Amazon EKS is now supported in all AWS Regions where AWS Batch is available. For more information, see Amazon EKS access entry authentication in the AWS Batch User Guide.

## 핵심 요약

요약 미지원
