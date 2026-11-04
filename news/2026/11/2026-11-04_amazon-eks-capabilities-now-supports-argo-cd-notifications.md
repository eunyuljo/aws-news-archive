---
title: "Amazon EKS Capabilities now supports Argo CD Notifications"
date: "2026-11-04"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-argo-cd-notifications"
tags: ["EKS", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon EKS Capabilities now supports Argo CD Notifications

**날짜:** 2026년 11월 04일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-argo-cd-notifications

## 내용

The Amazon Elastic Kubernetes Service (Amazon EKS) Capability for Argo CD now supports Argo CD Notifications, providing notifications when your applications sync, fail, or change health. You define triggers and message templates in your cluster and subscribe individual Applications with an annotation, the same way you do in upstream Argo CD. 
With this launch, you can deliver notifications to 16 notification services, including Slack, PagerDuty, Opsgenie, Amazon SQS, and Amazon EventBridge. The Amazon SQS and Amazon EventBridge services authenticate with your IAM Capability Role, so you can route deployment events into your own event-driven workflows without storing credentials in your cluster. For a service that requires third-party credentials such as a Slack token, you can specify an AWS Secrets Manager ARN in place of the secret and EKS will automatically use it on your behalf. 
Notifications are available in all AWS Regions where the EKS Capability for Argo CD is available, at no additional charge. Standard charges apply for resources related to the services your notifications use, for example Amazon SQS or Amazon EventBridge. To learn more, visit Amazon EKS&nbsp;and refer to the Amazon EKS User Guide.

## 핵심 요약

요약 미지원
