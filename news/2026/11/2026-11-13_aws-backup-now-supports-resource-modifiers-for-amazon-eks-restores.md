---
title: "AWS Backup now supports resource modifiers for Amazon EKS restores"
date: "2026-11-13"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-resource-modifiers-eks/"
tags: ["EKS", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Backup now supports resource modifiers for Amazon EKS restores

**날짜:** 2026년 11월 13일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-resource-modifiers-eks/

## 내용

Today, AWS Backup announces support for resource modifiers when restoring Amazon Elastic Kubernetes Service (Amazon EKS) backups. Resource modifiers let you transform Kubernetes resources during a restore, so you can adapt a restored cluster to its target environment. 
When you restore an EKS backup that has been copied across accounts or across AWS Regions, the restored cluster can carry references tied to the source environment, such as IAM roles, database endpoints, and Amazon ECR registry URIs. Previously, you had to locate and update these references manually after every restore, which was time consuming and error prone. With resource modifiers, you can define transformation rules once via a YAML file, and AWS Backup applies them automatically as part of the restore, improving the reliability of your cross-account and cross-Region disaster recovery workflows. 
AWS Backup support for resource modifiers for Amazon EKS backups is available in all commercial AWS Regions and AWS GovCloud (US) Regions. To get started, see the AWS Backup Documentation and read the launch blog.

## 핵심 요약

요약 미지원
