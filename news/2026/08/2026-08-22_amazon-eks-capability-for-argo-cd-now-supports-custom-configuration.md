---
title: "Amazon EKS Capability for Argo CD now supports custom configuration"
date: "2026-08-22"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-argo-cd-configuration"
tags: ["EKS", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon EKS Capability for Argo CD now supports custom configuration

**날짜:** 2026년 08월 22일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-argo-cd-configuration

## 내용

The Amazon Elastic Kubernetes Service (Amazon EKS) Capability for Argo CD now supports custom configuration through a standard argocd-cm ConfigMap in your cluster. This capability gives you a fully managed GitOps continuous delivery experience, and you can now tune it to fit how your teams work. You can define custom health checks for your Custom Resources, customize the Argo CD UI banner content, adjust how the capability watches and compares the resources it manages, and more. You configure these settings the same way you do in upstream Argo CD, and AWS applies them to your managed capability. 
With this launch, cluster administrators now have more control over how Argo CD reports application health. By default, Argo CD has no built-in health logic for Custom Resources, so an Application can report as healthy while its resources are still provisioning, and sync waves can advance before those resources are ready. With a custom health check, you define this logic yourself. For example, a health check for a database resource can hold an Application at progressing until the database is ready. The capability also includes built-in health checks for AWS Controllers for Kubernetes (ACK) and kro (Kube Resource Orchestrator) resources, so these report accurate health with no additional configuration. 
You can configure the EKS Capability for Argo CD in all AWS Regions where the capability is available. To learn more, see Amazon EKS and Configure Argo CD settings in the Amazon EKS User Guide. 
&nbsp;

## 핵심 요약

요약 미지원
