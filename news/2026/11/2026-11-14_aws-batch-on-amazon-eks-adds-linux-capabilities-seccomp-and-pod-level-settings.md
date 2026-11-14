---
title: "AWS Batch on Amazon EKS adds Linux capabilities, seccomp, and pod-level settings"
date: "2026-11-14"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/"
tags: ["RDS", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Batch on Amazon EKS adds Linux capabilities, seccomp, and pod-level settings

**날짜:** 2026년 11월 14일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/

## 내용

AWS Batch now supports additional Kubernetes security context settings in Amazon EKS job definitions, including Linux capabilities, seccomp profiles, and pod-level settings.&nbsp;For EKS clusters that enforce the Kubernetes Pod Security Standards restricted profile, you can now run AWS Batch jobs with only the privileges and system calls they require. 
To get started, use the RegisterJobDefinition API to set capabilities and seccompProfile in a container's securityContext, or set securityContext in podProperties to define pod-wide settings such as fsGroup. Container-level settings override pod-level defaults. You can configure these settings through the AWS Management Console, AWS CLI, AWS SDKs, or AWS CloudFormation. 
The additional security context settings for AWS Batch on Amazon EKS are now supported in all AWS Regions where AWS Batch is available. For more information, see the Amazon EKS properties section in the AWS Batch User Guide.

## 핵심 요약

요약 미지원
